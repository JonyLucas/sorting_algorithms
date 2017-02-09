import os
import sys
import assign_02

params = ['--commented', '--integer', '--average', '--ignore=12', '--ignored=']

def task(this_params, size, output):
	this_params = params + this_params
	print this_params
	sys.stdout.flush()

	print 'Starting process'
	process = assign_02.task(this_params, False)

	while process.poll() is None:
		out = process.stdout.readline()
		if out is '': continue
		
		if output != sys.stdout and not out.startswith('>>'):
			output.write(out)
			output.flush()

		sys.stdout.write(out)
		sys.stdout.flush()


in_folder = sys.argv[1]

if len(sys.argv) > 2:
	print 'Output to file ' + sys.argv[2]
	output = open(sys.argv[2], 'w')
else:
	output = sys.stdout

if not in_folder.endswith('/'):
	in_folder = in_folder + '/'

size = False
input_files = False
files = os.listdir(in_folder)
files.sort()

for file in files:
	tokens = file.split('.')
	print tokens

	if tokens[1] != size or tokens[1] == False:
		if input_files != False:
			task(input_files, size, output)

		size = tokens[1]
		input_files = []
	
	input_files.append(in_folder + file)

task(input_files, size, output)

if output != sys.stdout:
	output.flush()
	output.close()