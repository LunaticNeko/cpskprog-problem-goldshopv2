"""

TEST CODE (DO NOT MODIFY -- REVERT IF MODIFIED!)
01219114 Computer Programming
Week 10, Long Program Assignment: Mother Tux's Gold Shop (V2)
(C) 2024 Chawanat Nakasan
Department of Computer Engineering, Kasetsart University
MIT License

"""

from gold import Gold
from random import randint
from random import random
import copy

def test_1a_init():
    g = Gold()
    assert g.markup == 0
    g.markup = 100
    assert g.markup == 100
    assert g.name == "Gold"
    assert g.gold_mass == 0
    assert g.total_mass == 0
    assert Gold("name").name == "name"
    assert Gold("").name == ""
    assert Gold("namename", 100).markup == 100

def test_1b_init_with_mass():
    g = Gold(gold=10, other=20)
    assert g.gold_mass == 10
    assert g.other_mass == 20
    assert g.total_mass == 30

def test_1c_set_mass():
    g = Gold()
    g.gold_mass += 20
    assert g.gold_mass == 20
    assert g.other_mass == 0
    assert g.total_mass == 20
    g.other_mass += 10
    assert g.gold_mass == 20
    assert g.other_mass == 10
    assert g.total_mass == 30

def gen_random_gold_pricing():
    g = Gold(gold=randint(100, 1000), other=randint(10, 500))
    g.markup = 100*randint(1,20)
    return g

def test_1d_price_simple():
    gold_price = 2000
    for i in range(10):
        g = gen_random_gold_pricing()
        assert g.price == g.gold_mass * gold_price + g.markup
        assert g.manual_price(include_markup = False) == g.gold_mass * gold_price

def test_1e_price_floating():
    for i in range(10):
        gold_price = randint(1000, 5000)
        g = gen_random_gold_pricing()
        assert g.manual_price(gold_price) == g.gold_mass * gold_price + g.markup
        assert g.manual_price(gold_price, include_markup = False) == g.gold_mass * gold_price

def test_1f_price_adjust():
    for i in range(10):
        gold_price = randint(1000, 5000)
        purity = round(random(), 2)
        g = gen_random_gold_pricing()
        test_price = g.manual_price(gold_price, include_markup = False, force_purity = purity)
        expected_price = int(purity * g.total_mass * gold_price)
        assert test_price == expected_price

def test_1g_purity():
    for i in range(10):
        g = gen_random_gold_pricing()
        test_purity = g.purity
        expected_purity = round(g.gold_mass / g.total_mass, 4)

def test_1h_eq1():
    for i in range(10):
        g = gen_random_gold_pricing()
        g2 = copy.copy(g)
        assert g2 == g

def test_1i_eq2():
    for i in range(10):
        g = gen_random_gold_pricing()
        g2 = copy.copy(g)
        g2.other_mass += 1
        assert g2 != g

def test_1j_repr():
    for i in range(10):
        g = gen_random_gold_pricing()
        assert repr(g) == f"Gold: {g.name}, {g.gold_mass} g / {g.total_mass} g"
