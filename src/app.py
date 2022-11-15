from flask import Flask
from src.routes import tasks

app = Flask(__name__)

# * DATABASE CONFIGURATION
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:my-secret-pw@localhost:3306/flaskmsql'
app.config['SQLALCHEMY_TRACK_MOFIDICATIONS'] = False

# * ROUTES
app.register_blueprint(tasks)

