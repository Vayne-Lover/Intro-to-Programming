# -*- coding: utf-8 -*-

#Define class
class Movie():
    '''
    The class Movie provides a way to store movie related information.
    '''
    def __init__(self, title, poster, link):
        '''
        Initialize the class.
        :param title:
        :param poster:
        :param link:
        '''
        self.title = title
        self.poster_image_url = poster
        self.trailer_youtube_url = link

    def show_info(self):
        '''
        Show the info.
        :return:
        '''
        print self.title
        print self.poster_image_url
        print self.trailer_youtube_url