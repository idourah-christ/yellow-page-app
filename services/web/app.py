from distutils.log import debug
from project import create_app 
from config.config import DevelopmentConfig

app = create_app(config=DevelopmentConfig)

if __name__ == '__main__':
    app.run(port=4000, host='0.0.0.0')
   
    