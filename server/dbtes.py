import pymongo

myclient = pymongo.MongoClient("mongodb+srv://cristiana25:1qazse4rfvgy7@mbw.jttju.mongodb.net/smarthack?ssl=true&ssl_cert_reqs=CERT_NONE")

mydb = myclient.smarthack
user = mydb.smarthack
print(mydb.list_collection_names())
user.insert_one(
     { 'email': "testemail@gmail.com", 'passwords': ["1234","4567"], 'secrets': ["aaa","bbb"] },
)
user.insert_one(
     { 'email': "testemail2@gmail.com", 'passwords': ["78910","11234"], 'secrets': ["ccc","ddd"] },
)