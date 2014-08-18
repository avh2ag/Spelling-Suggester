"""
test_grid.py
Tests methods contained in Grid.py using pytest
"""
import pytest
from Grid import Grid

def test_init():
	g_1 = Grid()
	assert g_1.array == []
	g_2 = Grid(2,1)
	assert len(g_2.array) == 2
	assert len(g_2.array[1]) == 1
	assert g_2.array[0][0] == 0

def test_get_value():
	g_1 = Grid(3,3)
	assert g_1.get_value(2,2) == 0
	g_1.array[2][2] = 3
	assert g_1.get_value(2,2) == 3
	assert g_1.get_value(10, 10) == -1
	assert g_1.get_value(-5, -3) == -1

def test_set_value():
	g_1 = Grid(2,2)
	assert g_1.set_value(1,1,1)
	assert g_1.array[1][1] == 1
	assert not g_1.set_value(4, 4, 1)
	assert not g_1.set_value(2,2, 1)


def test_out_of_bounds():
	g_1 = Grid(3,3)
	assert g_1.out_of_bounds(5,5)
	assert g_1.out_of_bounds(-1,-1)
	assert not g_1.out_of_bounds(1,1)
	assert g_1.out_of_bounds(3,3)

def test_reset():
	grid = Grid(5,5)
	for i in range(4):
		for j in range(4):
			grid.set_value(i, j, 1)
	grid.reset()
	for i in range(4):
		for j in range(4):
			assert grid.get_value(i, j) == 0