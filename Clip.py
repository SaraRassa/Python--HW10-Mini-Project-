from Media import Media
class Clip(Media):
    def __init__(self, code, name, director, IMDB=None, URL=None, duration=None, cast=None):
        Media.__init__(self, code, name, director, IMDB, URL, duration, cast)
    
    def show_info(self):
        Media.show_info(self)
