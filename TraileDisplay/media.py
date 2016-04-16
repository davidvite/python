import webbrowser

class Movie(object):
	"""This class provides a way to store movie related information """

	VALID_RATINGS = ["G", "PG" , "PG-13" , "R"]

	"""docstring for ClassName"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline  = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_yourtube_url)

class TVshow(object):
	"""docstring for TVshow"""
	def __init__(self, arg):
		super(TVshow, self).__init__()
		self.arg = arg
		