from read_newdata import  tuple_titles, new_list
import time

def RabinKarp(string, pattern, list):
    n, m = len(string), len(pattern)
    hpattern = hash(pattern);
    for i in range(n-m+1):
        hs = hash(string[i:i+m])
        if hs == hpattern:
            if string[i:i+m] == pattern:
                list.append(string)
                break
    return list


list_of_pos_results = []
# for x in tuple_titles:
#     search('machine', x, d)
start_time = time.time()

for x in tuple_titles:
    RabinKarp(x,"machine", list_of_pos_results)

print("total time", time.time() - start_time)
print(len(list_of_pos_results))