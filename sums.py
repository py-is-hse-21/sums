def sums(array: list) -> int:
    sol = [0]
    for num1 in array:
        for num2 in sol:
            res = set(sol)
            res.update([num1 + num2])
            sol = list(res)
    return len(res)
print(sums([1, 1, 2]))
