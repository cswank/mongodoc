
If you have a mongodb database that you wish to document, a good
starting point might be to install mongodoc and use the mongodoc
command::

    % mongodoc test

After answering a few questions, you will get an output file that
will look something like this::


           _____________________________________________
          | hobbies                                     |
          |_____________________________________________|
       +--| _id: <class 'bson.objectid.ObjectId'>       |
       |  | title:               <type 'unicode'>       |
       |  |_____________________________________________|
       |  
       |   _____________________________________________
       |  | occupations                                 |
       |  |_____________________________________________|
    +--+--| _id: <class 'bson.objectid.ObjectId'>       |
    |  |  | duties:                 <type 'list'>       |
    |  |  | title:               <type 'unicode'>       |
    |  |  |_____________________________________________|
    |  |  
    |  |   ____________________________________________________________________________________
    |  |  | people                                                                             |
    |  |  |____________________________________________________________________________________|
    |  |  | _id:        <class 'bson.objectid.ObjectId'>       ________________________________|
    |  |  | address:                       <type 'dict'>     | address                        ||
    |  |  | first:                      <type 'unicode'>     |________________________________||
    |  +--| hobby:      <class 'bson.objectid.ObjectId'>     | number: <type 'unicode'>       ||
    |     | last:                       <type 'unicode'>     | state:  <type 'unicode'>       ||
    +-----| occupation: <class 'bson.objectid.ObjectId'>     | street: <type 'unicode'>       ||
          |                                                  | zip:    <type 'unicode'>       ||
          |                                                  |________________________________||
          |____________________________________________________________________________________|
      

The document in the people collection has a sub-document for
the value of the address field, so it appears as a box within 
the people diagram. You will get one of these diagrams for each
collection in the db.  MongoDoc found that there is a probable
link between the _id of occupations and the occupation field
of the people doc.  If the find links feature is not working
for you, you can disable it with the --find-links option

The mongodoc command has a few options for connecting to the db::

    % mongodoc -h                
    usage: mongodoc [-h] [--port PORT] [--host HOST] [--username USERNAME]
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
      --find-links         Enter no if you don't want to find links.

