file = open("aoc23_input.txt")
code = file.read().split("\n")
file.close()

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    
    return True

b = int(code[0].split()[-1])
start = b * int(code[4].split()[-1]) - int(code[5].split()[-1])
end = start - int(code[7].split()[-1])
step = -int(code[30].split()[-1])

h = 0
for i in range(start, end + 1, step):
    if not is_prime(i):
        h += 1

print(h)

#    The program checks how many non-prime numbers there
#    are between two numbers with a certain step size
#
#    set b 67                    b = 67
#    set c b                        c = 67
#    jnz a 2
#    jnz 1 5
#    ^    mul b 100                debug mode (activated):
#        sub b -100000            b = 100 * b + 100000 = 100 * 67 + 100000 = 106700
#        set c b                    ...
#        sub c -17000            c = b + 17000 = 123700
#    v    set f 1                    f = 1 (will remain 1 if b is a prime)
#        set d 2                    d = 2 (for-loop initialization)
#    v        set e 2                e = 2 (for-loop initialization)
#    v            set g d            ...
#                mul g e            ...
#                sub g b            ...
#                jnz g 2            if d * e == b: (if b is divisible by d or e)
#    ^                set f 0            f = 0 (b is not a prime)
#                sub e -1        e += 1
#                set g e            ...
#                sub g b            ...
#                jnz g -8        if e != b: repeat loop
#            sub d -1            d += 1
#            set g d                ...
#            sub g b                ...
#            jnz g -13            if d != b repeat loop
#        jnz f 2                    if f == 0: (b was not a prime)
#    ^        sub h -1                h += 1
#        set g b                    ...
#        sub g c                    ...
#        jnz g 2                    if b == c, exit the program
#        jnz 1 3                    ...
#    ^        sub b -17            ... else, b += 17 and
#            jnz 1 -23            loop back to start (loop gets run 1001 times like this)