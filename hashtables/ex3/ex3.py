def intersection(arrays):
    result = []
    cache = {}
    # store all array nums in dict key= num value = count
    # if num already exists in cache increment the count
    print(arrays)
    # else add it to the cache and icrement the count


    return result


if __name__ == "__main__":
    # arrays = []
    #
    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    # print(intersection(arrays))
    intersection([
        [1, 2, 3],
        [1, 4, 5],
        [1, 6, 7]
    ])
'''
# Intersections of Multiple Lists

Find the intersection between multiple lists of integers.

Do not use numpy or sets to solve this; use `dict` or hashtables,
please.

We're given a list of lists that contain integers:

```python
[
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
]
```

And we need to compute the _intersection_, that is, numbers that exist
in all lists.

From the above input, the return value will be:

```
[1, 2]
```

Because those are the numbers that exist in all the lists.

(Output can be in any order.)

Limits:

* There can be up to 10 lists in the list of lists.
* The lists can contain up to roughly 1,000,000 elements each.
'''