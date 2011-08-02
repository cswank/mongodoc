

class MongoDoc(object):

    def __init__(self, doc, name, x=0, y=0, inlist=False):
        self._doc = doc
        self._x = x
        self._y = y
        self._name = name
        self._max_row_width = 0
        self._height = 0
        self._subdocs = []
        self._subdoc_rows = None
        self._rows = []
        self._inlist = inlist
        self.get_rows(doc)
        self.get_subdocs(doc)
        self._width = self._get_width()

    def _get_width(self):
        subdoc_width = max([d._width for d in self._subdocs]) if len(self._subdocs) > 0 else 0
        return self._max_row_width + subdoc_width

    @property
    def text(self):
        return '\n'.join([row for row in self.rows])

    @property
    def rows(self):
        yield self.header[0].format('', width=self._width)
        yield self.header[1].format('', width=self._width - len(self._name) - 1)
        yield self.header[2].format('', width=self._width)
        sub_rows = None
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
        yield self.footer.format('', width=self._width)

    def _get_row_with_subdoc(self, row, subdoc_row):
        """
        | key: value      | subdoc key: subdoc value  ||
                          |                            |
                          |                            |
                          w1 = self._width - len key/value  |
                                                       w2 = self.width - len(subdoc_row)
        """
        if row[0] == '':
            kv = ''
        else:
            width = self._max_row_width - len(row[0]) - 10
            kv = '{0}: {1: >{width}}'.format(row[0], row[1], width=width)
            #kv = '{0}: {1}'.format(row[0], row[1])
        width = self._width - len(kv) - 2
        return '| {0} {1: >{width}}|'.format(
            kv,
            subdoc_row,
            width=width
            )

    def _get_row_without_subdoc(self, row):
        width = self._max_row_width - len(row[0]) - 10
        kv = '{0}: {1: >{width}}'.format(row[0], row[1], width=width)
        width = self._width - len(kv) - 1
        if width < 0:
            width = 0
        return '| {0}{1: <{width}}    |'.format(
            kv,
            ' ',
            width=width,
            )

    @property
    def header(self):
        return [
            ' {0:_>{width}}',
            '| {0}'.format(self._name) + '{0: >{width}}|',
            '|{0:_>{width}}|',
            ]

    @property
    def footer(self):
        return '|{0:_>{width}}|'

    def get_subdocs(self, doc):
        for key, value in doc.iteritems():
            if isinstance(value, dict):
                self._subdocs.append(MongoDoc(value, key))

    def get_rows(self, doc):
        for key, value in doc.iteritems():
            #row = '| {0}: {1: >{width}}'.format(key, str(type(value)), width=60 - len(key))
            row = (key, str(type(value)))
            l = len(row[0]) + len(row[1]) + 10
            if l > self._max_row_width:
                self._max_row_width = l
            self._height += 1
            self._rows.append(row)

    def _get_subdoc_row(self):
        if self._subdoc_rows is None and len(self._subdocs) == 0:
            return
        if self._subdoc_rows is None:
            subdoc = self._subdocs.pop(0)
            self._subdoc_rows = subdoc.rows
        try:
            row = self._subdoc_rows.next()
        except StopIteration:
            return
        return row
            
                

    

    

