#Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    if boolean == True:
        return 'Yes' #its working now as print is changed to return
    # else:
    return 'No'
        
print(bool_to_word(True))
print(bool_to_word(False))