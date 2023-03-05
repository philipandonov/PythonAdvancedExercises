import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


pattern = r"\w{4,}"
valid_domains = ['com', 'bg', 'org', 'net']
line = input()
while line != 'End':
    if "@" not in line:
        raise MustContainAtSymbolError("Email must contain @")
    email = line.split('@')
    name = email[0]
    domain = email[1].split('.')[1]
    if not re.findall(pattern, name):
        raise NameTooShortError("Name must be more than 4 characters")
    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    line = input()