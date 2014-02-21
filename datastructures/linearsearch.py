#!/usr/bin/python
import argparse

#get the command line arguments
parser=argparse.ArgumentParser()
parser.add_argument('--searchset')
parser.add_argument('--database')
args=parser.parse_args()

#read in our search sequences
ifh=open(args.searchset)
searchset=[]
for line in ifh.readlines():
    searchset.append(line.strip())
ifh.close()

#search for them in the database
db=open(args.database)
for seqid in searchset:
    db.seek(0)
    line=db.readline()
    while line[1:len(seqid)+1]!=seqid:
        line=db.readline()
db.close()

