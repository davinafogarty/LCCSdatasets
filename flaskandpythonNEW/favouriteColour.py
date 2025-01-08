from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dictionary to record votes
votes = {
    'red': 0,
    'blue': 0,
    'green': 0,
    'yellow': 0
}

# Route for the main page
@app.route('/')
def index():
    return render_template('index1.html')

# Route to handle the vote submission
@app.route('/vote', methods=['POST'])
def vote():
    color = request.form.get('color')
    if color in votes:
        votes[color] += 1
        return jsonify({'message': f'Thank you for voting for {color}!', 'votes': votes}), 200
    return jsonify({'message': 'Invalid color selection.'}), 400

app.run(host='0.0.0.0', port=6001, debug=False)

