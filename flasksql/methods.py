import requests
import random

@bp.route('/roll', methods=['GET', 'POST'])

def numOfRolls():

    arg = int(request.args.get('VAL'))

    for i in range(0,arg):
        roll = random.randint(1,6)

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

