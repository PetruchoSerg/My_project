from logging import setLogRecordFactory
from tkinter import *
import time

root = Tk()
root.title('Ремзона - расчет')
root['bg'] = 'pink'


def timing():
    current_time = time.strftime('%d - %m - %Y г.   %H : %M : %S')
    lb_time.config(text=current_time)
    lb_time.after(200, timing)

lb_time = Label(font=('Arial',20,'bold'), 
                bg='green',
                fg='white',
                height='2',
                width='10')
timing()
lb_time.grid(row=0, column=0, columnspan=6, sticky='nwse')

result = open(f"{time.strftime('%d - %m - %Y г')}.csv", "w+")
result.write(f"{time.strftime('%d - %m - %Y г')}")
result.close()




class Lift(Tk):
    def __init__(self, x, y, price, name = 'Lift', **kwargs):
        
        self.frame  = Frame( background='black', **kwargs)
        self.frame.grid(row = x, column= y, sticky='nwse', padx=5, pady=5)

        self.start = 0
        self.stop = 0
        self.id_after = 0
        self.finish_time = 0
        self.main_price = price
        self.lift_count = 0
        self.drill = 0
        self.drill_var = 0
        self.x_drill = 0
        self.grinding_machine = 0
        self.grinding_machine_var = 0
        self.x_grinding_machine = 0
        self.screwdriver = 0
        self.screwdriver_var = 0
        self.x_screwdriver = 0
        self.press = 0
        self.press_var = 0
        self.x_press = 0
        self.fan = 0
        self.fan_var = 0
        self.x_fan = 0
        self.cleaner = 0
        self.cleaner_var = 0
        self.x_cleaner = 0
        self.welding_machine_auto = 0
        self.welding_machine_auto_var = 0
        self.x_welding_machine_auto = 0
        self.polishing = 0
        self.polishing_var = 0
        self.x_polishing = 0
        self.tornador = 0
        self.tornador_var = 0
        self.x_tornador = 0
        self.welding_machine = 0
        self.welding_machine_var = 0
        self.x_welding_machine = 0
        self.time1 = 0
        self.time2 = 0
        self.main_list = ''
        
        


        
        

        
       




        def click_start():
            self.lb_start.config(text=time.strftime('%H : %M : %S'))
            self.time1 = time.strftime('%H : %M : %S')
            self.start = time.time()
            timer()
            self.bt_stop.config(stat = NORMAL)
            self.bt_start.config(stat = DISABLED)
            self.lb_main.config(bg = 'red')
            
  
        def timer():
            self.stop = time.time() 
            self.delta = int(self.stop - self.start)
            self.finish_time = time.strftime('%H : %M : %S',(time.gmtime(self.delta)))
            self.lb_finishtime.config(text=self.finish_time)
            self.id_after = self.lb_finishtime.after(300, timer)
            self.id_after

        def click_stop():
            self.lb_stop.config(text=time.strftime('%H : %M : %S'))
            self.time2 = time.strftime('%H : %M : %S')
            self.stop = time.time()
            self.delta = int(self.stop - self.start)
            self.finish_time = time.strftime('%H : %M : %S',(time.gmtime(self.delta)))
            self.lb_finishtime.after_cancel(self.id_after)
            self.lb_finishtime.config(text=self.finish_time)
            self.bt_stop.config(stat = DISABLED)
            self.bt_reset.config(stat = NORMAL)
            self.lb_main.config(bg = 'blue')
            self.check_tools = self.check_tools_var.get()
            
            counter()
            self.main_count = self.lift_count + self.drill + self.grinding_machine + self.screwdriver \
            + self.press + self.fan + self.cleaner + self.welding_machine_auto \
            + self.welding_machine # Здесь добавляем дополнительные услуги
            self.lb_main_count.config(text = f'Итого : {self.main_count} РУБ ')

            

            list()
            result = open(f"{time.strftime('%d - %m - %Y г')}.csv", "a+")
            result.write(f"\n{self.entry_main_var.get()},{self.time1},"\
                f"{self.finish_time},{self.time2},{self.main_list},{self.main_count}")
            result.close()
            
            calculation()
            

        def counter():
            self.count_hour = int(self.finish_time[:2])
            self.count_minute = int(self.finish_time[5:7])
            if self.count_minute <= 60 and self.count_hour == 0:
                self.lift_count += self.main_price
            elif self.count_hour > 0 and self.count_minute <= 10:
                self.lift_count += self.main_price * self.count_hour
            elif self.count_hour > 0 and 40 > self.count_minute > 10:
                self.lift_count += self.main_price * self.count_hour + (self.main_price / 2)
            elif self.count_hour > 0 and self.count_minute > 40:
                self.lift_count += self.main_price * (self.count_hour + 1)
            

        def reset():
            self.lb_start.config(text='-- : -- : --')
            self.lb_stop.config(text='-- : -- : --')
            self.lb_finishtime.config(text='-- : -- : --')
            self.bt_reset.config(stat = DISABLED)
            self.bt_start.config(stat = NORMAL)
            self.lb_main_count.config(text=' - - -   RUB')
            self.lift_count = 0
            self.check_tools_var.set(0)
            self.main_price = price
            self.drill = 0
            self.x_drill = 0
            self.grinding_machine = 0
            self.x_grinding_machine = 0
            self.screwdriver = 0
            self.x_screwdriver = 0
            self.press = 0
            self.x_press = 0
            self.fan = 0
            self.x_fan = 0
            self.cleaner = 0
            self.x_cleaner = 0
            self.welding_machine_auto = 0
            self.x_welding_machine_auto = 0
            self.polishing = 0
            self.x_polishing = 0
            self.tornador = 0
            self.x_tornador = 0
            self.welding_machine = 0
            self.x_welding_machine = 0
            self.entry_main.delete(0, END)
          

        def price_tools():
            self.main_price += self.check_tools_var.get() 

        

        def list():
            self.main_list = f'{name[:-3]}'
            
            if self.check_tools > 0:
                self.main_list += 'Инструмент '
            if self.drill == 50:
                self.main_list += 'Дрель '
            if self.grinding_machine == 50:
                self.main_list += 'Болгарка '
            if self.screwdriver == 100:
                self.main_list += 'Шуруповерт '
            if self.press == 150:
                self.main_list += 'Пресс '
            if self.fan == 150:
                self.main_list += 'Фен ' 
            if self.cleaner == 150:
                self.main_list += 'Пылесос '
            if self.welding_machine == 200:
                self.main_list += 'Сварка Инв. '
            if self.welding_machine_auto > 0:
                self.main_list += f'Сварка п\а ({self.welding_machine_auto}) '
            if self.polishing > 0:
                self.main_list += 'Полировка '
            if self.tornador  > 0:
                self.main_list += 'Торнадор '
            
             
        def calculation():
            self.win2 = Toplevel()
            self.win2.title(f'{self.entry_main_var.get()}  {name}')
            self.frame_calculation = Frame(self.win2, bg='red')
            self.frame_calculation.grid(row=0, column=0, columnspan=4, rowspan=2, sticky='nwse')

            self.lb_pay = Label(self.frame_calculation, font=('Arial',12,'bold'),           
                bg='blue',
                fg='white',
                height='4',
                width='60',
                text=f'Сумма : {self.main_count} РУБ \n Время : {self.finish_time} \n {self.main_list}')
            self.lb_pay.grid(row=0, column=0, columnspan=2, sticky='nwes')

        
             
             


        def options():
            self.win = Toplevel()
            self.win.title(f'{self.entry_main_var.get()}  {name}')
            self.win.grab_set()
            self.frame_options = Frame(self.win, bg='red')
            self.frame_options.grid(row=0, column=0, columnspan=6, rowspan=2, sticky='nwse')

            
            def price_drill(): 
                self.drill = 0
                self.drill += self.drill_var.get()

            def price_grinding_machine():
                self.grinding_machine = 0
                self.grinding_machine += self.grinding_machine_var.get()

            def price_screwdriver():
                self.screwdriver = 0
                self.screwdriver += self.screwdriver_var.get()

            def price_press(): 
                self.press = 0
                self.press += self.press_var.get()

            def price_fan(): 
                self.fan = 0
                self.fan += self.fan_var.get()

            def price_cleaner(): 
                self.cleaner = 0
                self.cleaner += self.cleaner_var.get()

            def price_welding_machine_auto(*args):
                self.welding_machine_auto = 0
                self.welding_machine_auto += self.welding_machine_auto_var.get()

            def price_polishing():
                self.polishing = 0
                self.polishing += self.polishing_var.get()
                self.main_price += self.polishing

            def price_tornador():
                self.tornador = 0
                self.tornador += self.tornador_var.get()
                self.main_price += self.tornador

            def price_welding_machine():
                self.welding_machine = 0
                self.welding_machine += self.welding_machine_var.get()



            
        
                

            def launch():
                self.drill_var.set(self.x_drill)
                self.grinding_machine_var.set(self.x_grinding_machine)
                self.screwdriver_var.set(self.x_screwdriver)
                self.press_var.set(self.x_press)
                self.fan_var.set(self.x_fan)
                self.cleaner_var.set(self.x_cleaner)
                self.welding_machine_auto_var.set(self.x_welding_machine_auto)
                self.polishing_var.set(self.x_polishing)
                self.tornador_var.set(self.x_tornador)
                self.welding_machine_var.set(self.x_welding_machine)

                

            def memory():
                self.x_drill = self.drill_var.get()
                self.x_grinding_machine = self.grinding_machine_var.get()
                self.x_screwdriver = self.screwdriver_var.get()
                self.x_press = self.press_var.get()
                self.x_fan = self.fan_var.get()
                self.x_cleaner = self.cleaner_var.get()
                self.x_welding_machine_auto = self.welding_machine_auto_var.get()
                self.x_polishing = self.polishing_var.get()
                self.x_tornador = self.tornador_var.get()
                self.x_welding_machine = self.welding_machine_var.get()
                
                self.win.destroy()

            self.win.protocol('WM_DELETE_WINDOW', memory)


            
            self.grinding_machine_var = IntVar()
            self.check_grinding_machine = Checkbutton(self.frame_options, text='Болгарка',
                        width='15',
                        height='1',
                        font=('Arial',10),
                        anchor='w',
                        command=price_grinding_machine,
                        onvalue=50,
                        offvalue=0,
                        variable=self.grinding_machine_var)
            self.check_grinding_machine.grid(row=0, column=0, sticky='nwes')


            self.drill_var = IntVar()
            self.check_drill = Checkbutton(self.frame_options, text='Дрель',
                        width='15',
                        height='1',
                        font=('Arial',10),
                        anchor='w',
                        command=price_drill,
                        onvalue=50,
                        offvalue=0,
                        variable=self.drill_var)
            self.check_drill.grid(row=0, column=1, sticky='nwes')

            self.screwdriver_var = IntVar()
            self.check_screwdriver = Checkbutton(self.frame_options, text='Шуруповерт',
                        width='15',
                        height='1',
                        font=('Arial',10),
                        anchor='w',
                        command=price_screwdriver,
                        onvalue=100,
                        offvalue=0,
                        variable=self.screwdriver_var)
            self.check_screwdriver.grid(row=1, column=0, sticky='nwes')

            self.press_var = IntVar()
            self.check_press = Checkbutton(self.frame_options, text='Пресс',
                        width='15',
                        height='1',
                        font=('Arial',10),
                        anchor='w',
                        command=price_press,
                        onvalue=150,
                        offvalue=0,
                        variable=self.press_var)
            self.check_press.grid(row=1, column=1, sticky='nwes')

            self.fan_var = IntVar()
            self.check_fan = Checkbutton(self.frame_options, text='Фен',
                        width='15',
                        height='1',
                        font=('Arial',10),
                        anchor='w',
                        command=price_fan,
                        onvalue=150,
                        offvalue=0,
                        variable=self.fan_var)
            self.check_fan.grid(row=2, column=0, sticky='nwes')
        


            self.cleaner_var = IntVar()
            self.check_cleaner = Checkbutton(self.frame_options, text='Пылесос',
                        width='15',
                        height='1',
                        font=('Arial',10),
                        anchor='w',
                        command=price_cleaner,
                        onvalue=150,
                        offvalue=0,
                        variable=self.cleaner_var)
            self.check_cleaner.grid(row=2, column=1, sticky='nwes')
            
            self.polishing_var = IntVar()
            self.check_polishing = Checkbutton(self.frame_options, text='Полировка',
                        width='15',
                        height='1',
                        font=('Arial',10),
                        anchor='w',
                        command=price_polishing,
                        onvalue=150,
                        offvalue=0,
                        variable=self.polishing_var)
            self.check_polishing.grid(row=3, column=0, sticky='nwes')

            self.tornador_var = IntVar()
            self.check_tornador = Checkbutton(self.frame_options, text='Торнадор',
                        width='15',
                        height='1',
                        font=('Arial',10),
                        anchor='w',
                        command=price_tornador,
                        onvalue=250,
                        offvalue=0,
                        variable=self.tornador_var)
            self.check_tornador.grid(row=3, column=1, sticky='nwes')

            self.lb_welding_machine_auto = Label(self.frame_options, text='Сварочный полуавтомат',
                        width='15',
                        height='1',
                        font=('Arial',10),
                        anchor= 'c')
            self.lb_welding_machine_auto .grid(row=5, column=0, columnspan=2, sticky='nwes')
            
            self.welding_machine_auto_var = IntVar()
            self.sc_welding_machine_auto = Scale(self.frame_options, from_ = 0, to = 1000,
                        resolution= 250, orient= HORIZONTAL, variable=self.welding_machine_auto_var, 
                        command= price_welding_machine_auto)
            self.sc_welding_machine_auto.grid(row=6, column=0, columnspan=2, sticky='nwes')

            self.welding_machine_var = IntVar()
            self.check_welding_machine = Checkbutton(self.frame_options, text='Сварочный инвертор',
                        width='15',
                        height='1',
                        font=('Arial',10),
                        anchor='w',
                        command=price_welding_machine,
                        onvalue=200,
                        offvalue=0,
                        variable=self.welding_machine_var)
            self.check_welding_machine.grid(row=4, column=0, columnspan=2, sticky='nwes')
            

           
            launch()


        self.lb_main = Label(self.frame, font=('Arial',12,'bold'),           
                bg='blue',
                fg='white',
                height='2',
                width='24',
                text=f'{name}')
        self.lb_main.grid(row=0, column=0, columnspan=2, sticky='nwes')

    
        self.entry_main_var = StringVar()
        self.entry_main = Entry(self.frame, bg='white', textvariable= self.entry_main_var)                        # Окно ввода 
        self.entry_main.grid(row=1, column=0, columnspan=2, sticky='nwes')

        self.check_tools_var = IntVar()
        self.check_tools = Checkbutton(self.frame, text='Инструмент',
                        width='12',
                        height='1',
                        font=('Arial',11),
                        anchor='w',
                        command=price_tools,
                        onvalue=50,
                        offvalue=0,
                        variable=self.check_tools_var
                        )
        self.check_tools.grid(row=2, column=0, columnspan=2, sticky='nwes')

        self.options = Button(self.frame, text='Опции', command=options)
        self.options.grid(row=2, column=1, sticky='nwse')

        self.lb_start = Label(self.frame, font=('Arial',12,'bold'), 
                bg='blue',
                fg='white',
                height='1',
                width='12',
                text='-- : -- : --')
        self.lb_start.grid(row=3, column=0, sticky='nwse')

        self.bt_start = Button(self.frame, text='Заезд/Старт', command=click_start)
        self.bt_start.grid(row=3, column=1, sticky='nwse')

        self.lb_finishtime = Label(self.frame, font=('Arial',12,'bold'), 
                bg='green',
                fg='white',
                height='1',
                width='12',
                text='-- : -- : --'
                )
        self.lb_finishtime.grid(row=4, column=0, sticky='nwse')

        self.bt_reset = Button(self.frame, text='Обнулить', stat=DISABLED, command=reset)
        self.bt_reset.grid(row=4, column=1, sticky='nwse')

        self.lb_stop = Label(self.frame, font=('Arial',12,'bold'), 
                bg='blue',
                fg='white',
                height='1',
                width='12',
                text='-- : -- : --')
        self.lb_stop.grid(row=5, column=0, sticky='nwse')

        self.bt_stop = Button(self.frame, text='Выезд/Стоп', stat=DISABLED, command=click_stop)
        self.bt_stop.grid(row=5, column=1, sticky='nwse')

        self.lb_main_count = Label(self.frame, font=('Arial',12,'bold'), 
                bg='green',
                fg='white',
                height='1',
                width='12',
                text=' - - -   RUB'
                )
        self.lb_main_count.grid(row=6, column=0, columnspan=2, sticky='nwse')

               

    
