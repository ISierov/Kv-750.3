# try:
#     data = int(input())
#     if data % 2 == 1: print('odd')
#     else: print('even')
# except ValueError:
#     print()
#

try:
    nums = input()
    a, b = nums.split(',')
    res = int(a) % int(b)
except (ZeroDivisionError, SyntaxError, ValueError) as e:
    print(e)
except:
    print('Error')
else:
    print(res)
finally:
    print('Thanks for using!')