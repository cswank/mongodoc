from pymongo.objectid import ObjectId

class CollectionDoc(object):

    def __init__(self, db, docs):
        self._db = db
        self._collection_names = db.collection_names()
        self._docs = docs

    @property
    def text(self):
        text = ''
        for doc in self._docs:
            text += '{0}\n\n'.format(doc.text)
        self._find_relationships(text)
        return text

    def _find_relationships(self, text):
        for doc in self._docs:
            fields = self._find_link_fields(doc.doc)
            self._make_links(fields, text)
            
    def _make_links(self, fields, text):
        for key, value in fields.iteritems():
            self._make_link(key, value, text)

    def _make_link(self, key, value, text):
        scores = []
        for name in self._collection_names:
            scores.append((name, difflib.SequenceMatcher(None, name, key)))
        print scores

    def _find_link_fields(doc):
        fields = {}
        for key, value in doc.iteritems():
            if key == '_id':
                continue
            if isinstance(value, ObjectId):
                fields[key] = value
        return fields


    

    



