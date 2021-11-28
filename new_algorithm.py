from read_newdata import tuple_titles
import time

start_time = time.time()

# d is the number of characters in the input alphabet
d = 256


# pat  -> pattern
# txt  -> text
# q    -> A prime number


def search(pat, txt, q, list_of_titles):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1
    # creating all my pattern hash
    for i in range(M):
        p = (d * p + ord(pat[i]))
    # creating dictionary
    windows = {}
    # creating window hashes and appending to dictionary

    for i in range(N - (M + 1)):
        for j in range(i, i + M):
            t = (d * t + ord(txt[j]))
        windows[i] = t
    for key in windows:
        if windows[key] == p:
            list_of_titles.append(txt)

            # if we find first match we stop searching

            break


q = 31
list_of_titles = []
for x in tuple_titles:
    (search('machine', x, q, list_of_titles))
print(list_of_titles)
print(len(list_of_titles))
print("total time", time.time() - start_time)
