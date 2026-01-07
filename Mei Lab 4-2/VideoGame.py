# Pornsawan Khararam
# 683040156-9

from datetime import datetime

class VideoGame:
    # Class Attributes
    total_players = 0
    difficulty_levels = ["Easy", "Medium", "Hard"]
    max_level = 100
    server_start_time = datetime.now()
    active_players = []
    leaderboard = {}

    def __init__(self, player_name, character_type):
        if not VideoGame.is_valid_character_name(player_name):
            raise ValueError("Invalid character name.")
        self.player_name = player_name
        self.character_type = character_type
        self.level = 1
        self.health = 100
        self.exp = 0
        self.coins = 0
        self.inventory = []
        self.is_alive = True
        VideoGame.total_players += 1
        VideoGame.active_players.append(player_name)
        VideoGame.leaderboard[player_name] = 0

    def level_up(self):
        if self.level < VideoGame.max_level:
            self.level += 1
            self.health = 100
            score = self.level * 100 + self.coins
            VideoGame.leaderboard[self.player_name] = score
            print(f"{self.player_name} leveled up! Level: {self.level}, Health: {self.health}, Score: {score}")

    def collect_coins(self, amount):
        if amount > 0:
            self.coins += amount
            score = self.level * 100 + self.coins
            VideoGame.leaderboard[self.player_name] = score
            print(f"{self.player_name} collected {amount} coins. Total Coins: {self.coins}, Score: {score}")

    def take_damage(self, damage):
        if damage > 0:
            self.health -= damage
            if self.health <= 0:
                self.health = 0
                self.is_alive = False
                VideoGame.active_players.remove(self.player_name)
                print(f"{self.player_name} has died! Health: {self.health}, Alive: {self.is_alive}")
            else:
                print(f"{self.player_name} took {damage} damage. Health: {self.health}, Alive: {self.is_alive}")

    def fight_monster(self, monster_name, monster_level):
        damage = VideoGame.calculate_damage(10, 5, self.level)  # Example attack/defense
        self.take_damage(damage)
        if self.is_alive:
            exp_gain = 10 * monster_level
            self.exp += exp_gain
            coins_gain = 3 * monster_level
            self.collect_coins(coins_gain)
            if self.exp >= VideoGame.calculate_exp_needed(self.level):
                self.level_up()
            print(f"{self.player_name} fought {monster_name} (Level {monster_level}). Damage taken: {damage}, Exp gained: {exp_gain}, Coins gained: {coins_gain}")

    def get_stats(self):
        return f"Player: {self.player_name} ({self.character_type}) - Level: {self.level}, Health: {self.health}, Exp: {self.exp}, Coins: {self.coins}, Inventory: {self.inventory}, Alive: {self.is_alive}"

    @classmethod
    def create_party(cls, players_list, player_type):
        party = []
        for name in players_list:
            party.append(cls(name, player_type))
        return party

    @classmethod
    def get_server_stats(cls):
        uptime = datetime.now() - cls.server_start_time
        return f"Total Players: {cls.total_players}\nActive Players: {cls.active_players}\nLeaderboard: {cls.leaderboard}\nServer Uptime: {uptime}"

    @classmethod
    def get_leaderboard(cls):
        sorted_leaderboard = sorted(cls.leaderboard.items(), key=lambda x: x[1], reverse=True)
        result = "----- Leaderboard -----\n"
        for i, (player, score) in enumerate(sorted_leaderboard, 1):
            result += f"{i}. {player}: {score}\n"
        result += "----- End Leaderboard -----"
        return result

    @classmethod
    def reset_server(cls):
        cls.total_players = 0
        cls.server_start_time = datetime.now()
        cls.active_players = []
        cls.leaderboard = {}

    @staticmethod
    def calculate_damage(attack_power, defense, level):
        damage = (attack_power * level) - defense
        return max(0, damage)

    @staticmethod
    def calculate_exp_needed(level):
        return 100 * level

    @staticmethod
    def is_valid_character_name(name):
        return 3 <= len(name) <= 20 and name.isalnum()

    @staticmethod
    def get_rank_title(level):
        if level < 10:
            return "Novice"
        elif level < 30:
            return "Apprentice"
        elif level < 60:
            return "Warrior"
        elif level < 90:
            return "Master"
        else:
            return "Legend"