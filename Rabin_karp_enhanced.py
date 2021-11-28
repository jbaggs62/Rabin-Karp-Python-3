from read_newdata import tuple_titles
import time

start_time = time.time()


def Search(txt, pat, l):
    n, m = len(txt), len(pat)
    if m > n:
        return
    hpattern = hash(pat);
    for i in range(n - m + 1):
        hs = hash(txt[i:i + m])
        if hs == hpattern:
            if txt[i:i + m] == pat:
                l.append(txt)
                break
    return l


list_of_pos_results = []

for x in tuple_titles:
    Search(x, "machine", list_of_pos_results)

print("total time", time.time() - start_time)
print(len(list_of_pos_results))
