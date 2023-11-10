import random as rd
import time

def inning_simu():
    ball_status_types = ['-', 'W', 'N']
    batsman_status_types = ['-', 'B', 'C', 'R', 'S']
    t_score = 0
    extras = 0
    wickets = 0
    number_balls = 0
    while number_balls <= 10:
        type = rd.randint(0, 2)  # generate the ball type randomly
        ball_status = ball_status_types[type]
        type = rd.randint(0, 4)
        batsman_status = batsman_status_types[type]  # generate batsman status randomly
        time.sleep(1)               # a small pause to give effect of simulation
        if wickets == 4:
            print("----- inning over ------")
            break
        if ball_status == '-':
            score = rd.randint(0, 6)  # score on current ball
            number_balls +=  1
            if batsman_status == '-':
                t_score += score
                print(ball_status, "  ", score, "  ")
            if batsman_status == 'R':
                t_score += score
                wickets += 1
                print(ball_status, "  ", score, "  ", batsman_status)
            if batsman_status == 'B' or batsman_status == 'C' or batsman_status == 'S':
                wickets += 1
                print(ball_status, "  ", '.', "  ", batsman_status)
        elif ball_status == 'W':
            score = rd.randint(1, 4)
            if batsman_status == '-':
                extras += 1  # penalty for wide ball
                score += 1
                t_score += score
                print(ball_status, "  ", score, "  ")
            if batsman_status == 'R':
                extras += 1  # penalty for wide ball
                score += 1
                t_score += score
                wickets += 1
                print(ball_status, "  ", score, "  ", batsman_status)
            if batsman_status == 'B' or batsman_status == 'C' or batsman_status == 'S':
                continue        # do nothing and move to next ball
        elif ball_status == 'N':
            score = rd.randint(0, 6)
            if batsman_status == '-':
                extras += 2
                score += 2
                t_score += score
                print(ball_status, "  ", score, "  ")
            if batsman_status == 'R':
                extras += 2
                score += 2
                t_score += score
                wickets += 1
                print(ball_status, "  ", score, "  ", batsman_status)
            if batsman_status == 'B' or batsman_status == 'C' or batsman_status == 'S':
                continue    # do nothing and move to next ball
    print("Total Score: ", t_score, "  Total Wickets: ", wickets, "  Extras: ", extras)

inning_simu()
