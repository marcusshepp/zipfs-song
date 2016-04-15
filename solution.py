#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
A programming challenge proposed by Savant Group.
(http://www.savantgroup.com/)

Problem Name: Zipf's Song
Original Problem Source: https://labs.spotify.com/puzzles/

THIS SOLUTION IS INVALID
"""
__author__ = "Marcus J. Shepherd"
__email__ = "marcusshepdotcom@gmail.com"
__date__ = "April 15, 2016"

import sys
import collections

def test_algo():
    def test_w_file(file_path, desired_result):
        with open(file_path) as f:
            albumsize, selectsize, tracks = handle_input(f)
            results = algo(tracks, albumsize, selectsize)
            print(algo(tracks, albumsize, selectsize))
            assert algo(tracks, albumsize, selectsize) == desired_result
    test_w_file(
        file_path="test_input/input1.txt", 
        desired_result="four\ntwo")
    test_w_file(
        file_path="test_input/input2.txt", 
        desired_result="19_2000\nclint_eastwood\ntomorrow_comes_today")
    
def to_namedtuple(tracks):
    temp_tracks = list()
    for plays, name in tracks:
        track = collections.namedtuple("Track", "name, plays, quality")
        track.name = name
        track.plays = plays
        temp_tracks.append(track)
    return temp_tracks
    
def algo(tracks, albumsize, selectsize):
    for i, v in enumerate(tracks, start=1):
        v.quality = v.plays * i
    new_tracks = sorted(tracks, key=lambda track: track.quality, reverse=True)[:selectsize]
    return "\n".join([track.name for track in new_tracks])

def handle_input(in_object):
    input_data = [line.split() for line in in_object]
    albumsize, selectsize = map(int, input_data.pop(0))
    tracks = to_namedtuple(input_data)
    return albumsize, selectsize, tracks
    
def main(DEBUG):
    if DEBUG:
        test_algo()
    else:
        albumsize, selectsize, tracks = handle_input(sys.stdin)
        results = algo(tracks, albumsize, selectsize)
        for name in results:
            print(name)

if __name__ == '__main__':
    if sys.stdin.isatty():
        main(DEBUG=1)
