# project part 2 template
# follow the template, inserting code as noted by FIXME
# import required modules (do not change)
import random as r
# import matplotlib.pyplot as plt
# define play_game function (do not change definition in next line)
rolls = 1
turns = 0 
win_turns = 0
max = 0
win = 0
def play_game(rolls, win_turns):
# loop through turns until win or loss condition
### FIXME write the loop to implement the game turns / rolls ###
    rolls = 1
    turns = 0 
    win_turns = 0
    max = 0
    while rolls <= 500:
        max = (max + 2)
        D1 = r.randint(1,max)
        D2 = r.randint(1,max)
        if (D1 and D2) == 1:
            break
            turns = rolls + 1

        else:
            win = win_turns + 1
            # return ending turn number
        
    return turns
# check if run as module or script (do not change)
if __name__ == "__main__":
    # initialize variables
    ### FIXME - initialize variables, define constants ###
    D1 = int()
    D2 = int()
    max = int()
    N = int()
    PW = float()
    PL = float()
    TL = int()
    AR = int()
    AP = int()
    # set random seed (do not change)
    seed = input("*** Enter random seed value (integer) or ENTER for none: ")
if seed:
    r.seed(int(seed))
    # for each game call play_game, collect results
    ### FIXME - write loop to play specified number of games, collect results ###
    x = input("*** Enter the number of games you want to play: ")
    N = int(x)
    i = 1
while i <= int(N):
    play_game
    TL = TL + turns
    i += 1
    # after game loop, calc prob win, prob loss, avg turns in loss, & avg turns played
    ### FIXME - calculate the required statistics ###
    PW = (win_turns / N) / 100
    PL = 1 - PW
    AR = TL / N
    AP = (win *500 + TL ) / N
    # print results using f-strings
    # ... you will need to use all five components of the format specification
    # ... see Unit 6 lectures for details
    # Also: the % type character prints floats as percents, for example:
    # ... f"{0.695:0.2%}" evaluates to "69.50%"

    ### FIXME - complete the following code ###
    # do not change the following line - use it to ensure your rows are correct
    print(f"\n|{'Result':-^19}|{'Value':-^9}|")

    # replace 'FIXME' with the correct expression to complete this line:
    print(f"{'| Max Turns Played':<20}|{'500':>8} |")
    print(f"{'| Min Turns Played':<20}|{'1':>8} |")
    print(f"{'| Avg Turns Played':<20}|{'{AP:.1f}':>8} |")
    print(f"{'| Win Probability':<20}|{'{PW:0.1%}':>8} |")
    print(f"{'| Loss Probability':<20}|{'{PL:0.1%}':>8} |")
    print(f"{'| Avg Turns in Loss':<20}|{'{AR:.2f}':>8} |")

### FIXME - add the remaining 5 print statements as specified ###
# generate a histogram plot of values for all dice rolled using matplotlib
### FIXME - replace all_rolls in the following line
### with the name of the variable you use to collect dice results in
# plt.hist(TL)
# # show the histogram plot (do not change)
# plt.show()