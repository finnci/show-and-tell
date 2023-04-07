import random


class Player:
    def __init__(self, name):
        self.name = name
        self.form_num = random.choice([8, 10, 12])

    def play_golf(self):
        # returns the players score for a round of golf
        # between 0 and self.form_num
        return random.choice(list(range(0, self.form_num)))


class CrazyGolf:
    max_player_count = 50
    days = ['Thursday', 'Friday', 'Saturday', 'Sunday']

    def __init__(self):
        self.players = []
        self.leader_board = {}
        self.days_played = 0
        self.current_day = self.days[0]
        self.cut_players = []

    def add_player(self, player):
        if len(self.players) < self.max_player_count:
            self.players.append(player)
        else:
            return "Sorry bud, we're full"
        return "Added"

    def advance_days(self):
        self.days_played += 1
        self.current_day = self.days[self.days_played]

    def play_round(self):
        self.leader_board = {}
        for player in self.players:
            if player in self.cut_players:
                # Can't play if you're cut!
                continue
            todays_score = self.get_score_for_today(player)
            if self.leader_board.get(todays_score):
                self.leader_board[todays_score].append(player)
            else:
                self.leader_board[todays_score] = [player]
        self.advance_days()

    def get_score_for_today(self, player):
        todays_score = player.play_golf()
        if todays_score > 8 and self.current_day in ['Thursday', 'Friday']:
            self.cut_players.append(player)
        return todays_score

    def print_results(self):
        results = {}
        for i, val in enumerate(sorted(self.leader_board)):
            results[val] = [p.name for p in self.leader_board[val]]
        print("\no--- Results after {} ---o".format(self.current_day))
        print("Score \t Name")
        print("-----------------------------")
        for i in results:
            p = ", ".join(results[i])
            print(i, "\t", p)
        print("-----------------------------")
        if not self.cut_players:
            return
        print("\n --- xxx Cut players xxx ---")
        print("Name")
        print("-----------------------------")
        for i in self.cut_players:
            print(i.name)
        print("-----------------------------")

