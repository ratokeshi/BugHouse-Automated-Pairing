import itertools
import datetime
from collections import defaultdict
seats4 = [2,3,5,7]
seats8 = [2,3,5,7,11,13,17,19]
partners = []
opponents = []
i=0
txtPairingAre = "The pairing options is: "
seperator = ","
print ("***********************************")
print(datetime.datetime.now())
print ("***********************************")
print("This is a bughouse set of 4: " + str(seats4) + str("\r\n"))

#   To print an element of the list.  In this case element 2
#       print (seats4[2])

print("This is a bughouse set of 8: " + str(seats8) + str("\r\n"))
print("This is the current partners set: " + str(partners) + str("\r\n"))
print("This is the current opponents set: " + str(opponents) + str("\r\n"))
#print (partners)
#print(opponents)
pairingresult = ()
#p = defaultdict(pairingresult)
print(pairingresult)
#print("The player number is: " + str(len(seats8)))
print ("***********************************")
#x = seats4[0]
#print (x)
for s in itertools.permutations(seats4):
    print (str(s))
    for t in itertools.permutations(seats4):
        print ("    " + str(t))



#toggle this for 4 or 8 players
#for s in itertools.permutations(seats4):
#for s in itertools.permutations(seats8):    
    
    #print (" ".join(map(str, s)))
#    paira = s[0] * s[1]
#    pairb = s[2] * s[3]
#    if len(s) > 4:
#        pairc = s[4] * s[5]
#        paird = s[6] * s[7]
#       
#    opp02 = s[0] * s[2]
#    opp03 = s[0] * s[3] 
#    opp12 = s[1] * s[2]
#    opp13 = s[1] * s[3]
#    if len(s) > 4:
#        opp45 = s[4] * s[5]
#        opp47 = s[4] * s[7] 
#        opp65 = s[6] * s[5]
#        opp67 = s[6] * s[7]
    
#    print (len(s))
    #print (paira)
    #print (str(paira) + " is the paira value")
    #if and example
    #if paira != 0 and partners.count(paira)< 2:
    #if partners.count(paira) < 2 and partners.count(pairb)< 2:
    #    print ("Pair A partner count is " + str(partners.count(paira)) + " -> less than 2 so appending pair A: A value is = " + str(paira))
    #    partners.append(paira)
    #else:
    #    print (str(paira) + " is either 0 or count in list " +  str(partners.count(paira)) + " is 2 or more.")        
    #if pairb != 0 and partners.count(pairb)< 2:
    #    print ("Pair B partner count is " + str(partners.count(pairb)) + " -> less than 2 so appending pair B: B value is = " + str(pairb))
    #    partners.append(pairb)
    #else:
    #    print (str(pairb) + " is either 0 or count in list " +  str(partners.count(pairb)) + " is 2 or more.") 

 #   if partners.count(paira) < 2 and partners.count(pairb) < 2:
 #       print ("Pair A or B partner count: " + str(partners.count(paira)) + " or " + str(partners.count(pairb)) + " -> both less than 2 so appending pair A and B: values are: " + str(paira) + " , " + str(pairb))
 #       partners.append(paira)
 #       partners.append(pairb)
        #pairingresult[i] = s 
 #   else:
 #       print (str(paira) + " and/or " + str(pairb) + " count in list " +  str(partners.count(paira)) + " or " + str(partners.count(pairb)) + " count in list is 2 or more.")        

    #if pairb != 0 and partners.count(pairb)< 2:
    #    print ("Pair B partner count is " + str(partners.count(pairb)) + " -> less than 2 so appending pair B: B value is = " + str(pairb))
    #    partners.append(pairb)
    #else:
    #    print (str(pairb) + " is either 0 or count in list " +  str(partners.count(pairb)) + " is 2 or more.") 



    #if pairc != 0:
    #    partners.append(pairc)
    #if paird != 0:
    #    partners.append(paird)        
#    print(partners)
    

    

    





