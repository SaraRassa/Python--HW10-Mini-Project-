import pytube
class Media:
    def __init__(self, code, name, director, IMDB, URL, duration, cast):
        self.code= code
        self.name= name
        self.director= director
        self.IMDB= IMDB
        self.URL= URL
        self.duration= duration
        self.cast= cast
    def show_info(self):
        print('Code:',self.code, '\nName:',self.name, '\nDirector:',self.director,'\nIMDB Score:',self.IMDB,
        '\nURL:',self.URL, '\nDuration:', self.duration, '\nCast:',self.cast)
    def download(self):
        first_stream=pytube.YouTube(self.URL).streams.first()
        first_stream.download(output_path='./', filename= 'Media.mp4')
        print("Download successfully!")

    
