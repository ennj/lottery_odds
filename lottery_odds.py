import random
import json

winning_numbers_draw = list(range(1,79))
power_ball_draw = list(range(1,27))

# TODO: ask input from the user for the tickets and drawings
tickets_for_drawing = 100 # 1 tickets each drawing
no_of_draws = 10000 # 1 drawing per week, 1 a year

# monetary metrics
money_spent = 0.0
money_earned = 0.0

winning_frequency = {
    "5+P": 0,
    "5": 0,
    "4+P": 0,
    "4": 0,
    "3+P": 0,
    "3": 0,
    "2+P": 0,
    "1+P": 0,
    "P": 0,
    "0": 0
}

def win_amount_calc(my_numbers, winning_numbers):
    win_amount = 0.0

    winnin_no_matches = len(my_numbers['winning_no'].intersection(winning_numbers['winning_no']))
    powerball_match = my_numbers['power_ball'] = winning_numbers['power_ball']

    if(winnin_no_matches == 5):
        if(powerball_match):
            win_amount = 2_000_000_000
            winning_frequency['5+P'] += 1
        else:
            win_amount = 1_000_000_000
            winning_frequency['5'] += 1
    elif(winnin_no_matches == 4):
        if(powerball_match):
            win_amount = 50_000
            winning_frequency['4+P'] += 1
        else:
            win_amount = 100
            winning_frequency['4'] += 1
    elif(winnin_no_matches == 3):
        if(powerball_match):
            win_amount = 100
            winning_frequency['3+P'] += 1
        else:
            win_amount = 7
            winning_frequency['3'] += 1

    elif(winnin_no_matches == 2 and powerball_match):
            win_amount = 4
            winning_frequency['2+P'] += 1
    elif(winnin_no_matches == 1 and powerball_match):
            win_amount = 4         
            winning_frequency['P'] += 1
    else:
            winning_frequency['0'] =+ 1         
       
    return win_amount

# iterating through all the drawings 
# for drawing in range(no_of_draws):
hit_jp = False
drawings = 0
years = 0 

while(True):

    drawings += 1
    winning_no_drawing = set(random.sample(winning_numbers_draw, k = 5))
    power_ball_drawing = random.choice(power_ball_draw)

    winning_numbers = {
        'winning_no': winning_no_drawing,
        'power_ball': power_ball_drawing
    }

    # iterating thorugh all the tickets
    for ticket in range(tickets_for_drawing):
        money_spent += 10

        my_winning_draw = set(random.sample(winning_numbers_draw, k = 5))
        my_powerball_draw = random.choice(power_ball_draw)

        my_win_numbers = {
            'winning_no': my_winning_draw,
            'power_ball': my_powerball_draw
        }

        win_amount = win_amount_calc(my_win_numbers, winning_numbers)
        money_earned += win_amount
        profit = money_earned - money_spent
        
        if(win_amount == 2_000_000_000):
             hit_jp = True
             break
        
        if drawings % 156 == 0:
             years += 1
             print(f'{years} years')

    if hit_jp:
         break

print(f'Spent: {money_spent}, Earnings: {money_earned}, Profit: {profit}')

print(json.dumps(winning_frequency, indent= 2))
