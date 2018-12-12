#!./lib/bin/python3
import logging
import signal
from sys import exit
from importlib import import_module
from telegram.ext import CommandHandler, Updater, MessageHandler
from threading import Thread
from utilities.config_manager import get_token
from utilities.config_manager import get_loglevel
from utilities.module_manager import scan_modules

updater = None


def initialize():
    logging.basicConfig(filename='/var/log/engel.log', level=get_loglevel(), format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    global updater
    updater = Updater(token=get_token(), user_sig_handler=sigint_handler)


def sigint_handler(sig, frame):
    if(sig == signal.SIGINT):
        exit()


def load_commands():
    """ Scans the commands folder and loads each one in a loop"""
    command_modules = scan_modules('commands')
    dispatcher = updater.dispatcher
    for module in command_modules:
        new_command_module = import_module(module)
        new_command_handler = CommandHandler(new_command_module.COMMAND_NAME, new_command_module.action)
        dispatcher.add_handler(new_command_handler)
        logging.info('Loading %s...' % module)


def load_responses():
    """ Scans the responses folder and loads each one in a loop"""
    response_modules = scan_modules('responses')
    dispatcher = updater.dispatcher
    for module in response_modules:
        new_response_module = import_module(module)
        new_response_handler = MessageHandler(new_response_module.FILTER_TYPE, new_response_module.action)
        dispatcher.add_handler(new_response_handler)
        logging.info('Loading %s...' % module)


def load_plugins():
    """ Scans the plugins folder and loads each one in a loop"""
    response_modules = scan_modules('plugins')
    for module in response_modules:
        new_plugin_module = import_module(module)
        thread = Thread(target=new_plugin_module.run, args=([updater]))
        thread.start()
        logging.info('Loading %s...' % module)


def main():
    initialize()
    load_commands()
    logging.info('Loading commands complete!')
    load_responses()
    logging.info('Loading responses complete!')
    load_plugins()
    logging.info('Loading plugins complete!')
    updater.start_polling()
    updater.idle()


main()
