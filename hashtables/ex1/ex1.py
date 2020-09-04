# def get_indices_of_item_weights(weights, length, weight_limit):
#     cache = {}
#
#     for index in range(length):
#         # track current weight
#         weight = weights[index]
#
#         # track
#         weight_comp = (weight_limit - weight)
#
#         # check if the needed combination exists in the cache
#        # |limit|weight|comp|                                   cache = {}
#         #  21 - (4)  = 17 is Not IN CACHE  => add curWeight to cache = {4:0}
#         #  21 - (6)  = 15 is Not IN CACHE  => add curWeight to cache = {4:0, 6:1}
#         #  21 - (10) = 11 is Not IN CACHE  => add curWeight to cache = {4:0, 6:1, 11:2}
#         #  21 - (15) =  6 is IN CACHE      => return curWeight's index & comp's index
#         if weight_comp in cache:
#             #   0  1   2   3   4
#             # [ 4, 6, 10, 15, 16]
#             weight_comp_idx = cache[weight_comp]
#             return index, weight_comp_idx
#         else:
#             # add key = weight & value = index of weight in weights array
#             cache[weight] = index
#
#
#     # if 1 item in cache, no complement
#     if len(cache) == 1:
#         return None
#
#     print(f'Cache: {cache}')

def get_indices_of_item_weights(weights, length, weight_limit):
    cache1 = {}
    cache2 = {}

    for index, val in enumerate(weights):
        weight_comp = weight_limit - weights[index]

        # store weights & their indicies
        if weight_comp not in cache2:
            cache2[val] = index
        # store weights & their comps
        if weight_comp not in cache1:
            cache1[val] = weight_comp
        else:
            # the values we need will get overwritten unless returned here.. return comp index and weight index
            print(index, val, weight_comp)
            return index, cache2[weight_comp]

    print(f'C1: {cache1}')
    print(f'C2: {cache2}')
    return None


# weights_1 = [9]
# print(get_indices_of_item_weights(weights_1, 1, 9))

# weights_2 = [4, 4]
# print(get_indices_of_item_weights(weights_2, 2, 8))
#
weights_3 = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights_3, 5, 21))

'''
Given a package with a weight limit `limit` and a list `weights` of item
weights, implement a function `get_indices_of_item_weights` that finds
two items whose sum of weights equals the weight limit `limit`. Your
function will return a tuple of integers that has the following form:

```
(zero, one)
```

where each element represents the item weights of the two packages.
_**The higher valued index should be placed in the `zeroth` index and
the smaller index should be placed in the `first` index.**_ If such a
pair doesn’t exist for the given inputs, your function should return
`None`.


## Hints

* A brute-force solution would involve two nested loops, yielding a
  quadratic-runtime solution. How can we use a hash table in order to
  implement a solution with a better runtime?

* Think about what we can store in the hash table in order to help us to
  solve this problem more efficiently. 

* What if we store each weight in the input list as keys? What would be
  a useful thing to store as the value for each key? 

* If we store each weight's list index as its value, we can then check
  to see if the hash table contains an entry for `limit - weight`. If it
  does, then we've found the two items whose weights sum up to the
  `limit`!
'''