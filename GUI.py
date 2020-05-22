from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import time

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.output(7, GPIO.LOW)
GPIO.output(11, GPIO.LOW)
GPIO.output(15, GPIO.LOW)

RedLed = LED(7)
GreenLed = LED(11)
BlueLed = LED(15)
win = Tk()
win.title("LED Selector")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12)

def Led1():
    if RedLed.is_lit:
        GPIO.output(7, GPIO.LOW)
        RedLed.off()
        ledButton["text"] = "Turn RedLed ON"
    else:
        RedLed.on()
        GreenLed.off()
        BlueLed.off()
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        ledButton["text"] = "Turn RedLed OFF"
        ledButton1["text"] = "Turn GreenLed ON"
        ledButton2["text"] = "Turn BlueLed ON"
def Led2():
    if GreenLed.is_lit:
        GreenLed.off()
        GPIO.output(11, GPIO.LOW)
        ledButton1["text"] = "Turn GreenLed ON"
    else:
        GreenLed.on()
        RedLed.off()
        BlueLed.off()
        GPIO.output(7, GPIO.LOW)
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        ledButton1["text"] = "Turn GreenLed OFF"
        ledButton["text"] = "Turn RedLed ON"
        ledButton2["text"] = "Turn BlueLed ON"
def Led3():
    if BlueLed.is_lit:
        BlueLed.off()
        GPIO.output(15, GPIO.LOW)
        ledButton2["text"] = "Turn BlueLed ON"
    else:
        BlueLed.on()
        RedLed.off()
        GreenLed.off()
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(7, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        ledButton2["text"] = "Turn BlueLed OFF"
        ledButton["text"] = "Turn RedLed ON"
        ledButton1["text"] = "Turn BlueLed ON"
def Quit():
    GPIO.cleanup()
    win.destroy()
    
ledButton = Button(win, text = 'Turn RedLed ON', font = myFont, command = Led1, bg = 'bisque2', height = 1, width = 50)
ledButton.grid(row=0, column=1)
ledButton1 = Button(win, text = 'Turn GreenLed ON', font = myFont, command = Led2, bg = 'bisque2', height = 1, width = 50)
ledButton1.grid(row=1, column=1)
ledButton2 = Button(win, text = 'Turn BlueLed ON', font = myFont, command = Led3, bg = 'bisque2', height = 1, width = 50)
ledButton2.grid(row=2, column=1)
QuitButton = Button(win, text = 'Quit', font = myFont, command = Quit, bg = 'bisque2', height = 1, width = 50)
QuitButton.grid(row=3, column=1)
