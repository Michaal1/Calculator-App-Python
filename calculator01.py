from tkinter import *
import math
import random



#nastavenia

root = Tk()
root.title("calculator")
root.maxsize(300, 350)
root.geometry("300x350")
label1 = Label(root, width=21,font=("Courier", 18),anchor = E  )
label = Label(root, width=41, anchor = E )
label.grid(row=1, column=0,columnspan=5, pady = (5,5))
label1.grid(row=0, column=0,columnspan=5, pady = (5,0))
frame = Frame(master=root, width=150, height=10, )
frame.grid(row=2, column=0,columnspan=5)
frame1 = Frame(master=root, width=30, height=100)
frame1.grid(row=3, column=4,rowspan=5)

# nastavenia premennych

memory = ""
ans = 7
fact = False
sin1 = False
tan1 = False
cos1 = False
sqrta = False
activation_menu = False
history = []
op_history = []
parenthesis_list = []
display = []
number = 0
doth_i= False
c = 0
zero = 1
negativity = False
prnt1_index = 0
end = False

# funkcie

def show(arg1):
    global tan1
    global cos1
    global sin1
    global sqrta
    global label1
    
    if len(String(display))<20:
        label1.config(width = 21)
        label1.config(font = ("Courier", 18))

        label1.config(pady = 1)
    if len(String(display))>20:
        label1.config(width = 22)
        label1.config(font = ("Courier", 16))
        label1.config(pady = 3)

    if len(String(display))>22:
        label1.config(width = 26)
        label1.config(font = ("Courier", 14))
        label1.config(pady = 4)

    if len(String(display))>26:
        label1.config(width = 31)
        label1.config(font = ("Courier", 11))
        label1.config(pady = 6)

    if arg1 != "error":
        label1.config(fg = "black")
    else:
        label1.config(text = arg1)
        label.config(text = "")
        return 

    if sqrta == True:

        try:

            if display[-1] != "(":
                for i in range(2):
                    a = display[-2]
                    str2 = a[0] + a[1]
            display[-2]=str2 + str(display[-1])
            display.pop()

            label.config(text = str(arg1))
            label1.config(text = display)
            
        except:
            label1.config(text = display)
            label.config(text = str(arg1))
    try:
        if "sin(" in str(display[-2]) and sin1 == True:
            
            display[-2]= f"sin({str(display[-1])})"
            display.pop()
            
            label.config(text = display[-1])
            label1.config(text = display)
            return ""


        elif "cos(" in str(display[-2]) and cos1 == True:
            display[-2]= f"cos({str(display[-1])})"
            display.pop()
            label.config(text = display[-1])
            label1.config(text = display)
            return ""


        elif "tan(" in str(display[-2]) and tan1 == True:
            display[-2]=  f"tan({str(display[-1])})"
            display.pop()
            label.config(text = display[-1])
            label1.config(text = display)
            return ""
            
        elif "!" in str(display[-1]) and fact == True:
            display[-2]= f"{str(display[-2])}!"
            display.pop()
            label.config(text = display[-1])
            label1.config(text = display)
            return ""
        else:
            label1.config(text = display)
            label.config(text = str(arg1))

    except:
        label1.config(text = display)
        label.config(text = str(arg1))
    
def error():
    global sin1
    global tan1
    global cos1
    global fact
    global label
    global history
    global c
    global zero
    global doth_i
    global negativity
    global end 
    sin1 = False
    tan1 = False
    cos1 = False
    fact = False
    end = False
    negativity = False
    zero = 0
    doth_i = False
    c=0
    history.clear()
    display.clear()
    if "error" in display:
        show("error")
    else:
        label1.config(fg = "red")
        show("error")
    
def String(list_):  
    
    str1 = ""  
     
    for item in list_:  
        str1 +=" "+ str(item) 

    
 
    return str1  
        
        

def int_is_float(number):
    if number < 1 and number >= 0:
        if number == 0:
            return int(0)
        return number
    try:
        if number/int(number) == float(1) :
            return int(number)
        return number
    except:
        return number

