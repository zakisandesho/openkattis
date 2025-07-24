def switch_to_99(n):
    #get number to the closest one ending w 99, down or up
    base = (n - 99) // 100
    lower = base * 100 + 99
    upper = lower + 100
    if n - lower < upper - n:  
        return lower
    else:
        return upper   

n = int(input("Enter a number: "))
p = switch_to_99(n)
print(f"The closest number ending with 99 is: {p}")
 