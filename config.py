import configparser, os, shutil, sys

class Config:
    def __init__(self):
        if not os.path.exists('config.ini'):
            shutil.copyfile('example_config.ini', 'config.ini')
            print("Required file \"config.ini\" does not exist.")
            print("Sample file \"example_config.ini\" being created, put the required data in it.")
            sys.exit()
        else:
            config = configparser.ConfigParser()
            config.read('config.ini')

        BOT = config['BOT']
        self.token = BOT['token']
        self.description = BOT['description']
        self.prefix = BOT['prefix']
        self.server = int(BOT['server'])

        def_channels = config['CHANNELS']
        self.owner = int(BOT['owner'])
        self.roles_channel = int(def_channels['roles'])
        #self.welcome_channel = int(def_channels['welcome'])