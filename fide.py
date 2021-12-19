import math

def Probability(rating1, rating2):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))


# K jest stała - może byc obliczona ze wzoru
# 800 / (liczba gier na których opiera się obecny ranking gracza + liczba gier zagranych w obecnym turnieju)
def EloRating(yours_rating, opponents_rating, K, score):
    your_p = Probability(yours_rating, opponents_rating)
    opponents_p = Probability(opponents_rating, yours_rating)

    # wygrana
    if score == 1:
        yours_diff = K * (1 - opponents_p)
        opponents_diff = K * (0 - your_p)
    # remis
    elif score == 0.5:
        yours_diff = K * (0.5 - opponents_p)
        opponents_diff = K * (0.5 - your_p)
    # przegrana
    else:
        yours_diff = K * (0 - opponents_p)
        opponents_diff = K * (1 - your_p)

    yours_diff = round(yours_diff, 1)
    opponents_diff = round(opponents_diff, 1)

    yours_new_rating = yours_rating + yours_diff
    opponents_new_rating = opponents_rating + opponents_diff


    return yours_new_rating, opponents_new_rating
