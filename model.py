"""
    # Created by phucdk at 05/12/2022

    @File    :   model
    @Contact :   phucdk@gmail.com
    @License :

    Description:
"""
import logging
import pickle

logger = logging.getLogger(__name__)

MODEL_FILE_PATH = 'item_predict_result.pkl'


class FutureSaleModel:
    """
    Model is stored in dictionary format item_id: [(shop_id, predict_sale), ...]
    Using singleton to only load model one time

    """
    __instance = None

    @classmethod
    def load_model(cls):
        return pickle.load(open(MODEL_FILE_PATH, 'rb'))

    def __new__(cls, *args, **kwargs):
        if FutureSaleModel.__instance is None:
            FutureSaleModel.__instance = object.__new__(cls)
            FutureSaleModel.__instance.model = FutureSaleModel.load_model()
            logger.info('done init online model singleton')
        return FutureSaleModel.__instance

    def predict(self, item_id: int):
        return self.model[item_id]
