
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

    return '<h1> Last Game Result Page </h1>'


@route('/Statperday')
def statperday():

    return template('Statperday', resultliste=mo.StatsPerDay.select())


@route('/Statpermatch')
def statpermatch():

    return template('Statpermatch.tpl', results_list=statpermatch.select())


if __name__ == '__main__':
    run(debug=True, reloader=True)
