"""

01219114 Computer Programming
Week 10, Long Program Assignment: Mother Tux's Gold Shop (V2)
(C) 2024 Chawanat Nakasan
Department of Computer Engineering, Kasetsart University
MIT License

DISCLAIMER: This task does NOT suggest any form of investment or financial
advice. NOR it does imply that the author understands any form of gold or
commodity trade. Treat this problem as a completely fantasy scenario.

"""

import copy
from gold import Gold

class GoldSet:
    """
    Represents a set of multiple Gold items.
    This is where Mother Tux really gets rich by putting things into bundles
    and stuff, so don't mess up on this one!

    Attributes (ALL MUST BE PRIVATE):
    name -- the name of the gold set. Default is "Gold Set" <<GET, SET>>
    gold_mass -- the total gold mass of all pieces combined <<GET>>
                  Initialize as 0.
    total_mass -- the total, uh, total mass of all pieces combined <<GET>>
                  Initialize as 0.
    markup -- how much to ADD to the value when attempting to sell this
                  set of multiple gold pieces in THB. Default 0. <<GET, SET>>
    purity -- work similarly to the one for the Gold class, but for all the
              pieces combined. ATTEMPTING TO ACCESS PURITY WITH
              total_mass == 0 MUST RAISE ZeroDivisionError WITHOUT MESSAGE
              <<GET>>

    HINT: You MUST implement something to hold all the gold pieces, and it
    obviously MUST be private!
    """

    def __init__(self, name: str, markup: int):
        """
        Create new set of possibly multiple gold pieces.
        If the name is not given, set it to "Gold Set".
        Do not change the case.

        >>> GoldSet().name
        'Gold Set'
        >>> GoldSet('gs').name
        'gs'
        >>> GoldSet().gold_mass
        0
        >>> GoldSet().total_mass
        0
        >>> GoldSet().markup
        0
        >>> GoldSet('b', 100).markup
        100
        """

    def add(self, gold: Gold) -> None:
        """
        Add one piece of Gold object into the GoldSet.
        DO NOT FORGET TO MAKE A COPY/DEEPCOPY AS NEEDED!

        >>> g1 = Gold(gold=10, other=10)
        >>> g2 = Gold(gold=20, other=40)
        >>> gs = GoldSet()
        >>> gs.add(g1)
        >>> gs.add(g2)
        >>> gs.gold_mass, gs.total_mass
        (30, 80)

        Make a copy! Changing the mass of g1 for example MUST NOT change the
        total mass of the object!
        >>> g1.gold_mass = 20
        >>> gs.gold_mass, gs.total_mass
        (30, 80)
        
        Since we don't care how you manage the internal state of the object,
        the doctest is not provided any further. You are expected to work on
        an appropriate doctest on your own if you want one. That said, your
        program will still be tested thoroughly using pytest.

        Ensure that no matter how you manage the internal state, everything
        that we do not describe as public must remain private.

        You must implement type checking. The following must raise TypeError.

        >>> gs.add(1) # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        TypeError

        EXTRA CREDIT (NO DOCTEST): Instead of accepting one piece of gold,
        accept multiple pieces in a list, such as:

        gs.add([g1, g2])

        This is not doctested. The pytest will also be in a separate file.
        """

    def pop(self) -> Gold:
        """
        Remove the latest Gold object added, returning it.
        >>> g1 = Gold(gold=10, other=10)
        >>> g2 = Gold(gold=20, other=20)
        >>> gs = GoldSet()
        >>> gs.add(g1)
        >>> gs.add(g2)
        >>> gpop = gs.pop()
        >>> gpop.gold_mass
        20
        >>> gpop = gs.pop()
        >>> gpop.gold_mass
        10

        Popping an empty Gold Set returns None.

        >>> gpop = gs.pop()
        >>> gpop is None
        True
        """

    def __repr__(self):
        """
        See the doctest for example. Basically, just append everything
        based on the add order, then summarize in a final line.

        >>> gs = GoldSet('GoldSet 1')
        >>> g1 = Gold('Piece 1', gold=10, other=15)
        >>> g2 = Gold('Piece 2', gold=15, other=10)
        >>> gs.add(g1)
        >>> gs.add(g2)
        >>> gs
        GoldSet: GoldSet 1 (2 items)
        - Gold: Piece 1, 10 g / 25 g
        - Gold: Piece 2, 15 g / 25 g
        Total: 25 g / 50 g
        """

    def __add__(self, other):
        """
        Only for when the 'other' is also a GoldSet object.

        Combine two GoldSet together, adding the contents of the 'other'
        (right side) to the contents of the 'self' (left side).

        You should create a completely new deepcopy of everything.

        Keep the name of the 'self' (this side).
        """

# Do not remove this block.
# Doctest will not run otherwise and you won't get score.
if __name__ == "__main__":
    import doctest
    doctest.testmod()
