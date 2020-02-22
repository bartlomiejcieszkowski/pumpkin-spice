def is_int(s):
    try:
        int(s)
    except:
        return False
    return True

from fabric import Connection

class SshTransport(object):
    def __init__(self, config):
        self.config = config

    @staticmethod
    def validate(config):
        if 'type' not in config:
            return False
        if config['type'] != 'ssh':
            return False
        if not is_int(config['port']):
            return False
        # validate config
        return True

    @staticmethod
    def generate_default_config():
        return {
            'type' : 'ssh',
            'host' : '127.0.0.1',
            'port' : '22',
            'user' : 'username',
            'authentication' : 'pubkey',
            'authentication_params' : {
                'path' : '.ssh/id_rsa',
                'password' : 'dont_do_this',
            }
        }

    def execute(self, command):
        with Connection(
            self.config['host'],
            user=self.config['user'],
            

        ) as c:
            c.run("uname -a")
        raise NotImplementedError
