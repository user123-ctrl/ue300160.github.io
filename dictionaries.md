# dictionaries and for-loops 
### 2024-11-11

## dictionaries

We introduced dictionaries as a way to save data where we need semantic (meaningful) connections between keys and their values.

Consider the naive case, where we have a list of names and a list of grades:

```python
names = ["sofia", "lina", "cora", "nathalie", "marko"]
grades = [1, 2, 3, 4, 5]
```

If we want to see the connection between the keys and the values, we would have to loop over both of them at once,
and suppose that the order is maintained between them:

```python
for i in range(len(names)):
    print(names[i], grades[i])
```

However, this means that if we change one of the lists, we would have to change all of them accordingly. Consider sorting the `names` list:

```python
names.sort()
```

Now the names and grades don't match any more. If we used a dictionary instead, not only could we save multiple grades (e.g. for the entire course) under
each name, but we'd also never lose the connection between name and grade:

```python
grades = {
    "sofia": [1, 1, 2, 1, 1],
    "lina": [2, 1, 2, 1, 1],
    "cora": [3, 1, 2, 1, 1, 1, 1],
    "nathalie": [4, 1, 2, 1, 1],
    "marko": [5, 1, 2, 1, 1],
}
```


## Nested directories

there is nothing preventing us from nesting dictionaries within dictionaries. We demonstrated this by creating a mini-dictionary of our own:

```python
dict_e = {
    "eel": "a sort of fish",
    "eat": "what i most enjoy"
}

dict_f = {
    "food": "best thing in the world",
    "feel": "you feel good when you eat",
}

real_dictionary = {
    "e": dict_e,
    "f": dict_f
}
```

## For-loops

When faced with the task of adding all the elements of a list to another list, we came up with multiple ideas.

```python
shopping = ['bead', 'potatoes', 'eggs']
extra_shopping = ['bread', 'soap', 'toothpaste', 'chocolate']
```

(examples included as done, think whether it works and why)

* Including the second list in the first one:

```python
test1 = ['bead', 'potatoes', 'eggs', extra_shopping]
```

* adding the second list to the first one:

```python
test2 = shopping + extra_shopping
```

* appending the second list to the first one 

```python
test3 = shopping.append(extra_shopping)
```

* going over all elements of the second list and appending them to the first:

```python
for stuff in extra_shopping:
    shopping.append(stuff)
```

