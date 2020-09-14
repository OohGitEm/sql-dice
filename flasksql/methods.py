import flask
import rolltide

app = flask.Flask(__name__)
@app.route('/roll', methods=['GET'])
def roll_n_sided_dice_n_times():
    num_of_sides = int(flask.request.args.get('num_of_sides'))
    num_of_rolls = int(flask.request.args.get('num_of_rolls'))
    rolls_dict = rolltide.roll_dice(num_of_rolls, num_of_sides)
    return flask.jsonify(rolls_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

