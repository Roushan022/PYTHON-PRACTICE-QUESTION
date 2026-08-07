# taek value in mixe int and float and then get the discount and then print the total amt
def cart_total(price,discount):
    total=0
    for i in price:
        total+=i
    cart_total_amt=total-discount
    print(f"{cart_total_amt:.2f}")
    return
price=list(map(float, input("Enter the price ").split()))
discount=float(input("Enter the discount:- "))
cart_total(price,discount)
