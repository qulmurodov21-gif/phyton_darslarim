#mashina1={
#    'model':'lamborgini_urus',
#    'rang':'tilla_rang',
#    'yil':2024,
#    'narx':3000000000000,
#    'km':500135,
#    'korobka':'avtomat'
#    }
#mashina2={
#    'model':'oppo',
#    'rang':'qora',
#    'yil':2026,
#    'narx':300000000000,
#    'km':5135,
#    'korobka':'mexanika'
#    }
#mashina3={
#    'model':'mersadez-benz_cls63amg',
#    'rang':'oq',
#    'yil':2019,
#    'narx':6700000000000,
#    'km':500155,
#    'korobka':'avtomat'
#    }
#mashinalar=[mashina1,mashina2,mashina3]
#for mashina in mashinalar:
#   print(f"{mashina['model'].title()}, " 
#      f"{mashina['rang']} " , 
#      f"{mashina['yil']}-yil, {mashina['narx']} so'm",)

#print(f"{mashinalar[2]['rang'].title()} "
#      f"{mashinalar[2]['narx']}")

#mclearns=[]
#for k in range(10):
#    new_car={
#        'nmodel':"mclearn",
#        'rang':None,
#        'yil':2026,
#        'narx':None,
#        'km':0,
#        'korobka':'avto'
#        }
#    mclearns.append(new_car)
#    
#for mclearn in mclearns:
#    print(mclearn)
#    
#for mclearn in mclearns[0:3]:
#    mclearn['rang']='tilla'
#    
#for mclearn in mclearns:
#    print(mclearn)

#for mclearn in mclearns[3:6]:
#    mclearn['rang']='qizil'
#    mclearn['korobka']='avtomat'
#    
#for mclearn in mclearns:
#    if mclearn['korobka']=='avtomat':
#        mclearn['narx']=100000
#    else:
#        mclearn['narx']=95000
#        
#for mclearn in mclearns:
#    print(mclearn)

#dasturchilar={
#    'kamolliddin':['sowtvare','c++'],
#    'azizbek':['html','css','js'],
#    'murod':['hardware','c++'],
#    'hasan':['php','sql'],
#    'husan':['phyton','php'],
#    'maryam':['c++','c#']
#    }
#
#for ism , ishlari in dasturchilar.items():
#    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi")
#    for ishi in ishlari:
#        print(f"{ishi.upper()} ", end='')

hamkasblar={
    'ali':{'familiya':'alijonov',
           't_yil':1990,
           "ma'lumot":'oliy',
           'tillar':['phyton','c++']
           },
    'vali':{'familiya':'valijonov',
           't_yil':1995,
           "ma'lumot":"o'rta-maxsus",
           'tillar':['html','css','js']},
    'hasan':{'familiya':'husanov',
           't_yil':2001,
           "ma'lumot":'maxsus',
           'tillar':['phyton','php']}
           }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['t_yil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info["ma'lumot"]}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())