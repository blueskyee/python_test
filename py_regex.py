import re

str='aabbc12345def567'

match = re.search(r'(\d{1,5}).(\d{1,5})', str)

print(match.group(0))
print(match.group(1))
print(match.group(2))

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Henry Chen")
print(m.group('first_name'))
print(m.group('last_name'))
print(m.group(1))
print(m.group(2))
