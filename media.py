import webbrowser

class  Movie(object):
	"""docstring for  """
	def __init__(self, movie, storyline, poster, trailer_url):
		self.title = movie
		self.storyline = storyline
		self.poster_image_url = poster
		self.trailer_youtube_url = trailer_url
		
	def show_trailer(self):
		webbrowser.open(self.trailer_url)