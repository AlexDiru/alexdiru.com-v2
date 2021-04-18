from flask_frozen import Freezer
from flask_main import app, portfolio_items

app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

@freezer.register_generator
def render_game():
	for key, value in portfolio_items.items():
		yield { "game_title" : key }

if __name__ == '__main__':
    freezer.freeze()