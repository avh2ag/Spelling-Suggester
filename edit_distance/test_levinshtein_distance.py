"""
test_levinshtein_distance.py 
Tests the methods contained in levinshtein_distance.py using pytest
"""
import pytest
from levinshtein_distance import *
def test_edit_distance():
	s1 = ""
	s2 = ""
	assert edit_distance(s1, s2) == 0
	s1 = "a"
	s2 = ""
	assert edit_distance(s1, s2) == 1
	assert edit_distance(s2, s1) == 1
	s1 = "a"
	s2 = "a"
	assert edit_distance(s1, s2) == 0
	s1 = "kitten"
	s2 = "sitting"
	assert edit_distance(s1, s2) == 3
	s2 = "kitte"
	assert edit_distance(s1, s2) == 1