def menu():
    global activation_menu
    if activation_menu == False:
        activation_menu = True
        button_sin = Button(root, text="sin",padx=24,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:sin()).grid(row=3,column=0)

        button_cos = Button(root, text="cos",padx=24,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:cos()).grid(row=3,column=1)

        button_tan = Button(root, text="tan",padx=24,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:tan()).grid(row=3,column=2)

        button_sqrt = Button(root, text="√",padx=32,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:sqrt()).grid(row=4,column=0)

        button_power = Button(root, text="^",padx=32,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:power()).grid(row=4,column=1)

        button_fact = Button(root, text="!",padx=32,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:factorial()).grid(row=4,column=2)

        button_Mplus = Button(root, text="M+",padx=24,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:memoryadd()).grid(row=5,column=0)

        button_MC = Button(root, text="MC",padx=24,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:memoryclear()).grid(row=5,column=1)

        button_MRC = Button(root, text="MRC",padx=18,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:memoryshow()).grid(row=5,column=2)

        button_pi = Button(root, text="π",padx=24,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:pi()).grid(row=6,column=0)

        button_per = Button(root, text="R",padx=29,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:randomn()).grid(row=6,column=1)

        button_ans = Button(root, text="ANS",padx=18,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:ans1()).grid(row=6,column=2)
    else:
        functions()
        activation_menu = False

def memoryadd():
    global memory
    memory = display[-1]
    functions()

def memoryclear():
    global memory
    memory = ""
    functions()

def memoryshow():
    global memory
    if memory != "":
        if end == True:
            history.clear()
            display.clear()
            end = False
        try:
            float(history[-1])
        except:
            history.append(memory)
            display.append(memory)
            show(memory)
    functions()



def add(number):
    global end
    global negativity
    global history
    global c
    global zero
    
    if end == True:
        history.clear()
        display.clear()
        end = False

    try:
        float(history[-1])
    except:
        display.append(0)
        history.append(0)
    if doth_i == True:
        if negativity == True:
            if number == 0 and c > 1:
                if sin1 == True or cos1 == True or tan1 == True or sqrta == True: 
                    if display[-1] == 0:
                        display.pop()
                    history[-1] = history[-1] - number*10**-c
                    display[-1]=str(history[-1]) + "0"*zero
                    c +=1
                    zero += 1
                    display.append(history[-1])
                    show(history[-1])
                else:
                    history[-1] = history[-1] - number*10**-c
                    display[-1]=str(history[-1]) + "0"*zero
                    zero += 1
                    c += 1
                    show(history[-1])
            else:
                if sin1 == True or cos1 == True or tan1 == True or sqrta == True: 
                    if display[-1] == 0:
                        display.pop()   
                    history[-1] = history[-1] - number*10**-c
                    c +=1
                    display.append(history[-1])
                    show(history[-1])
                else:
                    history[-1] = history[-1]- number*10**-c
                    display[-1]=history[-1]
                    c +=1
                    show(history[-1])
        else:
            if number == 0 and c > 1:
                if sin1 == True or cos1 == True or tan1 == True or sqrta == True: 
                    if display[-1] == 0 :
                        display.pop()
                    history[-1] = history[-1] + number*10**-c
                    display[-1]=str(history[-1]) + "0"*zero
                    display.append(history[-1])
                    show(history[-1])
                else:
                    history[-1] = history[-1] + number*10**-c
                    display[-1]=str(history[-1]) + "0"*zero
                    zero += 1 
                    c += 1
                    show(history[-1])
            else:
                if sin1 == True or cos1 == True or tan1 == True or sqrta == True: 
                    if display[-1] == 0:
                        display.pop()
                    history[-1] = history[-1] + number*10**-c
                    c+=1
                    display.append(history[-1])
                    show(history[-1])
                else:
                    history[-1] = history[-1] + number*10**-c
                    display[-1]=history[-1]
                    c +=1
                    show(history[-1])
    else:
        if negativity == True:
            if sin1 == True or cos1 == True or tan1 == True or sqrta == True: 
                if display[-1] == 0:
                    display.pop()
                history[-1] = history[-1]*10 - number
                display.append(history[-1])
                show(history[-1])
            else:
                history[-1] = history[-1]*10 - number
                display[-1]=history[-1]
                show(history[-1])
        else:
            if sin1 == True or cos1 == True or tan1 == True or sqrta == True: 
                if display[-1] == 0:
                    display.pop()

                history[-1] = history[-1]*10 + number
                display.append(history[-1])

                show(history[-1])

            else:
                history[-1] = history[-1]*10 + number
                display[-1] = (history[-1])
                show(history[-1])
    

def doth():
    global history
    global c
    global doth_i
    doth_i = True
    c=1

def negative():
    global history
    global c
    global zero
    global doth_i
    global negativity
    
    zero = 0
    doth_i = False

    try :

        float(history[-1])
        history[-1] = history[-1]*-1
        negativity = True
        display[-1] = history[-1]
        show(history[-1])
    except:
        negativity = True

