# Problem: Mother Tux's Gold Shop (continued, version 2)

There are two sets of instructions on separate matters. You must do them both.

## INSTRUCTION SET 1: Git Repository

You must do the following:

* You must continue developing the code, creating at least TWO more commits on
  top of the template code given.
* The commit pointed by the HEAD tag must contain both files listed below.
* The files to be graded MUST be called `gold.py` and `goldset.py`.
* Any other files can be left in, but they will be ignored.

To configure your username and email in the Git environment, from your command
line tool, use the following commands:

```
git config user.name "Kasetsart STUDENT"
git config user.email kasetsart.st@gmail.com
```

This changes your Git username and email just for this repository.

You can use any email address as long as your name matches the actual name in
the Kasetsart University system and you are connected to the identity provided
in the GitHub Classroom environment.

You can use `git config --global ...` instead to make the commands affect
every single repo onwards.

## INSTRUCTION SET 2: Programming Problem

(Previous lore, you can ignore.)

Following the gold price surges in 2024 and the recent drama about the quality
of gold, Tux (the Linux penguin) has a brilliant idea to also join in on the
drama and invest in a gold shop.

Unlike the other Tu\_\_, Tux is a nice proprietor (owner) and wants to be
honest about gold prices and purity. He also wants to be kind to his mother,
known as Mother Tux, but that's another story.

Mother Tux is not a very nice mother.

(Previous lore ends here.)

Previously, you already provided the Tux family (yes, the owner's name is
Tux Tux, and the mother's name is Mother Tux Tux) but they wanted more. They
want you to add the ability to combine multiple pieces of gold into a set to
sell them as a bundle, as well as a bit of functionality fixing and object
accessibility controls.

I've provided you with some code, based on talking with the Tuxes. Please
implement as directed in the files.

### DIRECTIONS:

This time you will work on two classes, each in their own files. One is
`gold.py` and another is `goldset.py`. Precisely, the GoldSet is a new class
proposed to combine multiple pieces of gold together. This is because another
clever way for Mother Tux (the penguin) to make money is by selling sets of
gold at an even higher markup!

You will be guided precisely in the program file. Implement everything based
on the docstring and doctest. You can do it!

NOTE: The doctest is CORRECT but NOT NECESSARILY COMPLETE. Always check the
docstring to see what else must be implemented!

## Type Hints

To guide you to using correct data types and letting you know what can be
assumed, type hints are given in the code. See the code how it works.

See also: [[https://docs.python.org/3/library/typing.html]]

## Grading Standard

  No. | Score | Criteria
 ---- | ----- | ---------
   1  |   10  | doctest (straightforward) (-1 per failed test, min 0)
   2  |   30  | pytest 1 (Gold class)
   3  |   20  | pytest 2 (GoldSet class)
   4  |   20  | pytest 3 (Error checking in both classes)
   5  |    0  | pytest 4 (Extra credit to be used later in evaluation)
   6  |   10  | PEP 8 (automated linter)
   7  |   10  | Repository Correctness (real name, at least 2 commits)

* TA's will check for plagiarism.
* Criteria 6 may still get deducted if we find other faults not detected by
  the linter. Instructor + TA decision is final.
* For Criteria 6, your score is calculated as follows:
    score = lambda x: math.ceil((x-5) * 2)
  This means you must score at least 5 on pylint to receive score in this
  criteria!

## Notes

* Inspecting pytest files is permitted but not encouraged.
* DO NOT MODIFY PYTEST FILES. If you want to make your own tests, create a
  new file. Fair grading depends on the pytest files being intact. If we
  find malicious modifications that make the tests pass more than they
  should, you will be flagged with academic dishonesty.
* GitHub Classroom will flag your submission if you modify the pytest file.
* Following the directions in the assignment file should be enough.
* ONLY the submission at GitHub classroom counts. Other LMS don't count.

Should you accidentally commit modifications of pytest file, you can restore
it by committing everything you've done so far (leave nothing uncommitted).

Check `git log` for the very first version of the template code (that you
originally cloned from us) to see the commit ID (first 8 digits is fine)
then use the following command:

```
git checkout [Commit_ID] -- test1.py
```

Then commit again.

## Problem Author

(C) 2024 Chawanat Nakasan, Department of Computer Engineering,
Faculty of Engineering, Kasetsart University

If you found this as a forked repository, any further work is not done by the
original problem author.

Starter and tester code originally released under MIT License.

