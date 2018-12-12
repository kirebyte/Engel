from subprocess import Popen
from telegram import ReplyKeyboardMarkup
from telegram import KeyboardButton
from utilities.access_manager import is_allowed
from utilities.command_parser import parse_command
from utilities.config_manager import get_rssh_config

COMMAND_NAME = 'enable'


def rssh(bot, update):
    """ Enables RSSH access """
    rssh_config = get_rssh_config()
    pid = Popen('ssh -NR %s:localhost:%s %s@%s' % (rssh_config['RemotePort'], rssh_config['SshPort'], rssh_config['RemoteUser'], rssh_config['RemoteServer']), env={'TERM': 'xterm-256color', 'PATH': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'}, shell=True).pid
    with open('/tmp/rssh-pid', 'w') as pid_file:
        pid_file.write(str(pid+1))
    bot.send_message(chat_id=update.effective_user.id, text="RSSH access enabled.")


def help(bot, update):
    """ Returns a list of commands as a custom keyboard for the user """
    keyboard_buttons = []
    for command in commands:
        keyboard_buttons.append([KeyboardButton(text='/%s %s' % (COMMAND_NAME, command))])
    help_arguments = ReplyKeyboardMarkup(keyboard=keyboard_buttons, one_time_keyboard=True)
    bot.send_message(chat_id=update.effective_user.id, text="Here's what I can do for you about /%s " % COMMAND_NAME, reply_markup=help_arguments)


commands = {
                'rssh':          rssh,
                'help':         help
}


def action(bot, update):
    """ Loads dynamically the commands as it parses the string """
    if(is_allowed(update.effective_user.id, COMMAND_NAME)):
        arguments = parse_command(COMMAND_NAME, update.message.text)
        for command in commands:
            if command in arguments:
                commands[command](bot, update)
                arguments.remove(command)
