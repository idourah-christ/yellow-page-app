from distutils.log import debug
from project import create_app 
from config.config import DevelopmentConfig
import logging

app = create_app(config=DevelopmentConfig)

if __name__ == '__main__':
    
    app.run(port=4000, host='0.0.0.0')
    logging.debug(app.config["SQLALCHEMY_DATABASE_URI"])
    