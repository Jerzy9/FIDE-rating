import math

# Function to calculate the Probability
def Probability(rating1, rating2):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))


# Function to calculate Elo rating
# K is a constant.
# score determines who won
#   1 - you won,
#   0.5d - draw,
#   0 - you lost)
def EloRating(yours_rating, opponents_rating, K, score):
    your_p = Probability(yours_rating, opponents_rating)
    opponents_p = Probability(opponents_rating, yours_rating)

    # win
    if score == 1:
        yours_diff = K * (1 - opponents_p)
        opponents_diff = K * (0 - your_p)
    # draw
    elif score == 0.5:
        yours_diff = K * (0.5 - opponents_p)
        opponents_diff = K * (0.5 - your_p)
    # lose
    else:
        yours_diff = K * (0 - opponents_p)
        opponents_diff = K * (1 - your_p)

    print(score)

    yours_diff = round(yours_diff, 1)
    opponents_diff = round(opponents_diff, 1)

    yours_new_rating = yours_rating + yours_diff
    opponents_new_rating = opponents_rating + opponents_diff

    print("Yours ELO:", yours_rating, "+", yours_diff, "=", yours_new_rating)
    print("Opponents ELO:", opponents_rating, "+", opponents_diff, "=", opponents_new_rating)

    return yours_rating, opponents_rating, yours_diff, opponents_diff, yours_new_rating, opponents_new_rating

# Ra = 1200
# Rb = 1000
# K = 30
# d = 0.5
# EloRating(Ra, Rb, K, d)