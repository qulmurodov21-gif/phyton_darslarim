#def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
#    avto={'kompaniya':kompaniya,
#          'rusum':model,
#          'rangi':rangi,
#          'korobka':korobka,
#          'yili':yili,
#          'narx':narxi
#          }
#    return avto
#
#avto1=avto_info('GM', 'malibu_2_turbo', 'qora', 'avtomat', 2024)
#avto2=avto_info('Mersadenz-benz', 'cls_63_amg', 'oq', 'mexanika', 2026, 85000)
#avtolar=[avto1, avto2]
#print("Onlayn bozordagi mavjud avtomabillar: ") 
#for avto in avtolar:
#    if avto['narx']:
#        narx=avto['narx']
#    else:
#        narx="Mavjud_emas"
#    print(f"{avto['rangi']}, {avto['rusum']}, {avto['narx']},")

#def summa(x,y,z,*sonlar):
#    """Kiritilgan sonlarni yig'indisini hisoblaydi"""
#    return x+y+z+sum(sonlar)
#print(summa(1,2,3))
#print(summa(1,2,3,4,5,6,7,8,90))

def avto_info(kompaniya, model, **malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar

avto1=avto_info('GM', 'Gentra', rang='qizil', yil=2024)

    
    
        
    
    