"""Tools and techniques for debugging: Exception and Assertions
"""

import traceback
# raise Exception


def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


# for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
#     try:
#         box_print(sym, w, h)
#     except Exception as err:
#         print('An exception happened: ' + str(err))

# box_print('**', 5, 5)
# box_print('+', 1, 3)
# box_print('-', 3, 2)
# box_print('/', 3, 3)

# tracebacks to file
try:
    raise Exception('This is the error message')
except:
    errorFile = open('errorInfo.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('Traceback info written to errorInfo.txt')

# assertions sanity checks
# assert condition, 'error message'

podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'


