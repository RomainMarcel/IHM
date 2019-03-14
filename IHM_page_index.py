from bottle import run, route , template


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
    return '<h1> Stat per day page <h1> '

@route('/Statpermatch')
def statpermatch():
    return '<h1> Stat per match page <h1>'


if __name__ == '__main__':
    run(debug=True, reloader=True)

