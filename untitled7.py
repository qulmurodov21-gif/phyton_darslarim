#def nom(argument):
#    """nima qilishi"""
#    return ifoda

#lambda argument:ifoda 

#import math

#aylana_uzunligi = lambda pi, r: 2*pi*r
#print(aylana_uzunligi(math.pi, 10))

#x_ning_y_inchi_darajasi=lambda x, y: x**y
#print(x_ning_y_inchi_darajasi(67,69))

#def daraja(n):
#    return lambda x:x**n

#kvadrat=daraja(2)
#kub=daraja(3)

#from  math  import sqrt

#sonlar=list(range(101))
#ildizlari=list(map(sqrt, sonlar))

#def daraja2(x):
#    """Bu funksiya kiritilgan sonning kvadratini hisoblaydi"""
#    return x*x
#
#sonlar=list(range(11))
#kvadrati=list(map(daraja2, sonlar))
#
#print(kvadrati)

#kvadrati=list(map(lambda x:x*x, sonlar))

#print(sonlar)
#print(kvadrati)

#a = [4, 5, 6]
#b = [7, 8, 9]

#a_plus_b = list(map(lambda x, y: x + y, a, b))

#print(a_plus_b)

#import random as r

#sonlar=r.sample(range(111),11)
#print(sonlar)

#def juftmi(x):
#    """x qiymat juft bo'lsa True, aks holda False qaytaradi"""
#    return x%2==0

#juft_sonlar=list(filter(lambda son: son%2==0,sonlar))
#print(juft_sonlar)

mevalar=['anjir','anor','olma','gilos','zardoli','banan','shaftoli','olcha']
#harf='a'
#mevalar_a=list(filter(lambda meva: meva.startswith(harf), mevalar))
#print(mevalar_a)

#meva_harflari=list(filter(lambda meva:len(meva)<=7, mevalar))
#print(meva_harflari)

#Bu listda meva harfi a bilan oxiri r bilan tugaydigan mevalarni filter qiladi.
list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))