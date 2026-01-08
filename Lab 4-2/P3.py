# Pornsawan Khararam
# 683040156-9

from VideoGame import VideoGame

player1 = VideoGame("Hero123", "Ninja")
party = VideoGame.create_party(["TeH", "MEIII"], "Wizard")

print(VideoGame.get_server_stats())
player1.collect_coins(50)
player1.fight_monster("Dragon", 5)
print(player1.get_stats())
print(f"Rank for level {player1.level}: {VideoGame.get_rank_title(player1.level)}")
print(VideoGame.get_leaderboard())