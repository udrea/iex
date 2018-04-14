# Filename: market.py

"""
Data provided for free by IEX (https://iextrading.com/developer/).
See https://iextrading.com/api-exhibit-a/ for more information.
"""

from iex.base import _Base, IEXAPIError

import pandas as pd
# import urllib.request


class TOPS(_Base):
	"""https://iextrading.com/developer/docs/#tops
	
	TOPS provides IEX’s aggregated best quoted bid and offer position in near
	real time for all securities on IEX’s displayed limit order book. TOPS is
	ideal for developers needing both quote and trade data.
	"""
	_ENDPOINT = '/tops'

	def get_symbols(self, symbols=None):
		if symbols is None:
			payload = ''
		else:
			payload = ''.join(['?symbols=', symbols])

		data = self._get_json(self._ENDPOINT, payload)
		symbols = pd.DataFrame(data)
		return(symbols)

	def get_symbols_last(self, symbols=None):
		_ENDPOINT = ''.join([self._ENDPOINT, '/last'])

		if symbols is None:
			payload = ''
		else:
			payload = ''.join(['?symbols=', symbols])

		data = self._get_json(_ENDPOINT, payload)
		symbols_last = pd.DataFrame(data)
		return(symbols_last)