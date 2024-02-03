
def caffeine():
    caffeine_mg = float(input())
    ''' Type your code here. '''  # (f'{ caffeine_mg/16 :.2f}')
    first = 'After 6 hours: ' +str( (f'{ caffeine_mg/2 :.2f}') ) + ' mg'
    second = 'After 12 hours: ' + str( (f'{ caffeine_mg/4 :.2f}') ) + ' mg'
    third = 'After 24 hours: ' + str( (f'{ caffeine_mg/16 :.2f}') ) + ' mg'
    print( first + '\n' + second + '\n' + third )
if __name__ == "__main__":
    caffeine()