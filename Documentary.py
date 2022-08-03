from Media import Media
class Documentary(Media):
    def __init__(self, code, name, director, IMDB, URL, duration, cast=None):
        Media.__init__(self,code, name, director, IMDB, URL, duration, cast)
        if cast is None:
            self.cast= '__Undefinde__'
        else:
            self.cast=cast
       
    def show_info(self):
        Media.show_info(self)