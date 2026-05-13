def gen():
    print('omar')
    yield 1
    for i in range(5):
        print('ibrahim')
        yield 2

aa = gen()
(next(aa))
for i in range(5):
    print (next(aa))
