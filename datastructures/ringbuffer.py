data = (79, 9, 77, 87, 34, 37, 87, 37, 1, 18, 64, 98, 80, 56, 85, 24, 98, 63, 82, 53)

buffersize=7
buffer=[]
buffertotal=0
position=0
result=[]
while len(buffer)<buffersize:
	buffer.append(data[position])
	buffertotal=buffertotal+data[position]
	position=position+1
	result.append(float(buffertotal)/buffersize)
for v in range(position, len(data)):
	buffertotal=buffertotal-buffer[v%buffersize]
	buffer[v%buffersize]=data[v]
	buffertotal=buffertotal+buffer[v%buffersize]
	result.append(float(buffertotal)/buffersize)
print result
