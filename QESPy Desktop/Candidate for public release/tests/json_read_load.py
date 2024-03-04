import json
from time import sleep

with open('sw_templates.json') as f:
    templates = json.load(f)

print(templates)

# for section, commands in templates.items():
#    print(section)
#    print('\n'.join(commands))
    
sleep(5)
