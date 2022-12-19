file = open("aoc16_input.txt")
l = file.read()
file.close()

MAX_VALUE = 10**100

b = ""
for c in l:
    b += bin(int(c, 16))[2:].zfill(4)

i = 0
packet_stack = []
operator_stack = []
value_stack = []
while 1:
    while 1:
        if len(packet_stack) < 2:
            break
        
        if packet_stack[-1] <= 0:
            if packet_stack[-1] == 0:
                packet_stack = packet_stack[:-1]
                value_stack, value = value_stack[:-1], value_stack[-1]
                operator_stack = operator_stack[:-1]
                
                op = operator_stack[-1]
                value_stack[-1] = op(value_stack[-1], value)
            else:
                packet_stack[-1] += 1
                break
        else:
            if i >= packet_stack[-1]:
                packet_stack = packet_stack[:-1]
                value_stack, value = value_stack[:-1], value_stack[-1]
                operator_stack = operator_stack[:-1]

                op = operator_stack[-1]
                value_stack[-1] = op(value_stack[-1], value)
            else:
                break
    
    if i > len(b) - 4:
        break
    
    type_id = int(b[i+3:i+6], 2)
    i += 6

    if type_id == 4:
        r = ""
        while 1:
            r += b[i+1:i+5]
            i += 5
            if b[i-5] == "0":
                break
        r = int(r, 2)

        if value_stack:
            op = operator_stack[-1]
            value_stack[-1] = op(value_stack[-1], r)
        else:
            value_stack += [r]
            break
    else:
        if b[i] == "0":
            length = int(b[i+1:i+16], 2)
            i += 16
            packet_stack += [i + length]
        else:
            num = int(b[i+1:i+12], 2)
            i += 12
            packet_stack += [-num]

        if type_id == 0:
            operator_stack += [lambda a, b: a + b]
            value_stack += [0]
        elif type_id == 1:
            operator_stack += [lambda a, b: a * b]
            value_stack += [1]
        elif type_id == 2:
            operator_stack += [lambda a, b: min(a, b)]
            value_stack += [MAX_VALUE]
        elif type_id == 3:
            operator_stack += [lambda a, b: max(a, b)]
            value_stack += [-MAX_VALUE]
        elif type_id == 5:
            operator_stack += [lambda a, b: b if a == MAX_VALUE else int(a > b)]
            value_stack += [MAX_VALUE]
        elif type_id == 6:
            operator_stack += [lambda a, b: b if a == MAX_VALUE else int(a < b)]
            value_stack += [MAX_VALUE]
        elif type_id == 7:
            operator_stack += [lambda a, b: b if a == MAX_VALUE else int(a == b)]
            value_stack += [MAX_VALUE]

print(value_stack[0])