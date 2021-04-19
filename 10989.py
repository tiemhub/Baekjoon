def c_sorting(n_list):
    c_list = [0]*(max(n_list)+1)

    for i in n_list:
        c_list[i] += 1

    for i in range(max(n_list)):
        c_list[i+1] += c_list[i]
        
    return c_list

def count_sorting(n_list,c_list):

    sort_list = [0] * len(n_list)

    n_list.reverse()

    for i in n_list:
        sort_list[c_list[i]-1] = i
        c_list[i] -= 1

    return sort_list

    
n = int(input())
num_list = []

for _ in range(n):
    temp = int(input())
    num_list.append(temp)
        
c_list = c_sorting(num_list)

sorted_list = count_sorting(num_list,c_list)

print(sorted_list)
