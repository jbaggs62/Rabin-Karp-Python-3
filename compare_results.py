from read_newdata import tuple_titles
import time
start_time = time.time()
d = 256
def search(pat, txt, q, list):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1

    # The value of h would be "pow(d, M-1)%q"
    for i in range(M-1):
        h = (h*d)%q

    # Calculate the hash value of pattern and first window
    # of text®
    for i in range(M):
        p = (d*p + ord(pat[i]))%q
    for i in range(N):
        t = (d*t + ord(txt[i]))%q

    # Slide the pattern over text one by one
    for i in range(N-M+1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p==t:
            # Check for characters one by one
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
                else:
                    j+=1

            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j==M:
                list.append(txt)
        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t+q
q = 31

list_of_pos_results = []
# for x in tuple_titles:
#     search('machine', x, d)
for x in tuple_titles:
    (search("machine", x, q, list_of_pos_results))
print(list_of_pos_results)
print(len(list_of_pos_results))
print("total time", time.time() - start_time)