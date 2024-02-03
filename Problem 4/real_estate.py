
def real_estate():
    
    current_price = int(input("write current price"))
    last_month_price = int(input("write last month's price"))
    true_price = str(current_price)
    difference = str(current_price-last_month_price)
    mortgage = str(f'{((current_price * 0.051) / 12 ):.2f}')
   # ((current_price * 0.051) / 12 )
 #(f'{your_value:.2f}')
    
    print('This house is $' + true_price + '.' + ' The change is $' + difference + ' since last month.')
    print( 'The estimated monthly mortgage is $' + mortgage + '.')
    # Your code goes here
if __name__ == "__main__":
    real_estate()