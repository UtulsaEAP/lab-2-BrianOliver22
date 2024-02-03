
def simple_stats():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    multi1 = str(f'{ num1*num2*num3*num4 :.0f}') 
    avg_1 = str (f'{(num1+num2+num3+num4)/4 :.0f}')
    multi2 = str (f'{ num1*num2*num3*num4  :.3f}')
    avg_2 = str (f'{(num1+num2+num3+num4)/4 :.3f}')
    print (multi1 + ' ' + avg_1 + '\n' + multi2 + ' ' + avg_2 )

    ''' Type your code here. '''
    
if __name__ == "__main__":
    simple_stats()