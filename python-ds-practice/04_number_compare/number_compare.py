def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    # if a > b, print 'First is greater'
    if a > b:
        print("First is greater")
    # if b > a, print 'Second is greater'
    if b > a:
        print("Second is greater")
    # if a == b, print 'Numbers are equal'
    if a == b:
        print("Number are equal")

        