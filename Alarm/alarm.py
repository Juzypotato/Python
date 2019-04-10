from tkinter import *
from threading import Thread
import simpleaudio as sa
import datetime
import os


def play(filename):
    sound = sa.WaveObject.from_wave_file(filename)
    play = sound.play()
    play.wait_done()


def wait(then_time, filename):
    while True:
        now_time = datetime.datetime.now().strftime("%H:%M")
        if now_time == then_time:
            play(filename)


def thread_wait():
    print("Thread created")
    then_time = time.get()
    filename = file.get()
    wait(then_time, filename)


def clicked():
    thread = Thread(target=thread_wait)
    thread.start()
    lb4 = Label(window, text="Just wait")
    lb4.pack()


def stop():
    os.system("taskkill /F /IM gui.exe /T")


if __name__ == '__main__':
    window = Tk()
    window.title("Im your GRAPHICAL alarm")
    window.geometry('400x160')
    lb1 = Label(window, text="Hello, please choose a filename and time")
    lb1.pack()
    lb2 = Label(window, text="Filename      Included file: Sample.wav")
    lb2.pack()
    file = Entry(window, width=15)
    file.pack()
    lb3 = Label(window, text="Time      Format: HH:MM")
    lb3.pack()
    time = Entry(window, width=15)
    time.pack()
    btn_start = Button(window, text="Start alarm", command=clicked)
    btn_start.pack()
    btn_stop = Button(window, text="Stop alarm", command=stop)
    btn_stop.pack()
    window.mainloop()
