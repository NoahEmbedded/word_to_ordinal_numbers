#disclaimer: I got the periodic.csv from http://www.paul-gabriel-mueller.de/blog/tag/periodic-table/

import csv
import sys

#--------------------------------------------#
# GLOBAL VARIABLES                           |
#--------------------------------------------#
all_elements = []
target_word = ""
global amount_found_solutions
amount_found_solutions = 0
#--------------------------------------------#
# FUNCTIONS                                  |
#--------------------------------------------#

def take_short(element):
    return element["short"]

def take_short_len(element):
    return len(element["short"])

def init():
    with open("periodic.csv", newline="\n") as elementFile:
        csv_reader = csv.reader(elementFile)
        for row in csv_reader:
            new_element = {
                "name":row[0].replace(" ",""),
                "number": row[2].replace(" ",""),
                "short": row[3].replace(" ","")
                #no need for density, i am dense enough lol
            }
            all_elements.append(new_element)
        all_elements.sort(key=take_short)
        global target_word
        target_word  = sys.argv[1].lower().replace(" ","")

def convert_to_number(remaining_target,previous_elements):
    #Check if finished
    if remaining_target == "":
        print("Solution found!")
        print("----------------------------------------")
        for element in previous_elements:
            print(element["short"],end = " ")
        print("\n----------------------------------------")
        for element in previous_elements:
            print(element["number"],end = " ")
        print("\n----------------------------------------")
        for element in previous_elements:
            print(element["name"],end = " ")
        print()
        global amount_found_solutions
        amount_found_solutions += 1
        return
    
    #get possible next steps
    remaining_possibilities = []
    for element in all_elements:
        if remaining_target.startswith(take_short(element).lower()):
            remaining_possibilities.append(element)

    #check possibilities
    for possibility in remaining_possibilities:
        next_target = remaining_target[len(possibility["short"]):]
        possible_solution = previous_elements + [possibility]
        convert_to_number(next_target,possible_solution)
    return

if __name__ == "__main__":
    init()
    print("target word:",target_word)
    convert_to_number(target_word,[])
    if amount_found_solutions == 0:
        print("no solution found for ", target_word)
