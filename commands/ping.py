from utilities.access_manager import is_allowed

COMMAND_NAME = 'ping'


def help(bot, update):
    """ Returns the description inside the action function """
    bot.send_message(chat_id=update.effective_user.id, text=action.__doc__)


def action(bot, update):
    """ /ping - Answers the user the ping query. """
    if(is_allowed(update.effective_user.id, COMMAND_NAME)):
        # Print help case
        if(update.message.text.lower() == ('/%s help' % COMMAND_NAME).lower()):
            help(bot, update)
            return 0
    bot.send_message(chat_id=update.effective_user.id, text='Pong!')
