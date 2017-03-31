# Range Generator

In this assignment we're going to build a generator (as a function) that mimics the well known `range` function from Python. As you know, in Python 3, `range` returns an iterator (in Python 2 we have `xrange`).

The general usage of our range generator is going to be quite similar to the Python's one:

```python
for num in rmotr_range(start=0, end=3):
    print(num)

>>> 0
>>> 1
>>> 2

for num in rmotr_range(start=1, end=5):
    print(num)

>>> 1
>>> 2
>>> 3
>>> 4

for num in rmotr_range(start=0, end=6, step=2):
    print(num)

>>> 0
>>> 2
>>> 4
```

Extra: Try to solve this assignment also with an Iterator (a class with `__next__` and `__iter__` method). Check the solutions for both Iterator and generator based solutions.
