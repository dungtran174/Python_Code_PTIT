n = int(input())
dict = {}
for t in range(n - 1):
    s = [int(i) for i in input().split()]
    if dict.get(s[1]) == None:
        dict.update({s[1]: 1})
    else:
        dict.update({s[1]: dict[s[1]] + 1})
    if dict.get(s[0]) == None:
        dict.update({s[0]: 1})
    else:
        dict.update({s[0]: dict[s[0]] + 1})
print("Yes" if n - 1 in dict.values() else "No")

# n = int(input())
# a = {str(i+1):0 for i in range(n)}
# for i in range(n-1):
#     x, y = input().split()
#     a[x]+=1
#     a[y]+=1
# cnt = 0
# for i in a: cnt += 1 if a[i]==1 else 0
# print('Yes' if cnt == n-1 else 'No')
