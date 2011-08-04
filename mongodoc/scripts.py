import argparse
import os
from .doc_doc import DocDoc
from pymongo import Connection

def get_args():
    parser = argparse.ArgumentParser(description='Document a mongo db')
    parser.add_argument('--port', default=27017, type=int, help='The db port number')
    parser.add_argument('--host', type=str, default='localhost', help='The db host')
    parser.add_argument('--username', type=str, help='The username for authenticating to the db')
    parser.add_argument('--password', type=str, help='The password for authenticating to the db')
    parser.add_argument('--name', required=True, type=str, help='The name of the mongo db to document')
    parser.add_argument('--file', type=str, help='The name of the output file')
    return parser.parse_args()

def get_db(host, port, name, username=None, password=None):
    connection = Connection(host=host, port=port)
    db = connection[name]
    if username is not None and password is not None:
        db.authenticate(username, password)
    return db

def document_collection(db, name):
    cursor = db[name].find()
    if cursor.count() == 0:
        return ''
    while True:
        try:
            doc = cursor.next()
        except StopIteration:
            print 'sorry, that was the last doc in this collection and it will be used for the output.'
            break
        mongo_doc = DocDoc(doc, name)
        text = mongo_doc.text
        print text
        answer = raw_input('Use this doc (y/n)?')
        if answer != 'n':
            break
    return mongo_doc

def write_output(text, args):
    filename = args.file
    if filename is None:
        filename = '{0}-mongodoc.txt'.format(args.name)
    if os.path.exists(filename):
        overwrite = raw_input('{0} already exists.  overwrite (y/n)? '.format(filename))
        if overwrite != 'y':
            print 'aborting'
            return
    f = open(filename, 'w')
    f.write(text)
    f.close()
    print 'The results were written to {0}'.format(filename)

def document_db():
    args = get_args()
    db = get_db(args.host, args.port, args.name)
    text = ''
    docs = []
    for name in db.collection_names():
        if name.startswith('system.'):
            continue
        docs.append(document_collection(db, name))
    collection_doc = CollectionDoc(db, docs)
    write_output(collection_doc.text, args)
    
        
    

