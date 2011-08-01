

class MongoDoc(object):

    def __init__(self, doc, name, x=0, y=0):
        self._doc = doc
        self._x = x
        self._y = y
        self._name = name
        self._width = 0
        self._height = 0
        self._subdocs = []
        self.get_lines(doc)
        self.get_subdocs(doc)
        self._lines = []

    @property
    def width(self):
        return self._width + max([d.width for d in self._subdocs])

    @property
    def pdf(self):
        pass
    
    @property
    def text(self):
        self._width += 5
        text = self.header
        for i, line in enumerate(self._lines):
            text += line + ' ' * (self._width - len(line)) + '  |\n'
        text += '|' + '_' * (self._width + 1) + '|\n'
        return text

    @property
    def header(self):
        return '{0:_>{width}} \n| {name: >{width}}|\n|{_:>{width}|\n'

    def get_subdocs(self, doc):
        for key, value in doc.iteritems():
            if isinstance(value, dict):
                self._subdocs.append(MongoDoc(value, key))
            #self._width += max([d.width for d in self._subdocs])

    def get_lines(self, doc):
        for key, value in doc.iteritems():
            #line = '| {0}: {1: >{width}}'.format(key, str(type(value)), width=60 - len(key))
            line = (key, str(type(value)))
            l = len(line[0] + len(line[1] + 5
            if l > self._width:
                self._width = l
            self._height += 1
            self._lines.append(line)
                

    

    

