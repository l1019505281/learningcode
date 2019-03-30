from tkinter import *
from tkinter import ttk
import struct

root=Tk()
root.title('my window')
root.geometry('200x200')
def Dec2Bin(dec):
    result = ''
    if dec:
        result = Dec2Bin(dec // 2)
        return result + str(dec % 2)
    else:
        return result


def fenjie(enter_text):
    byte_4 = struct.pack('>f',float(enter_text))
    B = struct.unpack(">i", byte_4)
    B1 = B[0]&0x000000ff
    B2 = B[0]&0x0000ff00
    B3 = B[0]&0x00ff0000
    B4 = B[0]&0xff000000

    B2 = B2 >> 8
    B3 = B3 >> 16
    B4 = B4 >> 24
    print(B[0]) 
    print(B1)
    print(B2)
    print(B3)
    print(B4)

    BI1 = Dec2Bin(B1)
    BI2 = Dec2Bin(B2)
    BI3 = Dec2Bin(B3)
    BI4 = Dec2Bin(B4)
    text.insert('insert',BI1)
    text.insert('insert',' ')
    text.insert('insert',BI2)
    text.insert('insert',' ')
    text.insert('insert',BI3)
    text.insert('insert',' ')
    text.insert('insert',BI4)
    

def helloCallBack():
    print("hello")
    enter_text = e.get()
    print(enter_text)
    output = fenjie(enter_text)
    #text.insert('insert',str(float(enter_text)/2))


def hello():
    print('hello menu')


def show_msg(*args):
    print(numberChosen.get())

'''
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
'''

B = Button(root, text ="点我", command = helloCallBack)#按钮
menubar = Menu(root)
e=Entry(root)#输入框
text = Text(root,height = 2)


for item in ['Python', 'Com', 'STM32']:
    menubar.add_command(label=item, command=hello) #菜单


'''
listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)


for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)
'''
    
number = StringVar()#开启下拉框
numberChosen = ttk.Combobox(root, width=12, textvariable=number)
numberChosen['values'] = ('com1', 'com2', 'com3', 'com8', 'com9')     # 设置下拉列表的值


numberChosen.bind("<<ComboboxSelected>>", show_msg)#时间发生功能，下拉框被选中时执行后面内容


e.pack()
numberChosen.pack()#放置下拉框
#listb.pack()                    # 将小部件放置到主窗口中
#listb2.pack()
B.pack()#放置按钮
root['menu'] = menubar#放置菜单
text.pack()
numberChosen.current(0)


root.mainloop() 
