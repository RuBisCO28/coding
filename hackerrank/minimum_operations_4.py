# The result satisfied expeted value but it doesn't work due to hackerrank edtor problem
def min_operations(r, g, b):
    return -1 if len(r)<sum(map(any,(r,g,b))) else sum(r+g+b)-sum(map(max,(r,g,b)))

r = []; g =[]; b = []
for _ in range(int(input())):
    ri, gi, bi = map(int, input().split(' '))
    r += [ri]; g += [gi]; b += [bi]

print(min_operations(r,g,b))
