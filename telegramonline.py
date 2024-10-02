import asyncio
from telethon import TelegramClient, events
from telethon.tl.types import UserStatusOffline, UserStatusOnline, PeerUser

# Your Telegram API credentials
api_id = 28444075
api_hash = 'b41b408ae48e6d159ee3e34595ec12a4'
phone = '+91 6382733469'

client = TelegramClient('session_name', api_id, api_hash)

# Variable to track online status
is_online = True

@client.on(events.UserUpdate)
async def handle_user_update(event):
    global is_online
    if isinstance(event.status, UserStatusOffline):
        is_online = False
        print("Status: Offline")
    elif isinstance(event.status, UserStatusOnline):
        is_online = True
        print("Status:Online")
        
@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):
    print("New message received!")  # Debug print
    if isinstance(event.peer_id, PeerUser):  # Check if the message is in a DM (private chat)
        sender = await event.get_sender()  # Get the sender of the message
        user_id = sender.id  # Get the user's ID

        # Constructing the reply message based on availability of the username
        if sender.username:
            sender_name = sender.username
            reply_message = (
                f"𝒉𝒂𝒊 @{sender_name} ! ✨😚\n"
                "@December_born_babe 𝐚𝐰𝐚𝐲 𝐟𝐨𝐫 𝐚 𝐛𝐢𝐭,\n"
                "𝐛𝐮𝐭 𝐢'𝐥𝐥 𝐛𝐞 𝐛𝐚𝐜𝐤 𝐬𝐨𝐨𝐧 😏✨\n"
                "𝐇𝐚𝐧𝐠 𝐭𝐢𝐠𝐡𝐭 𝐟𝐨𝐫 𝐦𝐞 𝐨𝐤𝐚𝐲 ? ✨🙈💗"
            )
        else:
            sender_name = sender.first_name  # Use first name if username is unavailable
            reply_message = (
                f"𝒉𝒂𝒊 {sender_name} ! (ID: {user_id})✨😚\n"
                "@December_born_babe 𝐚𝐰𝐚𝐲 𝐟𝐨𝐫 𝐚 𝐛𝐢𝐭,\n"
                "𝐛𝐮𝐭 𝐢'𝐥𝐥 𝐛𝐞 𝐛𝐚𝐜𝐤 𝐬𝐨𝐨𝐧 😏✨\n"
                "𝐇𝐚𝐧𝐠 𝐭𝐢𝐠𝐡𝐭 𝐟𝐨𝐫 𝐦𝐞 𝐨𝐤𝐚𝐲 ? ✨🙈💗"
            )


async def main():
    await client.start(phone)
    print("Client started!")
    await client.run_until_disconnected()

# Start the asyncio event loop to run the main function
asyncio.run(main())
