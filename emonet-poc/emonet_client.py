# -*- coding: utf-8 -*-


from emonet import EmoNet


em = EmoNet()

def get_prediction(utter):
	try:
		return em.predict(text=utter, with_dist=True)
	except Exception as error:
		return f"Error - Unable to obtain prediction due to: {error}"

