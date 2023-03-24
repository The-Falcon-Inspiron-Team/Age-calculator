import datetime

now = datetime.datetime.now()

try:
    y = int(input('กรุณากรอกปีเกิด (พ.ศ.เช่น 2531) : '))
except:
    y = 0

if y > 0 :
    y = int( now.year + 543 ) - y
    print( 'ปัจจุบันคุณอายุ', y )