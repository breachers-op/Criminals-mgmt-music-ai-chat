import asyncio
from pyrogram import Client

async def generate_session():
    print("--- Criminals Music AI - Session Generator ---")
    print("Get your API_ID and API_HASH from https://my.telegram.org\n")
    
    try:
        api_id = int(input("Enter API_ID: "))
        api_hash = input("Enter API_HASH: ")
    except ValueError:
        print("\nError: API_ID must be a number.")
        return

    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        session_str = await app.export_session_string()
        
        # Send to Saved Messages for safety
        await app.send_message(
            "me", 
            f"**Criminals Music AI - Session String**\n\n`{session_str}`\n\n"
            "⚠️ **Keep this secret!** Anyone with this string can access your account."
        )
        
        print("\n" + "="*50)
        print("SESSION STRING GENERATED SUCCESSFULLY!")
        print("="*50)
        print(f"\n{session_str}\n")
        print("="*50)
        print("\nNOTE: The string has also been sent to your Telegram Saved Messages.")

if __name__ == "__main__":
    asyncio.run(generate_session())
