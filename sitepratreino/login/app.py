from pymongo import MongoClient
import bcrypt

cliente = MongoClient("mongodb+srv://kevinburgos0709_db_user:kevin2006.0709@cluster0.nlkatoo.mongodb.net/?appName=Cluster0")

db = cliente["info"]
usuario = db["usuarios"]
usuario.create_index("email", unique=True)



