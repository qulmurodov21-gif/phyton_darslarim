def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
    avto={'kompaniya':kompaniya,
          'rusum':model,
          'rangi':rangi,
          'korobka':korobka,
          'yili':yili,
          'narx':narxi
          }
    return avto
def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylashga imkon beruvchi funksiya"""
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
    return avtolar

def info_print(avto_info):
    """Avtomobillar haqidagi ma'lumotlarni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rangi'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['rusum'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yili']}-yil, {avto_info['narx']}$")