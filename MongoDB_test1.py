import pymongo
client = pymongo.MongoClient("mongodb+srv://pratikkodilkar:20mar1998@cluster0.slmzr61.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

# client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# print(db)

d = {'name': 'sudhanshu',
     'email': 'sudhanshu@ineuron.ai',
     'suranme': 'kumar'}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)






