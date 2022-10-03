from pydoc import doc
import pymongo
USER = 'LOlbrich'
PASSWORD = 'kjgL12x4J0cO6tng'
SERVERNAME = 'Cluster0'
# make sure to remove <> from url
client = pymongo.MongoClient(f"mongodb+srv://{USER}:{PASSWORD}@cluster0.u1dgs.mongodb.net/{SERVERNAME}?retryWrites=true&w=majority".format(USER,PASSWORD,SERVERNAME))
db = client.test

#db.test.insert_one({'x':1})
#print(db.test.count_documents({'x':1}))

#this returns an object so lets assign it to a variable
cursor = db.test.find({'x':1})
list(cursor)

# insert many dictionaries from a list using 'insert_many'
logan = {
    'name':'Logan',
    'fav_food':'anything',
    'lucky_num':69
}
Angela = {
    'name':'Angela',
    'fav_food':'cake',
    'lucky_num':23
}
doc_list = [logan,Angela]
#db.test.insert_many(doc_list)

# we can look at all the documents in the DB by using .find(), if we dont pass a
# specific document into the function it will return all the documents
#(list(db.test.find()))

# you can pass a specific key:value pair into find() 
#print(db.test.find_one({'fav_food':'cake'}))

# You can use a for loop to add lots of documents into the table
more_docs = []
for i in range(10):
    doc = {'even':i%2==0}
    doc['value'] = i
    more_docs.append(doc)

db.test.insert_many(more_docs)

#print(list(db.test.find()))
#print(list(db.test.find({'even':True, 'value': 2})))

# Deleting Documents 
#db.test.delete_one({'x':1})

# update works in a similar way
result = db.test.update_one({'x':1},{'$inc':{'x':2}})
result.matched_count
#print(db.test.find())

