#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        x = ""
        score = 0
        for keys in a_dictionary:
            if a_dictionary[keys] >= score:
                x = keys
                score = a_dictionary[keys]
        return x
