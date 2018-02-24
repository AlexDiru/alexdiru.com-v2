from typing import Iterable

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
	def from_dict_entry(title, content):
		portfolio_type = "Main"
		if "Portfolio Type" in content:
			portfolio_type = content["Portfolio Type"]

		portfolio_item = PortfolioItem(portfolio_type)

		if "SubTitle" in content:
			portfolio_item.subtitle = content["SubTitle"]
		if "Logo" in content:
			portfolio_item.logo = content["Logo"]
		if "Short Text" in content:
			portfolio_item.shorttext = content["Short Text"]
		else:
			print("Warning Short Text not found in " + title)
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