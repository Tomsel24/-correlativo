from flask import Flask, jsonify

app = Flask(__name__)

# Variable global para almacenar el número correlativo actual
correlativo_actual = 0

@app.route('/correlativo', methods=['GET'])
def obtener_correlativo():
    global correlativo_actual
    correlativo_actual += 1
    return jsonify({'correlativo': correlativo_actual})

if __name__ == '__main__':
    app.run(debug=True)
