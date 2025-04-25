
count=0
with open('test.txt') as f:
    ss = f.read()
    for s in ss:
        if s.isupper():
            count=count+1

print(count)




