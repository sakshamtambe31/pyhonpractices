name = "harry"
print(name[2::1])
print(len(name))
print(name.endswith("rry"))
print(name.count("r"))
print(name.capitalize())
print(name.find("h"))
print(name.replace("rry","m"))
letter = '''Dear <|NAME|>,
you are selected!
Date:<|DATE|> '''
name = input("enter your name")
date = input("Enter date")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)
st = "This is a string with double  space"
doublespace = st.replace("  ", " ")
print(doublespace)
