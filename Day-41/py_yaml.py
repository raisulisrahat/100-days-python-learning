# Here I am showing the Yaml modules in python

import yaml

with open('demo.yaml', 'r') as file:
    files = yaml.safe_load_all(file)
    for readfile in files:
        print(readfile)

new = [{'Programming': 'C++'},
       {'Script': 'Batch Script'}]

with open('demo.yaml', 'w') as writefile:
    yaml.safe_dump(new, writefile)

with open('demo.yaml', 'r') as readfile:
    content = readfile.read()
    print(content)

