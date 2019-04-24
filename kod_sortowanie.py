imiona =['b','a']
wzrosty = [161,172]
i, w = map(list, (zip(sorted(zip(imiona, wzrosty)))))
print(w)
print(i)

p = list(zip(*sorted(zip(imiona, wzrosty))))
print(p)
