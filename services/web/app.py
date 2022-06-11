from project import create_app 
import logging

app = create_app(config="config.dev")

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')