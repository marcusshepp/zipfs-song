"""
A programming challenge proposed by Savant Group.
(http://www.savantgroup.com/)

Problem Name: Zipf's Song
Original Problem Source: https://labs.spotify.com/puzzles/

Solution By: 
Marcus J. Shepherd (marcusshepdotcom@gmail.com)
"""
from collections import namedtuple

def albumsize_selectsize():
    albumsize, selectsize = raw_input().split(" ")
    return albumsize, selectsize

def plays_name():
    plays, name = raw_input().split(" ")
    return int(plays), name
    
def to_namedtuple(tracks):
    temp_tracks = list()
    for plays, name in tracks:
        track = namedtuple("Track", ["name", "plays", "quality"])
        track.name = name
        track.plays = plays
        temp_tracks.append(track)
    return temp_tracks
    
def algo(tracks, albumsize, selectsize):
    """
    in: tracks = (plays, name) with len = albumsize
    """
    new_tracks = []
    for index, track in enumerate(tracks, 1):
        track.quality = track.plays * index
        if len(new_tracks) < selectsize:
            new_tracks.append(track)
        else:
            new_tracks.append(track)
            new_tracks = sorted(
                new_tracks, 
                key=lambda track: track.quality, 
                reverse=True)[:selectsize]
    return [track.name for track in new_tracks]

def main():
    albumsize, selectsize = albumsize_selectsize()
    tracks = to_namedtuple([plays_name() for _ in xrange(int(albumsize))])
    for i in algo(tracks, int(albumsize), int(selectsize)):
        print i

if __name__ == '__main__':
    main()
