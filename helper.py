from flask import flash
from datetime import date, datetime, timedelta

import cs304dbi as dbi

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
    if (p1.get('bedtime')==p2.get('bedtime')):
        score += 2
    elif (abs(p1.get('bedtime') - p2.get('bedtime')) <= 2):
        score += 1 #a decent match, if not perfect
    else:
        #score doesn't change
        pass

    #compare wake time
    if (p1.get('waketime')==p2.get('waketime')):
        score += 2
    elif (abs(p1.get('waketime') - p2.get('waketime')) <= 2):
        score += 1 #a decent match, if not perfect
    else:
        #score doesn't change
        pass

    #compare cleanliness
    if (p1.get('cleanliness')==p2.get('cleanliness')):
        score += 2
    elif (abs(p1.get('cleanliness') - p2.get('cleanliness')) <= 2):
        score += 1 #a decent match, if not perfect
    else:
        #score doesn't change
        pass

    #compare activity
    if (p1.get('activity')==p2.get('activity')):
        score += 2
    elif (abs(p1.get('activity') - p2.get('activity')) <= 2):
        score += 1 #a decent match, if not perfect
    else:
        #score doesn't change
        pass

    return score/9

# compares one person to entire db of people

if __name__ == '__main__':
    p1 = {'username': 'Wendy', 'descrip': 'Whoever I room with has to be okay with my pet hamster </3', 'contact': '5555555555', 'classyear': '2026', 'bedtime': 10, 'waketime': 8, 'cleanliness': 3, 'activity': 3, 'dorm': 'east'}
    p2 = {'username': 'Wanda', 'descrip': 'hi', 'contact': 'wanda@wanda', 'classyear': '2025', 'bedtime': 11, 'waketime': 8, 'cleanliness': 4, 'activity': 4, 'dorm': 'east'}
    print(compareTwo(p1,p2))