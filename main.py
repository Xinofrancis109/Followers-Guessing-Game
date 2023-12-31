from random import randint
from art import vs, game_name
from data import data
print(game_name)


def acct_num(mist):
    return mist[randint(0, len(mist))]


score = 0
i = 1

for i in range(0, len(data)-1):
    # print(i)
    account_A = acct_num(data)
    account_B = acct_num(data)
    A = f'Compare A: {account_A["name"]}, {account_A["description"]} from {account_A["country"]}'
    B = f'Compare B: {account_B["name"]}, {account_B["description"]} from {account_B["country"]}'
    print(A)
    print(vs)
    print(B)
    A_follow = account_A["follower_count"]
    B_follow = account_B["follower_count"]
    who = input("Who has the highest instagram followers? A/B ").upper()
    if A_follow > B_follow:
        if who == "A":
            score += 1
            print(f'Correct {account_A["name"]} has {A_follow} followers. Your score: {score}')

        elif who == "B":
            print(f"You failed! {account_A['name']} has {A_follow} followers. Your score: {score}")
            break
    elif B_follow > A_follow:
        if who == "A":
            score += 1
            print(f'You failed! {account_B["name"]} has {B_follow} followers. Your score: {score}')
            break
        elif who == "B":
            print(f"Correct! {account_B['name']} has {B_follow} followers. Your score: {score}")
