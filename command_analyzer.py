from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

allowed_vocal_commands = [
    'jouer',
    'chercher',
    'pause',
    'reprendre',
    'stop',
]

class Vocal(Resource):
    def get(self):
        command = ''
        params = []

        vocal = request.args.get('vocal')
        if vocal:
            vocal = vocal.split(' ')
            if vocal[0] in allowed_vocal_commands:
                command = vocal[0]
                if vocal[0] in ['jouer', 'chercher']:
                    params = ' '.join(x for x in vocal[1:])

        result = {'command': command, 'params': str(params)}
        return result


api.add_resource(Vocal, '/command')


if __name__ == '__main__':
     app.run(port='5002')
