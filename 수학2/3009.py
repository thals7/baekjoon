x_li = []; y_li = []
for i in range(3):
    x, y = input().split()
    x_li.append(x)
    y_li.append(y)
for x in x_li:
    if x_li.count(x) == 1:
        print(x, end='')
        break
for y in y_li:
    if y_li.count(y) == 1:
        print(" {}".format(y))
        break