from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

client = MongoClient("mongodb://localhost:27017/")
db = client["meu_banco"]
colecao = db["minha_colecao"]
