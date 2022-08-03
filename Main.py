import pytube
from Media import Media
from Movie import Movie
from Series import Series
from Documentary import Documentary
from Clip import Clip
class Main:
    def __init__(self):
        m=open('Mini Project\Database.txt','r')
        rows= m.read().split('\n')
        self.media=[]
        for j in range(len(rows)):
            self.info= rows[j].split(',')
            i= int(self.info[0])
            if i >= 1000 and i < 2000:
                self.media.append(Movie(self.info[0], self.info[1], self.info[2], self.info[3], self.info[4],self.info[5], self.info[6],self.info[7]))
            elif i >= 2000 and i < 3000:
                self.media.append(Series(self.info[0],self.info[1],self.info[2],self.info[3],
                                         self.info[4],self.info[5],self.info[6],self.info[7],self.info[8]))
            elif i >= 3000 and i < 4000:
                self.media.append(Documentary(self.info[0],self.info[1],self.info[2],self.info[3],
                                              self.info[4],self.info[5],self.info[6]))
            elif i >= 4000 and i < 5000:
                self.media.append(Clip(self.info[0], self.info[1], None, None, self.info[2], self.info[3], None))

            self.show_menu()
        m.close()

    def show_list(self):
        for M in self.media:
            M.show_info()


    def show_menu(self):
        print('1_ Add Media')
        print('2_ Edit Media')
        print('3_ Delete Media')
        print('4_ Search')
        print('5- Show list')
        print('6_ Show Cast')
        print('7_ Download')
        print('8_ Save & Exit') 
        self.choice= int(input('Select an option: '))
        if self.choice==1:
            self.add_media()
        elif self.choice==2:
            self.edit_media()
        elif self.choice==3:
            self.delet_media()
        elif self.choice==4:
            self.search_media()
        elif self.choice==5:
            self.show_list()
        elif self.choice==6:
            self.show_actors()
        elif self.choice==7:
            self.download_media()
        elif self.choice ==8:
            self.save_and_exit()
            exit()

    def show_actors(self):
        a= input('Enter the name of the movie you want to show the cast for: ')
        for film in self.media:
            if a == film.name:
                film.show_cast()

    def download_media(self):
        d= input('Enter the name of the movie you want to download: ')
        for film in self.media:
            if d == film.name:
                film.download()

    def add_media(self):
        self.add=[]
        self.code= int(input("Enter a 4 digit number: "))
        self.name= input('Enter name: ')
        self.director= input('Enter director: ')
        self.score= float(input('Enter IMDB score: '))
        self.URL= input('Enter link: ')
        self.duration= input('Enter duration: ')
        self.cast= input('Enter actor(s): ')
        self.add.append({self.code,self.name,self.director,self.score,self.URL,self.duration,self.cast})
        
        if self.code >= 1000 and self.code < 2000:
            self.genre = input('Enter movie genre: ')
            self.add.append({self.genre})
        elif self.code >= 2000 and self.code < 3000:
            self.seasons= int(input('Enter number of series seasons:' ))
            self.episods= int(input('Enter number of series episods: '))
            self.add.append({self.seasons, self.episods})
        elif self.code >= 4000 and self.code < 5000:
            del self.director
            del self.score
            del self.cast
            self.add.remove({self.director,self.score,self.cast})
            self.show_menu()
    
    def edit_media(self):
        code=int(input("Please enter the media code you want to edit: "))
        for c in self.media:
            if code == int(c.code):
                while True:
                    print('1_ Name')
                    print('2_ Director')
                    print('3_ Score')
                    print('4_ Link')
                    print('5_Duration')
                    print('6_ Cast')
                    print('7_ End editing')
                    self.editing=int(input("Please choose an option: "))
                    if self.editing==1:
                        c.name=input("Please enter new name: ")
                    elif self.editing==2:
                        c.director=input('Please enter new director: ')
                    elif self.editing==3:
                        c.IMDB=float(input('Please enter new score: '))
                    elif self.editing==4:
                        c.URL=input('Please enter new link: ')
                    elif self.editing==5:
                        c.duration=input('Please enter new duration: ')
                    elif self.editing==6:
                        c.cats=input('Please enter new cast: ')
                    elif self.editing==7:
                        self.show_list()
                        break
            else:
                print("The code is not valid!")

    def delet_media(self):
        code=int(input("Please enter the media code you want to delet: "))
        for d in self.media:
            if code == int(d.code):
                self.media.remove(d)
                print(d.name, 'Deleted!')
            else:
                print("The code is not valid!")

    def search_media(self):
        min= int(input('Enter desired minimum duration: '))
        max= int(input('Enter desired maximum duration: '))
        for film in self.media:
            if min < int(film.duration) < max:
                film.show_info()
    def save_and_exit(self):
        m=open('Mini Project\Database.txt','a')
        for med in self.media:
            if int(med.code)>= 1000 and int(med.code)< 2000:
                m.write(med.code+','+med.name+','+med.director+','+med.IMDB+','+med.URL+','+med.duration+','+
                        med.cast+','+med.genre+',')
            elif int(med.code)>= 2000 and int(med.code)< 3000:
                m.write(med.code+','+med.name+','+med.director+','+med.IMDB+','+med.URL+','+med.duration+','+
                        med.cast+','+med.seasons+','+med.episods)
            elif int(med.code)>= 3000 and int(med.code)< 4000:
                m.write(med.code+','+med.name+','+med.director+','+med.IMDB+','+med.URL+','+med.duration+','+
                        med.cast)
            elif int(med.code)>= 3000 and int(med.code)< 4000:
                m.write(med.code+','+med.name+','+med.URL+','+med.duration)
        print("Data saved successfully!")
        m.close()

Main()