from bottle import run, route, template, post, request, get, redirect
import models as mo
import peewee

# @route('/')
# def index():
#     return template('index')


@route('/gameserver')
def gameserver():
    return '<h1>Game Server Page </h1>'


@route('/lastgameresult')
def lastgameresult():

    return '<h1> Last Game Result Page </h1>'


@route('/Statperday')
def statperday():

    return template('Statperday', resultliste=mo.StatsPerDay.select())


@route('/Statpermatch')
def statpermatch():

    return template('Statpermatch.tpl', results_list=mo.StatsPerMatch.select())


@get('/configuration')
def configurateur():
    return template('configuration')


@post('/configuration')
def configurateur():
    adress_ip = request.forms.get('serveur')
    nom_serveur = request.forms.get('nom')
    game = request.forms.get('jeux')
    max_player_delay = request.forms.get('max')
    max_coin_blink_delay = request.forms.get('coin')
    victory_blink_delay = request.forms.get('victory')
    level = request.forms.get('level')
    player_1_color = request.forms.get('player1')
    player_2_color = request.forms.get('player2')

    mo.GameServer.get_or_create(adress_ip=adress_ip,
                                nom_serveur=nom_serveur,
                                game=game,
                                max_player_delay=max_player_delay,
                                max_coin_blink_delay=max_coin_blink_delay,
                                victory_blink_delay=victory_blink_delay,
                                level=level,
                                player_1_color=player_1_color,
                                player_2_color=player_2_color)

    return redirect('/configuration')

# @route('/modification')
# def modif():
#     return template('modification.tpl', nom=request.forms.get('nom'))
#
# @get('/modifications/<nom>')
# def configurateur(nom):
#
#     return template('modifications.tpl', nom_serveur=mo.GameServer.select().where(mo.GameServer.nom_serveur == nom))
#
#
# @post('/modifications/<nom>')
# def configurateur():
#
#     adress_ip = request.forms.get('serveur')
#     nom_serveur = request.forms.get('nom')
#     game = request.forms.get('jeux')
#     max_player_delay = request.forms.get('max')
#     max_coin_blink_delay = request.forms.get('coin')
#     victory_blink_delay = request.forms.get('victory')
#     level = request.forms.get('level')
#     player_1_color = request.forms.get('player1')
#     player_2_color = request.forms.get('player2')
#
#     mo.GameServer.get_or_create(adress_ip=adress_ip,
#                                 nom_serveur=nom_serveur,
#                                 game=game,
#                                 max_player_delay=max_player_delay,
#                                 max_coin_blink_delay=max_coin_blink_delay,
#                                 victory_blink_delay=victory_blink_delay,
#                                 level=level,
#                                 player_1_color=player_1_color,
#                                 player_2_color=player_2_color)
#
#     return redirect('/configuration')


if __name__ == '__main__':
    run(debug=True, reloader=True)

