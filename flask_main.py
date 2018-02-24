import markdown
import yaml
from flask import Flask
from flask import render_template
from flask import Markup
from typing import Iterable, List, Dict
from collections import MutableMapping

app = Flask(__name__)

UE4_LOGO = "img/ue4-logo.png"
LIBGDX_LOGO = "img/llllll.png"
CSHARP_LOGO = "img/dsfdsf"
IRRLICHT_LOGO = "img/adsdsa"
DARKGDK_LOGO = "img/dark"
R_LOGO = "img/rrrr"
UNITY_LOGO = "img/asdds"

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

	def get_main_portfolio_items(self):
		filtered = PortfolioItems()

		for key, val in self.__dict__.items():
			if val.is_main_portfolio_item():
				filtered[key] = val

		return filtered 

	def get_game_jam_portfolio_items(self):
		filtered = PortfolioItems()

		for key, val in self.__dict__.items():
			if val.is_game_jam_entry_item():
				filtered[key] = val

		return filtered 

	@staticmethod
	def from_yaml(yaml_text: str):
		yaml_data = yaml.load(yaml_text)
		portfolio_items = PortfolioItems()

		for title, content in yaml_data.items():
			portfolio_items[title] = PortfolioItem.from_dict_entry(content)

		return portfolio_items

class PortfolioItem:
	def __init__(self, portfolio_type :str = "Main") -> None:
		self.title = "" # Set when needed
		self.subtitle = ""
		self.logo = ""
		self.shorttext = ""
		self.content = ""
		self.images = [] # type: List[str]
		self.videos = [] # type: List[str]
		self.links = {} # type: Dict[str, str]
		self.portfolio_grid_image_index = 0
		self.__portfolio_type__ = portfolio_type

	def get_image_filename(self, index: int) -> str:
		return "img/portfolio/" + self.images[index]

	def get_portfolio_grid_image(self) -> str:
		return self.get_image_filename(self.portfolio_grid_image_index)

	def get_images_for_jinja(self) -> Iterable[str]:
		return map(lambda image: "img/portfolio/" + image, self.images)

	def is_main_portfolio_item(self) -> bool:
		return self.__portfolio_type__ == "Main"

	def is_game_jam_entry_item(self) -> bool:
		return self.__portfolio_type__ == "Game Jam"

	@staticmethod
	def from_dict_entry(content):
		portfolio_type = "Main"
		if "Portfolio Type" in content:
			portfolio_type = content["Portfolio Type"]

		portfolio_item = PortfolioItem(portfolio_type)

		if "SubTitle" in content:
			portfolio_item.subtitle = content["SubTitle"]
		if "Logo" in content:
			portfolio_item.logo = content["Logo"]
		if "ShortText" in content:
			portfolio_item.shorttext = content["ShortText"]
		if "Content" in content:
			portfolio_item.content = content["Content"]
		if "Images" in content:
			image_index = 0
			for image in content["Images"]:
				if "*" in image:
					portfolio_item.portfolio_grid_image_index = image_index
					image = image.replace("*", "")
				portfolio_item.images.append(image)
				image_index = image_index + 1
		if "Videos" in content:
			for video in content["Videos"]:
				portfolio_item.videos.append(video)
		if "Links" in content:
			for link_name, link_url in content["Links"].items():
				portfolio_item.links[link_name] = link_url

		return portfolio_item

portfolio_items = PortfolioItems.from_yaml(open("content/PortfolioItems.yaml"))

@app.route('/portfolio-item/<string:game_title>.html')
def render_game(game_title :str) -> str:
	portfolio_item = portfolio_items[game_title]
	portfolio_item.title = game_title
	return render_template('portfolio.html', portfolio_item=portfolio_item)

@app.route('/')
def site_index() -> str:
	return render_template('index.html', portfolio_items=portfolio_items)

#@app.route('/')
#def site_index() -> str:
#	content = """
#Chapter
#=======
#
#Section
#-------
#
#* Item 1
#* Item 2
#"""
#	content = Markup(markdown.markdown(content))
#	return render_template('index.html', **locals())

if __name__ == '__main__':
	app.run()