import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["project2"]
mycol = mydb["cidade"]

myobj = {
    "nome": "Araraquara",
    "empresas": [
        {
            "nome": "Empresa 1",
            "endereco": "Avenida seila, 100",
            "telefone": "16 3333 2222",
            "site": "http://www.siteempresaum.com.br/",
            "linhas": [
                {
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
                },
                {
                    "codigo": 3,
                    "nome": "Linha de um outro lugar",
                    "itinerario": [
                        {
                            "codigo": 22,
                            "descricao": "Logradourasso"
                        },
                        {
                            "codigo": 15,
                            "descricao": "Log Ra Douro"
                        }
                    ],
                    "quadroHorarios": {
                        "diasUteis": ["06:00", "09:00", "12:00", "15:00", "18:00", "21:00"],
                        "sabados": ["08:00", "12:00", "16:00", "20:00"],
                        "domingos": ["10:00", "15:00", "20:00"],
                        "feriados": ["10:00", "15:00", "20:00"]
                    }
                }
            ]
        }
    ]
}

x = mycol.insert_one(myobj)

print(x.inserted_id)