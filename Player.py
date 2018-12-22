import json


class Player:

    players = []

    def __init__(self, name):
        with open('players.json') as f:
            self.players = json.load(f)
        player_exists = self.find_player(name)
        if not player_exists:
            player_data = "[{'Name': '" + name + "', 'Wins': '0', 'Losses': '0'}]"
            with open('players.json', 'w', encoding='utf-8') as outfile:
                json.dump([], outfile)
            with open('players.json', mode='w', encoding='utf-8') as f:
                entry = {'Name': name, 'Wins': "0", 'Losses': "0"}
                self.players.append(entry)
                json.dump(self.players, f, indent=4)

    def find_player(self, name):
        for play in self.players:
            if play["Name"] == name:
                return True
        return False

    def update_record(self, name, win):
        for player in self.players:
            if player["Name"] == name:
                if win:
                    num_wins = int(player["Wins"])
                    num_wins += 1
                    player["Wins"] = str(num_wins)
                if not win:
                    num_losses = int(player["Losses"])
                    num_losses += 1
                    player["Losses"] = str(num_losses)
                with open('players.json', mode='w', encoding='utf-8') as f:
                    json.dump(self.players, f, indent=4)

