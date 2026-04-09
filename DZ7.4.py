def common_elements():
    return {x for x in range(100) if x % 15 == 0}
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")