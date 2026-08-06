def format_input(size_bites):
    units=["B","Kb","Mb","Gb","Tb"]
    unit=0
    size=float(size_bites)
    while size >= 1024 and unit < len(units)-1:
        size /=1024
        unit+=1
    print(f"{size:.2f} {units[unit]}")
    
data=int(input("Enter the memory size in byte "))
format_input(data)
