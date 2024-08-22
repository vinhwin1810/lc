res = []
subset = []
res.append(subset)  # Adding subset to res
subset.append(1)    # Modifying subset
res.append(subset)  # Adding modified subset to res

print(res)  # Output: [[1], [1]]
