import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["project2"]
mycol = mydb["linha"]

myobj = {
    "codigo": 1,
    "nome": "Linha do bairro la",
    "itinerario": [
        {
            "codigo": 2,
            "descricao": "Logradouro dois"
        },
        {
            "codigo": 37,
            "descricao": "Logradouro longe pacas"
        }
    ],
    "quadroHorarios": {
        "diasUteis": ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00"],
        "sabados": ["09:00", "12:00", "15:00", "18:00"],
        "domingos": ["08:00", "13:00", "18:00"],
        "feriados": ["08:00", "13:00", "18:00"]
    }
}

x = mycol.insert_one(myobj)

print(x.inserted_id)