
If you have a mongodb database that you wish to document, a good
starting point might be to install mongodoc and use the doc-db
command::

    % doc-db test

After answering a few questions, you will get an output file that
will look something like this::

     _____________________________________________________________________________
    | people                                                                      |
    |_____________________________________________________________________________|
    | last:                <type 'unicode'>       ________________________________|
    | mood:                <type 'unicode'>     | address                        ||
    | age:                     <type 'int'>     |________________________________||
    | location:            <type 'unicode'>     | state:  <type 'unicode'>       ||
    | address:                <type 'dict'>     | street: <type 'unicode'>       ||
    | _id: <class 'bson.objectid.ObjectId'>     | number:     <type 'int'>       ||
    | first:               <type 'unicode'>     | zip:        <type 'int'>       ||
    |                                           |________________________________||
    |_____________________________________________________________________________|


This document has a sub-document for the value of the address
field, so it appears as a box within the people diagram. You
will get one of these diagrams for each collection in the db.

The doc-db command has a few options for connecting to the db::

    % doc-db -h                
    usage: doc-db [-h] [--port PORT] [--host HOST] [--username USERNAME]
                  [--password PASSWORD] [--file FILE]
                  name

    Document a mongo db

    positional arguments:
      name                 The name of the mongo db to document

    optional arguments:
      -h, --help           show this help message and exit
      --port PORT          The db port number
      --host HOST          The db host
      --username USERNAME  The username for authenticating to the db
      --password PASSWORD  The password for authenticating to the db
      --file FILE          The name of the output file

