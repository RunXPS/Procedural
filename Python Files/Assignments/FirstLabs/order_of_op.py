class order_of_op ():
    #Proving and > or
    #and takes precedence
    x = (True or True and False)
    #or is FORCED to take precedence
    y = ((True or True) and False)
    print(x)
    print(y)
    
    z = False and True
    print(z)
    
    print(not False and True)
