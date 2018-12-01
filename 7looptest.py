import itertools
import datetime
from collections import defaultdict

# Define starting inputs
seats4 = [2,3,5,7]
seats8 = [2,3,5,7,11,13,17,19]
partners = []
opponents = []
txtPairingAre = "The pairing options is: "
seperator = ","


def roundcheck(seats, round):
    if round=1
        partners = []
        opponents = []
    else   
    # iterate all seats
    for i in itertools.permutations(seats):
        # identify paired teams sitting adjacent
        paira = i[0] * i[1]
        pairb = i[2] * i[3]
        pairc = i[4] * i[5]
        paird = i[6] * i[7]
        # identify both opponents across both boards for each player
        opp02 = i[0] * i[2]
        opp03 = i[0] * i[3] 
        opp12 = i[1] * i[2]
        opp13 = i[1] * i[3]
        opp46 = i[4] * i[6]
        opp47 = i[4] * i[7] 
        opp56 = i[5] * i[6]
        opp57 = i[5] * i[7]     

# use these variables to check round state
if (partners.count(paira) < 1 and partners.count(pairb) < 1 and partners.count(pairc) < 1 and partners.count(paird) < 1 and opponents.count(opp02) < 2 and opponents.count(opp03) < 2 and opponents.count(opp12) < 2 and opponents.count(opp13) < 2 and opponents.count(opp46) < 2 and opponents.count(opp47) < 2 and opponents.count(opp56) < 2 and opponents.count(opp57) < 2):
    print(" This round pairing is: " + str(i) + '-', end='') 



for s in seats8:
    partners = []
    opponents = []
    roundcheck
    if s<8:
        print('1s.' + str(s) + '<-')
    for t in seats4:
        if t<8:
            print('1.2t.' + str(t))
        for u in seats4:
            if u<8:
                print('1.2.3u.' + str(u) + '<-')
            for v in seats4:
                if v<8:               
                    print('1.2.3.4v.' + str(v) + '<-')
                for w in seats4:
                    if w<8:               
                        print('1.2.3.4.5w.' + str(w) + '<-')
                    for x in seats4:
                        if x<8:               
                            print('1.2.3.4.5.6x.' + str(x) + '<-')
                        for y in seats4:
                            if y<8:               
                                print('1.2.3.4.5.6.7y.' + str(y) + '<-')
                            else:
                                print('not y:' + str(y) + '->') 
                        else:
                            print('not x:' + str(x) + '->')   
                    else:
                        print('not w:' + str(w) + '->') 
                else:
                    print('not v:' + str(v) + '->')               
            else:
                print('not u:' + str(u) + '->')        
        else:
            print('not t:' + str(t) + '->')
    else:
        print('not s:' + str(s) + '->')











