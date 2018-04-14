# Filename: market/deep.py

"""
Data provided for free by IEX (https://iextrading.com/developer/).
See https://iextrading.com/api-exhibit-a/ for more information.
"""

from iex.base import _Base, IEXAPIError

import pandas as pd


class DEEP(_Base):
	"""https://iextrading.com/developer/docs/#deep"""
	_ENDPOINT = '/deep'
	_TRADES_LAST = range(1, 501)

	def get_symbols(self, symbols):
		"""https://iextrading.com/developer/docs/#deep"""
		payload = ''.join(['?symbols=', symbols])
		data = self._get_json(self._ENDPOINT, payload)
		return(data)

	def get_book(self, symbols):
		"""https://iextrading.com/developer/docs/#book52"""
		if len(symbols.split(',')) > 10:
			raise IEXAPIError('Maximum number of symbols exceeded.')
		else:
			payload = ''.join(['/book?symbols=', symbols])

		data = self._get_json(self._ENDPOINT, payload)
		return(data)

	def get_trades(self, symbols, last=None):
		"""https://iextrading.com/developer/docs/#trades"""
		if len(symbols.split(',')) > 10:
			raise IEXAPIError('Maximum number of symbols exceeded.')
		else:
			if last is None:
				payload = ''.join(['/trades?symbols=', symbols])	
			else:
				# if int(last) > 500:
				if int(last) not in self._TRADES_LAST:
					raise IEXAPIError('last is out of range. Must be between 1 and 500.')
				else:
					payload = ''.join(['/trades?symbols=', symbols, '?last=', str(last)])

		data = self._get_json(self._ENDPOINT, payload)
		return(data)

	def get_system_event(self):
		"""https://iextrading.com/developer/docs/#system-event"""
		payload = '/system-event'
		data = self._get_json(self._ENDPOINT, payload)
		return(data)

	def get_trading_status(self, symbols):
		"""https://iextrading.com/developer/docs/#trading-status"""
		if len(symbols.split(',')) > 10:
			raise IEXAPIError('Maximum number of symbols exceeded. Maximum is 10 symbols.')
		else:
			payload = ''.join(['/trading-status?symbols=', symbols])

		data = self._get_json(self._ENDPOINT, payload)
		trading_status = pd.DataFrame(data)
		return(trading_status)

	def get_op_halt_status(self, symbols):
		"""https://iextrading.com/developer/docs/#operational-halt-status"""
		if len(symbols.split(',')) > 10:
			raise IEXAPIError('Maximum number of symbols exceeded. Maximum is 10 symbols.')
		else:
			payload = ''.join(['/op-halt-status?symbols=', symbols])

		data = self._get_json(self._ENDPOINT, payload)
		operation_halt_status = pd.DataFrame(data)
		return(operation_halt_status)

	def get_ssr_status(self, symbols):
		"""https://iextrading.com/developer/docs/#short-sale-price-test-status"""
		if len(symbols.split(',')) > 10:
			raise IEXAPIError('Maximum number of symbols exceeded. Maximum is 10 symbols.')
		else:
			payload = ''.join(['/ssr-status?symbols=', symbols])

		data = self._get_json(self._ENDPOINT, payload)
		ssr_status = pd.DataFrame(data)
		return(ssr_status)

	def get_security_event(self, symbols):
		"""https://iextrading.com/developer/docs/#security-event"""
		if len(symbols.split(',')) > 10:
			raise IEXAPIError('Maximum number of symbols exceeded. Maximum is 10 symbols.')
		else:
			payload = ''.join(['/security-event?symbols=', symbols])

		data = self._get_json(self._ENDPOINT, payload)
		security_event = pd.DataFrame(data)
		return(security_event)

	def get_trade_breaks(self, symbols, last=None):
		"""https://iextrading.com/developer/docs/#trade-break"""
		if len(symbols.split(',')) > 10:
			raise IEXAPIError('Maximum number of symbols exceeded.')
		else:
			if last is None:
				payload = ''.join(['/trade-breaks?symbols=', symbols])	
			else:
				# if int(last) > 500:
				if int(last) not in self._TRADES_LAST:
					raise IEXAPIError('last is out of range. Must be between 1 and 500.')
				else:
					payload = ''.join(['/trade-breaks?symbols=', symbols, '?last=', str(last)])

		data = self._get_json(self._ENDPOINT, payload)
		return(data)

	def get_auction(self, symbols):
		"""https://iextrading.com/developer/docs/#auction"""
		if len(symbols.split(',')) > 10:
			raise IEXAPIError('Maximum number of symbols exceeded. Maximum is 10 symbols.')
		else:
			payload = ''.join(['/auction?symbols=', symbols])

		data = self._get_json(self._ENDPOINT, payload)
		auction = pd.DataFrame(data).transpose()
		return(auction)

	def get_official_price(self, symbols):
		"""https://iextrading.com/developer/docs/#official-price"""
		if len(symbols.split(',')) > 10:
			raise IEXAPIError('Maximum number of symbols exceeded. Maximum is 10 symbols.')
		else:
			payload = ''.join(['/official-price?symbols=', symbols])

		data = self._get_json(self._ENDPOINT, payload)
		official_price = pd.DataFrame(data)
		return(official_price)
