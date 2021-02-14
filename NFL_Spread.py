"""Football spread and upset percentage calculator"""


def calculate(team_name):
    games_beat = 0
    total_games = 0
    games_upset = 0
    games = nfl_teams[team_name]
    for game in games:
        total_games += 1
        predicted = game[0]
        actual = game[1]
        if predicted > 0 and actual >= predicted:
            games_beat += 1
        if predicted < 0 and actual >= 0:
            games_upset += 1

    beat_stat = int((games_beat / total_games) * 100)
    upset_stat = int((games_upset / total_games) * 100)
    return (beat_stat, upset_stat)


def get_stats(team1, spread1, upset1, team2, spread2, upset2):
    team1stat = calculate(team1)
    team2stat = calculate(team2)
    if spread1 and upset1:
        print(team1 + " beat the spread " + str(team1stat[0]) + "% of the time and and upset " + str(
            team1stat[1]) + "% of the time\n")
    if spread2 and upset2:
        print(team2 + " beat the spread " + str(team2stat[0]) + "% of the time and and upset " + str(
            team2stat[1]) + "% of the time\n")
    if spread1 and not upset1:
        print(team1 + " beat the spread " + str(team1stat[0]) + "% of the time\n")
    if upset1 and not spread1:
        print(team1 + " upset games " + str(team1stat[1]) + "% of the time\n")
    if spread2 and not upset2:
        print(team2 + " beat the spread " + str(team2stat[0]) + "% of the time\n")
    if upset2 and not spread2:
        print(team2 + " upset games " + str(team2stat[1]) + "% of the time\n")


