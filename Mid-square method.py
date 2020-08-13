n = 5           #number of digit
seed = 8888       
randnum = 20    #number of random numbers generated
filename = 'mid square.txt'
f = open(filename, 'w')

for i in range(randnum):
    seed = str(seed ** 2)   #square
    s = len(seed)

    if s % 2 != n % 2:      #add zeroes if required
        seed = '0' + seed
    if s < n:
        seed = '0' * (n - s) + seed
    s = len(seed)

    seed = seed[(s - n) // 2 : n + (s - n) // 2]    #take the middle part
    print(seed)
    f.write(seed + '\n')        #write into a txt file


    for j in range(s - 1):      #omit zeroes in the front
        if seed[j] != '0':
            seed = seed[j:]
            break
    seed = eval(seed)           #iterate, use the output as the new seed

f.close()