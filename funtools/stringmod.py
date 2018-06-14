
def last_first(x):
    return x[-1] + x[:len(x)-1]

def mirror(x):
    if not type(x)==str:
        raise ValueError("Not a string object")
    word = ""
    for i in range(len(x)):
        word =  x[i] + word + " "
    return word

def psen(x):
    return "This is your string " + x