# predicted spread, then actual score spread
# Starts at week 4
nfl_teams = {
    "Arizona Cardinals": [[3.5, -10], [7, 20], [2.5, 28], [-3.5, 3], [4, -3], [1.5, 2], [-3.5, -7],
                          [2.5, -3], [-2.5, -10], [6, 7]],
    "Atlanta Falcons": [[-7, -14], [1.5, -7], [-3.5, 17], [2, -1], [-1.5, 8], [4, 7], [-4.5, -15],
                        [-3, 37], [-3, -5], [-5.5, -4]],
    "Buffalo Bills": [[3, 7], [8.5, -26], [-4, -9], [13.5, 8], [3.5, 3], [-3, 10], [-1.5, -2],
                      [5.5, 10], [-1, 10], [5.5, 29]],
    "Baltimore Ravens": [[13, 14], [12.5, 24], [7.5, 2], [3.5, -4], [1.5, 14], [7, -6], [6.5, -6],
                         [-4, -5], [7.5, 17], [12.5, 26]],
    "Carolina Panthers": [[-3.5, 10], [-1.5, 7], [2.5, -7], [-7.5, -3], [1.5, -8], [-10, -2], [-5.5, -23], [1.5, 20],
                          [-4.5, -1], [-7.5, -8]],
    "Cincinnati Bengals": [[3, 8], [-12.5, -24], [-8, -4], [-3.5, -3], [-5.5, 11], [-6.5, -26], [-1.5, -11],
                           [-5.5, -2], [-11.5, -12], [-12.5, 10]],
    "Cleveland Browns": [[-4.5, 11], [-1.5, 9], [-3.5, -31], [3.5, 3], [2.5, -10], [3.5, 3], [3, 5],
                         [6.5, 2], [-5.5, 6], [5, 14]],
    "Chicago Bears": [[-2.5, -8], [-3.5, 1], [-2.5, 7], [-6, -14], [-4.5, -3], [-6.5, -7], [-2.5, -6],
                      [-8.5, -16], [3, -4], [-2.5, 6]],
    "Dallas Cowboys": [[4.5, -11], [9.5, 3], [-2.5, -28], [1, -22], [-8.5, -14], [-14, -5], [-7.5, 3],
                       [2.5, -25], [-7.5, -17], [-3, 8]],
    "Denver Broncos": [[1.5, 9], [-9.5, 6], [-9.5, -27], [-3, 1], [-4, -7], [-4.5, -25], [-3.5, 7],
                       [-5.5, -28], [-13.5, -6], [-5.5, -29]],
    "Detroit Lions": [[-4, -6], [3.5, 18], [-2, 1], [-2.5, -20], [-4.5, -14], [4.5, 3], [-1.5, -20],
                      [-3, -16], [-3, 4], [-10.5, -21]],
    "Green Bay Packers": [[7, 14], [2.5, -28], [3.5, 15], [7, -6], [7.5, 17], [13.5, 4], [-2.5, -3],
                          [8.5, 16], [8.5, 14], [7.5, 8]],
    "Houstan Texans": [[4.5, -8], [6.5, 16], [-3, -6], [-3.5, -15], [6.5, 3], [-3.5, -3], [-2.5, 7],
                       [3, 16], [-3.5, -6], [-7.5, -7]],
    "Indianapolis Colts": [[2.5, 8], [1.5, -9], [8, 4], [2.5, 20], [-1.5, -14], [1, 17], [2.5, 3],
                           [3.5, -19], [3.5, 6], [7.5, 7]],
    "Kansas City Chiefs": [[7, 16], [13, -8], [4, 9], [9.5, 27], [19.5, 26], [10, 2], [7, 4],
                           [3.5, 3], [13.5, 6], [3, 3]],
    "Jacksonville Jaguars": [[-3, -8], [-6.5, -16], [-3.5, -18], [-7.5, -10], [-6.5, -3], [-13.5, -4], [-10, -24],
                             [-6.5, -2], [-10, -3], [-12.5, -26]],
    "Las Vegas Raiders": [[-3, -7], [-13, 8], [-4, -25], [-2.5, 10], [2.5, 5], [4.5, 25], [-7, -4],
                          [3, -37], [9, 3], [3.5, -3]],
    "Los Angeles Chargers": [[-7.5, -7], [-8.5, -3], [7.5, 10], [3, -1], [-2.5, -5], [-2.5, -8], [8.5, 6],
                             [-5.5, -10], [-1, -45], [-3.5, 3]],
    "Los Angeles Rams": [[12.5, 8], [7.5, 20], [3.5, -8], [6, 14], [3, -11], [2, 7], [-3.5, 3],
                         [7, -3], [2.5, 10], [17, -3]],
    "Miami Dolphins": [[-6.5, -8], [-8.5, 26], [8.5, 24], [-3, 11], [-4, 3], [2.5, 8], [3.5, -7],
                       [6.5, 17], [11.5, 12], [1, 10]],
    "Minnesota Vikings": [[-4.5, 8], [-7, -1], [3.5, -17], [-7, 6], [4.5, 14], [2.5, 6], [7.5, -3],
                          [4.5, 1], [10, 3], [2.5, -6]],
    "New England Patriots": [[-7, -16], [9.5, -6], [2.5, -27], [-3.5, -3], [7, 3], [-7, 6], [2.5, -7],
                             [-2.5, 3], [1, 45], [-1, -10]],
    "New Orleans Saints": [[4, 6], [8.5, 3], [7.5, 3], [4.5, 3], [-4.5, 35], [9.5, 14], [4.5, 15],
                           [5.5, 28], [3, 5], [-3, -3]],
    "New York Giants": [[-12.5, -8], [-9.5, -3], [2.5, 1], [-4.5, -1], [-10.5, -2], [-2.5, 3], [-3.5, 10],
                        [5.5, 2], [-10.5, 5], [-5, -14]],
    "New York Jets": [[-1.5, -9], [-7, -20], [-8.5, -24], [-13.5, -8], [-19.5, -26], [-7, -3], [-8.5, -6],
                      [-6.5, -17], [-9, -3], [-17, 3]],
    "Philadelphia Eagles": [[-6, 5], [-7, -9], [-7.5, -2], [4.5, 1], [8.5, 14], [3.5, -10], [-3, -5],
                            [-5, -6], [-8.5, -14], [-6, -7]],
    "Pittsburgh Steelers": [[7, 9], [3.5, 31], [-1.5, 3], [-3.5, 4], [14, 5], [6.5, 26], [10, 24],
                            [4, 5], [7, -6], [12.5, -10]],
    "San Francisco 49ers": [[7, -5], [8.5, -26], [3.5, 8], [-2.5, 27], [-2.5, -10], [-7.5, -17], [-9.5, -14],
                            [-7, 3], [1, -10], [3, -8]],
    "Seattle Seahawks": [[6.5, 8], [7, 1], [3.5, -3], [2.5, 10], [3, -10], [-2, -7], [3.5, 7],
                         [5, 6], [10.5, -5], [5.5, 5]],
    "Tampa Bay Buccaneers": [[7.5, 7], [3.5, -1], [-2.5, 28], [4, 25], [10.5, 2], [4.5, -35], [5.5, 23], [3.5, -3],
                             [-3.5, -3], [5.5, 4]],
    "Tennessee Titans": [[-8.5, 26], [3, 6], [1.5, -3], [5.5, -11], [6.5, 7], [-1, -17], [-6.5, 6],
                         [-3.5, 19], [5.5, -6], [10.5, 21]],
    "Washington Football Team": [[-13, -14], [-7.5, -20], [-2.5, -1], [-1, 22], [2.5, -3], [-4.5, -3], [1.5, 11],
                                 [-2.5, 25], [-7, 6], [-5.5, -5]]
}

#first one is beat the spread, second is upset
get_stats("Buffalo Bills", True, False, "New England Patriots", False, True)
