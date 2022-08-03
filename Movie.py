from Media import Media
class Movie(Media):
    def __init__(self, code, name, director, IMDB, URL, duration, cast, genre):
        Media.__init__(self,code, name, director, IMDB, URL, duration, cast)
        self.genre= genre
    
    def show_info(self):
        Media.show_info(self)
        print('Genre: ',self.genre)
