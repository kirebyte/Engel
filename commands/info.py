from telegram import ReplyKeyboardMarkup
from telegram import KeyboardButton
from subprocess import check_output
from subprocess import CalledProcessError
import urllib.request
from utilities.access_manager import is_allowed
from utilities.command_parser import parse_command

COMMAND_NAME = 'info'


def chat_id(bot, update):
    """ Returns chat ID """
    chat_id = update.message.chat_id
    bot.send_message(chat_id=update.message.chat_id, text='Chat ID is %s' % chat_id)


def public_ip(bot, update):
    """ Returns public IP """
    public_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    bot.send_message(chat_id=update.message.chat_id, text='My current external IP is %s' % public_ip)


def private_ip(bot, update):
    """ Returns private IP """
    ip_address = check_output(['hostname', '-I']).decode('utf8')
    bot.send_message(chat_id=update.message.chat_id, text='My LAN IP is %s' % ip_address)


def ssid(bot, update):
    """ Returns network's SSID """
    try:
        wlan_name = check_output(['iwgetid', '-r']).decode('UTF-8')
        wlan_name = wlan_name[:-1]
        bot.send_message(chat_id=update.message.chat_id, text="I'm in %s" % wlan_name)
    except FileNotFoundError:
        bot.send_message(chat_id=update.message.chat_id, text="I'm not connected to a wireless network.")


def user_id(bot, update):
    """ Returns user ID """
    user_id = update.effective_user.id
    bot.send_message(chat_id=update.message.chat_id, text='Your user ID is %s' % user_id)


def help(bot, update):
    """ Returns a list of commands as a custom keyboard for the user """
    keyboard_buttons = []
    for command in commands:
        keyboard_buttons.append([KeyboardButton(text='/%s %s' % (COMMAND_NAME, command))])
    help_arguments = ReplyKeyboardMarkup(keyboard=keyboard_buttons, one_time_keyboard=False)
    bot.send_message(chat_id=update.effective_user.id, text="Here's what I can do for you about /%s " % COMMAND_NAME, reply_markup=help_arguments)


commands = {
                'chat-id': chat_id,
                'public-ip': public_ip,
                'private-ip': private_ip,
                'ssid': ssid,
                'user-id': user_id,
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
