i = 100
while i < 1000 :
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    i_len = len(str(i))
    if a**i_len + b**i_len + c**i_len == i :
        print(i,'是一个水仙花数')
    i += 1