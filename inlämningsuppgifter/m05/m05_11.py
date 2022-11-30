start = 10000
interest = 1.03
procent = "%"

cols = "|{:10} | {:10} | {:1} {:1} |"
print(cols.format("År", "Interest", "%", ""))
for i in range(1, 16):
    print("\n" + cols.format(str(i), str(round((start * (interest ** i)))),
                             str(round(((start * (interest ** i)) / start * 100 - 100))), procent))
