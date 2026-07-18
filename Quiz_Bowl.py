import requests
import json
import time
import keyboard
import jellyfish
import threading

tossup_url = "https://www.qbreader.org/api/random-tossup?"

# test git commit



class Game:
    def __init__(
        self,
        score=0,
        user=None,
        powers=None,
        not_powers=None,
        current_question=None,
        cat=None,
        diff=None,
        speed=None,
        strict=0
    ):
        self.score = score
        self.user = user
        self.powers = powers
        self.not_powers = not_powers
        self.current_question = current_question
        self.cat = cat if cat else []
        self.diff = diff if diff else []
        self.speed = speed
        self.strict = strict

class Question:
    def __init__(self, text, answer, cat, diff):
        self.text = text
        self.answer = answer
        self.cat = cat
        self.diff = diff

        self.position = 0
        self.done = False

    
    
    def check(self, user_answer, strict):
        correct_clean = self.answer.strip().lower()
        user_answer = user_answer.lower().strip()
        return jellyfish.levenshtein_distance(correct_clean, user_answer) <= strict
    


def get_question(number, cat, diff):

    params = {
        "number": number,
        "categories": cat,
        "difficulties": diff,
    }

    response = requests.get(tossup_url, params=params)
    data = response.json()

    tossup = data["tossups"][0]

    return Question(
        tossup["question"],
        tossup["answer"],
        tossup["category"],
        tossup["difficulty"]
    )
   


def check_answer(correct_answer, user_answer, strict):
    error = jellyfish.levenshtein_distance(correct_answer, user_answer)
    if error <= strict:
        return True
    else:
        return False
    
#def print_question(data, strict):
    i = 0
    tossup = data["tossups"][0]["question"].split()
    correct_answer = data["tossups"][0]["answer"]

    

    while i < len(tossup):
        if keyboard.is_pressed("space"):
            user_answer = input("\nAnswer: ").strip().lower()
            if check_answer(correct_answer, user_answer, strict):
                print("\n\nCorrect!!!\n\n")
                return True
            else:
                print("\n\nIncorrect\n\n")
        print(tossup[i], )
        time.sleep(0.1)
    
    
    
            
    
            
               

    
    
if __name__ == "__main__":
    main()