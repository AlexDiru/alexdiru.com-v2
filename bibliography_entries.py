import yaml

from instantiable_mutable_mapping import InstantiableMutableMapping
from bibliography_entry import BibliographyEntry

class BibliographyEntries(InstantiableMutableMapping):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


	def get_short_stories(self):
		return self._filter_bibliography_items(lambda x: x.type == "Short Story")

	def get_novels(self):
		return self._filter_bibliography_items(lambda x: x.type == "Novel")

	def _filter_bibliography_items(self, filter_fn):
		filtered = BibliographyEntries()

		for key, val in self.__dict__.items():
			if filter_fn(val):
				filtered[key] = val

		return filtered

	@staticmethod
	def from_yaml(yaml_text: str):
		yaml_data = yaml.load(yaml_text)
		bibliography_entries = BibliographyEntries()

		items = list(yaml_data.items())
		items.reverse()

		for title, content in items:
			bibliography_entries[title] = BibliographyEntry.from_dict_entry(title, content)

		return bibliography_entries
