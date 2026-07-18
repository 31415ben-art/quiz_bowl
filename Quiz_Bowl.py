import requests
import json
import jellyfish
import re
tossup_url = "https://www.qbreader.org/api/random-tossup?"




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
        user_answer = user_answer.strip().lower()
        answers = re.findall(r"<u>(.*?)</u>", self.answer)

        if not answers:
            answers = [self.answer]

        for answer in answers:
            answer = answer.lower().strip()

            similarity = jellyfish.jaro_winkler_similarity(
                answer, user_answer
            )
            
            if similarity >= strict:
                return True
  
        return False
    
def get_data(number, cat, diff):

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
   
game = Game()

while True:
    game.current_question = get_data(1, ["Science"], ["1"])

    print(game.current_question.text)

    user_answer = input("Answer: ")

    if game.current_question.check(user_answer, 0.8):
        print("Correct")
        game.score += 10
    else:
        print("Incorrect")
        game.score -= 5

    print(game.score)

    
            
    
            
               

    
    
if __name__ == "__main__":
    main()