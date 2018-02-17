import markdown
from flask import Flask
from flask import render_template
from flask import Markup

app = Flask(__name__)

UE4_LOGO = "img/ue4-logo.png"
LIBGDX_LOGO = "img/llllll.png"
CSHARP_LOGO = "img/dsfdsf"
IRRLICHT_LOGO = "img/adsdsa"
DARKGDK_LOGO = "img/dark"
R_LOGO = "img/rrrr"

class PortfolioItem:
	def __init__(self):
		self.subtitle = ""
		self.logo = ""
		self.shorttext = ""
		self.content = ""
		self.images = []
		self.videos = []
		self.links = {}
		self.portfolio_grid_image_index = 0

	def get_image_filename(self, index: int) -> str:
		return "img/portfolio/" + self.images[index]

	def get_portfolio_grid_image(self) -> str:
		return self.get_image_filename(self.portfolio_grid_image_index)

portfolio_items = {}
portfolio_items["Kuma Engine"] = PortfolioItem()
portfolio_items["Kuma Engine"].subtitle = "Current Project" 
portfolio_items["Kuma Engine"].logo = "img/opengl-logo.png"
portfolio_items["Kuma Engine"].shorttext = "Visual Novel Creator in OpenGL."
portfolio_items["Kuma Engine"].content = "This is a project to combine both a compiler and a game engine in OpenGL. The aim is to allow people to create visual novels similar to the Danganronpa series (which involve both 2D and 3D environments and minigames making it more complex than a standard visual novel)."

portfolio_items["Doom WAD Importer"] = PortfolioItem()
portfolio_items["Doom WAD Importer"].logo = "img/ue4-logo.png"
portfolio_items["Doom WAD Importer"].shorttext = "Import Doom levels into Unreal Engine."
portfolio_items["Doom WAD Importer"].content = "Imports floors, walls and doors of Doom levels into Unreal Engine using ear clipping polygon triangulation."
portfolio_items["Doom WAD Importer"].images = [ "doomwadue.jpg" ]

portfolio_items["Facade"] = PortfolioItem()
portfolio_items["Facade"].logo = UE4_LOGO
portfolio_items["Facade"].shorttext = "A turn-based battle system in Unreal Engine."
portfolio_items["Facade"].content = "A prototype of a turn-based RPG similar to Persona, Pokemon or Final Fantasy. This project started off by me wondering how to implement a turn-based RPG/overworld state system in engines such as Unreal Engine or Unity (see blogposts <a href=\"http://alexdiru.blogspot.co.uk/2017/04/facade-turn-based-rpg-system-with.html\">here</a> and <a href=\"http://alexdiru.blogspot.co.uk/2017/04/unreal-engine-turn-based-rpg-design-2.html\">here</a> with my rambling)."
portfolio_items["Facade"].videos = [ "https://youtu.be/BiMoemDqiYs" ]

portfolio_items["99th Street"] = PortfolioItem()
portfolio_items["99th Street"].subtitle = "Released on itch.io"
portfolio_items["99th Street"].logo = UE4_LOGO
portfolio_items["99th Street"].shorttext = "Prototype of a skating engine"
portfolio_items["99th Street"].content = "A prototype of a skating engine, with grinding, wallrides and a lack of skating animations. Made in Unreal Engine 4. Grinding uses splines and the game is fairly fun to play with a controller."
portfolio_items["99th Street"].videos = [ "https://youtu.be/0_wXn7VB8S8" ]
portfolio_items["99th Street"].links = { "itch.io": "https://alexdiru.itch.io/99th-street" }

