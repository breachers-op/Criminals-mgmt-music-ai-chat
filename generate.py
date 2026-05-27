import asyncio
from hydrogram import Client

async def gen():
    print("\n--- Hydrogram Session Generator ---")
    i = int(input("Enter API_ID: "))
    h = input("Enter API_HASH: ")
    async with Client(":memory:", api_id=i, api_hash=h, in_memory=True) as app:
        s = await app.export_session_string()
        print(f"\n✅ SESSION STRING:\n\n{s}\n")
        await app.send_message("me", f"**Session String:**\n`{s}`")

if __name__ == "__main__":
    asyncio.run(gen())
