a = input("Enter a string: ").replace(" ", "")
char_frequency = {char: a.count(char) for char in a}

print("\n".join([f"{char}: {frequency}" for char, frequency in char_frequency.items()]))
