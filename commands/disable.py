from subprocess import run
from telegram import ReplyKeyboardMarkup
from telegram import KeyboardButton
from utilities.access_manager import is_allowed
from utilities.command_parser import parse_command

COMMAND_NAME = 'disable'


def rssh(bot, update):
    """ Disables RSSH access """
    try:
        with open('/tmp/rssh-pid', 'r') as pid_file:
            pid = pid_file.readline()
            if (run(['kill', '%s' % pid]).returncode == 0):
                bot.send_message(chat_id=update.effective_user.id, text="RSSH closed.")
    except FileNotFoundError:
        bot.send_message(chat_id=update.effective_user.id, text="RSSH was not enabled.")


def help(bot, update):
    """ Returns a list of commands as a custom keyboard for the user """
    keyboard_buttons = []
    for command in commands:
        keyboard_buttons.append([KeyboardButton(text='/%s %s' % (COMMAND_NAME, command))])
    help_arguments = ReplyKeyboardMarkup(keyboard=keyboard_buttons, one_time_keyboard=True)
    bot.send_message(chat_id=update.effective_user.id, text="Here's what I can do for you about /%s " % COMMAND_NAME, reply_markup=help_arguments)


commands = {
                'rssh': rssh,
                'help': help
}


def action(bot, update):
    """ Loads dynamically the commands as it parses the string """
    if(is_allowed(update.effective_user.id, COMMAND_NAME)):
        arguments = parse_command(COMMAND_NAME, update.message.text)
        for command in commands:
            if command in arguments:
                commands[command](bot, update)
                arguments.remove(command)
