
def P_generator():
    for x in range (1, 100):
        yield x
def M_Generator():
    for y in range (1, 100000000000):
        yield y
def C_Generator():
    for z in range (1, 100000000000):
        yield z



def greeting(function):
    def f2(word):
        print("Your number is:")
        function(word)
        print("Please wait someone will be with you shortly")
        input("Press any key for a new ticket: ")




    return f2


