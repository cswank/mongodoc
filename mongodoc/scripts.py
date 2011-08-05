import argparse
import os
from .doc_doc import DocDoc
from .collection_doc import CollectionDoc
from collections import defaultdict
from pymongo import Connection

def get_args():
    parser = argparse.ArgumentParser(description='Document a mongo db')
    parser.add_argument('name', type=str, help='The name of the mongo db to document')
    parser.add_argument('--port', default=27017, type=int, help='The db port number')
    parser.add_argument('--host', type=str, default='localhost', help='The db host')
    parser.add_argument('--username', type=str, help='The username for authenticating to the db')
    parser.add_argument('--password', type=str, help='The password for authenticating to the db')
    parser.add_argument('--file', type=str, help='The name of the output file')
    parser.add_argument('--find-links', default='yes', type=str, help='Enter "no" if you don\'t want to find links')
    return parser.parse_args()

def get_db(host, port, name, username=None, password=None):
    connection = Connection(host=host, port=port)
    db = connection[name]
    if username is not None and password is not None:
        db.authenticate(username, password)
    return db

def count_docs(cursor, name):
    counter = dict()
    for i, doc in enumerate(cursor):
        mongo_doc = DocDoc(doc, name)
        if mongo_doc.text not in counter:
            counter[mongo_doc.text] = dict(doc=mongo_doc, count=1)
        else:
            counter[mongo_doc.text]['count'] += 1
    return counter, i

def find_representative_doc(db, name, skip):
    cursor = db[name].find().limit(20).skip(skip)
    if cursor.count(with_limit_and_skip=True) == 0:
        print 'WARNING: all the documents have been examined, reverting to the first set'
        cursor = db[name].find().limit(20)
    counter, i = count_docs(cursor, name)
    values = counter.values()
    m = max(values, key=lambda x: x['count'])
    return m['doc'], '{0:.02f}%'.format((100.0 * m['count'] / (i + 1))), i + 1

def document_collection(db, name):
    skip = 0
    if db[name].count() == 0:
        return ''
    while True:
        doc, percentage, count = find_representative_doc(db, name, skip)
        skip += 20
        print doc.text
        answer = raw_input('Use this doc ({0} of the {1} documents examined matched it) [Y/n]?'.format(percentage, count))
        if answer != 'n':
            break
    return doc

def write_output(text, args):
    filename = args.file
    if filename is None:
        filename = '{0}-mongodoc.txt'.format(args.name)
    if os.path.exists(filename):
        overwrite = raw_input('{0} already exists.  overwrite (y/N)? '.format(filename))
        if overwrite != 'y':
            print 'aborting'
            return
    f = open(filename, 'w')
    f.write(text)
    f.close()
    print 'The results were written to {0}'.format(filename)

def document_db():
    args = get_args()
    db = get_db(args.host, args.port, args.name, username=args.username, password=args.password)
    text = ''
    docs = []
    for name in sorted(db.collection_names()):
        if name.startswith('system.'):
            continue
        docs.append(document_collection(db, name))
    find_links = True if args.find_links == 'yes' else False
    collection_doc = CollectionDoc(db, docs, find_links=find_links)
    write_output(collection_doc.text, args)
    
        
    

