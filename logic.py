import random as r

def coin():
    storoni = ['Орел', 'Решка']
    pobeda = ''
    
    for i in range(1):
        pobeda = r.choice(storoni)
    
    return pobeda