
import re

increment = ''

search_pattern = '{}(\\d*)'.format('name')
instance_names   = ['name', 'name1', 'name2', 'otherName', 'otherName1']
instance_numbers = [re.search(search_pattern, y) for y in instance_names]
last_increment = max([x.group(1) for x in instance_numbers if x]) or None

if last_increment:
    increment = str(int(last_increment) + 1)

instance_name = '{}{}'.format('name', increment)

print(instance_name)

