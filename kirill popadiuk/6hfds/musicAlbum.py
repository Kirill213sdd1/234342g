# import random
#
# class MusicAlbum:
#
#     def __init__(self, title, artist, relais_year, genere, tracklist):
#         self.title = title
#         self.artist = artist
#         self.relais_year = relais_year
#         self.genere = genere
#         self.tracklist = tracklist
#
#     def info(self):
#         print('Название', self.title)
#         print('Исполнитель', self.artist)
#         print('Год', self.relais_year)
#         print('Жанр', self.genere)
#         print('Треки', self.tracklist)
#
#     def play_random_track(self):
#         return random.choice(self.tracklist)
#
# ma = MusicAlbum('T.A.T.U', 'All The Things She Said', '2002', 'pop misic', ['All the Things She Said', 'Running through my head'])
# ma.info()
# print('Сейчас играет:', ma.play_random_track())