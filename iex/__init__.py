# Filename: __init__.py

"""
A Python module to retrieve stock market data from The Investors Exchange (IEX)
Developer Platform.

Data provided for free by IEX (https://iextrading.com/developer/).
See https://iextrading.com/api-exhibit-a/ for more information.
"""

from iex.stock import Stock
from iex.reference import Reference
from iex.market.tops import TOPS
from iex.market.hist import HIST
from iex.market.deep import DEEP
from iex.stats import Stats

# __all__ = ['Stock', 'Reference', 'TOPS', 'HIST', 'DEEP', 'Stats']

__author__ = 'Iulian Udrea'

# PEP0440 compatible formatted version, see:
# https://www.python.org/dev/peps/pep-0440/
#
# Release marker: major.minor.micro
__version__ = '0.0.1'
