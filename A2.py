#profit 
ac = float(input("Enter actual cost"))
sc = float(input("Enter sales cost"))

if sc>ac:
    profit = sc-ac
    print("profit" ,profit, end = " Rs")
else:
    loss = ac-sc
    print("loss" ,loss, end = " Rs")
