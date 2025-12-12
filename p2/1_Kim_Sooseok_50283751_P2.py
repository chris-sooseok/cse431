

def power_mod(a, n, m):
    p = power(a, n)
    return p % m

def power(a, n):
    if n == 0:
         return 1    
    r = power(a, n // 2)
    r = r * r
    if n % 2 == 1:
         r = r * a
    return r

def read_input():
    line = input().strip()
    parts = line.split()
    a, n, m = map(int, parts)
    return a, n, m

if __name__ == "__main__":
        a, n, m = read_input()
        result = power_mod(a, n, m)
        print(result)
