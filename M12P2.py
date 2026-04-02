# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 19:06:30 2026

@author: apoll
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:59:33 2026

@author: apoll
"""

last_name_list = ["Smith", "Bartfast", "Moe", "Larry", "Curly", "Shemp", "Joe", "Snoopy", "Woodstock", "Popeye"]
exam_score_list = [90, 75, 80, 79, 90, 100, 85, 75, 80, 85]


def display_name_and_score():
    for x in last_name_list:
        print(x)
        
        
def display_parallel():
    for index in range(len(last_name_list)):
        print(last_name_list[index] + ' is ' + 
            str(exam_score_list[index]) + ' scored on exam')
        
        
def display_name_reverse():
    last_name_list.reverse()
    for x in last_name_list:
        print(x)
        
#display_name_and_score()
#display_name_reverse()
display_parallel()
