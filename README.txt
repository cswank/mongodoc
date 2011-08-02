
If you have a mongodb database that you wish to document, a good
starting point might be to install mongodoc and use the mongodoc
command:

doc-db --name test

After answering a few questions, you will get an output file that
will look something like this:

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


