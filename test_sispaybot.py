import unittest
from telegram import InlineKeyboardButton, InlineKeyboardMarkup  # Add both imports
from unittest.mock import MagicMock
from telegram import Update, User, Message
from sispaybot import start  # Import the function or class you want to test
import asyncio # <---make sure to import asynio--->

class TestSispayBot(unittest.TestCase):
    
    def test_start_command(self):
        # Create a mock update and context
        update = Update(
            update_id=1,
            message=Message(
                message_id=1,
                from_user=User(id=12345, first_name="Test", is_bot=False),
                chat=None, date=None, text='/start'
            )
        )
        
        context = MagicMock()
        
        # Run the start command handler
        asyncio.run(start(update, context))

        # Assert the bot sends the expected response
        context.bot.send_message.assert_called_once_with(
            chat_id=update.message.chat_id,
            text='Hello! Welcome to the bot.'
        )

if __name__ == '__main__':
    unittest.main()

