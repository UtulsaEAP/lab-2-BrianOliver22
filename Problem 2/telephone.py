def telephone():
    phone = int(input())
    area = str( phone // 10000000 )
    second = str( (phone % 10000000) // 10000 ) 
    third = str( phone % 10000)
    
    
    
    
    
    
    
    print( '(' + area + ')' + ' ' + second + '-' + third )
  # 9184089757
# section1 = phone_number  1000000
# section2 = phone_number // 1000000 
# section3 = phone_number // 1000000 

if __name__ == "__main__":
    telephone()