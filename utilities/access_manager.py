from utilities.config_manager import get_master


def is_master(user_id):
    return user_id == get_master()


def is_allowed(user_id, command_name):
    return is_master(user_id)
