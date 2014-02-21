from Bio import SeqIO
filename = "NC_000913.faa"
count = 0
for record in SeqIO.parse(filename, "fasta"):
	if len(record) <100:
		count = count + 1

print("There were " + str(count) + " records in file " + filename)
