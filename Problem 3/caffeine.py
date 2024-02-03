
def caffeine():
    caffeine_mg = float(input())
    ''' Type your code here. '''
    first = 'After 6 hours: ' +str( caffeine_mg/2 ) + ' mg'
    second = 'After 12 hours: ' + str( caffeine_mg/4 ) + ' mg'
    third = 'After 24 hours: ' + str( caffeine_mg ) + ' mg'
    print( first + '\n' + second + '\n' + third )
if __name__ == "__main__":
    caffeine()