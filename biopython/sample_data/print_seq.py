from Bio import SeqIO
for record in SeqIO.parse("NC_000913.faa", "fasta"):
	print(record.id + record.seq[:10] + "... " + record.seq[-10:])




