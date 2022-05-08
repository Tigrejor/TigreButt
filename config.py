import configparser, os, shutil, sys

class Config:
    def __init__(self):
        # Check if config.ini exists, if it doesn't copy from example_config.ini
        if not os.path.exists('config.ini'):
            shutil.copyfile('example_config.ini', 'config.ini')
            print("Required file \"config.ini\" does not exist.")
            print("Sample file \"example_config.ini\" copied, put the required data in \"config.ini\".")
            sys.exit()
        else:
            config = configparser.ConfigParser()
            config.read('config.ini')

        # Defining al config options from config.ini
        BOT = config['BOT']
        self.token = BOT['token']
        self.description = BOT['description']
        self.prefix = BOT['prefix']
        self.server = int(BOT['server'])

        def_channels = config['CHANNELS']
        self.owner = int(BOT['owner'])
        self.roles_channel = int(def_channels['roles'])
        #self.welcome_channel = int(def_channels['welcome'])