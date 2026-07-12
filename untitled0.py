#def toliq_ism_yasa(ism, familiya):
#    """To'liq ism qaytaruvchi funksiya"""
#    toliq_ism=f"{ism.title()} {familiya.title()}"
#    return toliq_ism
#    
#talaba1 = toliq_ism_yasa("odilbek","bekmirzaev")
#talaba2 = toliq_ism_yasa("azizbek","bekmirzayev")
#print(f"Bugun {talaba1} va {talaba2} kech qoldi")
#print(f"Bugun {talaba2} dachaga do'stlari bilan dachaga ketishini bilgan {talaba1} meniyam qo'shinglar dedi")

#def toliq_ism_yasa(ism, familiya, otasining_ismi=""):
#    """To'liq ismni qaytaruvchi funksiya"""
#    if otasining_ismi:
#        toliq_ism=f"{ism} {otasining_ismi} {familiya}"
#    else:
#        toliq_ism=f"{ism} {familiya}"
#    return toliq_ism.title()
#
#talaba3=toliq_ism_yasa("Kamoliddin","Bekmirzayev")
#talaba4=toliq_ism_yasa("Zulfizar","Xayitova","Nurxonovna")
#print(f"15 yil oldin Usmonovni shogirtlaridan shu 2 lasini taniyaman. 1-si:{talaba3} 2-si:{talaba4}")

def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
    avto = {'kompaniya':kompaniya,
           'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narx':narxi}
    return avto 

print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar=[]
while True:
    print("\nQuyidagi ma'lumotlarni kiriting")
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi: ")
    korobka=input("Korobka: ")
    yili=input("Ishlab chiqarilgan yili: ")
    narxi=input("Narxi: ")
    
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))

    javob=input("Yana avto qo'shasizmi? (yes/no): ")
    if javob== 'no':
          break
      
print("\n Salonimizdagi avtolar:")
for avto in avtolar:
    if avto['narx']:
        narx=avto['narx']
    else:
        narx="Mavjud_emas"
    print(f"{avto['rang'].title()} {avto['model'].title()} {avto['korobka'].title()} {avto['narx'].title()}")


#avto1=avto_info('GM','Matiz','Tilla','Mexanika',2020)
#avto2=avto_info('GM','Malibu','Qora','Avtomat',2025,24000)
#avtolar=[avto1, avto2]
#print('Onlayn bozordagi mavjud avtomashinalar:')
#for avto in avtolar:
#    if avto['narx']:
#        narx=avto['narx']
#    else:
#        narx="Mavjud_emas"
#    print(f"{avto['rang']} {avto['model']}. Narxi: {narx}")

#def oraliq(min,max, qadam=1):
#    sonlar=[]
#    while min<max:
#        sonlar.append(min)
#        min += qadam 
#    return sonlar 
#
#print(oraliq(0,10,2))
#print(oraliq(0,10))



