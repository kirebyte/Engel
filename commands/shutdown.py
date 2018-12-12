from subprocess import run
from utilities.access_manager import is_allowed

COMMAND_NAME = 'shutdown'


def help(bot, update):
    """ Returns the description inside the action function """
    bot.send_message(chat_id=update.effective_user.id, text=action.__doc__)


def action(bot, update):
    """ Requests the engel to shutdown itself. """
    if(is_allowed(update.effective_user.id, COMMAND_NAME)):
        # Print help case
        if(update.message.text.lower() == ('/%s help' % COMMAND_NAME).lower()):
            help(bot, update)
            return 0
        bot.send_message(chat_id=update.message.chat_id, text='Shutting down.')
        run(['poweroff', '-p'])