portfolio_items["Midnight Sun"] = PortfolioItem()
portfolio_items["Midnight Sun"].logo = UE4_LOGO
portfolio_items["Midnight Sun"].shorttext = "Stealth game with artificial intelligence."
portfolio_items["Midnight Sun"].content = """Stealth FPS game intended to be in the same style as the original Thief games. Written in UE4, I was quite proud of implementing noise arrows. The player can 
fire a noise arrow at any part of the map and it emits a noise, if the enemy is close enough then they will walk towards it. The extremely difficult part was integrating the noise
 sound with the navigation mesh (the predefined area of the both the AIs can walk on). Since most of the time the arrow will be shot at a wall or a roof of a building where the 
NPC cannot reach, thus the position the AI would need to investigate would need to be projected to the nearest point on its navigation mesh. It was way harder to implement than 
explain! And also researching OpenGL and the UE4 source code to work out the lighting algorithm UE uses to compute the amount of light hitting the player (because you need to be 
able to hide in the shadows!)"""
portfolio_items["Midnight Sun"].images = [ "amaya1.png", "amaya2.png", "amaya3.png" ]
portfolio_items["Midnight Sun"].videos = [ "https://youtu.be/H9KKS5-yW60" ]

portfolio_items["Red Leaf"] = PortfolioItem()
portfolio_items["Red Leaf"].subtitle = "Released on Google Play Store and itch.io"
portfolio_items["Red Leaf"].logo = LIBGDX_LOGO
portfolio_items["Red Leaf"].shorttext = "Stealth game with artificial intelligence."
portfolio_items["Red Leaf"].content = """After getting an Android phone I found myself getting addicted to the rhythm games similar to Guitar Hero where you tap the notes as they fall down the screen. 
While I was doing some coursework for University which involved creating games for Android phones, I had the idea to create one of those rhythm games for one of my favourite 
bands, LOST. Obviously the first hurdle would be to get permission to use the music.
(image)
So when I got this response, I was extremely happy!"""
portfolio_items["Red Leaf"].images = [ "lostresponse.png", "rl01.png", "rl02.png", "rl03.png" ]
portfolio_items["Red Leaf"].links = { "Google Play Store": "https://play.google.com/store/apps/details?id=com.alexdiru.redleaf", "itch.io": "https://alexdiru.itch.io/red-leaf" }
portfolio_items["Red Leaf"].portfolio_grid_image_index = 2

portfolio_items["Jet Set Reverse"] = PortfolioItem()
portfolio_items["Jet Set Reverse"].subtitle = "Open Source"
portfolio_items["Jet Set Reverse"].logo = CSHARP_LOGO
portfolio_items["Jet Set Reverse"].shorttext = "A texture modifier for a Dreamcast game."
portfolio_items["Jet Set Reverse"].content = """This was an application I developed to allow texture changes in the game Jet Set Radio HD. Jet Set Radio HD was a HD port of a 
Dreamcast game released in 1999, this means that all the files used by the HD re-release are Dreamcast files. As far as I know, I am the first person to develop support for 
texture changes on this game. It involved a lot of trial and error as the game uses its own custom file formats lacking a specification (or even any info about them), also the use
 of Dreamcast textures is annoying as many tools that still remain on the internet (being that the Dreamcast existed pre-millenium).

While developing the program, I made lots and lots of blog posts about hacking into the files:

<a href="http://alexdiru.blogspot.co.uk/2013/12/reverse-engineering-jet-set-radio-hd.html">Blog 1</a><br/>
<a href="http://alexdiru.blogspot.co.uk/2013/12/reverse-engineering-jet-set-radio-hd_28.html">Blog 2</a><br/>
<a href="http://alexdiru.blogspot.co.uk/2013/12/reverse-engineering-jet-set-radio-part-3.html">Blog 3</a><br/>
<a href="http://alexdiru.blogspot.co.uk/2013/12/reverse-engineering-jet-set-radio-part-4.html">Blog 4</a><br/>
<a href="http://alexdiru.blogspot.co.uk/2013/12/creating-custom-texture-for-gum-in-jet.html">Software Release 1</a><br/>
<a href="http://alexdiru.blogspot.co.uk/2013/12/reverse-engineering-jet-set-radio-hd_30.html">Blog 5</a><br/>
<a href="http://alexdiru.blogspot.co.uk/2013/12/reverse-engineering-jet-set-radio-hd_6611.html">Blog 6</a><br/>
<a href="http://alexdiru.blogspot.co.uk/2013/12/jet-set-reverse-v01131230-gum-beat-mew.html">Software Release 2</a><br/>
<a href="http://alexdiru.blogspot.co.uk/2014/01/reverse-engineering-jet-set-radio-hd.html">Blog 7</a><br/>
<a href="http://alexdiru.blogspot.co.uk/2014/01/reverse-engineering-jet-set-radio-hd_1.html">Blog 8</a><br/>
<a href="http://alexdiru.blogspot.co.uk/2014/01/reverse-engineering-jet-set-radio-hd_6255.html">Blog 9</a><br/>
<a href="http://alexdiru.blogspot.co.uk/2014/02/jet-set-reverse-v01140211-release.html">Software Release 3</a><br/><br/>"""
portfolio_items["Jet Set Reverse"].images = [ "jsr01.png", "jsr02.png", "jsr03.jpg" ]
portfolio_items["Jet Set Reverse"].links = { "Download" : "https://www.dropbox.com/s/vtlswmxgzk7dv07/JetSetReverse.rar", "Source Code" : "https://github.com/AlexDiru/jet-set-reverse" }

