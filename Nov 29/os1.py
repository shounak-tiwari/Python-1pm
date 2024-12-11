import os

name_of  = os.name


os_name_dict = {
    'posix': 'Unix-like (Linux, macOS, etc.)',
    'nt': 'Windows',
}

human = os_name_dict.get(name_of)

print(human)