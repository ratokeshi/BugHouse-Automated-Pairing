import itertools
import datetime
seats4 = [2,3,5,7]
seats8 = [2,3,5,7,11,13,17,19]
partners = []
opponents = []
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

#print("The player number is: " + str(len(seats8)))
print ("***********************************")
#x = seats4[0]
#print (x)


for s in itertools.permutations(seats8):    
    
    #print (" ".join(map(str, s)))
    paira = s[0] * s[1]
    pairb = s[2] * s[3]
    if len(s) > 4:
        pairc = s[4] * s[5]
        paird = s[6] * s[7]
       
    opp02 = s[0] * s[2]
    opp03 = s[0] * s[3] 
    opp12 = s[1] * s[2]
    opp13 = s[1] * s[3]
    if len(s) > 4:
        opp46 = s[4] * s[6]
        opp47 = s[4] * s[7] 
        opp56 = s[5] * s[5]
        opp57 = s[5] * s[7]
    
    #print (len(s))
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

    if (partners.count(paira) < 1 and partners.count(pairb) < 1 and partners.count(pairc) < 1 and partners.count(paird) < 1 and opponents.count(opp02) < 2 and opponents.count(opp03) < 2 and opponents.count(opp12) < 2 and opponents.count(opp13) < 2 and opponents.count(opp46) < 2 and opponents.count(opp47) < 2 and opponents.count(opp56) < 2 and opponents.count(opp57) < 2):
        print ("Pair partner count: A->" + str(partners.count(paira)) + " B->" + str(partners.count(pairb)) + " C->" + str(partners.count(pairc)) + " D->" + str(partners.count(paird)) + " All less than 1 so appending pairs A, B, C, D values -> " + str(paira) + " , " + str(pairb)+ " , " + str(pairc)+ " , " + str(paird))
        print ("Opponents count: 02->" + str(opponents.count(opp02)) + " 03->" + str(opponents.count(opp03)) + " 12->" + str(opponents.count(opp12)) + " 13->" + str(opponents.count(opp13)) + " 46->" + str(opponents.count(opp46)) + " 47->" + str(opponents.count(opp47)) + " 56->" + str(opponents.count(opp56)) + " 57->" + str(opponents.count(opp57)) + " adding to opponents list.")
        partners.append(paira)
        partners.append(pairb)
        partners.append(pairc)
        partners.append(paird)
        opponents.append(opp02)
        opponents.append(opp03)
        opponents.append(opp12)
        opponents.append(opp13)
        opponents.append(opp46)
        opponents.append(opp47)
        opponents.append(opp56)
        opponents.append(opp57)
        print("This round pairing is: " + str(s))
    else:
        print ("Partner Count is 1 or more: " + str(paira) + " , " + str(pairb) + " , " + str(pairc) + " , " + str(paird) + " counts are: " + str(partners.count(paira)) + " , " + str(partners.count(pairb)) + " , " + str(partners.count(pairc)) + " , " + str(partners.count(paird)) + " respectively.")        
        print ("Or opponent count is 2 or more: " + str(opp02) + "->" + str(opponents.count(opp02)) + " , " + str(opp03) + "->" + str(opponents.count(opp03)) + " , " + str(opp12) + "->" + str(opponents.count(opp12)) + " , " + str(opp13) + "->" + str(opponents.count(opp13)) + " , " + str(opp46) + "->" + str(opponents.count(opp46)) + " , " + str(opp47) + "->" + str(opponents.count(opp47)) + " , " + str(opp56) + "->" + str(opponents.count(opp56)) + " , " + str(opp57) + "->" + str(opponents.count(opp57)))

    
    #if pairb != 0 and partners.count(pairb)< 2:
    #    print ("Pair B partner count is " + str(partners.count(pairb)) + " -> less than 2 so appending pair B: B value is = " + str(pairb))
    #    partners.append(pairb)
    #else:
    #    print (str(pairb) + " is either 0 or count in list " +  str(partners.count(pairb)) + " is 2 or more.") 



    #if pairc != 0:
    #    partners.append(pairc)
    #if paird != 0:
    #    partners.append(paird)        
#print (partners)  
