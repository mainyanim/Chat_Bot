"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json
import random
import csv

@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    default = "Sorry, I can't talk about that now."
    user_message = request.POST.get('msg')
    user_message_lst = user_message.split(" ")
    GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up", "heya", "privet")
    GREETING_RESPONSES = ["hey", "nice to meet you", "hello there!", "shalom"]
    SWEAR_WORDS_LIST = ["fuck", "shit"]
    LOVE = ["I", "love", "you"]
    LOVE_LOW = ["i", "love", "you"]
    QUESTION_MARK = ["want"]
    HATE = ["i", "hate", "you"]
    SCARY = ["kill", "stole", "kidnap", "destroy",]
    JOKE = ["joke", "jokes"]
    POLITICS = ["hillary", "trump", "muslims", "vote", "usa"]
    ANIMALS = ["jiraffe", "zebra", "animal", "animals", "cats", "dogs", "mouse", "mice", "dog"]
    ACTIONS = ["dance", "fly", "eat", "cry", "struggle", "hate","learn", "run", "party", "?"]
    AGREE = ["shut", "away", "please", "talk"]
    MOOD = ["happy","excited", "loved", "tired", "?"]
    MOOD_RANDOM = ["how do you think", "take a look on me. really, you ask about it?", "oh yes. 100%."]
    MONEY_MAKE = ["pay", "beer", "winner"]
    IDEAS = ["let's", "idea", "fun", "come"]
    AWESOME = ["high", "fly", "home", "shop"]
    for word in user_message_lst:
        if word.lower() in SWEAR_WORDS_LIST:
            return json.dumps({"animation": "confused", "msg": "Don't talk to me like that!"})
        if word.lower() in GREETING_KEYWORDS:
            return json.dumps({"animation": "excited", "msg": random.choice(GREETING_RESPONSES)})
        if all(x in user_message_lst for x in LOVE) or all(x in user_message_lst for x in LOVE_LOW):
            return json.dumps({"animation": "inlove", "msg": "I love you too, dear!"})
        if any(x in user_message_lst for x in QUESTION_MARK):
            return json.dumps({"animation": "no", "msg": "Sometimes you have to say no"})
        if all(x in user_message_lst for x in HATE):
            return json.dumps({"animation": "heartbroke", "msg": "How could you!"})
        if any(x in user_message_lst for x in SCARY):
            return json.dumps({"animation": "afraid", "msg": "Is it real..?"})
        if any(x in user_message_lst for x in JOKE):
            return json.dumps({"animation": "laughing", "msg": "Three tomatoes are walkin' down the street.Papa Tomato, Mama Tomato and Baby Tomato.Baby Tomato starts lagging behind, and Papa Tomato gets really angry.Goes back and squishes him and says:\"Ketchup.\"Ketchup."})
        if word.lower() in POLITICS:
            return json.dumps({"animation": "dancing", "msg": "Make America Great Again!"})
        if any(x in user_message_lst for x in ANIMALS):
            return json.dumps({"animation": "dog", "msg": "All animals are good, but I love dogs. I have even one, his name is Jerry!"})
        if any(x in user_message_lst for x in ACTIONS):
            return json.dumps({"animation": "dancing", "msg": "Sure, I really love it!"})
        if any(x in user_message_lst for x in AGREE):
            return json.dumps({"animation": "ok", "msg": "Alright, fine, are you happy now?!"})
        if any(x in user_message_lst for x in MOOD):
            return json.dumps({"animation": "crying", "msg": random.choice(MOOD_RANDOM)})
        if any(x in user_message_lst for x in MONEY_MAKE):
            return json.dumps({"animation": "money", "msg": "Awww Yisssss!"})
        if any(x in user_message_lst for x in IDEAS):
            return json.dumps({"animation": "giggling", "msg": "I'm down!"})
        if any(x in user_message_lst for x in AWESOME):
            return json.dumps({"animation": "takeoff", "msg": "I'll be back soon!"})


    #I've been trying to use an external list of names in order to show greeting message according to the person's name,
    #but since we can't change .js file and JSON objects are immutable, I can't add anything to show in "msg" key. So it kinda works and shows greeting message if finds any name from the list given, but without person's name...

    #with open('data/names.csv', 'rt') as f:
    #    reader = csv.reader(f, delimiter=',')
    #    for row in reader:
    #        for field in row:
    #            if field == user_message:
    #                user_input = []
    #                user_input.append(user_message)
    #                GREETING_RESPONSES+=user_input
    #                return json.dumps({"animation": "excited", "msg": random.choice(GREETING_RESPONSES)})



@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
