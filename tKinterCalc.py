import tkinter as tk
import time
scr = tk.Tk()

x = None
y = None
oper = None

def setFirst(op):
	global x
	global y
	global oper
	if x == None:
		try:
			x = float(t["text"])
		except:
			x = int(t["text"])
		t["text"] = ""
	else:
		try:
			y = float(t["text"])
		except:
			y = int(t["text"])
		if oper == "a":
			x += y
		elif oper == "s":
			x -= y
		elif oper == "m":
			x *= y
		elif oper == "d":
			x /= y
		t["text"] = "<Your Output : " + str(x) + ">"
	oper = op
			
	
def write(x):
	r = t["text"]
	if(len(r)>10):
		t["text"] = "!!!Out of bounds!!!"
		return
	r += str(x)
	t["text"] = r

def clear():
	t["text"] = ""
	global x
	global y
	global oper
	x = None
	y = None
	oper = None
	
t = tk.Label(scr,anchor="se")
t["height"] = 25
t.grid(row=0,column=0,columnspan=4)

bt1 = tk.Button(scr,text="1",command= lambda : write(1))
bt1["width"]=5
bt1["height"] = 3
bt1.grid(row=1,column=0)

bt2 = tk.Button(scr,text="2",command= lambda : write(2))
bt2["width"]=5
bt2["height"] = 3
bt2.grid(row=1,column=1)

bt3 = tk.Button(scr,text="3",command= lambda : write(3))
bt3["width"]=5
bt3["height"] = 3
bt3.grid(row=1,column=2)

bt4 = tk.Button(scr,text="4",command= lambda : write(4))
bt4["width"]=5
bt4["height"] = 3
bt4.grid(row=2,column=0)

bt5 = tk.Button(scr,text="5",command= lambda : write(5))
bt5["width"]=5
bt5["height"] = 3
bt5.grid(row=2,column=1)

bt6 = tk.Button(scr,text="6",command= lambda : write(6))
bt6["width"]=5
bt6["height"] = 3
bt6.grid(row=2,column=2)

bt7 = tk.Button(scr,text="7",command= lambda : write(7))
bt7["width"]=5
bt7["height"] = 3
bt7.grid(row=3,column=0)

bt8 = tk.Button(scr,text="8",command= lambda : write(8))
bt8["width"]=5
bt8["height"] = 3
bt8.grid(row=3,column=1)

bt9 = tk.Button(scr,text="9",command= lambda : write(9))
bt9["width"]=5
bt9["height"] = 3
bt9.grid(row=3,column=2)

bt0 = tk.Button(scr,text="0",command= lambda : write(0))
bt0["width"]=5
bt0["height"] = 3
bt0.grid(row=4,column=1)

btdot = tk.Button(scr,text=".",command= lambda : write("."))
btdot["width"]=5
btdot["height"] = 3
btdot.grid(row=4,column=2)

btclear = tk.Button(scr, text="C", command = clear)
btclear["width"] = 5
btclear["height"] = 3
btclear.grid(row=4,column=0)

btadd = tk.Button(scr,text="+",command=lambda: setFirst("a"))
btadd["width"]=5
btadd["height"] = 3
btadd.grid(row=1,column=3)

btsub = tk.Button(scr,text="-",command=lambda: setFirst("s"))
btsub["width"]=5
btsub["height"] = 3
btsub.grid(row=2,column=3)

btmul = tk.Button(scr,text="x",command=lambda: setFirst("m"))
btmul["width"]=5
btmul["height"] = 3
btmul.grid(row=3,column=3)

btdiv = tk.Button(scr,text="÷",command=lambda: setFirst("d"))
btdiv["width"]=5
btdiv["height"] = 3
btdiv.grid(row=4,column=3)


scr.mainloop()  
