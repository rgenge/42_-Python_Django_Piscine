def my_var():
    numbint = 42
    numbstr = "42"
    numbstrext = "quarante-deux"
    numbfloat = 42.0
    bolltrue = True
    xlist = [42]
    xdict = {42:42}
    xtuple = (42,)
    setype = set()
    print(numbint, "has a type", type(numbint))
    print(numbstr, "has a type", type(numbstr))
    print(numbstrext, "has a type", type(numbstrext))
    print(numbfloat, "has a type", type(numbfloat))
    print(bolltrue, "has a type", type(bolltrue))
    print(xlist, "has a type", type(xlist))
    print(xdict, "has a type", type(xdict))
    print(xtuple, "has a type", type(xtuple))
    print(setype, "has a type", type(setype))

if __name__ == "__main__":
    my_var()
