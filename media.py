import webbrowser

class Movie():
	"""
	Movie is a class that stores and plays are Movies
	"""

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		"""
		Initializes our Movies
		"""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		"""
		Plays the trailer for our movies
		"""
		webbrowser.open(self.trailer_youtube_url)
