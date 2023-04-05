dir = 'phase_distribution_refrigerator_p-0.99.txt'
with open(dir,'r') as infile:
	table = [line.split(' ') for line in infile]
newdir = 'phase_distribution_refrigerator_-p0.99new.txt'
datasize = len(table)
with open(newdir,'w') as outfile:
	for i in range(datasize):
		if i<datasize-1:
			row = table[i]
			nextrow = table[i+1]
			if row[0]!= nextrow[0]:
				row = ' '.join(row)+"\n"
				outfile.write(row)
			else:
				row = ' '.join(row)
				outfile.write(row)
		else:
			row = ' '.join(table[i])
			outfile.write(row)

		

		


