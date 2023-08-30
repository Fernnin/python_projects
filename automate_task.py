import time, pyautogui as gui

x_axis= 514
y_axis= 1079
gui.mouseDown(x= x_axis, y= y_axis)
gui.mouseUp(x= x_axis, y= y_axis)


time.sleep(3)
x_axis= 1035
y_axis= 1049
gui.mouseDown(x= x_axis, y= y_axis)
gui.mouseUp(x= x_axis, y= y_axis, button='left')


time.sleep(4)
for i in range(55):
    x_axis = 475
    y_axis = 67
    gui.mouseDown(x= x_axis, y= y_axis)
    gui.mouseUp(x= x_axis, y= y_axis, button='left')
    str1=str(i)
    gui.write(str1)
    gui.press("enter")
    time.sleep(3)
    if i == 34:
        time.sleep(1)
        x_axis = 979
        y_axis = 371
        gui.mouseDown(x= x_axis, y= y_axis)
        gui.mouseUp(x= x_axis, y= y_axis, button='right')
        time.sleep(1)
        x_axis = 1056
        y_axis = 955
        gui.mouseDown(x= x_axis, y= y_axis)
        gui.mouseUp(x= x_axis, y= y_axis, button='left')
        time.sleep(4)  

# time.sleep(5)
# mouseX , mouseY = gui.position()
# print('x axis:', mouseX)
# print('y axis:', mouseY)