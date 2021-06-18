"""
Created on Fri Jun 18 13:30:42 2021

@author: daniel
"""

roman_algarisms = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def roman_to_dec(n):
    dec_num = 0
    
    for num, alg in enumerate(n):
        if(num < len(n) - 1):
            if(roman_algarisms[n[num]] >= roman_algarisms[n[num+1]]):
                dec_num += roman_algarisms[n[num]]
            else:
                dec_num -= roman_algarisms[n[num]]
        else:
            dec_num += roman_algarisms[n[num]]
    return dec_num