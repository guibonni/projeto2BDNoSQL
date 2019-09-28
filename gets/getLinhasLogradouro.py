import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["project2"]
mycol = mydb["logradouro"]

myquery = { "descricao": "Logradouro longe pacas" }

mydoc = mycol.find(myquery)

for x in mycol.find({},{ "_id": 0, "linhas": 1 }):
    print(x)