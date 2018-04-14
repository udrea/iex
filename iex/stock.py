# Filename: stock.py

"""
Data provided for free by IEX (https://iextrading.com/developer/).
See https://iextrading.com/api-exhibit-a/ for more information.
"""

from iex.base import _Base, IEXAPIError

import pandas as pd


class Stock(_Base):
	"""https://iextrading.com/developer/docs/#stocks"""
	_ENDPOINT = '/stock/'
	_NEWS_RANGE = range(1, 51)
	_PERIOD = ['5y', '2y', '1y', 'ytd', '6m', '3m', '1m']
	_CHART_RANGE = _PERIOD + ['date', 'dynamic']

	def batch_requests(self):
		"""https://iextrading.com/developer/docs/#batch-requests"""
		pass

	def get_book(self, symbol):
		"""https://iextrading.com/developer/docs/#book"""
		payload = ''.join([symbol, '/book'])
		data = self._get_json(self._ENDPOINT, payload)

		quote = pd.DataFrame(data['quote'], index=[0])
		bids = pd.DataFrame(data['bids'])
		asks = pd.DataFrame(data['asks'])
		trades = pd.DataFrame(data['trades'])
		systemEvent = pd.DataFrame(data['systemEvent'], index=[0])

		return(quote, bids, asks, trades, systemEvent)

	def get_chart(self, symbol, chart_range='1m'):
		"""https://iextrading.com/developer/docs/#chart"""
		if chart_range is None:
			payload = ''.join([symbol, '/chart'])
		elif chart_range not in self._CHART_RANGE:
			raise IEXAPIError('Out of range.')
		else:
			payload = ''.join([symbol, '/chart/', chart_range])

		data = self._get_json(self._ENDPOINT, payload)
		chart = pd.DataFrame(data)
		return(chart)

	def get_company(self, symbol):
		"""https://iextrading.com/developer/docs/#company"""
		payload = ''.join([symbol, '/company'])
		data = self._get_json(self._ENDPOINT, payload)
		company = pd.DataFrame(data, index=[0])
		return(company)

	def get_delayed_quote(self, symbol):
		"""https://iextrading.com/developer/docs/#delayed-quote"""
		payload = ''.join([symbol, '/delayed-quote'])
		data = self._get_json(self._ENDPOINT, payload)
		# delayed_quote = pd.DataFrame(data, index=[0])
		# return(delayed_quote)
		return(data)

	def get_dividends(self, symbol, period='1m'):
		"""https://iextrading.com/developer/docs/#dividends"""
		if period is None:
			payload = ''.join([symbol, '/dividends'])
		elif period not in self._PERIOD:
			raise IEXAPIError('Dividends period is out of range.')
		else:
			payload = ''.join([symbol, '/dividends/', period])

		data = self._get_json(self._ENDPOINT, payload)
		dividends = pd.DataFrame(data)
		return(dividends)

	def get_earnings(self, symbol):
		"""https://iextrading.com/developer/docs/#earnings"""
		payload = ''.join([symbol, '/earnings'])
		data = self._get_json(self._ENDPOINT, payload)
		earnings = pd.DataFrame(data['earnings'])
		return(earnings)

	def get_effective_spread(self, symbol):
		"""https://iextrading.com/developer/docs/#effective-spread"""
		payload = ''.join([symbol, '/effective-spread'])
		data = self._get_json(self._ENDPOINT, payload)
		effective_spread = pd.DataFrame(data)
		return(effective_spread)

	def get_financials(self, symbol):
		"""https://iextrading.com/developer/docs/#financials"""
		payload = ''.join([symbol, '/financials'])
		data = self._get_json(self._ENDPOINT, payload)
		financials = pd.DataFrame(data['financials'])
		return(financials)

	def get_threshold_securities(self, symbol, date=None):
		"""https://iextrading.com/developer/docs/#iex-regulation-sho-threshold-securities-list"""
		if date is None:
			payload = ''.join([symbol, '/threshold-securities'])
		else:
			payload = ''.join([symbol, '/threshold-securities/', date])

		data = self._get_json(self._ENDPOINT, payload)
		threshold_securities = pd.DataFrame(data)
		return(threshold_securities)

	def get_short_interest(self, symbol, date=None):
		"""https://iextrading.com/developer/docs/#iex-short-interest-list"""
		if date is None:
			payload = ''.join([symbol, '/short-interest'])
		else:
			payload = ''.join([symbol, '/short-interest/', date])

		data = self._get_json(self._ENDPOINT, payload)
		short_interest = pd.DataFrame(data)
		return(short_interest)

	def get_stats(self, symbol):
		"""https://iextrading.com/developer/docs/#key-stats"""
		payload = ''.join([symbol, '/stats'])
		data = self._get_json(self._ENDPOINT, payload)
		stats = pd.DataFrame(data, index=[0])
		return(stats)

	def get_list(self, list_type):
		"""https://iextrading.com/developer/docs/#list"""
		payload = ''.join(['/stock/market/list/', list_type])
		data = self._get_json(self._ENDPOINT, payload)
		lists = pd.DataFrame(data)
		return(lists)

	def get_logo(self, symbol):
		"""https://iextrading.com/developer/docs/#logo"""
		payload = ''.join([symbol, '/logo'])
		data = self._get_json(self._ENDPOINT, payload)
		logo = data['url']
		return(logo)

	def get_news(self, symbol, period='10'):
		"""https://iextrading.com/developer/docs/#news"""
		if period is None:
			payload = ''.join([symbol, '/news'])
		elif period not in self._PERIOD:
			raise IEXAPIError('News period is out of range.')
		else:
			payload = ''.join([symbol, '/news/last/', str(period)])

		data = self._get_json(self._ENDPOINT, payload)
		news = pd.DataFrame(data)
		return(news)

	def get_ohlc(self, symbol):
		"""https://iextrading.com/developer/docs/#ohlc"""
		payload = ''.join([symbol, '/ohlc'])
		data = self._get_json(self._ENDPOINT, payload)
		ohlc = pd.DataFrame(data)
		return(ohlc)

	def get_peers(self, symbol):
		"""https://iextrading.com/developer/docs/#peers"""
		payload = ''.join([symbol, '/peers'])
		data = self._get_json(self._ENDPOINT, payload)
		return(data)

	def get_previous(self, symbol):
		"""https://iextrading.com/developer/docs/#previous"""
		payload = ''.join([symbol, '/previous'])
		data = self._get_json(self._ENDPOINT, payload)
		return(data)

	def get_price(self, symbol):
		"""https://iextrading.com/developer/docs/#price"""
		payload = ''.join([symbol, '/price'])
		data = self._get_json(self._ENDPOINT, payload)
		return(data)

	def get_quote(self, symbol, displayPercent=False):
		"""https://iextrading.com/developer/docs/#quote"""
		if displayPercent:
			payload = ''.join([symbol, '/quote?displayPercent=true'])
		else:
			payload = ''.join([symbol, '/quote'])

		data = self._get_json(self._ENDPOINT, payload)
		return(data)

	def get_relevant(self, symbol):
		"""https://iextrading.com/developer/docs/#relevant"""
		payload = ''.join([symbol, '/relevant'])
		data = self._get_json(self._ENDPOINT, payload)
		relevant = pd.DataFrame(data)
		return(relevant)

	def get_splits(self, symbol, period='1m'):
		"""https://iextrading.com/developer/docs/#splits"""
		if period is None:
			payload = ''.join([symbol, '/splits'])
		elif period not in self._PERIOD:
			raise IEXAPIError('Splits period is out of range.')
		else:
			payload = ''.join([symbol, '/splits/', period])

		data = self._get_json(self._ENDPOINT, payload)
		return(data)
	
	def get_time_series(self, symbol):
		"""https://iextrading.com/developer/docs/#time-series"""
		payload = ''.join([symbol, '/time-series'])
		data = self._get_json(self._ENDPOINT, payload)
		time_series = pd.DataFrame(data)
		return(time_series)

	def get_volume_by_venue(self, symbol):
		"""https://iextrading.com/developer/docs/#volume-by-venue"""
		payload = ''.join([symbol, '/volume-by-venue'])
		data = self._get_json(self._ENDPOINT, payload)
		volume_by_venue = pd.DataFrame(data)
		return(volume_by_venue)
