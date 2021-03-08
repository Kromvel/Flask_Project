#!flask/bin/python
from app import app
if __name__ == '__main__':
    app.debug = True
    app.run(host = '192.168.1.101',port=80)


    