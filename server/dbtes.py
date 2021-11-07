import pymongo

myclient = pymongo.MongoClient("mongodb+srv://cristiana25:1qazse4rfvgy7@mbw.jttju.mongodb.net/smarthack?ssl=true&ssl_cert_reqs=CERT_NONE")

mydb = myclient.smarthack
user = mydb.smarthack
print(mydb.list_collection_names())


def new_user(email):
     global user
     user.insert_one(
          { 'email': email, 'passwords': [], 'secrets': [] },
     )