def ans1():
    global ans
    global sqrta
    global history
    global c
    global zero
    global doth_i
    global negativity
    global end 
    
    negativity = False
    zero = 0
    doth_i = False
    c=0
    if end == True:
        history.clear()
        display.clear()
        end = False
    if ans != "":
        try:
            float(history[-1])
        except:
            display.append(ans)
            history.append(ans)
            show(ans)
    functions()
    
def prnt(prnt_index):
    global history
    global c
    global zero
    global doth_i
    global negativity
    negativity = False
    zero = 0
    doth_i = False
    c=0
    history.append(prnt_index)
    display.append(prnt_index)
    show(prnt_index)

def randomn():
    random1 = random.randint(0,100)
    display.append(random1)
    history.append(random1)
    show(random1)



def factorial():
    global fact
    global history
    global c
    global zero
    global doth_i
    global negativity
    global end 
    fact = True
    end = False
    negativity = False
    zero = 0
    doth_i = False
    c=0
    display.append("!")
    history.append("!")
    show("!")
    functions()

def sqrt():
    global sqrta
    global history
    global c
    global zero
    global doth_i
    global negativity
    global end 
    sqrta = True
    end = False
    negativity = False
    zero = 0
    doth_i = False
    c=0
    num = display[-1]
    display.pop()
    display.append(f"{num}√")
    history.append("√")
    show("√")
    functions()

def power():
    global sqrta
    global history
    global c
    global zero
    global doth_i
    global negativity
    global end 

    end = False
    negativity = False
    zero = 0
    doth_i = False
    c=0
    display.append("^")
    history.append("^")

    show("^")
    functions()

def sin():
    global sin1
    global history
    global c
    global zero
    global doth_i
    global negativity
    global end 
    end = False
    negativity = False
    zero = 0
    doth_i = False
    c=0
    sin1 = True
    display.append("sin(")
    history.append("sin(")
    show("sin(")
    functions()

def cos():
    global cos1
    global history
    global c
    global zero
    global doth_i
    global negativity
    global end 
    end = False
    negativity = False
    zero = 0
    doth_i = False
    c=0
    cos1 = True
    display.append("cos(")
    history.append("cos(")
    show("cos(")
    functions()

def tan():
    global tan1
    global history
    global c
    global zero
    global doth_i
    global negativity
    global end 
    end = False
    negativity = False
    zero = 0
    doth_i = False
    c=0
    tan1 = True
    display.append("tan(")
    history.append("tan(")
    show("tan(")
    functions()

def pi():
    global history
    global c
    global zero
    global doth_i
    global negativity
    global end 
    end = False
    negativity = False
    zero = 0
    doth_i = False
    c=0
    if end == True:
        history.clear()
        display.clear()
        end = False
    try:
        float(history[-1])
    except:
        display.append(3.14)
        history.append(3.14)
        show("π")
    functions()



def plus():
    
    global history
    global c
    global zero
    global doth_i
    global negativity
    global end 
    global sin1
    global tan1
    global cos1
    global fact
    global sqrta
    sqrta = False
    sin1 = False
    tan1 = False
    cos1 = False
    fact = False
    end = False
    negativity = False
    zero = 0
    c=0
    doth_i = False
    try:
        if history[-1] != ")" :
            float(history[-1])
        display.append("+")
        history.append("+")
        show("+")
    except:
        pass
      
def minus():
    global history
    global c
    global zero
    global doth_i
    global negativity
    global end 
    global sin1
    global tan1
    global cos1
    global fact
    global sqrta
    sqrta = False
    sin1 = False
    tan1 = False
    cos1 = False
    fact = False
    end = False
    negativity = False
    zero = 0
    doth_i = False
    c=0
    try:
        if history[-1] != ")" :
            float(history[-1])
        display.append("-")
        history.append("-")
        show("-")
    except:
        pass

def multiply():
    global history
    global c
    global zero
    global doth_i
    global negativity
    global end 
    global sin1
    global tan1
    global cos1
    global fact
    global sqrta
    sqrta = False
    sin1 = False
    tan1 = False
    cos1 = False
    fact = False
    end = False
    negativity = False
    zero = 0
    doth_i = False
    c=0
    try:
        if history[-1] != ")" :
            float(history[-1])
        display.append("*")
        history.append("*")
        show("*")
    except:
        pass
    
def divide():
    global label
    global history
    global c
    global zero
    global doth_i
    global negativity
    global end 
    global sin1
    global tan1
    global cos1
    global fact
    global sqrta
    sqrta = False
    sin1 = False
    tan1 = False
    cos1 = False
    fact = False
    end = False
    negativity = False
    zero = 0
    doth_i = False
    c=0
    try:
        if history[-1] != ")" :
            float(history[-1])
        display.append("/")
        history.append("/")
        show("/") 
    except:
        pass
   
