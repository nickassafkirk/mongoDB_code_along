import os
import pymongo

if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDatabase"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print('Mongo is connected')
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]

new_docs = [{"first": "pamela", "last": "anderson", "dob": "13/03/1965", "gender": "f", "hair_color": "blonde", "occupation": "actress", "nationality": "american"},
            {"first": "sir terry", "last": "pratchet", "dob": "23/05/1940", "gender": "m", "hair_color": "grey", "occupaton": "author", "nationality": "british"}]

# coll.insert(new_docs)
coll.update_many({"nationality": "american"}, {"$set": {"anthem": "star spangled banner"}})

documents = coll.find()

for doc in documents:
    print(doc)

