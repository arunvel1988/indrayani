from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/teams')
def teams():
    return render_template('teams.html')

@app.route('/fixtures')
def fixtures():
    return render_template('fixtures.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

def read_team_data(file_name):
    players = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                name, position, photo = line.strip().split(",")
                players.append({"name": name, "position": position, "photo": photo})
    except FileNotFoundError:
        print(f"File {file_name} not found!")
    return players

@app.route('/teams/senior')
def senior_team():
    players = read_team_data("senior_team.txt")
    return render_template('team_details.html', team_name="Senior Team", players=players)

@app.route('/teams/junior')
def junior_team():
    players = read_team_data("junior_team.txt")
    return render_template('team_details.html', team_name="Junior Team", players=players)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
