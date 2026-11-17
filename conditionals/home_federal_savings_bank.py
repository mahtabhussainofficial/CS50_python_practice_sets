print("welcome to the home federal saving banks.")

greeting = input("greeting: what is happening? ").lower()
if greeting == "hello":
    print("$0")
elif "h" in greeting:
    print("$20")
else:
    print("$100")
