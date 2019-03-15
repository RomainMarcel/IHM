import json
import os
import datetime
import models as mo
import peewee

class Data:
    def __init__(self, json_formatted_string):
        data = json.loads(json_formatted_string)
        self.msg = json_formatted_string
        self.msg_id = data["Msg ID"]
        self.nom_serveur = mo.GameServer.get(mo.GameServer.nom_serveur == data["Machine name"])
        self.game = data["Game type"]
        self.start_game = data["Start time"]
        self.end_game = data["End time"]
        self.start_game_format = datetime.datetime.strptime(self.start_game, "%d/%m/%y %H:%M")
        self.end_game_format = datetime.datetime.strptime(self.end_game, "%d/%m/%y %H:%M")
        self.winner = data["Winner"]
        # self.nbr_partie_jour =

    def get_day(self):

        return self.start_game_format.date()

    def get_game_duration(self):

        return (self.end_game_format-self.start_game_format).total_seconds()

    def get_winner(self):
        return self.winner


for fiche in os.listdir('./partie'):
    with open('./partie/' + fiche, 'r') as fichier:
        test = fichier.read()
        stats = Data(test)

        mo.ReceiverMessage.get_or_create(msg_id=stats.msg_id,
                                         msg_machine=stats.nom_serveur,
                                         msg=stats.msg)
        mo.StatsPerMatch.get_or_create(machine_name=stats.nom_serveur,
                                       start_game=stats.get_day(),
                                       duree=stats.get_game_duration(),
                                       winner=stats.get_winner())
        try:
            mo.StatsPerDay.get(mo.StatsPerDay.machine_name == stats.nom_serveur, mo.StatsPerDay.date == stats.start_game_format)
            print("Cette enregistrement existe déja")


        except peewee.DoesNotExist:
            # winner_player_1 = 0
            # winner_player_2 = 0
            # winner_egalite = 0
            if mo.StatsPerMatch.winner == 'player1':
                winner_player_1 = 1
                winner_player_2 = 0
                winner_egalite = 0
            elif mo.StatsPerMatch.winner == 'player2':
                winner_player_1 = 0
                winner_player_2 = 1
                winner_egalite = 0
            else:
                winner_player_1 = 0
                winner_player_2 = 0
                winner_egalite = 1

            mo.StatsPerDay.create(date=stats.start_game_format,
                                  machine_name=stats.nom_serveur,
                                  nombre_partie=7,
                                  duree_moy_partie=54,
                                  joueur1_win=winner_player_1,
                                  joueur2_win=winner_player_2,
                                  egalite=winner_egalite)

        # print(stats.get_day)
        # print(stats.get_game_duration)
        # print(stats.get_winner)
