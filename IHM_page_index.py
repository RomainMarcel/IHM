<<<<<<< HEAD
from bottle import run, route, template
import models as mo

=======
from bottle import run, route , template , view
import models
>>>>>>> 21c37e43c20441a726541d6f80ef31b5d2bef442

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
<<<<<<< HEAD

    return template('Statperday', resultliste=mo.StatsPerDay.select())
=======
    return '<h1> Stat per day page <h1>'
>>>>>>> 21c37e43c20441a726541d6f80ef31b5d2bef442


@route('/Statpermatch')
def statpermatch():

    return template('Statpermatch.tpl', results_list=statpermatch.select())


if __name__ == '__main__':
    run(debug=True, reloader=True)

