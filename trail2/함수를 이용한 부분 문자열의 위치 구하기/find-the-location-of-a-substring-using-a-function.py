text = input()
pattern = input()

n_p = len(pattern)

def cal():
    n = 0

    for i, t in enumerate(text):
        for j in range(n_p):
            if i + j >= len(text) or text[i + j] != pattern[j]:
                break
            n += 1

        if n == n_p:
            return i

        n = 0

    return -1

print(cal())