import configparser
import logging
from pathlib import Path

config = configparser.ConfigParser()
config_file_path = '/etc/opt/engel/config'


def get_token():
    """ Retrieves bot's token from configuration file """
    config_file = Path(config_file_path)
    if not config_file.is_file():
        logging.critical('Config file not found, shutting down.')
        exit()
    config.read(config_file_path)
    if not config.has_section('INFO'):
        logging.critical('Section Info missing, shutting down.')
        exit()
    if not config.has_option('INFO', 'token'):
        logging.critical('Token configuration inside INFO section missing, shutting down.')
        exit()
    return config['INFO']['token']


def get_master():
    """ Retrieves user ID's with master permissions """
    config_file = Path(config_file_path)
    if not config_file.is_file():
        logging.critical('Config file not found, shutting down.')
        exit()
    config.read(config_file_path)
    if not config.has_section('INFO'):
        logging.critical('Section Info missing, shutting down.')
        exit()
    if not config.has_option('INFO', 'master'):
        logging.critical('Master configuration inside INFO section missing, shutting down.')
        exit()
    return int(config['INFO']['master'])


def get_loglevel():
    """ Retrieves the default log level"""
    config_file = Path(config_file_path)
    if not config_file.is_file():
        logging.critical('Config file not found, shutting down.')
        exit()
    config.read(config_file_path)
    if not config.has_section('LOG'):
        logging.critical('Section Log missing, shutting down.')
        exit()
    if not config.has_option('LOG', 'LogLevel'):
        logging.critical('LogLevel configuration inside LOG section missing, shutting down.')
        exit()
    return int(config['LOG']['LogLevel'])


def get_rssh_config():
    """ Retrieves the RSSH configuration """
    config_file = Path(config_file_path)
    if not config_file.is_file():
        logging.critical('Config file not found, shutting down.')
        exit()
    config.read(config_file_path)
    if not config.has_section('RSSH'):
        logging.critical('Section RSSH missing, shutting down.')
        return None
    if not config.has_option('RSSH', 'RemotePort'):
        logging.critical('RemotePort configuration inside LOG section missing, shutting down.')
        return None
    if not config.has_option('RSSH', 'SshPort'):
        logging.critical('SshPort configuration inside LOG section missing, shutting down.')
        return None
    if not config.has_option('RSSH', 'RemoteUser'):
        logging.critical('RemoteUser configuration inside LOG section missing, shutting down.')
        return None
    if not config.has_option('RSSH', 'RemoteServer'):
        logging.critical('RemoteServer configuration inside LOG section missing, shutting down.')
        return None
    rssh_config = {}
    rssh_config['RemotePort'] = config['RSSH']['RemotePort']
    rssh_config['SshPort'] = config['RSSH']['SshPort']
    rssh_config['RemoteUser'] = config['RSSH']['RemoteUser']
    rssh_config['RemoteServer'] = config['RSSH']['RemoteServer']
    return rssh_config
