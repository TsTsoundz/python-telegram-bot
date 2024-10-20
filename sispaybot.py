from telegram import Update
from telegram.ext import Application, CommandHandler

# Dictionary to store user points and tasks
user_data = {}

# Function to initialize the bot and send the initial interface
def start(update, context):
    user_id = update.message.from_user.id
    
    # Initialize user data if not exists
    if user_id not in user_data:
        user_data[user_id] = {'points': 0, 'completed_tasks': [], 'tasks': ['Task One', 'Task Two']}
    
    # Show the user interface
    update.message.reply_text(generate_ui(user_id))

# Generate the user interface
def generate_ui(user_id):
    points = user_data[user_id]['points']
    
    # Display user's points and available tasks
    task_buttons = []
    for task in user_data[user_id]['tasks']:
        task_buttons.append([InlineKeyboardButton(task, callback_data=f'complete_task|{task}')])
    
    # Add a claim points button
    task_buttons.append([InlineKeyboardButton('Claim Points', callback_data='claim_points')])
    
    message = f"SISPAY\nBalance: {points:.2f} pts\nNGN Equivalent: {points * 10:.2f} NGN\n\nToday's Tasks:"
    
    # Create a markup with task buttons
    return message, InlineKeyboardMarkup(task_buttons)

# Function to handle task completion
def complete_task(update, context):
    query = update.callback_query
    user_id = query.from_user.id
    _, task = query.data.split('|')
    
    # Check if task is already completed
    if task not in user_data[user_id]['completed_tasks']:
        user_data[user_id]['completed_tasks'].append(task)
        query.answer(f"You completed {task}!")
    else:
        query.answer(f"You already completed {task}.")
    
    # Update the UI
    query.edit_message_text(text=generate_ui(user_id)[0], reply_markup=generate_ui(user_id)[1])

# Function to handle point claiming
def claim_points(update, context):
    query = update.callback_query
    user_id = query.from_user.id
    
    # Points for each completed task
    points_earned = len(user_data[user_id]['completed_tasks']) * 10
    
    # Add points to user's balance and reset tasks
    user_data[user_id]['points'] += points_earned
    user_data[user_id]['completed_tasks'] = []
    
    query.answer(f"You claimed {points_earned} points!")
    
    # Update the UI
    query.edit_message_text(text=generate_ui(user_id)[0], reply_markup=generate_ui(user_id)[1])

def main():
    # Use your bot's API token here
    TOKEN = '7731390622:AAH312X60WCTKLT0qH277b1I9u3XR8isT4I'
    
    async def start(update: Update, context) -> None:
        
        await update.message.reply_text('Hello! Welcome to the bot.')

def main():
    # Create the Application object using the token
    application = Application.builder().token('7731390622:AAH312X60WCTKLT0qH277b1I9u3XR8isT4I').build()

    # Register the /start command
    application.add_handler(CommandHandler('start', start))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
    
    # Command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    
    # Callback handlers for task completion and claiming points
    dispatcher.add_handler(CallbackQueryHandler(complete_task, pattern='complete_task'))
    dispatcher.add_handler(CallbackQueryHandler(claim_points, pattern='claim_points'))
    
    # Start polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

