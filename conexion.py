from pymongo import MongoClient
from futbolista import Futbolista

# PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
mongoClient = MongoClient('localhost',27017)

# PASO 2: Conexión a la base de datos
db = mongoClient.futbol_db