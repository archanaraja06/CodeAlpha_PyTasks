#Stock portfolio tracker

stock_price={"AAPL":180,"TSLA":250,"GOOGL":150,"MSFT":300,"NVDA":285}
stock_quantity={}
total_investment={}
no_of_stocks = int(input("Enter no.of stocks to store : "))
for i in range(no_of_stocks):
    stock=input("Enter Stock_name : ")
    qty=int(input("Enter Quantity : "))
    stock_quantity[stock]=qty

for key in stock_price:
    val1=stock_price.get(key,1)
    val2=stock_quantity.get(key,1)
    total_investment[key]=val1*val2

for key,value in total_investment.items():
    print(f"{key} : {value}")

choice=input("Enter yes/no for saving in file : ")

if choice=="yes":
    file_type=input("Enter file type txt/csv : ")

    if file_type=="txt":
        with open("total_stocks.txt","w") as file1:
            for key,value in total_investment.items():
                file1.write(f"{key} : {value}\n")

    elif file_type=="csv":
        with open("total_stocks.csv","w",newline="") as file2:
            writer=csv.writer(file2)
            writer.writerow(["Key" , "Value"])
            for key,value in total_investment.items():
                writer.writerow([key,value])
