#!/usr/bin/python
import argparse
import dbindex#import index module

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
db=dbindex.DBIndex(args.database,args.database+".idx")
for seqid in searchset:
    print db.searchdatabase(seqid)#prints results for specific seq id

