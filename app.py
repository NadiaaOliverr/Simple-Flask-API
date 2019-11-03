from flask import Flask, jsonify, request

app = Flask(__name__)

devs = [
    {
        'id': 1,
        'name': 'Nádia Oliveira',
        'lang': 'Python'
    },
    {
        'id': 2,
        'name': 'Lucas Costa',
        'lang': 'C'
    },
    {
        'id': 3,
        'name': 'Lucas Ferreira',
        'lang': 'C++'
    }
]


@app.route('/devs', methods=['GET'])
def index():
    return jsonify(devs), 200


@app.route('/devs/<string:lang>', methods=['GET'])
def devs_per_lang(lang):
    devs_per_lang = [dev for dev in devs if dev['lang'] == lang]
    return jsonify(devs_per_lang), 200


@app.route('/devs/<int:id>', methods=['PUT'])
def change_lang(id):
    for dev in devs:
        if dev['id'] == id:
            dev['lang'] = request.get_json().get('lang')
            return jsonify(dev), 200

    return jsonify({'Error': 'Not Found'}), 404


@app.route('/devs/<int:id>', methods=['GET'])
def devs_per_id(id):
    for dev in devs:
        if dev['id'] == id:
            return jsonify(dev), 200

    return jsonify({'Error': 'Not Found'}), 404


@app.route('/devs/<int:id>', methods=['DELETE'])
def remove_dev(id):
    for dev in devs:
        if dev['id'] == id:
            index = id - 1
            del devs[index]
            return jsonify({'message': 'Removido com sucesso'}), 200

    return jsonify({'message': 'ID não encontrado'}), 404


@app.route('/devs', methods=['POST'])
def save_dev():
    data = request.get_json()
    devs.append(data)
    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)
