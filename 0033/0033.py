fraction = [1, 1]

for a in range(1,10):
    for b in range(1, 10):
        for c in range(1,10):
            numerator = 10 * a + b
            denominator = 10 * b + c
            if ((float(numerator) / float(denominator)) == (float(a) / float(c))) & (a != c):
                fraction[0] *= numerator
                fraction[1] *= denominator
                print "%i / %i = %i / %i" %(numerator, denominator, a, c)

print "Multiplied together: %i / %i" %(fraction[0], fraction[1])