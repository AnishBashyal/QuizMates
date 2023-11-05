import firebase_admin 
from firebase_admin import db, credentials


cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://quizmates-a94cc-default-rtdb.firebaseio.com"})


def quiz_list():
    ref = db.reference('/Quizes/History/Quiz 1')
    data = ref.get()

    qs_list = []
    ans_list = []

    for id, x in data.items():
        qs_list.append(x['quiz_qs'])
        ans_list.append(x['quiz_ans'])
    return [qs_list, ans_list]

