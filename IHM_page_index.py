from bottle import run, route, template
import models as mo


# @route('/')
# def index():
#     return template('index')


@route('/gameserver')
def gameserver():
    return '<h1>Game Server Page </h1>'


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

    return template('Statpermatch.tpl', results_list=mo.Statpermatch.select())


if __name__ == '__main__':
    run(debug=True, reloader=True)

