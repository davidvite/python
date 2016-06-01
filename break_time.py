import webbrowser
import time

total_breaks = 1
break_count = 1

print ("this program started on "+time.ctime())
while (break_count <= total_breaks):
        time.sleep(1)
        webbrowser.open("https://youtu.be/sHE0wmgljco?t=52s")
        break_count = break_count + 1
