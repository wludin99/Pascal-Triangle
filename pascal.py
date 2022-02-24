from itertools import product
from scipy.special import binom
def pascal_print(N, p):
    for n in range(0,N):
        print(f"N={n} | ", end=' ')
        for i in range(n+1):
            val = int(binom(n,i))
            print(val % p, end=' ')
        print()

def pascal(N, p):
    rows = []
    for n in range(0,N):
        row = ""
        for i in range(n+1):
            val = int(binom(n,i)) % p
            row += f"{val} "
        rows.append(row)
    return rows

def count_sequences(rows,p, sequence_length=2):
    sequences_found = set()
    for x in product([i for i in range(p)], repeat=sequence_length):
        seq = " ".join((str(i) for i in x))
        for row in rows:
            if seq in row:
                sequences_found.add(seq)
                break
    return sequences_found

if __name__=="__main__":
    p = 11
    rows = pascal(100,p)
    sequences_found = count_sequences(rows, p, sequence_length=2)
    print(sequences_found)
    print(len(sequences_found))
