def parse_command(command_name, command_string):
    stripped_command = trimm_command(command_name, command_string).split()
    return stripped_command


def trimm_command(command_name, command_string):
    trimmed_command = command_string.replace('/%s' % command_name, '')
    trimmed_command = command_string.replace('/%s' % command_name.lower(), '')
    trimmed_command = trimmed_command.strip()
    return trimmed_command
