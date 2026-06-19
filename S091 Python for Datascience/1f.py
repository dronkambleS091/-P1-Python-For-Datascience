sentence = input("Enter a sentence: ")

words = len(sentence.split())
characters = len(sentence)

lower = sentence.lower()
upper = sentence.upper()

replace = sentence.replace(" ", "_")

print("Number of Words:", words)
print("Number of Characters:", characters)
print("Lowercase:", lower)
print("Uppercase:", upper)
print("Replaced Sentence:", replace)
