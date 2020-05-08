import traceback
try:
    2/0
except:
    print(traceback.format_exc())


try:
    i = int('a')
except BaseException as e:
    print('str(Exception):\t', str(Exception))
    print('str(e):\t\t', str(e))
    print('repr(e):\t', repr(e))
    print('e.message:\t', e.args)
    # print('\n--traceback.print_exc():', traceback.print_exc())
    print('\n--traceback.format_exc():\n%s' % traceback.format_exc())
