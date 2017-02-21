bw = "log"
ew = "cog"
wl = ["hot","dot","dog","lot","log","cog"]
nword = bw
wrdlstfrchange=list()
wrdlstfrloop = wrdlstfrchange
lstoflists= []
count= 0
for word in wl:
                
    for i in range(len(bw)):
        if(bw[i]==word[i]):
            count= count+1
        if(count==len(bw)-1):
            wrdlstfrchange.append(word)
count=0
while(True):
    if(nword == ew):
        break
    else:
        for workingWord in wrdlstfrloop:
            
            for word in wl:
                
                for i in range(len(workingWord)):
                    if(workingWord[i]==word[i]):
                        count= count+1
                if(count==len(workingWord)-1):
                    wrdlstfrchange.append(word)
                count=0
            wrdlstfrloop = wrdlstfrchange
            lstoflists.append(wrdlstfrchange)
        nword=[ew for i in lstoflists if ew in i]
        print(lstoflists)


                        
    