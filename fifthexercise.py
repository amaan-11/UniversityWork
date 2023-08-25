tlt=float(input("Enter the talents,"))
pnds=float(input("Enter the pounds,"))
lts=float(input("Enter the lots,"))
tlt_pnds=(tlt*20)+pnds
tlt_pnds_lts=(tlt_pnds*32)+lts
fin=tlt_pnds_lts*13.3
if fin>=1000:
    kgs=fin/1000
    gms=fin%1000
    print("The weight in modern units:\n",int(kgs),"Kilograms and",int(gms),"grams.")