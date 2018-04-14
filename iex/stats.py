# Filename: stats.py

"""
Data provided for free by IEX (https://iextrading.com/developer/).
See https://iextrading.com/api-exhibit-a/ for more information.
"""

from iex.base import _Base, IEXAPIError

import pandas as pd


class Stats(_Base):
	"""https://iextrading.com/developer/docs/#iex-stats"""
	_ENDPOINT = '/stats'
	_HISTORICAL_DAILY_LAST = range(1, 91)

	def get_intraday(self):
		"""https://iextrading.com/developer/docs/#intraday"""
		payload = '/intraday'
		data = self._get_json(self._ENDPOINT, payload)
		intraday = pd.DataFrame(data)
		return(intraday)

	def get_recent(self):
		"""https://iextrading.com/developer/docs/#recent"""
		payload = '/recent'
		data = self._get_json(self._ENDPOINT, payload)
		recent = pd.DataFrame(data)
		return(recent)

	def get_records(self):
		"""https://iextrading.com/developer/docs/#records"""
		payload = '/records'
		data = self._get_json(self._ENDPOINT, payload)
		records = pd.DataFrame(data)
		return(records)

	def get_historical(self, date=None):
		"""https://iextrading.com/developer/docs/#historical-summary"""
		if date is not None:
			payload = ''.join(['/historical?date=', date])
		else:
			payload = '/historical'

		data = self._get_json(self._ENDPOINT, payload)
		historical_summary = pd.DataFrame(data)
		return(historical_summary)

	def get_historical_daily(self, date=None, last=None):
		"""https://iextrading.com/developer/docs/#historical-daily"""
		if date is not None:
			payload = ''.join(['/historical/daily?date=', date])
		elif last is not None and int(last) in self._HISTORICAL_DAILY_LAST:
			payload = ''.join(['/historical/daily?last=', last])
		elif last is not None and int(last) not in self._HISTORICAL_DAILY_LAST:
			raise IEXAPIError('last is out of range. Must be between 1 and 90.')
		else:
			payload = '/historical/daily'

		data = self._get_json(self._ENDPOINT, payload)
		historical_daily = pd.DataFrame(data)
		return(historical_daily)

	def get_markets(self):
		"""https://iextrading.com/developer/docs/#markets"""
		_ENDPOINT = '/market'
		payload = ''
		data = self._get_json(_ENDPOINT, payload)
		markets_volume = pd.DataFrame(data)
		return(markets_volume)
