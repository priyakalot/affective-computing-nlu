# -*- coding: utf-8 -*-


import os

from rasa.nlu.model import Interpreter


# In case we generate a different model, we just need to:
# 1. Go into /models, 2. Extract the tar.gz, and 3. Change the 5th term below.
MODEL_PATH = os.getcwd() + os.path.sep + 'models' + \
			 os.path.sep + 'nlu-20200529-143136' + \
			 os.path.sep + 'nlu'
try:
	interpreter = Interpreter.load(MODEL_PATH)
except Exception as error:
	print(f"Error - Unable to open Rasa NLU model: {error}")


def get_prediction(utter):
	pred = {d['name'] : d['confidence'] for d in interpreter.parse(utter)['intent_ranking']}
	print(pred)
	return pred


get_prediction('I\'m so glad to hear that!')
