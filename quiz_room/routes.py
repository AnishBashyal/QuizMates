import secrets
from flask import Blueprint, render_template, request, redirect, url_for, session
from team_room.routes import teams

quiz_room = Blueprint("quiz_room", __name__)

room_data = {}
scores_data = {}
attempts = {}
@quiz_room.route("/quiz/home")
def home():
    return render_template("quiz_home.html", title = "Quiz Home", team_code = session.get("team_code"), teams = teams, user = session.get("name"))

@quiz_room.route("/view_room")
def view_room():
    room_code = session.get("room_code")
    team_code = session.get("team_code")

    return render_template("room.html", room_code = room_code, team_messages = room_data[room_code][team_code])

@quiz_room.route("/create_room", methods = ["POST"])
def create_room(): 
    room_code = secrets.token_hex(4)
    team_code = session.get("team_code")
    
    session["room_code"] = room_code
    session["score"] = 0
    scores_data[room_code] = {team_code:0}
    room_data[room_code] = {
        'members' : 0,
        team_code : []
    }
    attempts[team_code] = 3
    return redirect(url_for("quiz_room.view_room"))

@quiz_room.route("/join_room", methods = ["POST"])
def join_room(): 
    room_code = request.form.get("room_code")
    team_code = session.get("team_code")
    
    session["room_code"] = room_code
    session["score"] = 0
    attempts[team_code] = 3
    if not room_data[room_code].get(team_code):
        room_data[room_code][team_code] = []
    if not scores_data[room_code].get(team_code):
        scores_data[room_code][team_code] = 0
    return redirect(url_for("quiz_room.view_room"))