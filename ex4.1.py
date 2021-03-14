name, char = input("enter you name and any character: ").split(",")
print(f"total charatcet of your name is {len(name)}")
print(f"character count of your name is {name.lower().count(char.lower())}")


