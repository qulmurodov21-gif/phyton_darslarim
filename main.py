#import avto_info_mod as a
#
#avto1=a.avto_info('GM', "Malibu", "qora", "mexanika", 2026, 40000)
#a.info_print(avto1)
#
#from avto_info_mod import avto_info, info_print
#
#avto1=avto_info('GM', "Malibu", "qora", "mexanika", 2026, 40000)
#info_print(avto1)
#
#from avto_info_mod import avto_info as ai, info_print as ip
#
#avto1=ai('GM', "Malibu", "qora", "mexanika", 2026, 40000)
#ip(avto1)

#from avto_info_mod import *
#
#avto1=avto_info('GM', "Malibu", "qora", "mexanika", 2026, 40000)
#info_print(avto1)

#import math
#
#print(math.pi)

import random as r

#son=r.randint(0,100)
#print(son)

#ismlar=['azizbek','odilbek','xadicha','kamoliddin']
#ism=r.choice(ismlar)
#print(ism)
#print(r.choice(ism))

#x=list(range(0,151,10))
#print(x)
#print(r.choice(x))

x=list(range(100))
print(x)
r.shuffle(x)
print(x)