from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

db_client = AsyncIOMotorClient(MONGO_URL)
db = db_client["CriminalsBot"]
flood_collection = db["flood_settings"]
FLOOD_CACHE = {}

async def get_flood_limit(chat_id: int) -> int:
    if chat_id in FLOOD_CACHE: return FLOOD_CACHE[chat_id]
    res = await flood_collection.find_one({"chat_id": chat_id})
    limit = res["limit"] if res else 5
    FLOOD_CACHE[chat_id] = limit
    return limit

async def set_flood_limit_db(chat_id: int, limit: int):
    await flood_collection.update_one({"chat_id": chat_id}, {"$set": {"limit": limit}}, upsert=True)
    FLOOD_CACHE[chat_id] = limit
