from bottle import run, route, template
import models as mo
import peewee



# @route('/')
# def index():
#     return template('index')


@route('/gameserver')
def gameserver():

    return template('game_server.tpl', data_list=mo.GameServer().select())

@route('/lastgameresult')
def lastgameresult():
    last_game = mo.StatsPerMatch.select().order_by(mo.StatsPerMatch.start_game.desc())[0]
    return template('lastgameresultpage', game=last_game)


@route('/Statperday')
def statperday():

    return template('Statperday', resultliste=mo.StatsPerDay.select())


@route('/Statpermatch')  # page stat globale
def statpermatch():

    return template('Statpermatch.tpl', results_list=mo.StatsPerMatch.select())


@route('/Statpermatch/machine/<machine_name>')  # page stat par machine
def statpermatch(machine_name):

    return template('Statpermatch.tpl', results_list=mo.StatsPerMatch.select().where(mo.StatsPerMatch.machine_name == mo.GameServer.get(mo.GameServer.nom_serveur == machine_name)))


@route('/Statpermatch/date/<date>')  # page stat par date
def statpermatch(date):

    return template('Statpermatch_date.tpl', results_list=mo.StatsPerMatch.select().where(mo.StatsPerMatch.start_game == date ).order_by(mo.StatsPerMatch.start_game))


if __name__ == '__main__':
    run(debug=True, reloader=True)

