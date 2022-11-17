man_city_matches = [
    {
        'home_team': 'Man City',
        'away_team': 'Liverpool',
        'home_team_score': 1,
        'away_team_score': 2,
        'result': 'Loss'
    },
    {
        'home_team': 'Man City',
        'away_team': 'Man United',
        'home_team_score': 1,
        'away_team_score': 1,
        'result': 'Draw'
    },
    {
        'home_team': 'Man City',
        'away_team': 'Arsenal',
        'home_team_score': 5,
        'away_team_score': 0,
        'result': 'Win'
    },
    {
        'home_team': 'Man City',
        'away_team': 'Tottenham',
        'home_team_score': 3,
        'away_team_score': 0,
        'result': 'Win'
    },
    {
        'home_team': 'Man City',
        'away_team': 'New Castle',
        'home_team_score': 1,
        'away_team_score': 0,
        'result': 'Win'
    },
]

print("Total matches: " + str(len(man_city_matches)))
print(man_city_matches)

wins = list(
    filter(lambda item: item['result'] == 'Win', man_city_matches))

print("Won matches: " + str(len(wins)))
print(wins)
