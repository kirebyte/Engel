from utilities.module_manager import scan_modules
from telegram import ReplyKeyboardMarkup
from telegram import KeyboardButton
from utilities.access_manager import is_allowed

COMMAND_NAME = 'help'


def help(bot, update):
    """ Returns the description inside the action function """
    bot.send_message(chat_id=update.effective_user.id, text=action.__doc__)


def action(bot, update):
    """ Returns all available commands. """
    if(is_allowed(update.effective_user.id, COMMAND_NAME)):
        # Print help case
        if(update.message.text.lower() == ('/%s help' % COMMAND_NAME).lower()):
            help(bot, update)
            return 0
        commands = scan_modules('commands')
        commands.remove('commands.help')
        keyboard_buttons = []
        for command in commands:
            trimmed_command = command.replace('commands.', '')
            keyboard_buttons.append([KeyboardButton(text='/%s help' % trimmed_command)])
        help_arguments = ReplyKeyboardMarkup(keyboard=keyboard_buttons, one_time_keyboard=True)
        bot.send_message(chat_id=update.effective_user.id, text="These are the available commands.", reply_markup=help_arguments)
