inp = input("Greeting: ").lower()
while True:
    if "hello" in inp:
        print("$0")
        break
    if inp[0] == "h":
        print("$20")
        break
    else:
        print("$100")
        break