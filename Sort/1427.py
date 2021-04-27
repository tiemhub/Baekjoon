#정렬
#역순으로 정렬

n = input()
n = list(n)
n.sort(reverse=True)

for i in n:
    print(i,end="")