def clear():
    global sin1
    global tan1
    global cos1
    global fact
    global label
    global history
    global c
    global zero
    global doth_i
    global negativity
    global end 
    sin1 = False
    tan1 = False
    cos1 = False
    fact = False
    end = False
    negativity = False
    zero = 0
    doth_i = False
    c=0
    history.clear()
    display.clear()
    show("")

def back():
    global sin1
    global tan1
    global cos1
    global label
    global history
    global c
    global zero
    global doth_i
    global negativity
    global end 
    end = False
    negativity = False
    zero = 0
    doth_i = False
    c=0
    if "√" in str(display[-1]):
        lst = list(str(display[-1]))
        lst.pop()
        history.pop()
        display[-1] = "".join(lst)
        show("")
    elif "sin(" in str(display[-1]) and "sin(" != str(display[-1]):
        lst = list(str(display[-1]))
        lst.pop()
        lst.pop()
        history.pop()
        display[-1] = "".join(lst)
        sin1 = True
        show("")
    elif "tan(" in str(display[-1]) and "tan(" != str(display[-1]):
        lst = list(str(display[-1]))
        lst.pop()
        lst.pop()
        history.pop()
        display[-1] = "".join(lst)
        tan1 = True
        show("")
        
    elif "cos(" in str(display[-1]) and "cos(" != str(display[-1]):
        lst = list(str(display[-1]))
        lst.pop()
        lst.pop()
        history.pop()
        display[-1] = "".join(lst)
        cos1 = True
        show("")
    elif "!" in str(display[-1]) and "cos(" != str(display[-1]):
        
        history.pop()
        history.pop()
        display.pop()
        show("")
    else:
        try:
            history.pop()
            display.pop()
            try:
                show("")
            except:
                show("")
        except:
            pass

def equals():
    try:
        global ans
        global end
        global parenthesis_list
        global label
        global history
        global c
        global zero
        global doth_i
        global negativity
        global display
        global op_history
        global sqrta
        sqrta = False
        end = True
        negativity = False
        zero = 0
        doth_i = False
        display.append("=")
        show("")
        op_history.clear()
        for i in history:
            op_history.append(i)    
        j=0
        while j < len(op_history):
            if op_history[j] == "(":
                prnt1_index = j 
                while op_history[j] != ")":
                    if op_history[j] == "(":
                        prnt1_index = j
                    j+=1
                j = prnt1_index
                op_history.pop(j)

                while op_history[j] != ")":

                    parenthesis_list.append(op_history[j])
                    op_history.pop(j)
                if parenthesis_list != []:
                    op_history[j]=make(parenthesis_list)
                    parenthesis_list.pop()
                j=0
            j+=1
        history.clear()
        display.clear()

        history.append(int_is_float(float(make(op_history))))
        display.append(int_is_float(float(make(op_history))))
        
        ans = history[-1]
        show(history[0])
    except:
        error()

def make(list_):
    try:
        j = 0
        
        while j < len(list_):
            if list_[j]== "-":
                try :
                    float(list_[j-1])
                    
                    list_[j+1] = list_[j+1]*-1
                    list_.pop(j)
                    list_.insert(j ,"+")
                    
                except : 
                    
                    list_[j+1]= list_[j+1] * -1
                    list_.pop(j)
                    
                
            j+=1

        j = 0
        try:
            while j < len(list_):
                
                if list_[j]== "sin(":

                    list_[j] = math.sin(list_[j+1])
                    list_.pop(j+1)

                    
                if list_[j]== "cos(" :

                    
                    list_[j] = math.cos(list_[j+1])
                    list_.pop(j+1)
                    

                if list_[j]== "tan(":
                    
                    
                    list_[j] = math.tan(list_[j+1])
                    list_.pop(j+1)
                    

                if list_[j]== "^":
                    
                    list_[j] = list_[j-1]**list_[j+1]
                    list_.pop(j+1)
                    list_.pop(j-1)

                if list_[j]== "√":
                    list_[j] = math.sqrt(float(list_[j+1]))
                    list_.pop(j+1)
                    list_.pop(j-1)

                if list_[j]== "!":

                    list_[j] = math.factorial(list_[j-1])
                    list_.pop(j-1)

                j+=1
        except:
            pass

        j = 0
        while j < len(list_):
            if list_[j] == "*":

                num1 = float(list_[j-1])
                num2 = float(list_[j+1])
                
                num3 = num1 * num2
                list_.pop(j-1)
                list_.pop(j-1)
                list_.pop(j-1)
                
                list_.insert(j-1,num3)

                j= j-1
            if list_[j] == "/":
                
                num1 = float(list_[j-1])
                num2 = float(list_[j+1])
                num3 = num1 / num2
                list_.pop(j-1)
                list_.pop(j-1)
                list_.pop(j-1)
                
                list_.insert(j-1,num3)

                j= j-1
            j+=1
        
        j=0
        
        while j < len(list_):
            
            if list_[j] == "+":
                
                num1 = float(list_[j-1])
                num2 = float(list_[j+1])
                num3 = num1 + num2
                list_.pop(j-1)
                list_.pop(j-1)
                list_.pop(j-1)
                
                list_.insert(j-1,num3)
                j= j-1
            j+=1
        
        list_= str(list_[0])
        return "".join(list_)
    except:
        error()



