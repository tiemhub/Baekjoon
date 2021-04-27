#동적 계획법
#복잡한 재귀함수 다루기

def w(num):
    if num in w_dict:
        return w_dict[num]
    
    if num[0] <= 0 or num[1] <= 0 or num[2] <= 0:
        value = 1
        w_dict[num] = value
        return value
    elif num[0] > 20 or num[1] > 20 or num[2] > 20:
        value = w((20,20,20))
        w_dict[num] = value
        return value
    elif num[0] < num[1] < num[2]:
        value = w((num[0],num[1],num[2]-1)) + w((num[0],num[1]-1,num[2]-1)) - w((num[0],num[1]-1,num[2]))
        w_dict[num] = value
        return value
    else:
        value = w((num[0]-1,num[1],num[2])) + w((num[0]-1,num[1]-1,num[2])) + w((num[0]-1,num[1],num[2]-1)) - w((num[0]-1,num[1]-1,num[2]-1))
        w_dict[num] = value
        return value

w_dict = {(0,0,0) : 1}


while True:
    num = tuple(map(int,input().split()))

    if num == (-1,-1,-1):
        break

    print("w({}, {}, {}) = {}".format(num[0],num[1],num[2],w(num)))
