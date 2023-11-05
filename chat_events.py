from flask import session
from extensions import socketio
from quiz_room.routes import room_data
from flask_socketio import send, join_room

@socketio.on("connect", namespace="/chat")
def handle_chat_connect(auth):
    room_code = session.get("room_code")
    name = session.get("name")
    team_code = session.get("team_code")
    join_room(room_code + team_code)
    room_data[room_code]["members"]+=1 

    message = {
        "name" : name,
        "message" : "has joined the chat"
    }
    send(message, to = room_code + team_code, namespace = "/chat")
    print("Client connected")

@socketio.on("message", namespace="/chat")
def handle_chat_message(data):
    room_code = session.get("room_code")
    team_code = session.get("team_code")
    name = session.get("name")
    message = {
        "name" : name ,
        "message": data["data"] 
    }
    room_data[room_code][team_code].append(message)
    # print("SESSION VALUES", name, room_code, score, scores_data)
    # print(room_data)
    # print("Message received " , message)
    send(message, to=room_code + team_code, namespace = "/chat" )