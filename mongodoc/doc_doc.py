class DocDoc(object):
    """
    Takes a dictionary and documents the type for each key.
    If the value for a key is a dict (or a list of dicts)
    then the sub-dict is documented as well.
    """

    _ROW_BUFFER = 10

    def __init__(self, doc, name, inlist=False):
        """
        
        Arguments:
        - `doc`: the dictionary that is to be documented
        - `name`: the name of the collection
        - `inlist`: did this dict come from a list?
        """

        self._doc = doc
        if inlist:
            self._name = '{0} <list>'.format(name)
        else:
            self._name = name
        self._max_row_width = 0
        self._subdocs = []
        self._subdoc_rows = None
        self._rows = []
        self._text = None
        self.get_rows(doc)
        self.get_subdocs(doc)
        self._width = self._get_width()

    def __eq__(self, other):
        return self.text == other.text

    @property
    def collection(self):
        return self._name

    @property
    def doc(self):
        return self._doc

    @property
    def text(self):
        if self._text is None:
            self._text = '\n'.join([row for row in self.rows])
        return self._text

    @property
    def rows(self):
        for item in self._get_header():
            yield item
        for row in self._rows:
            subdoc_row = self._get_subdoc_row()
            if subdoc_row is not None:
                row = self._get_row_with_subdoc(row, subdoc_row)
            else:
                row = self._get_row_without_subdoc(row)
            yield row
        subdoc_row = self._get_subdoc_row()
        while subdoc_row is not None:
            yield self._get_row_with_subdoc(['',''], subdoc_row)
            subdoc_row = self._get_subdoc_row()
        yield self._get_footer()

    def _get_row_with_subdoc(self, row, subdoc_row):
        if row[0] == '':
            kv = ''
        else:
            width = self._max_row_width - len(row[0]) - self._ROW_BUFFER
            kv = '{0}: {1: >{width}}'.format(row[0], row[1], width=width)
        width = self._width - len(kv) - 2
        return '| {0} {1: >{width}}|'.format(
            kv,
            subdoc_row,
            width=width
            )

    def _get_row_without_subdoc(self, row):
        width = self._max_row_width - len(row[0]) - self._ROW_BUFFER
        kv = '{0}: {1: >{width}}'.format(row[0], row[1], width=width)
        width = self._width - len(kv) - 1
        return '| {0}{1: <{width}}|'.format(
            kv,
            ' ',
            width=width,
            )

    def _get_header(self):
        return [
            ' {0:_>{width}}'.format('', width=self._width),
            '| {0}'.format(self._name) + '{0: >{width}}|'.format('', width=self._width - len(self._name) - 1),
            '|{0:_>{width}}|'.format('', width=self._width),
            ]

    def _get_footer(self):
        return '|{0:_>{width}}|'.format('', width=self._width)

    def get_subdocs(self, doc):
        for key, value in doc.iteritems():
            if isinstance(value, dict):
                self._subdocs.append(DocDoc(value, key))
            elif isinstance(value, list) and len(value) > 0 and isinstance(value[0], dict):
                self._subdocs.append(DocDoc(value[0], key, inlist=True))
            
    def get_rows(self, doc):
        rows = []
        for key, value in doc.iteritems():
            row = (key, str(type(value)))
            l = len(row[0]) + len(row[1]) + self._ROW_BUFFER
            if l > self._max_row_width:
                self._max_row_width = l
            rows.append((row, key))
        rows.sort(key=lambda x: x[1])
        self._rows = [item[0] for item in rows]

    def _get_subdoc_row(self):
        if self._subdoc_rows is None and len(self._subdocs) == 0:
            return
        if self._subdoc_rows is None:
            subdoc = self._subdocs.pop(0)
            self._subdoc_rows = subdoc.rows
        try:
            row = self._subdoc_rows.next()
        except StopIteration:
            self._subdoc_rows = None
            return
        return row

    def _get_width(self):
        subdoc_width = max([d._width for d in self._subdocs]) if len(self._subdocs) > 0 else 0
        return self._max_row_width + subdoc_width
