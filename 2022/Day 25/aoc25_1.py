file = open("aoc25_input.txt")
l = file.read().split("\n")
file.close()

def f(s):
    r = 0
    for i in s:
        r = 5 * r + "=-012".index(i) - 2
    return r

def g(n):
    s = ""
    while n != 0:
        x = (n + 2) % 5 - 2
        s = "012=-"[x] + s
        n = (n - x) // 5
    return s

print(g(sum(f(j) for j in l)))