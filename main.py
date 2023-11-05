from flask import Flask
from config import Config
from main.routes import main
from team_room.routes import team_room 
from quiz_room.routes import quiz_room 
from extensions import sess
from quiz_events import socketio


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(main)
app.register_blueprint(team_room)
app.register_blueprint(quiz_room)


sess.init_app(app)
socketio.init_app(app)

# socketio.run(app, debug=True)

socketio.run(app, host='0.0.0.0', port=3000, debug=True)
