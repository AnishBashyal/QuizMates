import secrets
from flask import Blueprint, render_template, request, redirect, url_for, session

team_room = Blueprint("team_room", __name__)

teams = {}
@team_room.route("/create_team", methods = ["POST"])
def create_team(): 
    name = request.form.get("name")
    team_name = request.form.get("team_name")
    team_code = secrets.token_hex(4)
    session["name"] = name
    session["team_code"] = team_code
    teams[team_code] = [team_name, name]
    return redirect(url_for("quiz_room.home"))

@team_room.route("/join_team", methods=["POST"])
def join_team():
    name = request.form.get("name")
    team_code = request.form.get("team_code")
    session["name"] = name
    session["team_code"] = team_code
    teams[team_code].append(name)
    return redirect(url_for("quiz_room.home"))
