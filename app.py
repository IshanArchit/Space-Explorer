from typing import Any
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def get_dict(id: int, date: str, mission_name: str, vehicle: str, place: str, link: str) -> dict[str, Any]:
    return {
        'id': id,
        'date': date,
        'mission_name': mission_name,
        'vehicle': vehicle,
        'place': place,
        'link': link
    }


@app.route('/upcoming_missions', methods=['GET'])
def get_mission():
    return jsonify([
        
        get_dict(1, 'January, 2025', 'NVS-02(IRNSS-1K)', 'GSLV MK II',
                 'Second Launch Pad, Satish Dhawan Space Centre, India', 'https://nextspaceflight.com/launches/details/7658'),
        get_dict(2, 'March, 2025', 'GaganYaan Demo Flight 1', 'LVM-3',
                 'Second Launch Pad, Satish Dhawan Space Centre, India', 'https://nextspaceflight.com/launches/details/1980l'),
        get_dict(3, 'March, 2025', 'NISAR', 'GSLV MK II',
                 'Second Launch Pad, Satish Dhawan Space Centre, India', 'https://nextspaceflight.com/launches/details/4085'),
        get_dict(4, '1st quarter, 2025', 'TDS-01', 'PSLV-XL',
                 'First Launch Pad, Satish Dhawan Space Centre, India', 'https://nextspaceflight.com/launches/details/7530'),
        get_dict(5, '1st quarter, 2025', 'BlueBird Block 2', 'LVM-3',
                 'Second Launch Pad, Satish Dhawan Space Centre, India', 'https://nextspaceflight.com/launches/details/7689'),
    ])


if __name__ == '__main__':
    app.run(debug=True)
