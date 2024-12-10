# Three ways to do parallel loops

Let's define two lists with the same length but different content:

```python
list_a = list(range(5))
list_b = list(range(5, 10))
```

One way to loop over both of them at the same time is to define an index variable
that will take values between 0 and their (shared) length:

```python
>>> for i in range(5):
# could also be range(len(list_a))
...     print(list_a[i], list_b[i])
...
0 5
1 6
2 7
3 8
4 9
```

A more elegant way to do the same is to use `enumerate`. This function returns the index `i`
and the value at position `list[i]` at the same time; we can then use the index to query the
other list:

```python
>>> for i, value in enumerate(list_a):
...     print(value, list_b[i])
...
0 5
1 6
2 7
3 8
4 9
```

Finally, if all we care for are the values that are at the same position in both lists,
we can use the `zip` function, which will glue the two lists next to each other and then
loop over them at the same time. This approach is handy for a small number of lists
(maybe 2-4) but quickly loses appeal the more lists we want to iterate over.

```python
>>> for a, b in zip(list_a, list_b):
...     print(a, b)
...
0 5
1 6
2 7
3 8
4 9
```