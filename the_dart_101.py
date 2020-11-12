import sys
import math


def check_round_counter(shoot_list):
    score_101 = 101
    rounds = 0
    tries = 0
    misses = 0
    previous_shoot = "."
    previous_score = 101
    for s in shoots:
        tries += 1
        if s == 'X':
            misses += 1
            amount = 20
            if previous_shoot == "X":
                amount += 10

            previous_shoot = "X"
            score_101 += amount
        else:
            previous_shoot = "."
            score_101 -= s

        if score_101 < 0:
            score_101 = previous_score
            rounds += 1
            previous_shoot = "."
            misses = 0
            tries = 0
            continue

        if tries == 3:
            if misses == 3:
                score_101 = 101

            previous_score = score_101
            previous_shoot = "."
            misses = 0
            tries = 0
            rounds += 1

    return rounds


def calculate_shoot_scores(shoots):   
    shoot_scores = []
    for s in shoots:
        if s == 'X':
            shoot_scores.append('X')
            continue

        shoot_scores.append(eval(s))

    return shoot_scores


players_scores = []

n = int(input())
for i in range(n):
    player = input()
    players_scores.append({
        "player": player,
        "shoots": []
    })

for i in range(n):
    shoots = input().split(' ')
    players_scores[i]["shoots"] = calculate_shoot_scores(shoots)

    shoots = players_scores[i]["shoots"]
    players_scores[i]["rounds"] = check_round_counter(shoots)

#print("Debug messages...", players_scores, file=sys.stderr, flush=True)

best_player = players_scores[0]
for p in players_scores:
    if p["rounds"] <= best_player["rounds"]:
        best_player = p

print(best_player["player"])
