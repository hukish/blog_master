import os
class Config:
    '''
    General configuration parent class
    '''

    SECRET_KEY = ('1234')
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
  
    QUOTE_API_BASE_URL = os.environ.get('QUOTE_API_BASE_URL')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hudson:1234@localhost/mblog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
   
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