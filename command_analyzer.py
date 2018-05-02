from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import socket

app = Flask(__name__)
api = Api(app)

valid_vocal_commands = {
    'play':   ['jouer', 'play', 'lancer'],
    'search': ['chercher', 'cherche', 'search'],
    'pause':  ['pause'],
    'resume': ['reprendre', 'reprend', 'resume'],
    'stop':   ['arrêt', 'arrête', 'arrêter', 'stop'],
}

ip = socket.gethostbyname(socket.gethostname())

class Vocal(Resource):
    def get(self):
        command = ''
        params = []

        vocal = request.args.get('vocal')
        if vocal:
            vocal = vocal.split(' ')
            # Search in which category ('play', 'search', 'pause', ...)
            # the vocal command belongs to
            for category, commands in valid_vocal_commands.items():
                if vocal[0] in commands:
                    command = category
                    if category in ['play', 'search']:
                        params = ' '.join(x for x in vocal[1:])
                    break

        result = {'command': command, 'params': str(params)}
        return result


api.add_resource(Vocal, '/command')


if __name__ == '__main__':
     app.run(host=str(ip), port='5002')
