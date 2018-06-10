import configparser
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request

application = Flask(__name__)

config = configparser.ConfigParser()

def config_reader():
    config.read('E:\pythonLbs\Lab5/olympic_db.conf')

config_reader()

application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + config.get('DB', 'user') + \
                                                ':' + config.get('DB', 'password') + '@' + \
                                                config.get('DB', 'host') + '/' + config.get('DB', 'db')

application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

mysql = SQLAlchemy()
mysql.init_app(application)

class Games(mysql.Model):
    __tablename__ = 'olympic'
    id = mysql.Column(mysql.Integer, primary_key=True)
    length = mysql.Column(mysql.Integer, nullable=False)
    name = mysql.Column(mysql.String(128), nullable=False)
    capacity = mysql.Column(mysql.Integer, nullable=False)
    location = mysql.Column(mysql.String, nullable=False)

    def __repr__(self):
        return '<Olympic Games (%s, %s, %s, %s, %s) >' % (self.id, self.length, self.name, self.capacity, self.location)


@application.route('/game', methods=['POST'])
def create_game():
    id = request.get_json()["id"]
    length = request.get_json()["length"]
    name = request.get_json()["name"]
    capacity = request.get_json()["capacity"]
    location = request.get_json()["location"]
    curr_session = mysql.session

    game = Games(id=id, length=length, name=name, capacity=capacity, location=location)

    try:
        curr_session.add(game)
        curr_session.commit()
    except:
        curr_session.rollback()
        curr_session.flush()

    game_id = game.id
    data = Games.query.filter_by(id=game_id).first()

    config_reader()

    result = [data.id, data.name, data.length, data.capacity, data.location]

    return jsonify(session=result)


@application.route('/game', methods=['GET'])
def get_games():
    data = Games.query.all()

    data_all = []

    for game in data:
        data_all.append([game.id, game.name, game.length, game.capacity, game.location])

    return jsonify(games=data_all)


@application.route('/game', methods=['PATCH'])
def update_game():
    global game
    game_id = request.get_json()["id"]
    length = request.get_json()["length"]
    name = request.get_json()["name"]
    capacity = request.get_json()["capacity"]
    location = request.get_json()["location"]
    curr_session = mysql.session

    try:
        game = games.query.filter_by(id=game_id).first()
        game.length = length
        game.name = name
        game.capacity = capacity
        game.location = location
        curr_session.commit()
    except:
        curr_session.rollback()
        curr_session.flush()

    game_id = game.id
    data = games.query.filter_by(id=game_id).first()

    config_reader()

    result = [data.id, data.name, data.length, data.capacity, data.location]

    return jsonify(session=result)


@application.route('/game/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    curr_session = mysql.session

    games.query.filter_by(id=game_id).delete()
    curr_session.commit()

    return get_game()


if __name__ == "__main__":
    application.run()
