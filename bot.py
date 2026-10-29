import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, ChatMemberHandler, ContextTypes

MY_LINK = "https://t.me/MNaimislamBot"

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = update.chat_member
    old_status = result.old_chat_member.status
    new_status = result.new_chat_member.status
    
    if old_status in ['left', 'kicked'] and new_status in ['member', 'administrator']:
        new_member = result.new_chat_member.user
        chat_name = result.chat.title
        
        text = f"Welcome {new_member.mention_html()} to {chat_name}! 🎉"
        
        button = [[InlineKeyboardButton("Contact Admin", url=MY_LINK)]]
        
        await context.bot.send_message(
            chat_id=result.chat.id,
            text=text,
            reply_markup=InlineKeyboardMarkup(button),
            parse_mode="HTML"
        )

def main():
    token = os.environ.get("BOT_TOKEN")
    app = Application.builder().token(token).build()
    app.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))
    app.run_polling()

if __name__ == "__main__":
    main()
