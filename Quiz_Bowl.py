import requests
import json
import time
import keyboard
import jellyfish

tossup_url = "https://www.qbreader.org/api/random-tossup?"

def main():
    number = int(input("How many tossups? "))
    cat = int(input("Category: \nScience = 1\nHistory = 2\nLiterature = 3\n\n"))
    diff = int(input("Difficulty: "))
    strict = (3) #change later
    data = get_data(number, cat, diff)  
    if not cat or cat == 1:  # redefining cat to for api, later loop until something is chosen
        cat == "Science"
    elif cat == 2:
        cat = "History"
    elif cat == 3:
        cat = "Literature"
    else:
        cat == "Science"

    get_data(number, cat, diff)
    print_question(data, strict)



   

def get_data(number, cat, diff):
    params = {
        "number": number,
        "categories": cat,
        "difficulties": diff,
        }

    response = requests.get(tossup_url, params=params)
    data = response.json()
    return data

def check_answer(correct_answer, user_answer, strict):
    error = jellyfish.levenshtein_distance(correct_answer, user_answer)
    if error <= strict:
        return True
    else:
        return False
    
def print_question(data, strict):
    i = 0
    tossup = data["tossups"][0]["question"].split()
    correct_answer = data["tossups"][0]["answer"]

    while i < len(tossup):
        if keyboard.is_pressed("space"):
            user_answer = input("\nAnswer: ").strip().lower()
            if check_answer(correct_answer, user_answer, strict):
                print("\n\nCorrect!!!\n\n")
                break
            else:
                print("\n\nIncorrect\n\n")
        print(tossup[i])
        i += 1
        time.sleep(0.1)
    
    
            
    
            
        

    
    
if __name__ == "__main__":
    main()