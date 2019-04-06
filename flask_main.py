import markdown
from flask import Flask
from flask import render_template
from flask import Markup
from typing import Iterable, List, Dict

from portfolio_items import PortfolioItems
from bibliography_entries import BibliographyEntries

app = Flask(__name__)

UE4_LOGO = "img/ue4-logo.png"
LIBGDX_LOGO = "img/llllll.png"
CSHARP_LOGO = "img/dsfdsf"
IRRLICHT_LOGO = "img/adsdsa"
DARKGDK_LOGO = "img/dark"
R_LOGO = "img/rrrr"
UNITY_LOGO = "img/asdds"

portfolio_items = PortfolioItems.from_yaml(open("content/PortfolioItems.yaml"))
bibliography_entries = BibliographyEntries.from_yaml(open("content/Writing.yaml"))

@app.route('/portfolio-item/<string:game_title>.html')
def render_game(game_title :str) -> str:
	portfolio_item = portfolio_items[game_title]
	portfolio_item.title = game_title
	return render_template('portfolio.html', portfolio_item=portfolio_item)

@app.route('/')
def site_index() -> str:
	return render_template('index.html', portfolio_items=portfolio_items)

@app.route('/writing.html')
def render_writing() -> str:
	return render_template('writing.html', bibliography_entries=bibliography_entries)

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
