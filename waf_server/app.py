from flask.app import Flask
from config import APP_CONFIG
from engine.detection import DetectionEngine

# Intialiasing the flask application
app = Flask(__name__)
config = APP_CONFIG[APP_CONFIG['ENV']]
engine = DetectionEngine(config)

# Registering the sub modules
from tracking import tracking_view
app.register_blueprint(tracking_view)
    
# Setting up logging
import logging
import datetime
import os
date = datetime.datetime.now()
log_dir = config['LOG_DIR']
if not os.path.exists(log_dir):
	os.mkdir(log_dir)
log_file_name = os.path.join(log_dir, "{}{}{}.log".format(date.year, date.month, date.day))
logger = logging.getLogger('werkzeug')
handler = logging.FileHandler(log_file_name)
logger.addHandler(handler)
