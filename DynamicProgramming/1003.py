#동적 계획법
#피보나치 재귀함수에서 f(0)과 f(1)의 호출 횟수

 
zero = [1,0,1]
one = [0,1,1]
 
def fibo(num):
    length = len(zero)
    if length <= num:
        for i in range(length,num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[num],one[num])
 
for _ in range(int(input())):
    n = int(input())
    fibo(n)


    
