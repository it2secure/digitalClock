from tkinter import *   
import time             
def display_time():  
    hour = str(time.strftime("%H"))  
    minute = str(time.strftime("%M"))  
    second = str(time.strftime("%S"))  
    if int(hour) >= 12 and int(hour) < 24 and int (minute) >= 0:  
        meridiem_label.config(text = "PM")  
    else:  
        meridiem_label.config(text = "AM")  
    if int(hour) > 12:  
        hour = str((int(hour) - 12))  
    elif int(hour) == 0:  
        hour = str(12)  
    hour_label.config(text = hour)  
    minute_label.config(text = minute)  
    second_label.config(text = second)  
    hour_label.after(200, display_time)  
if __name__ == "__main__":  
    gui_root = Tk()  
    gui_root.title("Digital Clock")  
    gui_root.geometry("650x250+650+250")  
    gui_root.resizable(0, 0)  
    gui_root.config(bg = "#2C3C3F")  
    header_frame = Frame(gui_root, bg = "#2C3C3F")  
    body_frame = Frame(gui_root, bg = "#2C3C3F")  
    header_frame.pack(pady = 15)  
    body_frame.pack()  
    header_label = Label(  
        header_frame,  
        text = "Digital Clock",  
        font = ("consolas", "14", "bold"),  
        bg = "#2C3C3F",  
        fg = "#CAF6FF"  
        )  
    header_label.pack()  
    hour_label = Label(  
        body_frame,  
        text = "00",  
        font = ("radioland", "48"),  
        bg = "#2C3C3F",  
        fg = "#00D2FF"  
        )  
    colon_label_one = Label(  
        body_frame,  
        text = ":",  
        font = ("radioland", "48"),  
        bg = "#2C3C3F",  
        fg = "#00D2FF"  
        )  
    minute_label = Label(  
        body_frame,  
        text = "00",  
        font = ("radioland", "48"),  
        bg = "#2C3C3F",  
        fg = "#00D2FF"  
        )  
    colon_label_two = Label(  
        body_frame,  
        text = ":",  
        font = ("radioland", "48"),  
        bg = "#2C3C3F",  
        fg = "#00D2FF"  
        )  
    second_label = Label(  
        body_frame,  
        text = "00",  
        font = ("radioland", "48"),  
        bg = "#2C3C3F",  
        fg = "#00D2FF"  
        )  
    meridiem_label = Label(  
        body_frame,  
        text = "AM",  
        font = ("radioland", "48"),  
        bg = "#2C3C3F",  
        fg = "#00D2FF"  
        )  
    hour_label.grid(row = 0, column = 0, padx = 5, pady = 5)  
    colon_label_one.grid(row = 0, column = 1, padx = 5, pady = 5)  
    minute_label.grid(row = 0, column = 2, padx = 5, pady = 5)  
    colon_label_two.grid(row = 0, column = 3, padx = 5, pady = 5)  
    second_label.grid(row = 0, column = 4, padx = 5, pady = 5)  
    meridiem_label.grid(row = 0, column = 5, padx = 5, pady = 5)  
    display_time()  
    gui_root.mainloop()  