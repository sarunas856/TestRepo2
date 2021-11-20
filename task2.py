def minimum(x):
    mini = x[0]
    for i in x[0:]:
        if i < mini:
            mini = i
        else:
            mini = x[0]
    return mini
b = [1,2,3,4,5]
print (minimum(b))