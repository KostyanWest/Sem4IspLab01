s = 0
print( "Enter numbers to sum (0 is exit)." )
while True:
    try:
        t = int( input() )
        if t == 0:
            break
        s = s + t
        print( "Sum: {0}".format(s) )
    except Exception:
        print( "It's not a number!" )
