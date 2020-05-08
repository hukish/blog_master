import os
class Config:
    '''
    General configuration parent class
    '''

    SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
  
    QUOTE_API_BASE_URL = os.environ.get('QUOTE_API_BASE_URL')
   
class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")



class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config : the parent configuration class with General configuration settings
    '''
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}