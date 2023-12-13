person = {'name': 'Roman', 'surname': 'Smith', 'date_of_birth': '12.12.2001'} 

"""
name Roman
surname Smith
date_of_birth 12.12.2001
"""

def save_person_to_file(person, path):
    with open(path, 'w') as fh:
        output = ''
        for key, value in person.items():
            output += f'{key} {value}\n'
        fh.write(output)

def read_person_from_file(path):
    person = dict()
    with open(path) as fh:
        for line in fh:
            key, value = line.replace('\n', '').split(' ')
            person.update({key : value})
    return person

# save_person_to_file(person, 'test.txt')
print(read_person_from_file('test.txt'))