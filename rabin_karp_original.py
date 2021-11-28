import sys

from read_newdata import tuple_titles
import time
start_time = time.time()
d = 256
def rk_search(pat, txt, q, list):
    m = len(pat)
    n = len(txt)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0

    if m>n:
        return

    for i in range(m-1):
        h = (h*d) % q

    # Calculate hash value for pattern and text
    for i in range(m):
        p = (d * p + ord(pat[i])) % q
        #print("This is i value and the txt and pattetn %s %s %s", (i,text,pattern))
        t = (d*t + ord(txt[i])) % q



    # Find the match
    for i in range(n-m+1):
        if p == t:

            for j in range(m):
                if txt[i+j] != pat[j]:
                    break

            j += 1
            if j == m:
                #print("Pattern is found at position: " + str(i+1))
                list.append(txt)
                break


        if i < n-m:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+m])) % q

            if t < 0:
                t = t+q
    return list


# create list to append result back too
list_of_pos_results = []

q=101

for x in tuple_titles:
    rk_search("machine",x,q, list_of_pos_results)

print("total time", time.time() - start_time)
print(len(list_of_pos_results))