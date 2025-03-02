import random
import os

class RiddleGame:
    def __init__(self):
        # List of riddles with their answers and hints
        self.riddles = [
            {
                "question": "What is always in front of you but can't be seen?",
                "answer": "future",
                "hints": [
                    "It's the time that is yet to come.",
                    "You can't touch it, but you know it's coming."
                ]
            },
            {
                "question": "I can talk, but I don't have a mouth. I can listen, but I don't have ears. What am I?",
                "answer": "telephone",
                "hints": [
                    "You use it to communicate.",
                    "It allows you to talk to someone far away."
                ]
            },
            {
                "question": "I am always hungry, but I never eat. I drink a lot, but never thirst. What am I?",
                "answer": "fire",
                "hints": [
                    "It can be dangerous if not controlled.",
                    "It needs oxygen to keep burning."
                ]
            },
            {
                "question": "I can't move, but I always move forward. What am I?",
                "answer": "time",
                "hints": [
                    "It keeps ticking even if you don't notice.",
                    "It’s often measured in hours, minutes, and seconds."
                ]
            },
            {
                "question": "The more of this there is, the less you see. What is it?",
                "answer": "darkness",
                "hints": [
                    "It's the opposite of light.",
                    "When the sun sets, it appears."
                ]
            },
            {
                "question": "What has keys but can't open locks?",
                "answer": "piano",
                "hints": [
                    "It makes sound when played.",
                    "You play it by pressing black and white keys."
                ]
            },
            {
                "question": "What has a head, a tail, but no body?",
                "answer": "coin",
                "hints": [
                    "It's something you flip.",
                    "It has two sides, heads and tails."
                ]
            },
            {
                "question": "What can travel around the world while staying in the corner?",
                "answer": "stamp",
                "hints": [
                    "It sticks to something to help it travel.",
                    "You place it on envelopes."
                ]
            },
            {
                "question": "I am tall when I am young, and I am short when I am old. What am I?",
                "answer": "candle",
                "hints": [
                    "I provide light.",
                    "I burn down as I age."
                ]
            },
            {
                "question": "What has a heart that doesn't beat?",
                "answer": "artichoke",
                "hints": [
                    "It's a vegetable.",
                    "It’s often used in cooking."
                ]
            },
            {
                "question": "The more you take, the more you leave behind. What am I?",
                "answer": "footsteps",
                "hints": [
                    "You leave these when you walk.",
                    "They are left in the sand or snow."
                ]
            },
            {
                "question": "What comes down but never goes up?",
                "answer": "rain",
                "hints": [
                    "It falls from the sky.",
                    "It’s often part of a weather forecast."
                ]
            },
            {
                "question": "What can be cracked, made, told, and played?",
                "answer": "joke",
                "hints": [
                    "It makes people laugh.",
                    "People often tell them to lighten the mood."
                ]
            },
            {
                "question": "What has one eye but can't see?",
                "answer": "needle",
                "hints": [
                    "It's used in sewing.",
                    "It’s sharp at one end and used with thread."
                ]
            },
            {
                "question": "What begins with T, ends with T, and has T in it?",
                "answer": "teapot",
                "hints": [
                    "You use this to make tea.",
                    "It has a handle and a spout."
                ]
            },
            {
                "question": "What is full of holes but still holds a lot of weight?",
                "answer": "sieve",
                "hints": [
                    "You use it in cooking to strain liquids.",
                    "It’s often made of metal or plastic."
                ]
            },
            {
                "question": "What has hands but can't clap?",
                "answer": "clock",
                "hints": [
                    "It helps you keep track of time.",
                    "It usually has numbers and moving hands."
                ]
            },
            {
                "question": "What has a neck but no head?",
                "answer": "bottle",
                "hints": [
                    "You can fill it with liquids.",
                    "It has a narrow opening at the top."
                ]
            },
            {
                "question": "What can you catch but not throw?",
                "answer": "cold",
                "hints": [
                    "It makes you feel unwell.",
                    "You can catch it from others, especially in winter."
                ]
            }
        ]
        self.score = 0
        self.hint_counter = {}

        # ASCII art
        self.question_mark_art = """
             ________
        _jgN########Ngg_
      _N##N@@""  ""9NN##Np_
     d###P            N####p
     "^^"              T####
                       d###P
                    _g###@F
                 _gN##@P
               gN###F"
              d###F
             0###F
             0###F
             0###F
             "NN@'

              ___
             q###r
              ""
        """
        self.fox_art = """
        /\   /\  
       //\_//\     ____
       \_     _/    /   /
        / * * \    /^^^]
        \_\O/_/    [   ]
         /   \_    [   /
         \     \_  /  /
          [ [ /  \/ _/
         _[ [ \  /_/  
        """
        self.rose_art = """
        .      .'
            :`...' `.,'  ' 
        `.  ' .**.  ; ; ':
        ` ``:`****,'  .' :
    ..::.  ``**":.''   `.
    .:    `: ; `,'        :
    `:    `   :         ;
        :   :   :        ;
        :    :   :     .:
        :    :   :..,'  ``::.
        `....:..'  ..:;''
        .:   . ...::::
        ,'''''``:::::::
                `::::
                    `::.
                    `::
            . ,.    ::::'      ,.. 
            .'.'  ``.  ::      .'.. `.
            '        .: ::    ,'.'     .
        .' ,'    .::::::   ,.'    .:::.
        .' .'  ..:'     ::: .,   .;'     ~
    ,;::;.::''        ::.:..::'
    ~                  ::;'
                        ::
                    ,:::
                        ::.
                        `::
                        ::
                        ::
                        ::
                        ::
                        ::
                        ::
                        ::
        """
        self.mushroom_art = """
        ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⡶⢶⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⣀⠴⠛⠛⠉⠄⠀⠀⠀⠀⠀⠀⠀⠈⠑⠒⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⣤⡊⠁⣀⣤⣄⣤⣤⣤⣀⣤⣤⣤⣀⣤⣠⣶⣠⣀⠉⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⡠⠋⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠐⣡⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡹⣽⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣟⣀⣠⡤⠶⢄⡀⠲⢄⠀⠀⠀⠀⠀⠀
        ⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡴⠶⣾⣿⣿⣿⣿⡿⠛⠛⠉⠉⠁⠀⠉⠀⠀⠀⠀⠈⠉⠒⢷⣄⠀⠀⠀⠀
        ⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠘⣿⡿⢿⣯⣶⣶⣶⣶⣠⣴⣂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀
        ⠀⠀⠀⠀⠀⠉⠉⠉⠛⠋⠉⠉⡀⠀⠀⠹⡀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣺⢶⣶⣤⣀⡀⠀⠀⠘⣆⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠂⣧⠀⠀⠉⠛⠻⠿⣿⣿⣿⣿⠟⠉⠛⣾⣿⣿⣷⣶⣄⡀⠘⢆⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠈⠉⢻⠏⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣶⣼⡆
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠰⣖⠾⢧⣴⣲⣿⡏⠉⠛⠛⠻⠿⠿⣿⠿⠃
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠄⠀⢄⣧⠀⠀⠀⠀⠀⠀⠈⢹⠷⣶⡿⣯⣵⡤⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⡀⢆⢠⣿⠀⠀⠀⠀⠀⠀⡰⠋⠠⣿⣷⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⠿⡿⢹⣿⣆⠀⠀⠀⠀⡰⠉⠉⢹⡟⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣖⠘⣾⣹⡇⠀⠀⠀⡸⠁⠀⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣨⣾⣿⣧⡀⠀⠀⣇⠐⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢛⣿⠿⣄⣾⢷⠦⠀⢸⡿⢧⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢀⣿⣟⡾⢿⣿⣷⢽⡍⢷⣯⣿⠓⢤⣒⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⢠⣴⡶⣀⠀⠀⢸⡽⠂⢸⣿⣽⣻⣿⣤⣾⣿⣿⣿⣿⣄⡀⡸⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠈⠉⠫⡁⠀⢻⠿⢷⣤⣿⣿⣶⣿⣿⣿⣯⣿⣻⣿⣿⣶⣠⣳⠀⠀⠐⣿⡿⠄⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠘⠲⠞⠒⠛⠛⠛⠛⠛⠋⠻⠛⠓⠛⠛⠛⠛⠛⠛⠓⠚⠓⠛⠛⠂⠀⠀⠀⠀⠀⠀⠀
        """
        self.sheep_art = r"""
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡿⠿⢿⣦⡀⢀⣴⡿⠿⠿⢷⣄⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠁⠀⠀⠀⠙⢿⡿⠋⠀⠀⠀⠈⢿⣦⡾⠟⠋⠻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡶⠾⠿⢶⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⠁⠀⠀⠀⣿⣗⣤⣤⣀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⣠⣤⡴⠶⠒⠒⠲⢦⣤⡀⠀⠀⠀⠀⠀⣴⡿⠉⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠉⠉⢿⡆⠀⠀⠀⠀⠀
            ⠀⣤⡞⠋⠁⠀⠀⠀⠀⠀⠀⡈⢙⣷⣴⡶⠶⠶⠿⢷⣦⣄⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀
            ⢠⣿⠀⠀⠀⠀⠀⢀⣀⣤⣤⣶⣿⡋⠁⠀⠀⠀⠀⠀⠈⠙⢷⣄⢀⣤⡶⠞⠋⠉⠉⠙⠛⠲⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡿⠷⠶⣶⣄⠀⠀
            ⠀⠙⠿⢦⣤⡴⠾⠋⠁⣰⣿⣿⠟⠛⠛⠿⣦⠀⣀⣀⣀⣀⡀⠿⣿⡁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⣼⢟⢸⡇⠀⡀⣤⣄⣹⡿⠯⠁⠀⠈⠻⣦⣸⣿⠛⠛⠻⠶⣤⣀⠀⠀⠀⢀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⣼⡟⠀⠸⣷⣄⠀⢟⣇⣿⡇⣾⣷⠀⠀⠀⢸⡟⣿⡄⠀⠀⠀⠀⠈⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠻⠿⣷⣆
            ⠀⠀⠀⠀⠀⠀⣼⡟⠐⠀⠀⠀⠉⠛⠛⠉⠸⣧⣈⠁⠀⠀⣠⡾⠃⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿
            ⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠓⠒⠚⠋⠀⢀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡾⠟
            ⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣯⡥⠀
            ⠀⠀⠀⠀⠀⢸⣿⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀
            ⠀⠀⠀⠀⠀⠸⣿⡄⠀⣿⡟⠀⣴⣤⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣶⡿⠆
            ⠀⠀⠀⠀⠀⠀⠙⣿⣆⠊⠁⠀⠉⠉⠀⠀⠀⠀⠀⣠⣶⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⣿⡉⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠈⠻⢷⣤⣤⣤⣤⣤⣤⣶⢾⣿⣯⣥⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⢀⣿⠇⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⣹⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠻⠟⠋⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⣤⣴⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⢀⣿⡄⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡁⠀⢀⣴⣶⠀⠀⠀⢠⠀⠀⠀⢀⣄⠀⠀⠀⢸⣧⠀⠀⠀⣿⣿⣶⡾⠋⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡇⠻⡿⢻⣿⣿⡀⢀⣴⣿⣇⠀⢀⣾⣿⣶⣤⣤⣿⣿⣷⣶⣾⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⣇⠀⣇⢸⡇⠉⠙⠛⠉⠘⠛⠿⠛⠋⠀⠉⠉⠉⢹⣯⣷⠀⢻⡘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢻⠀⣿⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⣿⣿⡆⠸⡇⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣿⢸⡇⢹⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⣟⣫⣼⠟⠃⠀⣷⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣟⣫⣴⠾⠟⠁⢸⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠁⠀⠀⠀⠀⣿⡠⣿⡀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⠀⠀⠀⠀⢸⡄⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠾⠟⣋⣤⡾⠃⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠿⠶⠶⠚⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """

        self.welcome_art = """
        ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
        │           Welcome to Riddle Game!        │
        │     Solve riddles, earn points, and      │
        │   become the ultimate Riddle Master!     │
        ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
        """

    def clear_screen(self):
        """Clear the screen for a cleaner interface."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_score(self):
        """Display the current score."""
        print(f"\033[1;33mYour current score: {self.score}\033[0m")
        print("=" * 50)

    def check_exit(self, user_input):
        """Check if the user wants to exit."""
        if user_input == "EXIT":
            print("\033[1;31mExiting the game... Thank you for playing!\033[0m")
            exit()  # Exit the game

    def ask_riddle(self):
        """Ask the riddle to the user."""
        riddle = random.choice(self.riddles)  # Chooses a random riddle
        display_art = random.choice([self.question_mark_art, self.fox_art, self.rose_art, self.mushroom_art, self.sheep_art, None])  # Randomly choose art

        self.clear_screen()

        # Print the random ASCII art (Question Mark, Fox, or Rose)
        if display_art:
            print(display_art)

        print("\033[1;36m*******************\033[0m")
        print("\033[1;35m   RIDDLE GAME   \033[0m")
        print("\033[1;36m*******************\033[0m")

        print(self.welcome_art)  # Always show this only at the beginning

        print("\033[1;32mTry to solve this riddle:\033[0m")
        print(f"\033[1;34mRiddle: {riddle['question']}\033[0m")

        while True:  # Loop to allow user to retry the riddle after hint
            # Ask for user input and check if they want to exit
            user_answer = input("\nYour answer (or type 'HINT' for a hint, 'EXIT' to quit): ").strip().lower()
            self.check_exit(user_answer.upper())

            if user_answer == "hint":
                self.show_hint(riddle)  # Show hint and let them guess again
                print(f"\033[1;34mRiddle: {riddle['question']}\033[0m")  # Display the riddle again
                continue  # Allow the user to guess the same riddle again after hint

            if user_answer == riddle["answer"]:
                self.score += 1  # Update score immediately
                self.clear_screen()
                self.display_score()
                print("""
        ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
        │       Correct Answer!       │
        │  You're on fire, well done!  │
        ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
                """)
                input("\nPress [ENTER] to continue to the next riddle...")  # Wait for user to press ENTER to continue
                break  # Exit the loop and move to the next riddle
            else:
                self.clear_screen()
                self.display_score()
                print("""
        ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
        │     Incorrect answer!       │
        │    The correct answer is:   │
        │    \033[1;33m{}\033[0m              │
        ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
                """.format(riddle["answer"]))
                input("\nPress [ENTER] to continue to the next riddle...")  # Wait for user to press ENTER to continue
                break  # Exit the loop and move to the next riddle

    def show_hint(self, riddle):
        """Show a hint for the riddle."""
        if riddle["question"] not in self.hint_counter:
            self.hint_counter[riddle["question"]] = 0

        # Get the hint based on how many times the user has asked for a hint
        hint_index = self.hint_counter[riddle["question"]] % len(riddle["hints"])
        print(f"\033[1;36mHint: {riddle['hints'][hint_index]}\033[0m\n")
        self.hint_counter[riddle["question"]] += 1

        # After showing the hint, let the user try again
        input("\nPress [ENTER] to attempt the riddle again...")  # Wait for user to press ENTER before continuing

    def start_game(self):
        """Start the Riddle Game."""
        self.clear_screen()
        print(self.welcome_art)  # Display welcome ASCII art when game starts
        print("Ready to begin? Solve as many riddles as you can!")
        input("\nPress [ENTER] to start...")  # Wait for user to press ENTER to start the game

        # Start asking riddles
        while True:
            self.ask_riddle()

# Main function to start the game
if __name__ == "__main__":
    game = RiddleGame()
    game.start_game()