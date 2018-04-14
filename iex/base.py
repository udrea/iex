# Filename: base.py

"""
Data provided for free by IEX (https://iextrading.com/developer/).
See https://iextrading.com/api-exhibit-a/ for more information.
"""

import requests


class _Base:
	def __init__(self):
		self.s = requests.Session()
		self.uri = 'https://api.iextrading.com/'
		self.api = '1.0'

	def close_session(self):
		self.s.close()

	def _get_json(self, endpoint, payload):
		url_path = ''.join([self.uri, self.api, endpoint, payload])
		r = self.s.get(url_path)
		
		if r.status_code == 200:
			data = r.json()
			return(data)
		else:
			raise IEXAPIError('Response {}: {}'.format(r.status_code, r.text))


class IEXAPIError(Exception):
	"""IEX API error."""
	pass
