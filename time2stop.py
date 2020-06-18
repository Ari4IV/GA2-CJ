from multiprocessing import Process
import time
from pynput.keyboard import Key, Controller
fkeyboard = Controller()

print('ZA WARUDO !')

time.sleep(5) #not so fast. 5秒冷卻時間

print('TOKI WO TOMARE !')

b = 0 #建立變數b宣告為0，用於計算阻止任何反制可能次數
t_end = time.time() + 9 #計算阻止任何反制可能幾秒 9秒大約4800次以上
while time.time() < t_end:
    fkeyboard.release('z')
    fkeyboard.release('x')
    fkeyboard.release('c')
    fkeyboard.release('v')
    fkeyboard.release('a')
    fkeyboard.release('s')
    fkeyboard.release('d')
    fkeyboard.release('f')
    fkeyboard.release(Key.space)
    time.sleep(0.0005)
    b += 1 #計算阻止任何反制可能次數
#報告
print('\n阻止對手任何反制可能次數為 ' + str(b) + ' 次')
