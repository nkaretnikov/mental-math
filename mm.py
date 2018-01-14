# Multiply a two digit number by 11
for i in range(10,100):
    print "{} * 11,{}".format(i, i * 11)

# Square a two digit number that ends on 5
for i in range(10,100):
    if (i % 5 == 0 and i % 10 != 0):
        print "{}^2,{}".format(i, i**2)

# Multiply a two digit number with the same first digits and the sum of last digits = 10
for i in range(10,100):
    for j in range(10, 100):
        i_str = str(i)
        j_str = str(j)
        if (int(i_str[0]) == int(j_str[0]) and
            int(i_str[1]) + int(j_str[1]) == 10):
            print "{} * {},{}".format(i,j, i*j)
