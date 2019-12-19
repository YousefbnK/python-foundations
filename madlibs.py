time = raw_input("What time is it ?   ")
items = raw_input("Enter a noun:   ")
name = raw_input("What is your name ?   ")
scream = raw_input("Enter any sentence:   ")
action = raw_input("Enter a verb:   ")


print """ It was %s o'clock when I heard a knock at the door.
I opened the door and there was a box full of %s with a note saying "From Mr. %s."
Just as I closed the door I heard a scream "%s."
I froze in place and all I could do was %s. """ %(time, items, name.title(), scream.upper(), action)