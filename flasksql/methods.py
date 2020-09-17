import flask
import rolltide
import sqlite3
import datetime

app = flask.Flask(__name__)
@app.route('/roll', methods=['GET'])
def roll_n_sided_dice_n_times():
    num_of_sides = int(flask.request.args.get('num_of_sides'))
    num_of_rolls = int(flask.request.args.get('num_of_rolls'))
    rolls_dict = rolltide.roll_dice(num_of_rolls, num_of_sides)
    return flask.jsonify(rolls_dict)

##---- TODO
# First write a REST endpoint that allows someone to initialize a new game. General structure will look like:
app.route('/initializeGame', methods=['POST'])
def initialize_game():
    with open("game_name.json", "w") as json_file:
        data = json.load(json_file)

# Create an endpoint to roll a dice and record to json file with persons name, roll id, timestamp, and roll
@app.route('/rollAndSave')
def roll_n_save():
    json.load(json_file) #LOAD JSON FILE AND ASSIGN NEWEST ID

    if 'name' in request.args:
        name = str(request.args['name']) #GET QUERY ARGS FOR NAME, NUM SIDES, NUM_DICE
    if 'num_sides' in request.args:
        num_sides = int(request.args['num_sides'])
    if 'num_dice' in request.args:
        num_dice = int(request.args['num_dice'])
    else:
        return "ERROR"

    ts = datetime.datetime.now().timestamp() #CREATE A TIMESTAMP OBJECT WITH THE DATETIME LIBRARY

    json.dump([name, num_sides, num_dice, ts]) #WRITE TO JSON FILE (JSON.DUMP), DON'T USE STRINGIFIED VERSION

@app.route('/', methods=['GET'])
def trump_lied_200k_died():
    return jsonify(rolls)

app.run()

# Bonus Round create an endpoint that accepts an id (or timestamp) for roll and returns the roll
@app.route('/', methods=['GET'])
def id_roll():
    query_paramaters = request.args

    id = query_paramaters.get('id')

    query = "SELECT * FROM rolls WHERE"
    to_filter = []

    if id:
        query += ' id=?'
        to_filter.append(id)
    else:
        return "ERROR"

    conn = sqlite3.connect('rolls.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    id_query = cur.execute(query, to_filter).fetchall()

    return jsonify(id_query)

##---- END TODO
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

@app.route('/', methods=['GET'])
def down_with_capitalism():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    c.execute("INSERT INTO rolls VALUES (flask.jsonify(rolls_dict))")

    conn.commit()
    conn.close()
