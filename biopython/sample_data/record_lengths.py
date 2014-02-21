
from Bio import SeqIO
filename = "NC_000913.faa"

for record in SeqIO.parse(filename, "fasta"):
	if len(record) <100: 
		print("Record " + record.id + ", length " + str(len(record.seq)))