portfolio_items["Electric Rain"] = PortfolioItem()
portfolio_items["Electric Rain"].shorttext = "A 2D RPG with a battle system."
portfolio_items["Electric Rain"].logo = LIBGDX_LOGO
portfolio_items["Electric Rain"].content = """Electric Rain was an RPG which I attempted to create using the Slick2D engine from Java. It has a turn based battle system in the 
vain of the Final Fantasy series, and supports types of attacks/spells such as ones which can have a single target and others which can have an area of effect and hit multiple 
targets. Attacks/spells don't neccessarily need to be targetted at enemies, healing spells are in place which can heal your own team. All of the data the game uses are stored in 
XML files and thus can be easily parsed and amended. The main game is reminescent of Pokemon - a top down view of the world with wild encounters found in grass."""
portfolio_items["Electric Rain"].images = [ "er1.png", "er2.png" ]
portfolio_items["Electric Rain"].links = { "Source Code" : "https://github.com/AlexDiru/electric-rain" }

portfolio_items["Neuron Warfare"] = PortfolioItem()
portfolio_items["Neuron Warfare"].shorttext = "Strategy shooter in C++ using Irrlicht."
portfolio_items["Neuron Warfare"].logo = IRRLICHT_LOGO
portfolio_items["Neuron Warfare"].content = """Neuron Warfare was an open source game creating in C++ using Irrlicht. Originally I intended the project just to be demo to see if I
 could implement the A* algorithm. However, it has quickly increased beyond that. It's beginning to form into a turn based strategy game where you have a party of players who move
 across a map and must kill the ememies before they kill you."""
portfolio_items["Neuron Warfare"].images = [ "nw01.png", "nw02.png" ]
portfolio_items["Neuron Warfare"].links = { "Source Code" : "https://github.com/AlexDiru/NeuronWarfare" }

portfolio_items["Barricade"] = PortfolioItem()
portfolio_items["Barricade"].shorttext = "A 2.5D puzzle game using DarkGDK."
portfolio_items["Barricade"].logo = DARKGDK_LOGO
portfolio_items["Barricade"].content = """Barricade was a simple puzzle game I made for a competition in 2009. The prize for the winner was that the game's graphics were remade 
(by David Gervais), and as a awful artist myself that would mean I could have a decent looking game if I won. I had drafted up some not so great looking prototypes. The gameplay 
was simplistic yet it worked - it involved navigated throughout a map to reach the end, however things were in your way such as boxes, locked 'doors' and spike pits. This game won
 the competition...

...However, my game was the only entrant so I had to win! I felt bad for the organiser as lots of people said they would join in but they never did - though not a problem with me 
as I would finally have a finished game with decent graphics. To make the deadline, even though I knew there were no other entrants I still wanted to finish the game so I pulled a
 few all-nighters to get it done."""
portfolio_items["Barricade"].images = [ "barricadeoriginal.jpg", "barricadenew.jpg"]
portfolio_items["Barricade"].links = { "Download" : "http://www.mediafire.com/?fq4a1n22n67329a" }
portfolio_items["Barricade"].portfolio_grid_image_index = 1

