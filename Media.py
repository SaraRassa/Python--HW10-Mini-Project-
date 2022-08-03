from Actors import Actor
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

    def show_cast(self):
        actor= self.cast.split('&')
        for a in actor:
            Actor(a).actor_list()
        
    def download(self):
        link= self.URL
        first_stream=pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./', filename= 'Media.mp4')
        print("Download successfully!")

    