def functions():
    global activation_menu
    button_menu = Button(master = frame, text="menu", padx=12 ,pady=14, relief = FLAT, bg = "#e8e8e8", borderwidth = 0, command=lambda:menu()).grid(row=0,column=0)

    button_prnt0= Button(master = frame, text="(",padx=26,pady=14, relief = FLAT, bg = "#e8e8e8", borderwidth = 0, command=lambda:prnt("(")).grid(row=0,column=1,)
    
    button_prnt1= Button(master = frame, text=")",padx=26,pady=14, relief = FLAT, bg = "#e8e8e8", borderwidth = 0, command=lambda:prnt(")")).grid(row=0,column=2,)

    button_back = Button(master = frame, text="C",padx=24,pady=14, relief = FLAT,  bg = "#e8e8e8", borderwidth = 0, command=lambda:back()).grid(row=0,column=3,)

    button_clear = Button(master = frame, text="<-",padx=18,pady=14, relief = FLAT, bg = "#e8e8e8", borderwidth = 0, fg = "blue", command=lambda:clear()).grid(row=0,column=4,columnspan=2)   


    button_divide = Button(master = frame1, text=":",padx=22,pady=13, relief = FLAT, bg = "#e8e8e8", borderwidth = 0, command=lambda:divide()).grid(row=0,column=0)

    button_multiply = Button(master = frame1, text="x",padx=23,pady=13, relief = FLAT, bg = "#e8e8e8", borderwidth = 0, command=lambda:multiply()).grid(row=1,column=0)

    button_minus = Button(master = frame1, text="-",padx=23,pady=13, relief = FLAT, bg = "#e8e8e8", borderwidth = 0, command=lambda:minus()).grid(row=2,column=0)

    button_plus = Button(master = frame1, text="+",padx=21,pady=13, relief = FLAT, bg = "#e8e8e8", borderwidth = 0, command=lambda:plus()).grid(row=3,column=0)

    button_equals = Button(master = frame1, text="=",padx=21,pady=14, relief = FLAT, bg = "#e8e8e8", borderwidth = 0, fg = "blue", command=lambda:equals()).grid(row=4,column=0)


    button_9 = Button(root, text="9",padx=32,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:add(9)).grid(row=3,column=2)

    button_8 = Button(root, text="8",padx=32,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:add(8)).grid(row=3,column=1)

    button_7 = Button(root, text="7",padx=32,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:add(7)).grid(row=3,column=0)


    button_6 = Button(root, text="6",padx=32,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:add(6)).grid(row=4,column=2)

    button_5 = Button(root, text="5",padx=32,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:add(5)).grid(row=4,column=1)

    button_4 = Button(root, text="4",padx=32,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:add(4)).grid(row=4,column=0)


    button_3 = Button(root, text="3",padx=32,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:add(3)).grid(row=5,column=2)

    button_2 = Button(root, text="2",padx=32,pady=16, font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:add(2)).grid(row=5,column=1)

    button_1 = Button(root, text="1",padx = 32,pady=16, font=( 14),  bg = "#ffffff", borderwidth = 0, command=lambda:add(1)).grid(row=5,column=0)


    button_negativity = Button(root, text="+/-",padx=29,pady=19, relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:negative()).grid(padx=(0, 0),row=6,column=2)

    button_doth = Button(root, text=" , ",padx=33,pady=19, relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:doth()).grid(padx=(0, 0),row=6,column=1)

    button_0 = Button(root, text="0",padx=32,pady=16,font=( 14), relief = FLAT,  bg = "#ffffff", borderwidth = 0, command=lambda:add(0)).grid(row=6,column=0)
    activation_menu = False

functions()



root.mainloop()
 