from Bio import SeqIO
filename = "NC_000913.faa"
good = 0
for record in SeqIO.parse(filename, "fasta"):
	if record.seq.endswith("*"):
		good = good + 1
		print(record.id + "ends with " + record.seq[0])
print("Found " + str(good) + " records in " + filename + " which end in *")
