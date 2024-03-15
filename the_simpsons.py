import random
liste13 = ["1"]
liste20 = ["19"]
liste21 = ["12","16","20","29"]
liste22 = ["2","4","5","11","13","14","15","17","18","22","23","24","25","26","27","28","31","32","33"]
liste23 = ["10","21","30"]
liste24 = ["3","34"]
liste25 = ["6","7","8","9"]


x = str(random.randrange(1,35))
if x in liste13 :
   a = str(random.randrange(1,14))
elif x in liste22 :
   a = str(random.randrange(1,23))
elif x in liste24 :
   a = str(random.randrange(1,25))
elif x in liste25 :
   a = str(random.randrange(1,26))
elif x in liste23 :
   a = str(random.randrange(1,24))
elif x in liste21 :
   a = str(random.randrange(1,22))
elif x in liste20 :
   a = str(random.randrange(1,21))

print("Saison :",x , " Episode :",a)