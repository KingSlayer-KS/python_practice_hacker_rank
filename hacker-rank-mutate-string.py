def mutate_string(string, position, character):
    z = list()
    for i in string:
        z.append(i)
    z[position]=character
    z="".join(z)
    return z
s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)