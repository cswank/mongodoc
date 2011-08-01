

class MongoDoc(object):

    def __init__(self, doc, name, x=0, y=0):
        self._doc = doc
        self._x = x
        self._y = y
        self._name = name
        self._width = 0
        self._height = 0
        self._subdocs = []
        self._lines = []
        self.get_lines(doc)
        self.get_subdocs(doc)
        

    @property
    def lines(self):
        for line in self.header:
            yield line.format('', width=self.width)
        for line in self._lines:
            if len(self._subdocs) > 0:
                line = '| {0}: {1: >{width}} {2} |'.format(line[0], line[1], self._subdocs[0].lines.next(), width=self._width)
            else:
                line = '| {0}: {1: >{width}} |'.format(line[0], line[1], width=self.width)
            yield line
        yield self.footer.format('', width=self.width)
        
    @property
    def width(self):
        if len(self._subdocs) > 0:
            return self._width + max([d.width for d in self._subdocs])
        return self._width

    @property
    def pdf(self):
        pass
    
    @property
    def text(self):
        return '\n'.join([line for line in self.lines])
        
    @property
    def header(self):
        return [
            '{0:_>{width}}',
            '| {0}'.format(self._name) + '{0: >{width}}|',
            '|{0:_>{width}}|',
            ]

    @property
    def footer(self):
        return '{0:_>{width}}'

    def get_subdocs(self, doc):
        for key, value in doc.iteritems():
            if isinstance(value, dict):
                self._subdocs.append(MongoDoc(value, key))

    def get_lines(self, doc):
        for key, value in doc.iteritems():
            #line = '| {0}: {1: >{width}}'.format(key, str(type(value)), width=60 - len(key))
            line = (key, str(type(value)))
            l = len(line[0]) + len(line[1]) + 5
            if l > self._width:
                self._width = l
            self._height += 1
            self._lines.append(line)
                

    

    

