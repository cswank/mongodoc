from nose.tools import eq_
from doc import doc
from mongodoc import MongoDoc

class TestMongoDoc(object):

    def setup(self):
        self.md = MongoDoc(doc, 'campaigns')

    def test_create(self):
        pass

    def test_text(self):
        #eq_(self.md.text, '')
        print 'result:'
        print self.md.text

    def test_get_boxes(self):
        self.md.get_boxes(doc)

    
            
        


