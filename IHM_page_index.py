from bottle import run, route , template , view
import models


@route('/')
def index():
    return template('index')


@route('/gameserver')
def gameserver():
    # data_list = [
    #     {"adress_ip": "142.3.6.4", "nom_serveur": "A", "game": "puissance4",},
    #     {"adress_ip": "142.3.6.5", "nom_serveur": "B", "game": "morpion", },
    # ]
    return template('game_server.tpl', data_list=models.GameServer().select())



@route('/lastgameresult')
def lastgameresult():
    last_game = {
        "machine_name": "A",
        "start_game": "12/02/2019",
        "duree": "120",
        "winner": "Player 1",
    }
    last_game = StatsPerMatch.select().order_by(StatsPerMatch.start_game.desc())[0]
    return template('lastgameresultpage', game=last_game)



@route('/Statperday')
def statperday():

    return template('Statperday', resultliste=mo.StatsPerDay.select())



@route('/Statpermatch')
def statpermatch():

    return template('Statpermatch.tpl', results_list=statpermatch.select())


if __name__ == '__main__':
    run(debug=True, reloader=True)
