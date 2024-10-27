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

def test_2a_init():
    g = GoldSet()
    assert g.markup == 0
    g.markup = 100
    assert g.markup == 100
    assert g.name == "Gold Set"
    assert g.gold_mass == 0
    assert g.total_mass == 0
    assert Gold("name").name == "name"
    assert Gold("").name == ""
    assert Gold("namename", 100).markup == 100

def test_2b_add():
    g1 = Gold(gold=8, other=2)
    g2 = Gold(gold=16, other=4)
    gs = GoldSet()
    gs.add(g1)
    gs.add(g2)
    
def test_2c_pop():
    g1 = Gold(gold=8, other=2)
    g2 = Gold(gold=16, other=4)
    gs = GoldSet()
    gs.add(g1)
    gs.add(g2)
    assert gs.pop() == g2
    assert gs.pop() == g1

def test_2d_copy():
    g1 = Gold("A", gold=10, other=10)
    gs = GoldSet()
    gs.add(g1)
    g1.gold_mass = 20
    g_added = gs.pop()
    assert g_added.gold_mass == 10

def test_2e_deepcopy():
    g1 = Gold(gold=8, other=2)
    g2 = Gold(gold=16, other=4)
    gs = GoldSet(name='s')
    gs.add(g1)
    gt = GoldSet(name='u')
    gt.add(g2)
    gu = GoldSet(name='s')
    gu.add(g1)
    gu.add(g2)
    gv = gs + gt
    assert gv.pop() == gu.pop()
    assert gv.pop() == gu.pop()
