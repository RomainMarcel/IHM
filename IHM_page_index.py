from bottle import run, route , template , view
import models

@route('/')
def index():
    return template('index')

@route('/gameserver')
def gameserver():
    return '<h1>Game Server Page </h1>'

@route('/lastgameresult')
def lastgameresult():
    return '<h1> Last Game Result Page </h1>'

@route('/Statperday')
def statperday():
    return '<h1> Stat per day page <h1>'


@route('/Statpermatch')
def statpermatch():

    return template('Statpermatch.tpl', results_list=statpermatch.select())


if __name__ == '__main__':
    run(debug=True, reloader=True)

