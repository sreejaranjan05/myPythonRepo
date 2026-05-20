import random
c = random.randint(1, 3)
if c == 1:
    c = "🪨"
elif c == 2:
    c = "📄"
else:
    c = "✂"
x = "yes"
while x == "yes":
    y = input("Rock Paper or Scissors? (r/p/s)")
    if y in ("r", "R"):
        print("You chose 🪨")
    elif y in ("p", "P"):
        print("You chose 📄")
    elif y in ("s", "S"):
        print("You chose ✂")
    else:
        print("Invalid choice")
    print("Computer chose", c)
    if y in ("r", "R"):
        if c == "🪨":
            print("TIE")
        elif c == "📄":
            print("YOU LOSE")
        else:
            print("YOU WIN")
    elif y in ("p", "P"):
        if c == "🪨":
            print("YOU WIN")
        elif c == "📄":
            print("TIE")
        else:
            print("YOU LOSE")
    else:
        if c == "🪨":
            print("YOU LOSE")
        elif c == "📄":
            print("YOU WIN")
        else:
            print("TIE")
    x = input("Play again? (yes/no)")
