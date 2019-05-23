def makeNumber(number, digits, path = []):
    if digits == 1:
        if number not in path:
            path += [number]
            path.sort()
            if number < 10 and path not in combinations:
                combinations.append(path)

    else:
        nums = list(range(1, min(number - digits + 2, 10)))
        nums = list(set(nums).difference(path))

        for i in nums:
            makeNumber(number - i, digits - 1, path + [i])


import itertools as it
def makeNumber2(number, digits):
    return list(filter(lambda x: sum(x) == number, it.combinations(range(1,10), digits)))

combinations = []
makeNumber(15,3)
print(combinations)
