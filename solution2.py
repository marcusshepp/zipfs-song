"""
Let's try this again.
ACCEPTED!!!!!!!!!!!
AYYYYYY

THIS SOLUTION WAS ACCEPTED
"""
__author__ = "Marcus J. Shepherd"
__email__ = "marcusshepdotcom@gmail.com"
__date__ = "April 15, 2016"
import sys

def main():
    incoming_data = list()
    while True:
        try:
            incoming_data.append(raw_input())
        except EOFError:
            break
    n_songs, n_select = map(int, incoming_data.pop(0).split())
    zipfed_songs = list()
    for index, track in enumerate(incoming_data, start=1):
        quality = int(track.split()[0]) * index
        zipfed_songs.append((quality, track.split()[1]))
    zipfed_songs = sorted(zipfed_songs, key=lambda tup: tup[0], reverse=True)[:n_select]
    for  _, name in zipfed_songs:
        print name
    
if __name__ == "__main__":
    main()