import markdown
from flask import Flask
from flask import render_template
from flask import Markup

app = Flask(__name__)

game = {}
game["Kuma Engine"] = { "title": "Kuma Engine", "subtitle": "Current Project", "logo": "img/opengl-logo.png", "content": "This is a project to combine both a compiler and a game engine in OpenGL. The aim is to allow people to create visual novels similar to the Danganronpa series (which involve both 2D and 3D environments and minigames making it more complex than a standard visual novel)." }

@app.route('/game/<string:game_title>')
def render_game(game_title):
	game_content = game[game_title]
	print(game_content)
	return render_template('game.html', game_content=game_content)

@app.route('/')
def site_index():
	content = """
Chapter
=======

Section
-------

* Item 1
* Item 2
"""
	content = Markup(markdown.markdown(content))
	return render_template('index.html', **locals())

app.run()