def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    lower_phrase = phrase.lower()
    
    if (lower_phrase == lower_phrase[::-1]):
        print ("True")
    else:
        print ("False")
    

    is_palindrome("tacocat")
# This will print true. input other phrases to print the correct true or false.