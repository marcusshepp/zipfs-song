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
import collections
import itertools

def test_algo():
    def test_w_file(file_path, desired_result):
        with open(file_path) as f:
            a_s, s_s = map(int, f.readline().split(" "))
            original_track_tuples = (
                plays_name(f) for _ in xrange(a_s))
            tracks = to_namedtuple(original_track_tuples)
            assert algo(tracks, original_track_tuples, a_s, s_s) == desired_result
    test_w_file(
        file_path="test_input/input1.txt", 
        desired_result=["four", "two"])
    test_w_file(
        file_path="test_input/input2.txt", 
        desired_result=["19_2000", "clint_eastwood", "tomorrow_comes_today"])
    
def albumsize_selectsize():
    albumsize, selectsize = map(int, sys.stdin.readline().split(" "))
    algo_info = (albumsize, selectsize)
    return algo_info

def plays_name(input_):
    plays, name = input_.readline().split(" ")
    track = (int(plays), name)
    return track
    
def strip_newline(s):
    return s.replace("\n", "")
    
def align(l1, l2):
    """ 
    Used to align the resulting list with the original list.
    Called only when in need of a track quality tie breaker.
    """
    new_l2 = [y for x in l1 for y in l2 if x == y]
    return new_l2
    
def to_namedtuple(tracks):
    temp_tracks = list()
    for plays, name in tracks:
        track = collections.namedtuple("Track", ["name", "plays", "quality"])
        track.name = strip_newline(name)
        track.plays = plays
        temp_tracks.append(track)
    return temp_tracks
    
def algo(tracks, original_track_tuples, albumsize, selectsize):
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
    assert len(new_tracks) == selectsize
    duplicates = list()
    for track1, track2 in itertools.combinations(new_tracks, 2):
        if track1.quality == track2.quality:
            duplicates.append(track1)
            duplicates.append(track2)
    if duplicates:
        aligned = align(
            [t.name for t in duplicates], 
            [tup[0] for tup in original_track_tuples])
        assert len(aligned) == selectsize
        return aligned
    return "\n".join([track.name for track in new_tracks])

def main(DEBUG):
    if DEBUG:
        test_algo()
    else:
        albumsize, selectsize = albumsize_selectsize()
        original_track_tuples = (
            plays_name(sys.stdin) for _ in xrange(albumsize))
        tracks = to_namedtuple(original_track_tuples)
        results = algo(tracks, original_track_tuples, albumsize, selectsize)
        for name in results:
            sys.stdout.writelines(name)

if __name__ == '__main__':
    if sys.stdin.isatty():
        main(DEBUG=False)
