import re

# sc === Operation Split or Combine
# mcv === M -> method, C -> class, V -> variable

while True:
    try:
        string = input().rstrip()
        sc, mcv, operation = string.split(";")

        if sc == "S":
            if mcv == "M":
                cap = operation[:-2]

            if mcv == "C" or mcv == "V":
                cap = operation

            s = re.sub("(\w)([A-Z])", r"\1 \2", cap)
            print(s.lower())

        if sc == "C":
            cap = operation.title()
            s = re.sub(r" ", r"", cap)
            q = s[:1].lower() + s[1:]

            if mcv == "M":
                print(q + "()")

            if mcv == "C":
                print(s)

            if mcv == "V":
                print(q)

    except EOFError:
        break
