
from tkinter import *
from tkinter import messagebox
import datetime as dt
from dateutil.relativedelta import relativedelta

WINDOW_BG = 'white'   #'#FFF8D6'
INPUT_BG = '#F7E1AE'
OUTPUT_BG = '#A4D0A4'
FONT_COLOUR = '#617A55'
LABEL_FONT = ('Verdana', 12, 'bold')
OUTPUT_FONT = ('Verdana', 38, 'bold')


def validate_input(input, value):
    if value == '':
        messagebox.showerror(message=f'Your birth {input} is empty.')
    elif input == 'day' and int(value) not in range(1, 32):
        messagebox.showerror(message='Your birth day seems to be wrong.')
    elif input == 'month' and int(value) not in range(1, 13):
        messagebox.showerror(message='Your birth month seems to be wrong.')
    elif (input == 'year' and len(value) != 4) or (input == 'year' and int(value) not in (range(1900, (dt.datetime.now().year + 1)))):
        messagebox.showerror(message='Your birth year seems to be wrong.')
    else:
        return int(value)


def calculate_age():
    birth_day = validate_input('day', day_entry.get())
    birth_month = validate_input('month', month_entry.get())
    birth_year = validate_input('year', year_entry.get())

    birth_date = dt.datetime(birth_year, birth_month, birth_day)
    current_date = dt.datetime.now()

    delta = relativedelta(current_date, birth_date)

    years_canvas.itemconfig(years_output, text=delta.years)
    months_canvas.itemconfig(months_output, text=delta.months)
    days_canvas.itemconfig(days_output, text=delta.days)


window = Tk()
window.title("Age Calculator")
window.config(padx=50, pady=50, bg=WINDOW_BG)

# User input elements

input_canvas = Canvas(width=200, height=300, bg=INPUT_BG, highlightthickness=0)
input_canvas.grid(row=0, rowspan=3, column=0, columnspan=2 )

day_label = Label(text='DAY', font=LABEL_FONT, bg=INPUT_BG, fg=FONT_COLOUR)
day_label.grid(row=0, column=0, sticky=(S, E))
day_entry = Entry(width=8, bg=WINDOW_BG, fg=FONT_COLOUR, highlightthickness=0)
day_entry.focus()
day_entry.grid(row=0, column=1, padx=(0,20), sticky=(S))

month_label = Label(text='MONTH', font=LABEL_FONT, bg=INPUT_BG, fg=FONT_COLOUR)
month_label.grid(row=1, column=0, sticky=(E))
month_entry = Entry(width=8, bg=WINDOW_BG, fg=FONT_COLOUR, highlightthickness=0)
month_entry.grid(row=1, column=1, padx=(0,20))

year_label = Label(text='YEAR', font=LABEL_FONT, bg=INPUT_BG, fg=FONT_COLOUR)
year_label.grid(row=2, column=0, sticky=(N, E))
year_entry = Entry(width=8, bg=WINDOW_BG, fg=FONT_COLOUR, highlightthickness=0)
year_entry.grid(row=2, column=1, padx=(0,20), sticky=(N))

btn = Button(text="Calculate Age", command=calculate_age)
img = PhotoImage(file='double_arrow.png')
btn.config(image=img, bg=WINDOW_BG, highlightthickness=0)
btn.grid(row=1, column=2, padx=(20,0))

# Age output elements

years_canvas = Canvas(width=100, height=100, bg=WINDOW_BG, highlightthickness=0)
years_canvas.create_oval(0, 0, 96, 96, fill=OUTPUT_BG, outline=OUTPUT_BG)
years_output = years_canvas.create_text(48, 48, text='', font=OUTPUT_FONT)
years_canvas.grid(row=0, column=3, padx=(20, 0))
years_label = Label(text='YEARS', bg=WINDOW_BG, fg=FONT_COLOUR, font=OUTPUT_FONT)
years_label.grid(row=0, column=4, padx=(20, 0))

months_canvas = Canvas(width=100, height=100, bg=WINDOW_BG, highlightthickness=0)
months_canvas.create_oval(0, 0, 95, 95, fill=OUTPUT_BG, outline=OUTPUT_BG)
months_output = months_canvas.create_text(48, 48, text='', font=OUTPUT_FONT)
months_canvas.grid(row=1, column=3, padx=(20, 0))
months_label = Label(text='MONTHS', bg=WINDOW_BG, fg=FONT_COLOUR, font=OUTPUT_FONT)
months_label.grid(row=1, column=4, padx=(20, 0))

days_canvas = Canvas(width=100, height=100, bg=WINDOW_BG, highlightthickness=0)
days_canvas.create_oval(0, 0, 95, 95, fill=OUTPUT_BG, outline=OUTPUT_BG)
days_output = days_canvas.create_text(48, 48, text='', font=OUTPUT_FONT)
days_canvas.grid(row=2, column=3, padx=(20, 0))
days_label = Label(text='DAYS', bg=WINDOW_BG, fg=FONT_COLOUR, font=OUTPUT_FONT)
days_label.grid(row=2, column=4, padx=(20, 0))

window.mainloop()