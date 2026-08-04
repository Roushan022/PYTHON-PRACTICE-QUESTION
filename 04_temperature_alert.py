def celsius(cel):
    f=round((cel*9/5+32),1)
    if f<32:
        print(f"Freeze Warning {f} ")
    elif f>=32 and f<100:
        print(f"Normal temp {f} ")
    else:
        print(f"Heat Warning {f}")
    return 
far=float(input("Enter Celsius value:- "))
celsius(far)
