"""
    # Created by phucdk at 05/12/2022

    @File    :   main
    @Contact :   phucdk@gmail.com
    @License :

    Description:
"""

from flask import request
from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
from model import FutureSaleModel

app = Flask(__name__,
            static_folder='web/static',
            template_folder='web/templates')


def init_logger():
    logger = logging.getLogger('future_sale_predict')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)

    rotate_handler = RotatingFileHandler('log/future_sale_predict.log', maxBytes=200000000, backupCount=10)
    rotate_handler.setLevel(logging.INFO)
    rotate_handler.setFormatter(formatter)

    logger.addHandler(rotate_handler)
    logger.addHandler(ch)


@app.route('/')
def hello():
    return app.send_static_file('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    args = request.args
    item_id = int(args['item_id'])
    result = FutureSaleModel().predict(item_id)
    str_result = ''
    for shop_id, predict_sale in result:
        str_result += f"{shop_id}:&nbsp&nbsp&nbsp&nbsp{predict_sale} <br \>"
    return str_result


if __name__ == '__main__':
    init_logger()
    app.run(host="0.0.0.0", port=5000)
