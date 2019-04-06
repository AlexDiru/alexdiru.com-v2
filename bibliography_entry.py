from typing import Iterable

class BibliographyEntry:
	def __init__(self) -> None:
		self.title = "" # Set when needed
		self.genre = ""
		self.year = 0
		self.links = {}
		self.type = ""
		self.word_count = 0
		self.status = ""

	@staticmethod
	def from_dict_entry(title, content):
		bibliography_entry = BibliographyEntry()
		bibliography_entry.title = title

		if "Genre" in content:
			bibliography_entry.genre = content["Genre"]
		if "Year" in content:
			bibliography_entry.year = content["Year"]
		if "Type" in content:
			bibliography_entry.type = content["Type"]
		if "Word Count" in content:
			bibliography_entry.word_count = content["Word Count"]
		if "Status" in content:
			bibliography_entry.status = content["Status"]
		if "Links" in content:
			for link_name, link_url in content["Links"].items():
				bibliography_entry.links[link_name] = link_url

		return bibliography_entry