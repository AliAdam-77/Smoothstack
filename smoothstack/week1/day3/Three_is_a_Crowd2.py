def crowd_test(l):
    if len(l)>3:
        print("The room is crowded.")
    else:
        print("The room is not very crowded.")
    return


l = ["john","doe","foo","bar"]

crowd_test(l)

del l[0]
del l[0]

crowd_test(l)