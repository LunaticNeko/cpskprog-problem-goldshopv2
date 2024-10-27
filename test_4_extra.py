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

def test_3a_add_list():
    g1 = Gold("Test 1", gold=10, other=20)
    g2 = Gold("Test 2", gold=10, other=20)
    g3 = Gold("Test 3", gold=20, other=40)
    g4 = Gold("A", gold=0, other=1)
    g5 = Gold("A", gold=1, other=1)
    gold_list = [g1, g2, g3, g4, g5]
    gs = GoldSet()
    gs.add(gold_list)
    gt = GoldSet()
    for g in gold_list:
        gt.add(g)
    assert repr(gs) == repr(gt)

