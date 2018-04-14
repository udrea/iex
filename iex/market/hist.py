# Filename: market/hist.py

"""
Data provided for free by IEX (https://iextrading.com/developer/).
See https://iextrading.com/api-exhibit-a/ for more information.
"""

from iex.base import _Base, IEXAPIError

import pandas as pd


class HIST(_Base):
	"""https://iextrading.com/developer/docs/#hist"""
	_ENDPOINT = '/hist'

	def get_hist(self, date=None):
		if date is None:
			payload = ''
			data = self._get_json(self._ENDPOINT, payload)

			all_hist = pd.DataFrame()
			for k in data.keys():
				all_hist = all_hist.append(pd.DataFrame(data[k]))

			all_hist = all_hist.reset_index(drop=True)
			return(all_hist)
		else:
			payload = ''.join(['?date=', date])
			data = self._get_json(self._ENDPOINT, payload)
			hist = pd.DataFrame(data)
			return(hist)
