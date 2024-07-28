import inflect

p = inflect.engine()
name = []
while True:
    try:
        inp = input("name: ")
        name.append(inp)
    except:
        break
mylist = p.join(name)
print ("Adieu, adieu, to", mylist)