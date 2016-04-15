#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
A programming challenge proposed by Savant Group.
(http://www.savantgroup.com/)

Problem Name: Zipf's Song
Original Problem Source: https://labs.spotify.com/puzzles/

This was my 5th script. It took me a while to boil down all
of the logic into its barebones. 
The only nessessary steps are as follows:
    - gather all data
    - extract the number of songs on album and the number of songs to select
    - extract the song plays and their respective names
    - for all songs calculate their respective quality 
    which is, album index by number of plays
    - sort the container in decending order by quality
    - slice container by number of songs to select
    - print each name from container
    - get hired by spotify
    
Solution By: 
Marcus J. Shepherd (marcusshepdotcom@gmail.com)
"""
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