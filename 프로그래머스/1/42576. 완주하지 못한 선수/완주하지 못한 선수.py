'''
["mislav", "stanko", "mislav", "ana"]
["stanko", "ana", "mislav"]
'''
def solution(participant, completion):
    players = {}
    
    for name in participant:
        players[name] = players.get(name, 0) + 1
    
    for name in completion:
        players[name] -= 1
    
    for name in participant:
        if players[name] > 0:
            return name