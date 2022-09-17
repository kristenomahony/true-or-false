from data import question_data
import random


play_btn = Element("play")
question_label = Element("output")
true_false_div = Element("true_or_false")
true_btn = Element("true")
false_btn = Element("false")
title_text = Element("title")
score_text = Element("score")
play_again_btn = Element("play_again")
correct_audio = Element("correct")
wrong_audio = Element("wrong")
game_div = Element("game")


question_list = []
question_set = []
question_number = 0
score = 0
current_question = None



for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = [question_text, question_answer]
        
        question_set.append(new_question)
random.shuffle(question_set)       
question_list = question_set[0:10]



def game_is_over():
    if question_number == len(question_list):
        return True
    else:
        return False


def next_question(*args):
    global score
    global current_question
    global question_list
    
    global question_number
    question_label.remove_class('hidden')
    if not game_is_over():
        current_question = question_list[question_number]
        question_number += 1
        text = current_question[0]
        question_label.element.innerText = text
        true_false_div.remove_class("hidden")
        play_btn.add_class("hidden")
        title_text.add_class("hidden")
        print(current_question[1]) 
    else:
        text = "Game Over"
        question_label.element.innerText = text
        play_again_btn.remove_class("hidden")

def check_true_answer(*args):
    global score
    global question_list
    total = len(question_list)
    if question_number < len(question_list):

        if current_question[1] == "True":
            score += 1
            
            
        score_text.element.innerText = f"Your Score is: {score}"
        return next_question()
    else:
        
        text = "Game Over"
        question_label.element.innerText = text
        score_text.element.innerText = f"Your Score is: {score + 1}/ {len(question_list)}"
        play_again_btn.remove_class("hidden")

def check_false_answer(*args):
    global score
    global question_list
    total = len(question_list)
    if question_number < len(question_list):

        if current_question[1]  == "False":
            score += 1
            
            
       
        score_text.element.innerText = f"Your Score is: {score}"
        return next_question()
    else:
        
        text = "Game Over"
        question_label.element.innerText = text
        score_text.element.innerText = f"Your Score is: {score + 1}/ {len(question_list)}"
        play_again_btn.remove_class("hidden")

def reset(*args):
    global question_number
    global score
    global current_question
    global question_set
    global question_list
    question_number = 0
    score = 0
    current_question = None
    title_text.remove_class("hidden")
    play_btn.remove_class("hidden")
    true_false_div.add_class("hidden")
    play_again_btn.add_class("hidden")
    question_label.add_class("hidden")
    score_text.element.innerText = f"Your Score is: {score}"
    random.shuffle(question_set)       
    question_list = question_set[0:10]
    next_question()


play_btn.element.onclick = next_question
true_btn.element.onclick = check_true_answer
false_btn.element.onclick = check_false_answer
play_again_btn.element.onclick = reset