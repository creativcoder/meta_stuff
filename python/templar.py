import re

parsed_template = []

subs_dict = {
	'title':'Feynaman Point',
	'entry': {
	'author':'Feynmann',
	'post':'Mathematics',
	'timestamp':'10/01/96'
	}
}

class Template(object):
	def __init__(self,literal,_type):
		self.literal = literal.group()
		self._type = _type
	def __str__(self):
		return str(self.literal)+','+str(self._type)

def match_var_temp(line):
	matches = re.search(r'{{.+}}',line)
	if matches:
		return matches
	else:
		return None


def extract_var(temp_var):
	if temp_var._type == 'VAR_TEMP':
		return temp_var._type.strip('{{}}')
	elif temp_var._type == 'BLOCK_TEMP':
		return temp_var._type.strip('{%%}')

def match_block_temp(line):
	matches = re.search(r'{%.+%}',line)
	if matches:
		return matches
	else:
		return None

template = open('template.txt','r')
for line in template.readlines():
	if match_var_temp(line):
		t = Template(match_var_temp(line),'VAR_TEMP')
		parsed_template.append(t)
	elif match_block_temp(line):
		t = Template(match_block_temp(line),'BLOCK_TEMP')
		parsed_template.append(t)

def flip(tup):
	return (tup[1],tup[0])

for i in parsed_template:
	var = extract_var(i)
	print('exists ',var)
	if subs_dict.has_key(var):
			print('exists ',var)

for i in enumerate(subs_dict):
	print(flip(i))
