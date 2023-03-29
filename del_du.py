# -*- coding: utf-8 -*-

def read_fasta(handle):
    i = 0
    matr = []
    while True:
        line = handle.readline()
        if line == "":
            i +=1
            if i>100:
                print ("100 empty line")
                break
        if not line:
            break
        if line[0] =='>':
            break
    while True:
        if not line:
            return matr
        if line[0] != '>':
            print ("Records in Fasta files should start with '>' character")
            break
        if line[0] == '>':
            title = line[1:].rstrip()
            lines = []
            line = handle.readline()
            while True:
                if not line:
                    break
                if line[0] =='>':
                    break
                lines.append(line.rstrip())
                line = handle.readline()
            matr.append((title, "".join(lines).replace(" ", "").replace("\r", "")))    
            
            
            
#read all sequence into an array,
#compare sequences in the array and delete duplicated sequences
#write other sequence into a file 
#usage " python *.py *.fasta"
           
import sys
if len(sys.argv)!=2:
    print ("fasta file" )            
fasta_name = str(sys.argv[1])
fasta_handle=open(fasta_name,'r')
list_2=read_fasta(fasta_handle)
i=0
a=len(list_2) 
out_name = open ('name.txt','w')
           
while True:
    if i >= a:
        
        break
    else: 
        out_name.write(str(list_2[i][0])+'_')
        n = i + 1
        print (n)
        print (a)    
    while True:
#        print a
        if n >= a:
            break        
        if list_2[i][1] == list_2[n][1]:
            out_name.write(str(list_2[n][0])+'_')
#            if len(list_2[i][1].replace('-','')) < 
#            print n
#            print a
#            print i
            del list_2[n]
            a -= 1
            print ("OK!")
            
        else:
            n +=1
    a = len(list_2)
    i += 1
    out_name.write('\n')
out_name = fasta_name + '.output'
out_handle = open(out_name,'w')    
for i in range(0,len(list_2)):
    out_handle.write('>%s\n' % str(list_2[i][0]))
    out_handle.write("%s\n" % str(list_2[i][1]) )
out_handle.close()
print ("all done!" )