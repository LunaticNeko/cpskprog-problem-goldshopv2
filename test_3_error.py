"""

TEST CODE (DO NOT MODIFY -- REVERT IF MODIFIED!)
01219114 Computer Programming
Week 10, Long Program Assignment: Mother Tux's Gold Shop (V2)
(C) 2024 Chawanat Nakasan
Department of Computer Engineering, Kasetsart University
MIT License

"""

from gold import Gold
from goldset import GoldSet
from random import randint
from random import random
import copy
import pytest

def test_2a_name():
    with pytest.raises(TypeError):
        g = Gold(name=1)
    with pytest.raises(TypeError):
        g = Gold(name=None)
    with pytest.raises(TypeError):
        g = Gold(name=[1,2])

def test_2b_gold_mass():
    g = Gold()
    with pytest.raises(TypeError):
        g.gold_mass = 1.1
    with pytest.raises(TypeError):
        g.gold_mass = '1'
    with pytest.raises(ValueError):
        g.gold_mass = -1

def test_2c_other_mass():
    g = Gold()
    with pytest.raises(TypeError):
        g.other_mass = 1.1
    with pytest.raises(TypeError):
        g.other_mass = '1'
    with pytest.raises(ValueError):
        g.other_mass = -1

def test_2d_markup():
    g = Gold()
    with pytest.raises(TypeError):
        g.markup = 1.1
    with pytest.raises(TypeError):
        g.markup = '1'
    with pytest.raises(ValueError):
        g.markup = -1

def test_2e_set_name():
    with pytest.raises(TypeError):
        g = GoldSet(name=1)
    with pytest.raises(TypeError):
        g = GoldSet(name=None)
    with pytest.raises(TypeError):
        g = GoldSet(name=[1,2])

def test_2f_set_markup():
    g = GoldSet()
    with pytest.raises(TypeError):
        g.markup = 1.1
    with pytest.raises(TypeError):
        g.markup = '1'
    with pytest.raises(ValueError):
        g.markup = -1

def test_2g_set_add():
    g = GoldSet()
    with pytest.raises(TypeError):
        g.add(1)
        g.add('a')
        g.add(None)

