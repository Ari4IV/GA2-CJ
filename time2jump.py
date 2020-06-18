from multiprocessing import Process
import time
from pynput.keyboard import Key, Controller
fkeyboard = Controller()

def loop_a(): #a迴圈_跳樓
    a = 0 #建立變數a宣告為0，用於計算跳樓次數
    t_end = time.time() + 5 #計算跳樓幾秒 5秒大約4次
    while time.time() < t_end:
        time.sleep(0.6)
        fkeyboard.press(Key.down)
        time.sleep(0.1)
        fkeyboard.release(Key.down)
        time.sleep(0.1)
        fkeyboard.press(Key.down)
        time.sleep(0.3)
        fkeyboard.release(Key.up)
        fkeyboard.release(Key.left)
        fkeyboard.release(Key.right)
        fkeyboard.press('v')
        time.sleep(0.25)
        fkeyboard.release('v')
        time.sleep(0.2)
        fkeyboard.press('v')
        time.sleep(0.1)
        fkeyboard.release('v')
        fkeyboard.release(Key.down)
        a += 1 #計算跳樓次數
    #報告
    print('\n敵人控制器失效')
    time.sleep(0.5)
    print('\n總命令對手跳樓次數為 ' + str(a) + ' 次')
    
def loop_b(): #b迴圈_阻止任何反制可能
    b = 0 #建立變數b宣告為0，用於計算阻止任何反制可能次數
    t_end = time.time() + 6 #計算阻止任何反制可能幾秒 6秒大約3400次以上
    while time.time() < t_end:
        fkeyboard.release(Key.up)
        fkeyboard.release(Key.left)
        fkeyboard.release(Key.right)
        fkeyboard.release(Key.space)
        time.sleep(0.0005)
        b += 1 #計算阻止任何反制可能次數
    #報告
    time.sleep(2.5)
    print('\n阻止對手任何反制可能次數為 ' + str(b) + ' 次')

if __name__ == '__main__':

    time.sleep(0.5)
    print('\n偵測到遊戲漏洞，漏洞載入中...')
    time.sleep(4) #別這麼快發動:D
    print('\n遊戲漏洞載入完成' + '\n' + '\n敵人控制器發動')
    time.sleep(0.5)
    print('\n上上下下左右AB')
    
    Process(target=loop_a).start()
    Process(target=loop_b).start()