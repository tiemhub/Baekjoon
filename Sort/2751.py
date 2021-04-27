#정렬
#O(n*lgn)으로 풀어보기
#합병정렬으로 풀기

def usersort(n_list):

    if len(n_list) == 1:
        return n_list

    mid = len(n_list) // 2
    
    front_list = usersort(n_list[:mid])
    back_list = usersort(n_list[mid:])
    
    sorted_list = merge(front_list,back_list)
    
    return sorted_list

def merge(list1,list2):

    merge_list = []

    while (len(list1) != 0) and (len(list2) != 0):
        if list1[0] < list2[0]:
            merge_list.append(list1[0])
            list1.pop(0)
        else:
            merge_list.append(list2[0])
            list2.pop(0)


    if len(list1) == 0:
        merge_list += list2
    else:
        merge_list += list1

    return merge_list


n = int(input())
num_list = []

for _ in range(n):
    num_list.append(int(input()))

sort_list = usersort(num_list)

print(sort_list)
