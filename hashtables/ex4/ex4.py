cache = {}

def has_negatives(a):
    result = []

    for num in a:
        # if num is positive add to cache w/ value 0
        if num > 0:
            # add positive num to cache
            cache[num] = 0
    print(cache)
    for num in a:
        # if num is negative, add num as the value of it's opposite key
        if num < 0:
            # check if it's opp is in the cache
            if -(num) in cache:
                # add the neg num as the value of positive key
                cache[-(num)] = num
            else:
                cache[num] = 0

    # if key's value is not a 0, add key to result list
    for key, value in cache.items():
        if value != 0:
            result.append(key)

    # print(len(result))
    return result

if __name__ == "__main__":

    print(has_negatives([1,2,3,-4]))

    print(cache)