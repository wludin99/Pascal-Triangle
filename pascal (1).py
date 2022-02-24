from itertools import product
import math
from scipy.special import binom
def pascal_print(N, p):
    rows = []
    for n in range(0,N):
        row = []
        for i in range(n+1):
            if i == 0 or i == n:
                row.append(1)
            else:
                val = (rows[n-1][i-1] + rows[n-1][i]) % p
                row.append(val)
        rows.append(row)
    max_val = len(str(max(max(row) for row in rows)))
    for i, row in enumerate(rows):
        text = ""
        for j, val in enumerate(row):
            if val in {0}:
                text += ' '
            else:
                text += str(val)
            if j < len(row):
                text += " "
        text = " " * (len(rows)-i) + text
        print(text)

def pascal(N, p):
    rows = []
    for n in range(0,N):
        row = []
        for i in range(n+1):
            if i == 0 or i == n:
                row.append(1)
            else:
                val = (rows[n-1][i-1] + rows[n-1][i]) % p
                row.append(val)
        rows.append(row)

    output = []
    for row in rows:
        output.append(" ".join(str(x) for x in row))
    return output

def count_sequences(p, n_rows = 500, sequence_length=2):
    sequences_found = set()
    rows = pascal(n_rows, p)
    for x in product([i for i in range(p)], repeat=sequence_length):
        seq = " ".join((str(i) for i in x))
        for row in rows:
            if seq in row:
                sequences_found.add(seq)
                break
    ans = list(sequences_found)
    ans.sort()
    return ans

def missing_sequences(p, n, sequences):
    total = set(" ".join((str(j) for j in x)) for x in product([i for i in range(p)], repeat=n))
    return total - set(sequences)

if __name__=="__main__":
    p = 2
    n = 4
    sequences_found = count_sequences(p, n_rows=500, sequence_length=n)
    print(sequences_found)
    print(len(sequences_found))
    print("missing:")
    print(missing_sequences(p, n, sequences_found))
    pascal_print(100,p)
