from collections import MutableMapping
import yaml

from portfolio_item import PortfolioItem

class InstantiableMutableMapping(MutableMapping):
	def __init__(self, *args, **kwargs):
		self.__dict__.update(*args, **kwargs)


	def __setitem__(self, key, value):
		self.__dict__[key] = value


	def __getitem__(self, key):
		return self.__dict__[key]


	def __delitem__(self, key):
		del self.__dict__[key]


	def __iter__(self):
		return iter(self.__dict__)


	def __len__(self):
		return len(self.__dict__)


	def __str__(self):
		return str(self.__dict__)


	def __repr__(self):
		return '{}, D({})'.format(super(D, self).__repr__(), self.__dict__)

class PortfolioItems(InstantiableMutableMapping):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def _filter_portfolio_items(self, filter_fn):
		filtered = PortfolioItems()

		for key, val in self.__dict__.items():
			if filter_fn(val):
				filtered[key] = val

		return filtered

	def get_main_portfolio_items(self):
		return self._filter_portfolio_items(lambda x: x.is_main_portfolio_item())

	def get_game_jam_portfolio_items(self):
		return self._filter_portfolio_items(lambda x: x.is_game_jam_entry_item())

	def get_university_portfolio_items(self):
		return self._filter_portfolio_items(lambda x: x.is_university_portfolio_item())

	@staticmethod
	def from_yaml(yaml_text: str):
		yaml_data = yaml.load(yaml_text)
		portfolio_items = PortfolioItems()

		for title, content in yaml_data.items():
			portfolio_items[title] = PortfolioItem.from_dict_entry(title, content)

		return portfolio_items
