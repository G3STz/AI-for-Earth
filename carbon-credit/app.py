from flask import Flask, request
import json
from services.calculations import Calculations
from services.tree_translate import *

app = Flask(__name__)

@app.route('/health_check', methods=["GET"])
def health_check():
    return { "status": "OK" }, 200

@app.route('/carbon_credit', methods=["POST"])
def carbon_credit():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = json.loads(request.data)
    
        area = data["area"]
        unit = data["unit"]
        plant_list = data["plant_list"]



        if (len(plant_list) == 0):
            msg = "no data"
            res = []
        else:
            new_plant_list = filter_plant(plant_list)

            c = Calculations()
            # plant_list_en = trans_list(plant_list)  # handle non-tree in database
            msg = "success"
            res = c.calc(new_plant_list, area, unit)

        
        enc_json = json.dumps(
            {
                "status": True,
                "message": msg,
                "values": res
            }
            ).encode("utf8")

        return enc_json.decode()
        
   
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8010)