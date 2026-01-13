# GENERATOR FUNCTION WITH YIELD

# MY-WAY (done itself in advance)
def even_generator(limit):
    even_nums = []
    for i in range(2,limit+1):
        if i%2==0:
            even_nums.append(i)
    
    return even_nums

result = even_generator(10)
for i in result:
    print(i, end=" ")
print()


# CHAI-WAY
def even_gen(limit):
    for i in range(2,limit+1,2): # range(start,end(non-inclusive),step(non-inclusive))
        # return i
        yield i # it returns value as well as remember the memory address

for num in even_gen(10):
    print(num)