def LiftOne():
    lift_one = Lift(1, 0, 200, name = 'Подъемник № 1', bg = 'red')
    
def LiftTwo():
    lift_two = Lift(1, 1, 200, name = 'Подъемник № 2',bg = 'red')

def LiftThree():
    lift_three = Lift(1, 2, 200, name = 'Подъемник № 3', bg = 'red')
    
def LiftFour():
    lift_four = Lift(1, 3, 200, name = 'Подъемник № 4', bg = 'white')

def PlaceOne():
    lift_four = Lift(1, 4, 100, name = 'Место № 1')

def PlaceTwo():
    lift_four = Lift(1, 5, 100, name = 'Место № 2')

def PitOne():
    pit_one = Lift(2, 0 , 150, name = 'Яма № 1', bg = 'white')
    

def PitTwo():
    pit_two = Lift(2, 1 , 150, name = 'Яма № 2', bg = 'white')
    

def PitThree():
    pit_three = Lift(2, 2, 150, name = 'Яма № 3', bg = 'white')
    

def PitFour():
    pit_four = Lift(2, 3, 150, name = 'Яма № 4', bg = 'white')
    
def PlaceThree():
    lift_four = Lift(2, 4, 100, name = 'Место № 3')

def PlaceFour():
    lift_four = Lift(2, 5, 100, name = 'Место № 4')



LiftOne()
LiftTwo()
LiftThree()
LiftFour()
PitOne()
PitTwo()
PitThree()
PitFour()
PlaceOne()
PlaceTwo()
PlaceThree()
PlaceFour()


root.mainloop()


    

