Turns=input()
for  i in range(0,Turns):
    on = sum(b=='1' for b in bin(input()-1)[2:])

    if on&1:    
        print "Louise"
    else:
        print "Richard"
