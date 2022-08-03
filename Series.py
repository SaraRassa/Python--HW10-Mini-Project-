from Media import Media
class Series(Media):
    def __init__(self, code, name, director, IMDB, URL, duration, cast, seasons, episods):
        Media.__init__(self,code, name, director, IMDB, URL, duration, cast)
        self.seasons= seasons
        self.episods= episods
    
    def show_info(self):
        Media.show_info(self)
        print('Seasons:', self.seasons, 'Episods:', self.episods)
