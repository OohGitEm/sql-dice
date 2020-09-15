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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

conn = sqlite3.connect('test.db')
c = conn.cursor()

c.execute("INSERT INTO stocks VALUES (flask.jsonify(rolls_dict))")
# how to make work por que

conn.commit()
conn.close()
