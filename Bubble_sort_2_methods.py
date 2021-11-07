# METHOD 1########################################################
l = [98, 1, 45, 7, 67, 89, 203, 12]
print(l)
for i in range(1, len(l)):
    for k in range(len(l)):
        if l[i] < l[k]:
            l[k], l[i] = l[i], l[k]
print(l)

# METHOD 2########################################################

print(l)
s = 0
while s != len(l):
    try:
        if l[s] > l[s + 1]:
            temp = l[s]
            l[s] = l[s + 1]
            l[s + 1] = temp
        s += 1
    except IndexError:
        break
print(l)
