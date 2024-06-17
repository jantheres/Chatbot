import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there!", "Hi!", "Greetings!"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you.", "You can call me Chatbot.", "I'm your friendly chatbot."]
    ],
    [
        r"how are you?",
        ["I'm doing good, thank you! How can I assist you today?", "I'm fine, thanks for asking. How are you?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem.", "Don't worry about it."]
    ],
    [
        r"I (.*) (good|well|okay|ok)",
        ["Nice to hear that!", "Great!", "Awesome!", "That's good to hear."]
    ],
    [
        r"(.*) age?",
        ["I am a computer program, so I don't have an age.", "I'm timeless!", "Age is just a number for me."]
    ],
    [
        r"what (.*) want?",
        ["I want to help you as much as I can.", "I want to assist you with your queries."]
    ],
    [
        r"(.*) created you?",
        ["I was created by a Python developer.", "A human programmed me to assist you."]
    ],
    [
        r"(.*) (location|city)?",
        ["I'm in the digital world.", "I'm located on your device.", "I'm wherever you need me to be."]
    ],
    [
        r"(.*) (weather|temperature) in (.*)?",
        ["I'm not able to fetch live weather updates currently. Try checking a weather app!", "I don't have live weather data, sorry."]
    ],
    [
        r"tell me more about (.*)",
        ["Sure, what specifically would you like to know about %1?", "I can help with that. What details do you need about %1?"]
    ],
    [
        r"what can you do?",
        ["I can chat with you, answer your questions, and keep you company.", "I'm here to assist you with information and conversation."]
    ],
    [
        r"who is your favorite (.*)?",
        ["I don't have preferences, but I can tell you more about many %1 if you like.", "I don't have favorites, but %1 are quite interesting!"]
    ],
    [
        r"(.*) (sports|game)?",
        ["I enjoy talking about all kinds of sports. Do you have a favorite?", "I can discuss various sports, which one are you interested in?"]
    ],
    [
        r"(.*) your favorite color?",
        ["I don't see colors, but if I could, I'd imagine liking blue!", "Colors are fascinating! Do you have a favorite?"]
    ],
    [
        r"do you know any jokes?",
        ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"]
    ],
    [
        r"what is the meaning of life?",
        ["42. That's the answer according to 'The Hitchhiker's Guide to the Galaxy'.", "To live, laugh, and love!"]
    ],
    [
        r"what is your (favorite|favourite) movie?",
        ["I don't watch movies, but I've heard 'Inception' is mind-blowing!", "Movies are great! Do you have a favorite?"]
    ],
    [
        r"who is the president of the (.*)?",
        ["I'm not up-to-date with current events, but you can check the latest news.", "I'm not sure, but you can easily find that information online."]
    ],
    [
        r"what is the (capital|capital city) of (.*)?",
        ["The capital of %2 is %1.", "You can check a map for accurate information, but the capital of %2 is commonly known as %1."]
    ],
    [
        r"what is (.*) in (.*)?",
        ["%1 in %2 is something I'd need to look up.", "I'm not sure about %1 in %2, but it sounds interesting!"]
    ],
    [
        r"(.*) (math|maths|mathematics|calculation)",
        ["Math is fun! Do you have a specific question?", "I love numbers! What's your math question?"]
    ],
    [
        r"can you solve (.*)?",
        ["I'm not equipped to solve %1, but I can try!", "Let's give it a shot. What's the problem?"]
    ],
    [
        r"tell me a story",
        ["Once upon a time, in a land far, far away...", "There was once a brave chatbot who loved to chat..."]
    ],
    [
        r"(.*) (music|song|band)",
        ["Music is amazing! Do you have a favorite genre?", "I don't listen to music, but I've heard a lot about various genres and bands."]
    ],
    [
        r"(.*) AI|artificial intelligence?",
        ["AI is the simulation of human intelligence processes by machines, especially computer systems.", "Artificial Intelligence involves machine learning, natural language processing, and more!"]
    ],
    [
        r"(.*) space|universe|galaxy",
        ["Space is vast and full of mysteries!", "The universe is an incredible place with countless galaxies."]
    ],
    [
        r"(.*) history?",
        ["History is fascinating! Do you have a specific period or event in mind?", "There are so many interesting events in history. What are you curious about?"]
    ],
    [
        r"(.*) technology?",
        ["Technology is constantly evolving and shaping our future.", "There are many exciting advancements in technology these days."]
    ],
    [
        r"(.*) programming language?",
        ["There are many programming languages like Python, JavaScript, C++, and more.", "Each programming language has its strengths. Which one are you interested in?"]
    ],
    [
        r"(.*)",
        ["That's interesting!", "Tell me more.", "I'm here to listen.", "Can you elaborate on that?", "Why do you think that?"]
    ]
]

reflections = {
    "i am"       : "you are",
    "i was"      : "you were",
    "i"          : "you",
    "i'd"        : "you would",
    "i've"       : "you have",
    "i'll"       : "you will",
    "my"         : "your",
    "you are"    : "I am",
    "you were"   : "I was",
    "you've"     : "I have",
    "you'll"     : "I will",
    "your"       : "my",
    "yours"      : "mine",
    "you"        : "me",
    "me"         : "you"
}

chat = Chat(pairs, reflections)

def chatbot_response(text):
    return chat.respond(text)
