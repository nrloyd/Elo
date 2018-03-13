from math import log

#calculates the probability of the first team winning
#first = the elo of the first team
#second = the elo of the second team
#homeAdvantage = the elo provisionally added to the first team's elo to account for any advantage
def predict(first, second, homeAdvantage=0):
    fir = first + homeAdvantage
    difference = float(second-fir)
    exponent = difference / float(400)
    right = float(10)**exponent
    bottom = float(1) + right
    return float(1)/bottom

#calculates the points that should be added to the elo of the first team
#first = the elo of the first team
#second = the elo of the second team
#homeAdvantage = the elo provisionally added to the first team's elo to account for any advantage
#k = a value that can be increased to increase the amount that the elo changes, or decreased to do the opposite
#win = true if the first team wins, false if the second team wins
#margin = the difference in score; (winning team's score) - (losing team's score)
def result(first, second, homeAdvantage=0, k=float(40), win=True, margin=0):
    expecteda = predict(first, second, homeAdvantage)
    actuala = float(0)
    if win:
        actuala = float(1)
    scorecoef = 1
    if margin != 0:
        scorecoef = log(margin+1)
    differencea = actuala - expecteda
    return int(k * (0.5 + scorecoef) * differencea)
