import yaml

from portfolio_item import PortfolioItem
from instantiable_mutable_mapping import InstantiableMutableMapping

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

	def get_phd_portfolio_items(self):
		return self._filter_portfolio_items(lambda x: x.is_phd_portfolio_item())

	@staticmethod
	def from_yaml(yaml_text: str):
		yaml_data = yaml.load(yaml_text)
		portfolio_items = PortfolioItems()

		for title, content in yaml_data.items():
			portfolio_items[title] = PortfolioItem.from_dict_entry(title, content)

		return portfolio_items
