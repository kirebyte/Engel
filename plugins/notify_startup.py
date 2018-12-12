import logging

from utilities.config_manager import get_master
from time import sleep
from subprocess import Popen
from urllib import request


def run(updater):
        try:
                request.urlopen('https://www.google.com', timeout=1)
                updater.bot.send_message(chat_id=get_master(), text="Reporting for duty!")
        except:
                sleep(10)
                logging.warning('Internet connection not found, restarting...')
                Popen(['service engel restart'], env={'TERM': 'xterm-256color', 'PATH': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'}, shell=True)
