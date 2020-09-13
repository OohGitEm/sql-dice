import requests
import random
import rolltide

# This is using the completely wrong library
# Use flask not requests

# app = flask.Flask(__name)__)
# @app.route('/roll', methods=['GET', 'POST'])
# def num_of_rolls():
#     num_of_dice = int(request.args.get('numOfDice')
#
#
#     ... Finish the rest using the rolltide library you've created
#     This will require you to rewrite the input statement such that the
#     dice sides and num of dice can be passed as a function argument
#     return an hashmap object like {'1': 2, '2': 5, '3': 6, '4': 1, '5': 0, '6': 3}
#     where the values of the dictionary are the number of rolls, so this should sum to the number
#     of dice given by the function argument
#     Before trying to write these to a database, first try returning them to the client via a return statement in the flask method

@bp.route('/roll', methods=['GET', 'POST'])

def numOfRolls(): # Dont mix case syntax

    arg = int(request.args.get('VAL'))

    rolltide(num_of_dice, num_of_side)
    
    if request.method == 'POST':
        return print(f'You rolled a {roll}')

    db = get_db()
    error = None



    if error is None:
        db.execute(
            'INSERT INTO rolls (result, num_rolls) VALUES (?, ?)'
            (result, num_rolls)
        )
        db.commit()

