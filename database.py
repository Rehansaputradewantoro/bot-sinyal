import pymongo
from config import MONGO_URI, DATABASE_NAME

client = pymongo.MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

def save_trade(data):
    """Menyimpan data transaksi ke MongoDB"""
    db.trades.insert_one(data)
    print("✅ Data transaksi disimpan.")
