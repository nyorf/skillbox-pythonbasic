players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

team_a_resting = [
    player['name'] for player in players_dict.values()
    if player['team'] == 'A' and player['status'] == 'Rest'
]
team_b_training = [
    player['name'] for player in players_dict.values()
    if player['team'] == 'B' and player['status'] == 'Training'
]
team_c_travelling = [
    player['name'] for player in players_dict.values()
    if player['team'] == 'C' and player['status'] == 'Travel'
]

print('Члены команды из команды А, которые отдыхают: {}'.format(
    ', '.join(team_a_resting)
))
print('Члены команды из команды B, которые отдыхают: {}'.format(
    ', '.join(team_b_training)
))
print('Члены команды из команды C, которые отдыхают: {}'.format(
    ', '.join(team_c_travelling)
))
