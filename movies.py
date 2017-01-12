class Movies(object):
    def __init__(self, **kwargs):
        short_plot = kwargs.get('Plot')[0:170]
        self.title = kwargs.get('Title')
        self.poster_link = kwargs.get('Poster')
        self.rated = kwargs.get('Rated')
        self.type = kwargs.get('Type')
        self.awards = kwargs.get('Awards')
        self.year = kwargs.get('Year')
        self.released = kwargs.get('Released')
        self.genre = kwargs.get('Genre')
        self.runtime = kwargs.get('Runtime')
        self.actors = kwargs.get('Actors')
        self.director = kwargs.get('Director')
        self.writer = kwargs.get('Writer')
        self.link_id = 'http://www.imdb.com/title/' + kwargs.get('imdbID')
        self.plot = short_plot
        # self.plot = kwargs.get('Plot')
        self.imdb_rating = kwargs.get('imdbRating')
        self.imdb_votes = kwargs.get('imdbVotes')
        self.language = kwargs.get('Language')
        self.trailer = kwargs.get('trailer')

    def __str__(self):
        return str(self.title)

    def get_imdb_link(self):
        pass

    def get_youtube_trailer_link(self):
        pass
