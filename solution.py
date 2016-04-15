#!/usr/bin/python
"""
A programming challenge proposed by Savant Group.
(http://www.savantgroup.com/)

Problem Name: Zipf's Song
Original Problem Source: https://labs.spotify.com/puzzles/

Solution By: 
Marcus J. Shepherd (marcusshepdotcom@gmail.com)
"""
import sys
from collections import namedtuple

def test_algo():
    def test_w_file(file_path, desired_result):
        with open(file_path) as f:
            a_s, s_s = map(int, f.readline().split(" "))
            album = list()
            for _ in xrange(a_s):
                plays, name = plays_name_from_file(f)
                album.append((int(plays), strip_newline(name)))
            assert algo(to_namedtuple(album), a_s, s_s) == desired_result
    test_w_file(
        file_path="test_input/input1.txt", 
        desired_result=["four", "two"])
    test_w_file(
        file_path="test_input/input2.txt", 
        desired_result=["19_2000", "clint_eastwood", "tomorrow_comes_today"])
    
def albumsize_selectsize():
    albumsize, selectsize = map(int, sys.stdin.readline().split(" "))
    return albumsize, selectsize

def plays_name():
    plays, name = sys.stdin.readline().split(" ")
    return int(plays), name
    
def plays_name_from_file(f):
    plays, name = f.readline().split(" ")
    return strip_newline(plays), strip_newline(name)

def strip_newline(s):
    return s.replace("\n", "")
    
def to_namedtuple(tracks):
    temp_tracks = list()
    for plays, name in tracks:
        track = namedtuple("Track", ["name", "plays", "quality"])
        track.name = strip_newline(name)
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

def main(DEBUG):
    if DEBUG:
        return test_algo()
    else:
        albumsize, selectsize = albumsize_selectsize()
        tracks = to_namedtuple([plays_name() for _ in xrange(albumsize)])
        for i in algo(tracks, albumsize, selectsize):
            print i

if __name__ == '__main__':
    if sys.stdin.isatty():
        main(DEBUG=False)
