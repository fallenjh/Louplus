for i in range(101):
    beishu = i%7==0
    han7 = i%10==7 or i//10%10==7
    if beishu or han7:
        continue
    print(i)

