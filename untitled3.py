#ismlar=[]
#n=1
#while True:
#    savol=f"{n}-do'stingiz ismini kiriting>"
#    ism=input(savol)
#    ismlar.append(ism)
#    takrorlash=input("Yana ism qo'shamizmi? (ha/yoq)")
#    n+=1
#    if takrorlash!="ha":
#        break
#    
#    
#print("Do'stlaringiz ro'yxati")
#for ism in ismlar:
#    print(ism.title())

#print("Do'stlaringiz yoshini aniqlaymiz")
#dostlar={}
#ishora=True
#while ishora:
#    ism=input("Do'stingiz ismini kiriting: ")
#    yosh=input(f"{ism.title()}ning yoshini kiriting: ")
#    dostlar[ism]=int(yosh)
#    
#    javob=input("Yana ma'lumot qo'shasizmi? (ha/yoq)")
#    if javob=="yoq":
#        ishora=False
#        
#for ism,yosh in dostlar.items():
#    print(f"{ism.title()} {yosh} yoshda")

#cars=['lamborghini', 'nexia', 'damas', 'toyota', 'nexia', 'audi', 'nexia']
#while 'nexia' in cars:
#    cars.remove('nexia')
#print(cars)

talabalar=["qodir","azizbek",'zafar','xamida','sarvar','sherbek']
baholangan_talabalar={}
while talabalar:
    talaba=talabalar.pop()
    baho=input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba]=int(baho)
    