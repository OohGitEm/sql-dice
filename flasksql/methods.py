import flask
import rolltide
import sqlite3

app = flask.Flask(__name__)
@app.route('/roll', methods=['GET'])
def roll_n_sided_dice_n_times():
    num_of_sides = int(flask.request.args.get('num_of_sides'))
    num_of_rolls = int(flask.request.args.get('num_of_rolls'))
    rolls_dict = rolltide.roll_dice(num_of_rolls, num_of_sides)
    return flask.jsonify(rolls_dict)

##---- TODO
#
# As a user of this project in its current state I can only get a new roll
# I'd like to be able to see all dice rolls throughout a game to look back on everyones rolls and
# ensure no one is cheating. A sqlite db would work but is likely overkill, so instead we can use a json
# file as a lightweight data storage method.
#
# First write a REST endpoint that allows someone to initialize a new game. General structure will look like:
# app.route('/initializeGame', methods=['POST']
# def initialize_game():
#     GET GAMES NAME
#     CREATE NEW JSON
#     SAVE JSON FILE AS GAME_NAME.json
#
# Create an endpoint to roll a dice and record to json file with persons name, roll id, timestamp, and roll
# @app.route('rollAndSave')
# def roll_n_save():
#     LOAD JSON FILE AND ASSIGN NEWEST ID
#     GET QUERY ARGS FOR NAME, NUM SIDES, NUM_DICE
#     CREATE A TIMESTAMP OBJECT WITH THE DATETIME LIBRARY
#     WRITE TO JSON FILE (JSON.DUMP), DON'T USE STRINGIFIED VERSION
#
# Create and endpoint that allows me to query all dice rolls from a game
# -- YOU WRITE THIS CODE --
#
# Bonus Round create an endpoint that accepts an id (or timestamp) for roll and returns the roll
# -- YOU WRITE THIS CODE
#
##---- END TODO
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

##---------------------------------------------------------------------
# Everything below this will not run, make this into a function and change the column name as
# I am assuming that your dice database does not have a column calls "Stonks" hopefully.
#

conn = sqlite3.connect('test.db')
c = conn.cursor()

c.execute("INSERT INTO stocks VALUES (flask.jsonify(rolls_dict))")
# how to make work por que

conn.commit()
conn.close()
