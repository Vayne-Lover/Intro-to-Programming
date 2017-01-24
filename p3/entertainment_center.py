# -*- coding: utf-8 -*-

#Import modules
import media
import fresh_tomatoes

#Initialize the instances
toy_story = media.Movie('Toy Story',
                        'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=vwyZH85NQC4')
avatar = media.Movie('Avatar',
                     'https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg' ,
                     'https://www.youtube.com/watch?v=-9ceBgWV8io')
hunger_games = media.Movie('Hunger Games',
                    'https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg',
                    'https://www.youtube.com/watch?v=PbA63a7H0bo')

#Generate the page
movies = [toy_story, avatar, hunger_games]
fresh_tomatoes.open_movies_page(movies)
