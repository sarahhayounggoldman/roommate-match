from flask import flash
from datetime import date, datetime, timedelta

import cs304dbi as dbi
import math

# a function to compare two people and return compatability score
def compareTwo(p1, p2):
    # p1 and p2 will be dictionaries that contain all of the info of a person as they are stored in db
    #compat score starts at 0, max possible is 9
    score = 0

    #compare dorm prefs
    if ((p1.get('dorm') == "no pref" or p2.get('dorm') == "no pref") or (p1.get('dorm') == p2.get('dorm'))):
        score += 1
    else:
        #score doesn't change
        pass
    
    #compare bed time
    if (int(p1.get('bedtime'))==p2.get('bedtime')):
        score += 2
    elif (abs(int(p1.get('bedtime')) - p2.get('bedtime')) <= 2):
        score += 1 #a decent match, if not perfect
    else:
        #score doesn't change
        pass

    #compare wake time
    if (int(p1.get('wakeup'))==p2.get('waketime')):
        score += 2
    elif (abs(int(p1.get('wakeup')) - p2.get('waketime')) <= 2):
        score += 1 #a decent match, if not perfect
    else:
        #score doesn't change
        pass

    #compare cleanliness
    if (int(p1.get('clean'))==p2.get('cleanliness')):
        score += 2
    elif (abs(int(p1.get('clean')) - p2.get('cleanliness')) <= 2):
        score += 1 #a decent match, if not perfect
    else:
        #score doesn't change
        pass

    #compare activity
    if (int(p1.get('social'))==p2.get('activity')):
        score += 2
    elif (abs(int(p1.get('social')) - p2.get('activity')) <= 2):
        score += 1 #a decent match, if not perfect
    else:
        #score doesn't change
        pass

    # return score as a percentage
    return math.trunc(score/9 * 100)

# compares one person to entire db of people, stored in list form
# takes in one person's data (in dictionary form) and a list of everyone else (in list form)
# returns a dict of the best match found out of everyone in the list, as well as their score
# AT THE MOMENT: Doesn't handle ties, just happens to return one person who is best match
def compareAll(p1, all):
    bestScore = 0
    for p2 in all:
        currScore = compareTwo(p1,p2)
        if currScore >= bestScore:
            bestScore = currScore
            bestMatch = p2 # set the best match to the information of the person with the best match

    return bestScore, bestMatch


if __name__ == '__main__':
    p1 = {'username': 'Wendy', 'descrip': 'Whoever I room with has to be okay with my pet hamster </3', 'contact': '5555555555', 'classyear': '2026', 'bedtime': 10, 'waketime': 8, 'cleanliness': 3, 'activity': 3, 'dorm': 'east'}
    p2 = {'username': 'Wanda', 'descrip': 'hi', 'contact': 'wanda@wanda', 'classyear': '2025', 'bedtime': 11, 'waketime': 8, 'cleanliness': 4, 'activity': 4, 'dorm': 'east'}
    print(compareTwo(p1,p2))