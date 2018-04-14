# Filename: reference.py

"""
Data provided for free by IEX (https://iextrading.com/developer/).
See https://iextrading.com/api-exhibit-a/ for more information.
"""

from iex.base import _Base, IEXAPIError

import pandas as pd


class Reference(_Base):
	"""https://iextrading.com/developer/docs/#reference-data"""
	_ENDPOINT = '/ref-data/'

	def get_symbols(self):
		"""https://api.iextrading.com/1.0/ref-data/symbols"""
		payload = 'symbols'
		data = self._get_json(self._ENDPOINT, payload)
		symbols = pd.DataFrame(data)
		return(symbols)

	def get_corporate_actions(self, date=None, sample=False):
		"""https://iextrading.com/developer/docs/#iex-corporate-actions"""
		if date is not None:
			payload = ''.join(['daily-list/corporate-actions/', date])
		elif sample is True:
			payload = 'daily-list/corporate-actions/sample'
		else:
			payload = 'daily-list/corporate-actions'

		data = self._get_json(self._ENDPOINT, payload)
		corporate_actions = pd.DataFrame(data)
		return(corporate_actions)

	def get_dividends(self, date=None, sample=False):
		"""https://iextrading.com/developer/docs/#iex-dividends"""
		if date is not None:
			payload = ''.join(['daily-list/dividends/', date])
		elif sample is True:
			payload = 'daily-list/dividends/sample'
		else:
			payload = 'daily-list/dividends'

		data = self._get_json(self._ENDPOINT, payload)
		dividends = pd.DataFrame(data)
		return(dividends)
		

	def get_next_day_ex_date(self, date=None, sample=False):
		"""https://iextrading.com/developer/docs/#iex-next-day-ex-date"""
		if date is not None:
			payload = ''.join(['daily-list/next-day-ex-date/', date])
		elif sample is True:
			payload = 'daily-list/next-day-ex-date/sample'
		else:
			payload = 'daily-list/next-day-ex-date'

		data = self._get_json(self._ENDPOINT, payload)
		next_day_ex_date = pd.DataFrame(data)
		return(next_day_ex_date)

	def get_listed_symbol_directory(self, date=None, sample=False):
		"""https://iextrading.com/developer/docs/#iex-listed-symbol-directory"""
		if date is not None:
			payload = ''.join(['daily-list/symbol-directory/', date])
		elif sample is True:
			payload = 'daily-list/symbol-directory/sample'
		else:
			payload = 'daily-list/symbol-directory'

		data = self._get_json(self._ENDPOINT, payload)
		symbol_directory = pd.DataFrame(data)
		return(symbol_directory)
