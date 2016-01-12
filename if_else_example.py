# Gets name and greets user depending on the length of the name
print("Hello! I'm Chitti. What's your name?")
uName = input()
print('Nice to meet you, ' + uName + '!')

if len(uName) >= 7:
    print("And btw, you should probably shorten your name...")
elif len(uName) == 0:
    print("You poor thing! You were never named!")
else:
    print("And btw, are you sure you are not as small as your name? *wink* *wink*")