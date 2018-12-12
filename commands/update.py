from subprocess import Popen
from utilities.access_manager import is_allowed

COMMAND_NAME = 'update'


def help(bot, update):
    """ Returns the description inside the action function """
    bot.send_message(chat_id=update.effective_user.id, text=action.__doc__)


def action(bot, update):
    """ Requests the engel to restart itself. """
    if(is_allowed(update.effective_user.id, COMMAND_NAME)):
        # Print help case
        if(update.message.text.lower() == ('/%s help' % COMMAND_NAME).lower()):
            help(bot, update)
            return 0
        bot.send_message(chat_id=update.effective_user.id, text='Update in progress.')
        Popen(['/usr/bin/at now -f /opt/engel/integrations/updater/update_wrapper.sh'], env={'TERM': 'xterm-256color', 'PATH': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'}, shell=True)
