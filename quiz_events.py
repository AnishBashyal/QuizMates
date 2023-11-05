from flask import session
from chat_events import socketio
from quiz_room.routes import room_data, scores_data, attempts
from team_room.routes import teams
from flask_socketio import emit, join_room
from quiz_db import quiz_list
 
questions, answers = quiz_list()

current_index  = 0
def teams_codes_finder(room_code):
    arr =  list(room_data[room_code].items())
    ans = []
    for i in arr:
        if i[0] != "members":
            ans.append(i[0])
    return ans

@socketio.on("connect", namespace="/quiz")
def handle_quiz_connect(auth):
    room_code = session.get("room_code")
    join_room(room_code)
    # print("Player connected")
    emit("displayQuestion", {"question":questions[current_index]}, to= room_code, namespace="/quiz")
    team_codes = teams_codes_finder(room_code)
    # print(team_codes)
    emit("displayTable", [scores_data[room_code], teams, team_codes], to=room_code, namespace="/quiz")

@socketio.on("nextQuestion", namespace="/quiz")
def handle_next_question():
    print("NextQuestionPythoncalledby", session.get("name"))
    global current_index
    room_code = session.get("room_code")
    if current_index < len(questions) - 1:
        current_index += 1
        # print("Increased current_index", current_index)
        emit("displayQuestion", {"question":questions[current_index]}, to = room_code, namespace="/quiz")
 

@socketio.on("answer", namespace="/quiz")
def handle_answer(data):
    global current_index
    room_code = session.get("room_code")
    team_code = session.get("team_code")
    guess_answer = data["data"]
    team_codes = teams_codes_finder(room_code)

    if attempts[team_code] <= 0:
        emit("alert", {"message": "You reached max attempts for this question", "category" : "warning"}, to= room_code, namespace="/quiz")
        return
    attempts[team_code] -= 1
    if guess_answer.lower() == answers[current_index].lower():
        for code in team_codes:
            attempts[code] = 3
        scores_data[room_code][team_code] += 1
        emit("alert", {"message": str(teams[team_code][0]) + " guessed it correct", "category" : "success"}, to= room_code, namespace="/quiz")
        emit("displayTable", [scores_data[room_code], teams, team_codes], to=room_code, namespace="/quiz")
    #    emit("nextQuestion",{}, to = room_code, namespace = "/quiz")
       
        if current_index == len(answers) -1: 
            maxC = -1
            winner = ""
            dup = False
            print("ATEMPTS", attempts)
            for code in team_codes:
                if scores_data[room_code][code] > maxC:
                    maxC = scores_data[room_code][code]
                    winner = teams[code][0] 
                    dup = False
                elif scores_data[room_code][code] == maxC:
                    dup = True
            print("ATEMPTS2", attempts)
            if dup:
                emit("alert", {"message":"It's a draw!", "category" : "success"}, to= room_code, namespace="/quiz")
            else:
                emit("alert", {"message":"Winning team is " + winner, "category" : "success"}, to= room_code, namespace="/quiz")
            emit("alert", {"message": "Quiz ended!", "category":"info"}, to = room_code, namespace="/quiz")
            current_index = 0
        else:
            current_index += 1
            emit("displayQuestion", {"question":questions[current_index]}, to = room_code, namespace="/quiz")
            # print("Increased current_index", current_index)


    else:
        emit("alert", {"message": str(teams[team_code][0]) + " guessed it incorrect", "category" : "danger"}, to= room_code, namespace="/quiz")
    # print("SESSION VALUES", name, room_code, score, scores_data)
