import struct

class DBIndex():
    '''Class to create and use databasse indexes'''
    indexfile=None
    sequencefile=None
    indexed=False
    indexformat='L24s'
    sequencecount=0
    recordsize=32 #each record is a fixed length of 32bytes

    def __init__(self, sequencefile, indexfile=None):
        self.sequencefile=open(sequencefile)#file handle
	if indexfile!=None:
            self.indexfile=open(indexfile)
            self.indexed=True
            self.indexfile.seek(0,2)#position zero from the ned
            size=self.indexfile.tell()#tells you how large the file is
            if size%self.recordsize!=0:
                raise Exception('indexfile has incorrect file size')
            else:
                self.sequencecount=size/self.recordsize


    def buildindex(self, indexfile=None):#optionally give it a file name
        if indexfile==None:
            indexfile=self.sequencefile.name+'.idx'#get it from file handle
        fh=open(indexfile, 'w')#open index file for writing
        self.sequencefile.seek(0)#go to start
        seqids={}#creates dictionary of ids
        curpos=0#store current position
        line = self.sequencefile.readline()
	while line !='':#not at end of file
            if len(line)>0 and line[0]=='>':#found new sequence
                seqids[line[1:].strip().split()[0].lower()]=curpos#stores id in lowercase
            else:
                curpos=self.sequencefile.tell()#if it is not a new sequence then current position is where you are now
            line=self.sequencefile.readline()
        sortseqs=sorted(seqids.keys())#gives list of ids in order
	for k in sortseqs:
            fh.write(struct.pack(self.indexformat,seqids[k],k))
        fh.close()
        self.indexfile=open(indexfile)#reopen file so that it is ready for use
        self.indexed=True#proves that file is now indexed
        self.sequencecount=len(sortseqs)

    def getseqid(self,count):#reading an entry from the index
        '''retrieves the sequence at position count in the index'''
	pos=count*self.recordsize
        self.indexfile.seek(pos)
        (seqpos,seqid)=struct.unpack(self.indexformat, self.indexfile.read(self.recordsize))
        return (seqpos,seqid.replace('\0',''))#removes the null bytes

    def getseq(self,pos):
        self.sequencefile.seek(pos)#get sequence using id and position
        seq=self.sequencefile.readline()
        line=self.sequencefile.readline()
        while line !=None and line[0] != '>':
            seq=seq+line
            line=self.sequencefile.readline()
        return seq#returns the one sequence after reading it
    
    def searchdatabase(self,sequenceid):#binary code to search through the database
        '''searches for the sequence with id sequenceid. Returns it as text in FASTA format'''
        maxpos=self.sequencecount
        minpos=0
	seqfound=False
        curseqpos=curseq=None
	iter=0
        while seqfound==False: 
            iter=iter+1 
            curpos=(maxpos+minpos)/2 
            (curseqpos,curseq)=self.getseqid(curpos)
            if curseq.rstrip() == sequenceid.lower().rstrip():
                seqfound=True
            elif curpos==minpos:
                minpos=maxpos
            elif curseq >sequenceid.lower():
                maxpos=curpos
            elif minpos==maxpos:
                raise Exception('sequence not found')
            else:
                minpos=curpos
            if iter>20:
                raise Exception('too many iterations')
            
        return self.getseq(curseqpos)
