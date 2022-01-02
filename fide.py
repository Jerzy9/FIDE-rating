import math


def Probability(rating1, rating2):
    return 1.0 / (1 + math.pow(10, (rating1 - rating2) / 400))


# K jest stała - może byc obliczona ze wzoru
# 800 / (liczba gier na których opiera się obecny ranking gracza + liczba gier zagranych w obecnym turnieju)
def rating(yours_rating, opponents_rating, K, score):
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


def initial_rating(avg_rating, score, n):
    calculations, init_rating = 0, 0

    # róźnica rankingu
    dp = {
            1.0:800, 0.99:677, 0.98:589, 0.97:538, 0.96:501, 0.95:470, 0.94:444, 0.93:422, 0.92:401 , 0.91:383, 0.9:366 ,
            0.89:351 , 0.88:336 , 0.87:322 , 0.86:309 , 0.85:296 , 0.84:284, 0.83:273, 0.82:262, 0.81:251, 0.8:240,
            0.79:230, 0.78:220, 0.77:211, 0.76:202, 0.75:193, 0.74:184, 0.73:175, 0.72:166, 0.71:158, 0.7:149,
            0.69:141, 0.68:133, 0.67:125, 0.66:117, 0.65:110, 0.64:102, 0.63:95, 0.62:87, 0.61:80, 0.6:72,
            0.5: 0, 0.49: -7, 0.48: -14, 0.47: -21, 0.46: -29, 0.45: -36, 0.44: -43, 0.43: -50, 0.42: -57, 0.41: -65, 0.4: -72,
            0.39: -80, 0.38: -87, 0.37: -95, 0.36: -102, 0.35: -110, 0.34: -117, 0.33: -125, 0.32: -133, 0.31: -141,
            0.3: -149, 0.29: -158, 0.28: -166, 0.27: -175, 0.26: -184, 0.25: -193, 0.24: -202, 0.23: -211, 0.22: -220, 0.21: -230, 0.2: -240,
            0.19: -251, 0.18: -262, 0.17: -273, 0.16: -284, 0.15: -296, 0.14: -309, 0.13: -322, 0.12: -336, 0.11: -351, 0.1: -366,
            0.09: -383, 0.08: -401, 0.07: -422, 0.06: -444, 0.05: -470, 0.04: -501, 0.03: -538, 0.02: -589, 0.01: -677, 0.00: -800
          }

    # Jeżeli gracz zdobył 50 % punktów, to ranking_początkowy = średni_ranking < br >
    if score == n/2:
        init_rating = avg_rating
        calculations = f"{init_rating} = {avg_rating}"

    # Jeżeli zdobył więcej niż 50%, to ranking_początkowy = średni_ranking + 20 (za każdy 0,5 pkt ponad 50%)
    elif score > n/2:
        diff = score - n/2
        init_rating = avg_rating + diff * 40
        calculations = f"{init_rating} = {avg_rating} + {diff * 40}"

    # Jeżeli zdobył mniej niż 50%, to ranking_początkowy = średni_ranking + róźnica rankingu
    elif score < n/2:
        d = round(score/n, 2)
        init_rating = avg_rating + dp.get(d)
        calculations = f"{init_rating} = {avg_rating} + ({dp.get(d)})"

    return init_rating, calculations



