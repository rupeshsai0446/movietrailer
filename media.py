#!/usr/bin/env python
import webbrowser  # webbrowser module is imported.


class Movie():
    '''
     here class name is taken as a movie and some arguments are taken.
     argument1:movie_title defines the movie name.
     argument2:poster_image defines the  image of that movie.
     argument3:traier_youtube gives the youtube url of that moivie trailer.
    '''
    def __init__(self, movie_title, poster_image, trailer_youtube):
        # initializes the space for storing the arguments.
                self.title = movie_title
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube


def show_trailer(self):  # opens the movie trailer in a updated modern browser.
            webbrowser.open(self.trailer_youtube_url)
