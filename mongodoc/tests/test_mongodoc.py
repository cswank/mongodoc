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
        eq_(len(self.md._subdocs), 1)
        print 'result:'
        eq_(self.md.text, '')


    
            
        


