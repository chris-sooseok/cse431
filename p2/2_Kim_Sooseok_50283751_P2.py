
def LCS(s1, s2):
    opt = [[(0, None) for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    opt2 = [[(0, None) for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                opt[i][j] = (opt[i-1][j-1][0] + 1, "left-up")
                opt[]
            elif opt[i][j-1][0] >= opt[i-1][j][0]:
                opt[i][j] = (opt[i][j-1][0], "left")
            else:
                opt[i][j] = (opt[i-1][j][0], "up")
        
    i, j = len(s1), len(s2)
    is1, is2 = 0, 0
    length_of_LCS = 0
    while i >= 0 and j >= 0:
        l, arw = opt[i][j]
        if arw == "left-up":
            i -= 1
            j -= 1
            if length_of_LCS == 0:
                length_of_LCS = l
            is1 = i
            is2 = j
        elif arw == "left":
            j -= 1
        elif arw == "up":
            i -= 1
        else:
            break

    return length_of_LCS, len(s1[is1:]) + len(s2[is2:])

def read_input():
    s1 = input().strip()
    s2 = input().strip()
    return s1, s2

if __name__ == "__main__":
    s1, s2 = read_input()
    len_of_LCS, len_of_seqs = LCS(s1, s2)
    print(len_of_LCS)
    print(len_of_seqs)