portfolio_items["Jet Set Radio Air"] = PortfolioItem()
portfolio_items["Jet Set Radio Air"].shorttext = "A skating game using DarkGDK"
portfolio_items["Jet Set Radio Air"].logo = DARKGDK_LOGO
portfolio_items["Jet Set Radio Air"].content = """Unfortunately this is one of the many projects I have lost the source code. Though 15 year old me would have probably written indecipherable code. The reason I stopped this project was mainly due to the spaghetti code this had become. Whenever I ran
the game I would get an exception which I just couldn't find the fix to. I'm not sure if I knew about debugging then - I must have done, because if not bug fixing would have been horrible. But I didn't know what version control was so there was no way I could revert to 
a previous build.

Videos:

<a href="https://www.youtube.com/watch?v=WHSH2HgXZ9M">Video 1</a><br/>
<a href="https://www.youtube.com/watch?v=UZsbvNxw9WE">Video 2</a><br/>
<a href="https://www.youtube.com/watch?v=GQjLLsFdEOo">Video 3</a><br/>
<a href="https://www.youtube.com/watch?v=Pn4Idl29wTw">Video 4</a><br/>
<a href="https://www.youtube.com/watch?v=ij_5JmTDsiQ">Video 5</a><br/>
<a href="https://www.youtube.com/watch?v=bPNH2h1xFn0">Video 6</a><br/>
<a href="https://www.youtube.com/watch?v=GtEIAT9naVU">Video 7</a><br/>
<a href="https://www.youtube.com/watch?v=DYUmfT9PTDs">Video 8</a><br/>
<a href="https://www.youtube.com/watch?v=YEboSNYr0ik">Video 9</a><br/>
<a href="https://www.youtube.com/watch?v=CQMN0Igs064">Video 10</a><br/>
<a href="https://www.youtube.com/watch?v=cV73EkxdxAw">Video 11</a><br/>
<a href="https://www.youtube.com/watch?v=jPoP3navVGE">Video 12</a><br/>
<a href="https://www.youtube.com/watch?v=r5zLDYsyd7s">Video 13</a><br/>
<a href="https://www.youtube.com/watch?v=eGlSQOn0OUA">Video 14</a><br/>
<a href="https://www.youtube.com/watch?v=saw9PTOuMGc">Video 15</a><br/>
<a href="https://www.youtube.com/watch?v=EEjPZ84-lIQ">Video 16</a><br/>
<a href="https://www.youtube.com/watch?v=mCfzv5qA-qo">Video 17</a><br/>
<a href="https://www.youtube.com/watch?v=lDlr_afvJ7U">Video 18</a><br/>
<a href="https://www.youtube.com/watch?v=dQAzhXF73K0">Video 19</a><br/>
<a href="https://www.youtube.com/watch?v=2UKKCiEc9Ag">Video 20</a><br/>
<a href="https://www.youtube.com/watch?v=O56oEPwL5aA">Video 21</a><br/>
<a href="https://www.youtube.com/watch?v=rei89rxCmZM">Video 22</a><br/>
<a href="https://www.youtube.com/watch?v=vdif7S65IXs">Video 23</a><br/>
<a href="https://www.youtube.com/watch?v=b1Gy0ItT8eU">Video 24</a><br/>
"""

portfolio_items["rsurfer"] = PortfolioItem()
portfolio_items["rsurfer"].shorttext = "An R package for MRI data"
portfolio_items["rsurfer"].logo = R_LOGO
portfolio_items["rsurfer"].links = { "Source Code" : "https://github.com/AlexDiru/rsurfer" }

#@app.route('/game/<string:game_title>')
#def render_game(game_title :str) -> str:
#	game_content = game[game_title]
#	print(game_content)
#	return render_template('game.html', game_content=game_content)

@app.route('/bsindex')
def bsindex() -> str:
	return render_template('bsindex.html', portfolio_items=portfolio_items)

@app.route('/')
def site_index() -> str:
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