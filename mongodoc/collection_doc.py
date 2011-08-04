import difflib, re
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
        text = text.split('\n')
        self._find_relationships(text)
        return '\n'.join(text)

    def _find_relationships(self, text):
        level = 0
        for doc in self._docs:
            fields = self._find_link_fields(doc.doc)
            level = self._make_links(fields, text, level)
            
    def _make_links(self, fields, text, level):
        for key, value in fields.iteritems():
            collection_name = self._find_collection(key, value)
            if collection_name is not None:
                self._make_link(collection_name, key, value, text, level)
                level += 1
        return level
            
    def _make_link(self, collection_name, key, value, text, level):
        for i, row in enumerate(text):
            j = row.find(key)
            if -1 < j < 20:
                break
        for k, row in enumerate(text):
            j = row.find('{0} '.format(collection_name))
            if -1 < j < 20:
                break
        start, end = sorted([i, k])
        for i in xrange(len(text) - 1):
            self._append_row(start, end, i, text, level)


    def _append_row(self, start, end, i, text, level):
        j = 3 * level
        prefix = text[i][:j]
        rest = text[i][j:]
        print 'prefix:', len(prefix), level, prefix
        if (i == start or i == end) and '|' not in prefix:
            prefix = '+--{0}'.format(prefix.replace(' ', '-'))
        elif (i == start or i == end) and '|' in prefix:
            prefix = '+--{0}'.format(prefix.replace(' ', '-').replace('|', '+'))
        elif start > i or i > end:
            prefix = '   {0}'.format(prefix)
        elif start < i or i < end:
            prefix = '|  {0}'.format(prefix)
        text[i] = prefix + rest
        

    def _find_collection(self, key, value):
        scores = []
        for collection_name in self._collection_names:
            scores.append((collection_name, value, difflib.SequenceMatcher(None, collection_name, key).ratio()))
        scores.sort(key=lambda x: x[2], reverse=True)
        for item in scores:
            collection_name = item[0]
            value = item[1]
            doc = self._db[collection_name].find_one({'_id': value})
            if doc is None:
                continue
            else:
                return collection_name
            
    def _find_link_fields(self, doc):
        fields = {}
        for key, value in doc.iteritems():
            if key == '_id':
                continue
            if isinstance(value, ObjectId):
                fields[key] = value
        return fields


    

    



