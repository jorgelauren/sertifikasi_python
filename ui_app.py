from flask import Flask, render_template, jsonify, request
from db_manager import Session, init_db, seed_data, word_to_numeric, get_sorted_numbers, delete_by_parity, Number
from shapes import Square, Rectangle, Circle
import os

app = Flask(__name__)

# Ensure DB is initialized
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/db/init', methods=['POST'])
def db_init():
    session = Session()
    try:
        init_db()
        seed_data(session)
        return jsonify({"status": "success", "message": "Basis data berhasil diinisialisasi."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        session.close()

@app.route('/api/db/update', methods=['POST'])
def db_update():
    session = Session()
    try:
        word_to_numeric(session)
        return jsonify({"status": "success", "message": "Kata berhasil diubah menjadi simbol angka."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        session.close()

@app.route('/api/db/list', methods=['GET'])
def db_list():
    session = Session()
    try:
        nums = get_sorted_numbers(session)
        data = [{"id": n.id, "angka": n.angka} for n in nums]
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        session.close()

@app.route('/api/db/delete', methods=['POST'])
def db_delete():
    data = request.json
    parity = data.get('parity') # 'even' or 'odd'
    session = Session()
    try:
        delete_by_parity(session, parity)
        return jsonify({"status": "success", "message": f"Angka {parity} berhasil dihapus."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        session.close()

@app.route('/api/shapes/calculate', methods=['POST'])
def calculate_shape():
    data = request.json
    shape_type = data.get('type')
    params = data.get('params', {})
    
    try:
        if shape_type == 'square':
            side = float(params.get('side'))
            shape = Square(side)
        elif shape_type == 'rectangle':
            w = float(params.get('width'))
            h = float(params.get('height'))
            shape = Rectangle(w, h)
        elif shape_type == 'circle':
            r = float(params.get('radius'))
            shape = Circle(r)
        else:
            return jsonify({"status": "error", "message": "Tipe bangun datar tidak valid."}), 400
            
        return jsonify({
            "status": "success",
            "name": str(shape),
            "area": round(shape.calculate_area(), 2),
            "perimeter": round(shape.calculate_perimeter(), 2)
        })
    except ValueError as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Running on a custom port to avoid common conflicts
    app.run(debug=True, port=5000)
