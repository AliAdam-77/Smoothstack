def crowd_test(l):
    if len(l)>5:
        print("There being a mob in the room.")
    elif len(l)>= 3 and len(l) <= 5:
        print("The room being crowded.")
    elif len(l)== 1 and len(l) == 2:
        print("the room not being crowded.")
    else:
        print("The room being empty.")
    return


l = ["john","doe","foo","bar","jack","mike"]

crowd_test(l)

del l[0]
del l[0]

crowd_test(l)