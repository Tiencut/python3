import re

string = input()

pattern = r"\d+"
matches = re.findall(pattern, string)

print(len(matches))