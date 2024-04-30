from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import routes
from models import Program, Artifact
from config import Config
from apscheduler.schedulers.background import BackgroundScheduler
from utils import check_for_new_commits
import atexit
from database import db

app = Flask(__name__)
app.register_blueprint(routes)
app.config.from_object(Config)
db.init_app(app)


scheduler = BackgroundScheduler()
scheduler.add_job(func=check_for_new_commits, trigger="interval", seconds=120)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))