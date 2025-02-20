import random

class Player:
    def __init__(self, strategy):
        self.strategy = strategy
        self.score = 0
        self.last_action = 'Benevolence'  # Default for Copycat

    def choose_action(self, opponent_last_action=None):
        if self.strategy == 'Peacelover':
            return 'Benevolence'
        elif self.strategy == 'Copycat':
            return opponent_last_action if opponent_last_action else 'Benevolence'
        elif self.strategy == 'Betrayer':
            return 'Malice' if random.random() < 0.9 else 'Benevolence'
        return 'Benevolence'

def play_round(player1, player2):
    action1 = player1.choose_action(player2.last_action)
    action2 = player2.choose_action(player1.last_action)
    
    if action1 == 'Benevolence' and action2 == 'Benevolence':
        player1.score += 2
        player2.score += 2
    elif action1 == 'Malice' and action2 == 'Malice':
        player1.score += 0
        player2.score += 0
    elif action1 == 'Benevolence' and action2 == 'Malice':
        player1.score -= 2
        player2.score += 3
    elif action1 == 'Malice' and action2 == 'Benevolence':
        player1.score += 3
        player2.score -= 2
    
    player1.last_action = action1
    player2.last_action = action2

def simulate_game(population, iterations):
    players = []
    
    for _ in range(population['Peacelover']):
        players.append(Player('Peacelover'))
    for _ in range(population['Copycat']):
        players.append(Player('Copycat'))
    for _ in range(population['Betrayer']):
        players.append(Player('Betrayer'))
    
    for _ in range(iterations):
        p1, p2 = random.sample(players, 2)
        play_round(p1, p2)
    
    print("Final Scores:")
    for strategy in population.keys():
        total_score = sum(p.score for p in players if p.strategy == strategy)
        count = population[strategy]
        avg_score = total_score / count if count > 0 else 0
        print(f"{strategy}: Avg Score = {avg_score:.2f}, Total Score = {total_score}")
    
    print("Individual Scores:")
    for strategy in population.keys():
        print(f"{strategy}:")
        for p in players:
            if p.strategy == strategy:
                print(f"  Score: {p.score}")

if __name__ == "__main__":
    population_config = {
        'Peacelover': 5,
        'Copycat': 10,
        'Betrayer': 5
    }
    iterations = 1000
    
    simulate_game(population_config, iterations)

