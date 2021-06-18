"""
Created on Fri Jun 18 11:39:16 2021

@author: daniel
"""

import os

choices = []

print('Are you sure you want to run this python code?')
print('1. yes')
print('2. Lol, no')

answer = '0'
while answer != '1' and answer != '2':
    answer = input('')

if(answer == '1'):
    print('When you ran a weird python code you just downloaded on github')
    print('suddenly you got sucked into the screen by a vortex and got stuck into the pc')
    print('You\'re in the workspace, what do you do?')
    print('1. search on google how to get out')
    print('2. cry really loud')
    
    answer = '0'
    while answer != '1' and answer != '2':
        answer = input('')
    
    if(answer == '1'):
        print('you access the internet exploder (ie), you need to wait it start, but is very slow')
        print('What do you do now?')
        print('1. keep pressing the internet exploder until the computer get really slow and open 50 tabs at the same time')
        print('2. wait')
        
        answer = '0'
        while answer != '1' and answer != '2':
            answer = input('')
        
        if(answer == '1'):
            print('The computer got too slow and somehow you managed to open the task mananger, you see a task named vortex_mananger, it feels like you need to do something about it, what do you do?')
            print('1. Kill the task')
            print('2. Give highest priority')
            answer = '0'
            while answer != '1' and answer != '2':
                answer = input('')
            
            if answer == '1':
                print('LOL, now you\'re stuck forever here...')
                print('Bad ending (unless you\'re introverted)')
            else:
                print('The vortex got stronger and absorved the rest of the world and now the whole world is inside your computer')
                print('Good ending (usless you\'re introverted)')
        else:
            print('you waited forever and died')
            print('Bad ending')
    else:
        print('A virus listened your loud crying and now it\'s trying to kill you')
        print('What will you do?')
        print('1. Hide on documents folder')
        print('2. Battle de virus')
        answer = '0'
        while answer != '1' and answer != '2':
            answer = input('')
            
        if answer == '1':
            print('You got lost and somehow went to the thrash bin')
            print('Your cat walk through your keybord and empty the thrash bin')
            print('You\'re gone forever')
            print('bad ending')
        else:
            print('You fought the virus back, but the antivirus came and want to put you both in quarantine')
            print('1. Try to explain the situation')
            print('2. Ruuuuuuuunnnn!!!')
            answer = '0'  
            while answer != '1' and answer != '2':
                answer = input('')
            if answer == '1':
                print('You try to explain the situation, but the antivirus doesn\'t listen to you')
                print('Now you\'re in quarantine')
                print('At least you don\'t need to work anymore')
                print('Good ending (yes, is good since you don\'t need to work anymore)')
            else:
                print('You ran the faster you can')
                print('The antivirus is right behind you')
                print('You think you\'re going to die')
                print('You see the light in the end of the tunnel')
                print('It was actually an openned portal through the USB port')
                print('You\'re free now')
                print('You\'re back to the hipocritical society that forces you to be perfect and only cares about money')
                print('You need to work again in the monday and gain money to live')
                print('Bad ending, but you still alive')
                
else:
    print('Happy ending! (even thought you didn\'t really played the game)')