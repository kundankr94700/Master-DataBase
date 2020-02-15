import pyttsx3 as t2s
from tkinter import *
from os import listdir,mkdir
from os.path import isfile, join
import numpy as np
import cv2,os
from tkinter import messagebox
from tkinter.font import  Font
from PIL import ImageTk, Image
import sqlite3
from tkinter.ttk import Combobox
import threading
from playsound import playsound
from time import *
from tkinter import filedialog
face_cascade = cv2.CascadeClassifier('face_cas.xml')

def Main():
    root.destroy()

    def sq():
        conn = sqlite3.connect('school_education_database.sqlite')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE if not exists Student
                                                             (Roll INT PRIMARY KEY     NOT NULL,
                                                             FIRST_NAME           TEXT    NOT NULL,
                                                             LAST_NAME           TEXT    NOT NULL,
                                                             FATHER_NAME           TEXT    NOT NULL,
                                                             MOTHER_NAME           TEXT    NOT NULL,
                                                             DATE_OF_BIRTH          DATE    NOT NULL,
                                                             COURSE           TEXT    NOT NULL,
                                                             STATE           TEXT    NOT NULL,
                                                             SEMESTER           TEXT    NOT NULL,
                                                             BATCH           DATE    NOT NULL,
                                                             MOBILE_NO           TEXT    NOT NULL,
                                                             COUNTRY          TEXT    NOT NULL,
                                                             DROP_OUT_YEAR       DATE NOT NULL,
                                                             REASON          TEXT    NOT NULL,
                                                             IMAGE varchar2(150) not null,
                                                             SIGN varchar2(150) not null,
                                                             MARKS          INT);''')

        conn.commit()
        conn.close()

        conn = sqlite3.connect('higher_education_database.sqlite')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE if not exists Student
                                                                     (Roll INT PRIMARY KEY     NOT NULL,
                                                                     FIRST_NAME           TEXT    NOT NULL,
                                                                     LAST_NAME           TEXT    NOT NULL,
                                                                     FATHER_NAME           TEXT    NOT NULL,
                                                                     MOTHER_NAME           TEXT    NOT NULL,
                                                                     DATE_OF_BIRTH          DATE    NOT NULL,
                                                                     COURSE           TEXT    NOT NULL,
                                                                     STATE           TEXT    NOT NULL,
                                                                     SEMESTER           TEXT    NOT NULL,
                                                                     BATCH           DATE   NOT NULL,
                                                                     MOBILE_NO           TEXT    NOT NULL,
                                                                     COUNTRY          TEXT    NOT NULL,
                                                                     DROP_OUT_YEAR       DATE NOT NULL,
                                                                     REASON          TEXT    NOT NULL,
                                                                     IMAGE varchar2(150) not null,
                                                                     SIGN varchar2(150) not null,
                                                                     MARKS          INT);''')

        conn.commit()
        conn.close()

        conn = sqlite3.connect('Technical_education_database.sqlite')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE if not exists Student
                                                                     (Roll INT PRIMARY KEY     NOT NULL,
                                                                     FIRST_NAME           TEXT    NOT NULL,
                                                                     LAST_NAME           TEXT    NOT NULL,
                                                                     FATHER_NAME           TEXT    NOT NULL,
                                                                     MOTHER_NAME           TEXT    NOT NULL,
                                                                     DATE_OF_BIRTH          DATE    NOT NULL,
                                                                     COURSE           TEXT    NOT NULL,
                                                                     STATE           TEXT    NOT NULL,
                                                                     SEMESTER           TEXT    NOT NULL,
                                                                     BATCH           DATE    NOT NULL,
                                                                     MOBILE_NO           TEXT    NOT NULL,
                                                                     COUNTRY          TEXT    NOT NULL,
                                                                     DROP_OUT_YEAR       DATE NOT NULL,
                                                                     REASON          TEXT    NOT NULL,
                                                                     IMAGE varchar2(150) not null,
                                                                     SIGN varchar2(150) not null,
                                                                     MARKS          INT);''')

        conn.commit()
        conn.close()

    def feed_data(database_name, cour, sem):
        def lis_box():
            conn = sqlite3.connect('%s.sqlite' % (database_name))
            cursor = conn.cursor()
            z = 0
            listNodes.delete(0, 100)
            for row in cursor.execute(
                    "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,STATE,REASON,IMAGE,SIGN,MARKS   from Student"):
                z += 1
                a11 = row[1] + " " + row[2]
                sss = str(row[0]) + ",  \t\t" + a11 + ',  \t\t' + str(row[5]) + ',  \t\t' + str(
                    row[9]) + ',  \t\t' + str(
                    row[7]) + ',  \t\t' + str(row[8]) + ',  \t\t' + str(row[10]) + ', \t\t' + str(
                    row[11]) + ', \t\t' + str(
                    row[12] + ',  \t\t' + str(row[15]))
                listNodes.insert(END, sss)
            #
            conn.commit()
            conn.close()
            LLL2 = Label(top1, text='Number Of Records : %d ' % z, font=f7, fg='green').place(
                x=670, y=400)

        top1 = Toplevel()
        top1.title("Student Database")

        f4 = Font(family="Time New Roman", size=13, weight="bold", underline=1)
        f5 = Font(family="Time New Roman", size=16, weight="bold", underline=1)
        f6 = Font(family="Time New Roman", size=14, weight="bold")
        f7 = Font(family="Time New Roman", size=12)

        LL2 = Label(top1, text='Database Management', fg='Red', font=f5).place(x=450, y=15)

        def add(roll, f_name, l_name, fa_name, ma_name, dob, course, state, sem, batch, mobile, country, drop, marks,
                reason, image, sign):
            conn = sqlite3.connect('%s.sqlite' % (database_name))
            cursor = conn.cursor()

            cursor.execute("INSERT INTO Student (Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,STATE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,REASON,IMAGE,SIGN,MARKS) \
                                 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ", (
                roll, f_name, l_name, fa_name, ma_name, dob, course, state, sem, batch, mobile, country, drop, reason,
                image, sign, marks,));
            conn.commit()
            conn.close()
            lis_box()
            clear()

        def display():

            class tt11(threading.Thread):
                def run(self):

                    t5 = Toplevel()
                    t5.geometry("800x900+400+10")

                    llll = Listbox(t5)
                    conn = sqlite3.connect('%s.sqlite' % (database_name))
                    cursor = conn.cursor()
                    l3 = Label(t5, text="Student DataBase Management System", fg='red', font=f1).place(
                        x=300, y=30)
                    lis1 = []
                    lis2 = []
                    for row in cursor.execute(
                            "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,STATE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,REASON,MARKS from Student"):
                        lis1.append(str(row[0]))
                        lis2.append(row[1] + ' ' + row[2])

                    conn.commit()
                    conn.close()

                    def dis1():
                        y15 = int(x15.get())
                        conn = sqlite3.connect('%s.sqlite' % (database_name))
                        cursor = conn.cursor()

                        for row in cursor.execute(
                                "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,STATE,REASON,IMAGE,SIGN,MARKS from Student where Roll=?",
                                (y15,)):
                            a2 = row[1] + ' ' + row[2]
                            LL3 = Label(t5, text='Name \t\t: %s' % a2, font=f6, fg='Skyblue').place(
                                x=240, y=180)
                            LL5 = Label(t5, text='Father\'s Name        :%s                         ' % row[3], font=f6,
                                        fg='Skyblue').place(x=240, y=220)
                            LL6 = Label(t5, text='Mother\'s Name       :%s                          ' % row[4], font=f6,
                                        fg='Skyblue').place(x=240, y=260)
                            LL7 = Label(t5, text='Date of Birth \t: %s                              ' % row[5], font=f6,
                                        fg='Skyblue').place(x=240, y=300)

                            LL8 = Label(t5, text='Course \t\t: %s                                   ' % row[6], font=f6,
                                        fg='Skyblue').place(x=240, y=340)
                            LL9 = Label(t5, text='Semester\t: %s                                    ' % row[7], font=f6,
                                        fg='Skyblue').place(x=240, y=380)
                            LL10 = Label(t5, text='Batch \t\t:%s                                    ' % row[
                                8], font=f6, fg='Skyblue').place(x=240, y=420)
                            LL11 = Label(t5, text='Mobile \t\t: %s                                  ' % row[9], font=f6,
                                         fg='Skyblue').place(x=240, y=460)
                            LL12 = Label(t5, text='Country \t\t: %s                                 ' % row[10],
                                         font=f6,
                                         fg='Skyblue').place(x=240, y=500)
                            LL13 = Label(t5, text='DROP_OUT_YEAR \t\t: %s                                 ' % row[
                                11], font=f6, fg='Skyblue').place(x=240, y=540)
                            LL14 = Label(t5,
                                         text='RoLL  \t\t: %s                                   ' % row[
                                             0], font=f6, fg='Skyblue').place(x=240, y=570)
                            LL14 = Label(t5,
                                         text='Marks  \t\t: %s                                  ' % row[
                                             15], font=f6, fg='Skyblue').place(x=240, y=600)
                            LL14 = Label(t5,
                                         text='State  \t\t: %s                                  ' % row[
                                             12], font=f6, fg='Skyblue').place(x=240, y=630)
                            LL14 = Label(t5,
                                         text='Reason  \t\t: %s                                  ' % row[
                                             16], font=f6, fg='Skyblue').place(x=240, y=660)
                            ph = row[13]
                            si = row[14]
                            print(ph, si, row[13])
                        conn.commit()
                        conn.close()
                        ima = ('Do You Want to See Image ')
                        l = Label(t5, text=ima, font=f6).place(x=10, y=700)
                        d1 = IntVar()
                        d2 = IntVar()
                        r1 = Radiobutton(t5, text='Photo', value=1, variable=d1, font=f6).place(x=250,
                                                                                                y=740)
                        r2 = Radiobutton(t5, text='Signature', value=2, variable=d2, font=f6).place(
                            x=350, y=740)

                        def pho():
                            if d1.get() == 1 and d2.get() == 2:
                                Image.open(ph).show()
                                Image.open(si).show()
                                d1.set(0)
                                d2.set(0)
                            elif d1.get() == 1 or d2.get() == 2:
                                if d1.get() == 1:
                                    Image.open(ph).show()
                                    d1.set(0)
                                else:
                                    Image.open(si).show()
                                    d2.set(0)
                            else:
                                pass

                        BBB1 = Button(t5, text='Next', bg='Green', fg='white', width=25, font=f4,
                                      command=pho).place(x=450, y=740)

                    def dis2():
                        y16 = x16.get()
                        conn = sqlite3.connect('%s.sqlite' % (database_name))
                        cursor = conn.cursor()
                        z1, z2 = y16.split(' ')

                        for row in cursor.execute(
                                "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,ADDRESS,MARKS,IMAGE,SIGN from Student where FIRST_NAME=? and LAST_NAME= ?",
                                (z1, z2,)):
                            a2 = row[1] + ' ' + row[2]
                            LL3 = Label(t5, text='Name \t\t: %s' % a2, font=f6, fg='Skyblue').place(
                                x=240, y=180)
                            LL5 = Label(t5, text='Father\'s Name        :%s                         ' % row[3], font=f6,
                                        fg='Skyblue').place(x=240, y=220)
                            LL6 = Label(t5, text='Mother\'s Name       :%s                          ' % row[4], font=f6,
                                        fg='Skyblue').place(x=240, y=260)
                            LL7 = Label(t5, text='Date of Birth \t: %s                              ' % row[5], font=f6,
                                        fg='Skyblue').place(x=240, y=300)

                            LL8 = Label(t5, text='Course \t\t: %s                                   ' % row[6], font=f6,
                                        fg='Skyblue').place(x=240, y=340)
                            LL9 = Label(t5, text='Semester\t: %s                                    ' % row[7], font=f6,
                                        fg='Skyblue').place(x=240, y=380)
                            LL10 = Label(t5, text='Batch \t\t:%s                                    ' % row[
                                8], font=f6, fg='Skyblue').place(x=240, y=420)
                            LL11 = Label(t5, text='Mobile \t\t: %s                                  ' % row[9], font=f6,
                                         fg='Skyblue').place(x=240, y=460)
                            LL12 = Label(t5, text='Country \t\t: %s                                 ' % row[10],
                                         font=f6,
                                         fg='Skyblue').place(x=240, y=500)
                            LL13 = Label(t5, text='DROP_OUT_YEAR \t\t: %s                                 ' % row[
                                11], font=f6, fg='Skyblue').place(x=240, y=540)
                            LL14 = Label(t5,
                                         text='RoLL  \t\t: %s                                   ' % row[
                                             0], font=f6, fg='Skyblue').place(x=240, y=570)
                            LL14 = Label(t5,
                                         text='Marks  \t\t: %s                                  ' % row[
                                             15], font=f6, fg='Skyblue').place(x=240, y=600)
                            LL14 = Label(t5,
                                         text='State  \t\t: %s                                  ' % row[
                                             12], font=f6, fg='Skyblue').place(x=240, y=630)
                            LL14 = Label(t5,
                                         text='Reason  \t\t: %s                                  ' % row[
                                             16], font=f6, fg='Skyblue').place(x=240, y=660)
                            ph = row[13]
                            si = row[14]
                        conn.commit()
                        conn.close()
                        ima = ('Do You Want to See Image ')
                        l = Label(t5, text=ima, font=f6).place(x=140, y=740)
                        d1 = IntVar()
                        d2 = IntVar()
                        r1 = Radiobutton(t5, text='Photo', value=1, variable=d1, font=f6).place(x=250,
                                                                                                y=740)
                        r2 = Radiobutton(t5, text='Signature', value=2, variable=d2, font=f6).place(
                            x=350, y=740)

                        def pho():
                            if d1.get() == 1 and d2.get() == 2:
                                Image.open(ph).show()
                                Image.open(si).show()
                                d1.set(0)
                                d2.set(0)
                            elif d1.get() == 1 or d2.get() == 2:
                                if d1.get() == 1:
                                    Image.open(ph).show()
                                    d1.set(0)
                                else:
                                    Image.open(si).show()
                                    d2.set(0)
                            else:
                                pass

                        BBB1 = Button(t5, text='Next', bg='Green', fg='white', width=25, font=f4,
                                      command=pho).place(x=450, y=740)

                    x15 = StringVar()
                    x16 = StringVar()
                    x17 = StringVar()
                    c6 = Combobox(t5, values=lis1, width=18, textvariable=x15).place(x=280, y=80)
                    x15.set('Select Roll Number ')
                    c7 = Combobox(t5, values=lis2, width=18, textvariable=x16).place(x=280, y=120)
                    x16.set('Select Name ')

                    b1 = Button(t5, text='Display', command=dis1, width=30, height=1, bg='green', fg='white',
                                font=f3).place(x=480, y=80)
                    b3 = Button(t5, text='Display', command=dis2, width=30, height=1, font=f3).place(x=480, y=120)

            class tt12(threading.Thread):
                def run(self):
                    playsound('C:\\Users\\Kundan Kumar\\PycharmProjects\\Python\\Audio\\disp.mp3')

            ttt11 = tt11()
            ttt12 = tt12()
            ttt11.start()
            sleep(0.05)
            ttt12.start()

        def search(pp):
            conn = sqlite3.connect('%s.sqlite' % (database_name))
            cursor = conn.cursor()
            z, y = 0, 0
            for row in cursor.execute(
                    "SELECT Roll from Student"):
                if pp == row[0]:
                    y = 1

            conn.commit()
            conn.close()
            if y == 1:

                conn = sqlite3.connect('%s.sqlite' % (database_name))
                cursor = conn.cursor()
                top4 = Toplevel()
                top4.title("Display Record")
                top4.geometry("800x900+400+10")
                l3 = Label(top4, text="DataBase Management System", fg='red', font=f1).place(x=120, y=30)
                for row in cursor.execute(
                        "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,STATE,REASON,IMAGE,SIGN,MARKS from Student where Roll=?",
                        (pp,)):
                    a2 = row[1] + ' ' + row[2]
                    LL3 = Label(top4, text='Name \t\t: %s' % a2, font=f6, fg='Skyblue').place(
                        x=240, y=180)
                    LL5 = Label(top4, text='Father\'s Name        :%s                         ' % row[3], font=f6,
                                fg='Skyblue').place(x=240, y=220)
                    LL6 = Label(top4, text='Mother\'s Name       :%s                          ' % row[4], font=f6,
                                fg='Skyblue').place(x=240, y=260)
                    LL7 = Label(top4, text='Date of Birth \t: %s                              ' % row[5], font=f6,
                                fg='Skyblue').place(x=240, y=300)

                    LL8 = Label(top4, text='Course \t\t: %s                                   ' % row[6], font=f6,
                                fg='Skyblue').place(x=240, y=340)
                    LL9 = Label(top4, text='Semester\t: %s                                    ' % row[7], font=f6,
                                fg='Skyblue').place(x=240, y=380)
                    LL10 = Label(top4, text='Batch \t\t:%s                                    ' % row[
                        8], font=f6, fg='Skyblue').place(x=240, y=420)
                    LL11 = Label(top4, text='Mobile \t\t: %s                                  ' % row[9], font=f6,
                                 fg='Skyblue').place(x=240, y=460)
                    LL12 = Label(top4, text='Country \t\t: %s                                 ' % row[10], font=f6,
                                 fg='Skyblue').place(x=240, y=500)
                    LL13 = Label(top4, text='DROP_OUT_YEAR \t\t: %s                                 ' % row[
                        11], font=f6, fg='Skyblue').place(x=240, y=540)
                    LL14 = Label(top4,
                                 text='RoLL  \t\t: %s                                   ' % row[
                                     0], font=f6, fg='Skyblue').place(x=240, y=570)
                    LL14 = Label(top4,
                                 text='Marks  \t\t: %s                                  ' % row[15], font=f6,
                                 fg='Skyblue').place(x=240, y=600)
                    LL14 = Label(top4,
                                 text='State  \t\t: %s                                  ' % row[
                                     12], font=f6, fg='Skyblue').place(x=240, y=630)
                    LL14 = Label(top4,
                                 text='Reason  \t\t: %s                                  ' % row[
                                     16], font=f6, fg='Skyblue').place(x=240, y=660)
                    ph = row[13]
                    si = row[14]
                conn.commit()
                conn.close()
                ima = ('Do You Want to See Image ')
                l = Label(top4, text=ima, font=f6).place(x=20, y=740)
                d1 = IntVar()
                d2 = IntVar()
                r1 = Radiobutton(top4, text='Photo', value=1, variable=d1, font=f6).place(x=300, y=740)
                r2 = Radiobutton(top4, text='Signature', value=2, variable=d2, font=f6).place(x=400,
                                                                                              y=740)

                def pho():
                    if d1.get() == 1 and d2.get() == 2:
                        Image.open(ph).show()
                        Image.open(si).show()
                        d1.set(0)
                        d2.set(0)
                    elif d1.get() == 1 or d2.get() == 2:
                        if d1.get() == 1:
                            Image.open(ph).show()
                            d1.set(0)
                        else:
                            Image.open(si).show()
                            d2.set(0)
                    else:
                        pass

                BBB1 = Button(top4, text='Next', bg='Green', fg='white', width=15, font=f4,
                              command=pho).place(x=500, y=740)

            else:
                top8 = Toplevel()
                top8.title("Display Record")
                top8.geometry("350x50+600+300")
                l = Label(top8, text='Record Not Found', font=f6, fg='red').pack()
                playsound('C:\\Users\\Kundan Kumar\\PycharmProjects\\New\\Audio\\record1.mp3')

        def updateM(j, i):

            conn = sqlite3.connect('%s.sqlite' % (database_name))
            conn.execute("UPDATE Student set SIGN = ? where ROLL = ?", (i, j))
            conn.commit()
            lis_box()

        def updateA(j, i):
            conn = sqlite3.connect('%s.sqlite' % (database_name))
            conn.execute("UPDATE Student set ADDRESS = ? where ROLL = ?", (i, j))
            conn.commit()

            lis_box()

        def updateP(j, i):
            conn = sqlite3.connect('%s.sqlite' % (database_name))
            conn.execute("UPDATE Student set MOBILE_NO = ? where ROLL = ?", (i, j))
            conn.commit()
            lis_box()

        def delete(k):
            conn = sqlite3.connect('%s.sqlite' % (database_name))
            cursor = conn.cursor()
            z, y = 0, 0
            for row in cursor.execute(
                    "SELECT Roll from Student"):
                if k == row[0]:
                    y = 1

                z += 1
            conn.commit()
            conn.close()
            if y == 1:
                conn = sqlite3.connect('%s.sqlite' % (database_name))
                conn.execute("DELETE from  Student where ROLL =?", (k,))
                conn.commit()
                lis_box()

            else:
                top8 = Toplevel()
                top8.title("Display Record")
                top8.geometry("350x50+600+300")
                l = Label(top8, text='Record Not Found', font=f6, fg='red').pack()
                playsound('C:\\Users\\Kundan Kumar\\PycharmProjects\\Python\\Audio\\record1.mp3')

        def add_record():
            yy1 = xx1.get()
            yy2 = xx2.get()
            yy3 = xx3.get()
            yy4 = xx4.get()
            yy5 = xx5.get()
            yy6 = xx6.get()
            yy7 = xx7.get()
            yy8 = xx8.get()
            yy9 = xx9.get()
            yy10 = xx10.get()
            yy11 = xx11.get()
            yy12 = xx12.get()
            yy13 = xx13.get()
            yy14 = xx14.get()
            yy15 = xx15.get()
            yy16 = xx177.get()
            yy17 = xx178.get()

            l11 = 'ABCDEFGHIJKLMNOPQRSTUVWXYQ '
            l12 = list(l11)

            def valid(qq):
                for i in qq:
                    if i not in l12:
                        return 1

            if yy1 == '' or yy2 == '' or yy3 == '' or yy4 == '' or yy5 == '' or yy6 == '' or yy7 == '' or yy8 == '' or yy9 == '' or yy10 == '' or yy11 == '' or yy12 == '' or yy13 == '' or yy14 == '' or yy15 == '':
                if yy14 == '' or yy15 == '':
                    top11 = Toplevel()
                    top11.title("ADD  Record")
                    top11.geometry("320x80+600+200")
                    l3 = Label(top11, text="Please Upload Photos And Signature Both .",
                               fg='skyblue', font=f1).place(x=50, y=15)
                    playsound('C:\\Users\\Kundan Kumar\\PycharmProjects\\Python\\Audio\\add11.mp3')
                else:

                    top11 = Toplevel()
                    top11.title("ADD  Record")
                    top11.geometry("320x80+600+200")
                    l3 = Label(top11,
                               text="Some Details are Not Entered \n please Fill all the details",
                               fg='skyblue', font=f1).place(x=50, y=15)
                    playsound('C:\\Users\\Kundan Kumar\\PycharmProjects\\Python\\Audio\\add1.mp3')


            elif yy9.isdigit() == FALSE or len(yy9) != 10 or yy12.isdigit() == False or yy13.isdigit() == False:
                if (yy9.isdigit() == FALSE or len(yy9) != 10) and (yy12.isdigit() == False):
                    top11 = Toplevel()
                    top11.title("ADD  Record")
                    top11.geometry("320x80+600+200")
                    l3 = Label(top11, text="Invalid ROll and Mobile Number.", fg='skyblue',
                               font=f1).place(x=50, y=15)
                    playsound('C:\\Users\\Kundan Kumar\\PycharmProjects\\Python\\Audio\\add2.mp3')


                elif yy12.isdigit() == False:
                    top11 = Toplevel()
                    top11.title("ADD  Record")
                    top11.geometry("320x80+600+200")
                    l3 = Label(top11, text="Invalid Roll Number.", fg='skyblue',
                               font=f1).place(x=80, y=25)
                    playsound('C:\\Users\\Kundan Kumar\\PycharmProjects\\Python\\Audio\\add3.mp3')

                elif yy13.isdigit() == False:
                    top11 = Toplevel()
                    top11.title("ADD  Record")
                    top11.geometry("320x80+600+200")
                    l3 = Label(top11, text=" Invalid Marks", fg='skyblue',
                               font=f1).place(x=80, y=25)
                    playsound('C:\\Users\\Kundan Kumar\\PycharmProjects\\Python\\Audio\\add9.mp3')

                else:
                    top11 = Toplevel()
                    top11.title("ADD  Record")
                    top11.geometry("320x80+600+200")
                    l3 = Label(top11, text="Invalid  Mobile Number.", fg='skyblue',
                               font=f1).place(x=80, y=25)
                    playsound('C:\\Users\\Kundan Kumar\\PycharmProjects\\Python\\Audio\\add4.mp3')

            elif yy1.isalpha() == False or yy2.isalpha() == False or valid(yy3.upper()) == 1 or valid(yy4.upper()) == 1:
                top11 = Toplevel()
                top11.title("ADD  Record")
                top11.geometry("400x80+600+200")
                l3 = Label(top11,
                           text="Some Details are Not in Appropriate Format ",
                           fg='skyblue', font=f1).place(x=50, y=15)
                playsound('C:\\Users\\Kundan Kumar\\PycharmProjects\\Python\\Audio\\add8.mp3')

            else:
                yyx12 = int(yy12)
                yy13 = int(yy13)
                if (yy13) > 100:
                    top11 = Toplevel()
                    top11.title("ADD  Record")
                    top11.geometry("320x80+600+200")
                    l3 = Label(top11, text=" Marks Greater Then 100 .", fg='skyblue',
                               font=f1).place(x=80, y=25)
                    playsound('C:\\Users\\Kundan Kumar\\PycharmProjects\\Python\\Audio\\add10.mp3')
                else:
                    v = 1
                    conn = sqlite3.connect('%s.sqlite' % (database_name))
                    cursor = conn.cursor()
                    for row in cursor.execute("SELECT Roll from Student "):
                        zz = row[0]
                        if zz == yyx12:
                            top11 = Toplevel()
                            top11.title("ADD  Record")
                            top11.geometry("400x80+600+200")
                            l3 = Label(top11, text="Record Already Exist.", fg='skyblue',
                                       font=f1).place(x=120, y=25)
                            v = 10

                            break

                    conn.commit()
                    conn.close()
                    if v == 1:
                        add(yyx12, yy1, yy2, yy3, yy4, yy5, yy6, yy16, yy7, yy8, yy9, yy10, yy11, yy17, yy14, yy15,
                            yy13)
                        conn = sqlite3.connect('%s.sqlite' % (database_name))
                        cursor = conn.cursor()
                        z = 0
                        for row in cursor.execute(
                                "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,STATE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,MARKS from Student"):
                            z += 1
                        conn.commit()
                        conn.close()
                        LLL2 = Label(top1, text='Number Of Records : %d ' % z, font=f7,
                                     fg='green').place(
                            x=670, y=400)
                        playsound('C:\\Users\\Kundan Kumar\\PycharmProjects\\Python\\Audio\\add5.mp3')
                    else:
                        playsound('C:\\Users\\Kundan Kumar\\PycharmProjects\\Python\\Audio\\add7.mp3')

        def delete_record():
            sss = listNodes.get(ACTIVE)
            delete(int(sss[:7]))

        def Search_record():
            sss = listNodes.get(ACTIVE)
            search(int(sss[:7]))

        def clear():
            aaa = messagebox.askyesno('Clear', 'Do you Want to Clear')
            if aaa == True:
                xx1.set('')
                xx2.set('')
                xx3.set('')
                xx4.set('')
                xx5.set('')
                xx6.set('Select course')
                xx7.set('select semester')
                xx8.set('')
                xx9.set('')
                xx10.set('select country')
                xx11.set('')
                xx12.set('')
                xx13.set('')
                xx177.set('')
                xx178.set('')

        def update_record():
            def upda():
                conn = sqlite3.connect('%s.sqlite' % (database_name))
                cursor = conn.cursor()
                z, y = 0, 0
                sss = listNodes.get(ACTIVE)

                for row in cursor.execute(
                        "SELECT Roll from Student"):
                    if int(sss[:7]) == row[0]:
                        y = 1
                    z += 1

                conn.commit()
                conn.close()
                if y == 1:

                    yyyy1 = int(sss[0:7])
                    top5 = Toplevel()
                    top5.title("Update  Record")
                    top5.geometry("400x400+450+100")

                    def marks():
                        def Mar():
                            top5.destroy()
                            zz1 = int(qq1.get())
                            updateM(yyyy1, zz1)

                            top7.destroy()

                        top7 = Toplevel()
                        top7.title("Search  Record")
                        top7.geometry("400x200+600+200")
                        qq1 = StringVar()
                        l3 = Label(top7, text="Student DataBase Management System",
                                   fg='skyblue',
                                   font=f1).place(
                            x=50, y=15)
                        LLL1 = Label(top7, text='Enter New Marks:', font=f6, fg='red').place(
                            x=40,
                            y=50)
                        EEE1 = Entry(top7, textvariable=qq1, width=14, font=f7).place(x=240,
                                                                                      y=53)
                        BBB1 = Button(top7, text='Done', bg='Green', fg='white', width=25,
                                      font=f4,
                                      command=Mar).place(x=70, y=110)

                    def address():
                        def Arr():
                            top5.destroy()
                            zzz1 = qqq1.get()
                            updateA(yyyy1, zzz1)

                            top8.destroy()

                        top8 = Toplevel()
                        top8.title("Modify  Record")
                        top8.geometry("600x200+600+200")
                        qqq1 = StringVar()
                        l3 = Label(top8, text="Student DataBase Management System",
                                   fg='skyblue',
                                   font=f1).place(x=200, y=15)

                        LLL1 = Label(top8, text='Enter New Address:', font=f6, fg='red').place(
                            x=40,
                            y=50)
                        EEE1 = Entry(top8, textvariable=qqq1, width=30, font=f7).place(x=240,
                                                                                       y=53)
                        BBB1 = Button(top8, text='Done', bg='Green', fg='white', width=25,
                                      font=f4,
                                      command=Arr).place(x=150, y=110)

                    def phone():
                        def pho():
                            top5.destroy()
                            zzzz1 = int(qqqq1.get())
                            updateP(yyyy1, zzzz1)

                            top9.destroy()

                        top9 = Toplevel()
                        top9.title("Modify  Record")
                        top9.geometry("400x200+600+200")
                        qqqq1 = StringVar()
                        l3 = Label(top9, text="Student DataBase Management System",
                                   fg='skyblue',
                                   font=f1).place(x=50, y=15)

                        LLL1 = Label(top9, text='Enter New Phone:', font=f6, fg='red').place(
                            x=40,
                            y=50)
                        EEE1 = Entry(top9, textvariable=qqqq1, width=14, font=f7).place(x=240,
                                                                                        y=53)
                        BBB1 = Button(top9, text='Done', bg='Green', fg='white', width=25,
                                      font=f4,
                                      command=pho).place(x=70, y=110)

                    l3 = Label(top5, text="Student DataBase Management System", fg='skyblue',
                               font=f1).place(x=50, y=15)

                    LLL1 = Label(top5, text='Select The Field:', font=f6, fg='red').place(x=120,
                                                                                          y=50)
                    BBB1 = Button(top5, text='Marks', bg='Green', fg='white', width=25, font=f4,
                                  command=marks).place(x=70, y=110)
                    BBB2 = Button(top5, text='Address', bg='skyblue', fg='white', width=25,
                                  font=f4,
                                  command=address).place(x=70, y=160)
                    BBB3 = Button(top5, text='Phone', bg='white', fg='black', width=25, font=f4,
                                  command=phone).place(x=70, y=210)
                    BBB4 = Button(top5, text='Close', bg='red', fg='white', width=25, font=f4,
                                  command=top5.destroy).place(x=70, y=260)
                else:
                    top15 = Toplevel()
                    top15.title("Display Record")
                    top15.geometry("350x50+600+300")
                    l = Label(top15, text='Record Not Found', font=f6, fg='red').pack()
                    playsound('C:\\Users\\Kundan Kumar\\PycharmProjects\\Python\\Audio\\record1.mp3')

            upda()

        xx1 = StringVar()
        xx2 = StringVar()
        xx3 = StringVar()
        xx4 = StringVar()
        xx5 = StringVar()
        xx6 = StringVar()
        xx7 = StringVar()
        xx8 = StringVar()
        xx9 = StringVar()
        xx10 = StringVar()
        xx11 = StringVar()
        xx12 = StringVar()
        xx13 = StringVar()
        xx14 = StringVar()
        xx15 = StringVar()
        xx177 = StringVar()
        xx178 = StringVar()

        LL3 = Label(top1, text='First Name:', font=f6, fg='Skyblue').place(x=260, y=80)
        LL4 = Label(top1, text='Last Name:', font=f6, fg='Skyblue').place(x=550, y=80)
        LL5 = Label(top1, text='Father\'s Name:', font=f6, fg='Skyblue').place(x=260, y=120)
        LL6 = Label(top1, text='Mother\'s Name:', font=f6, fg='Skyblue').place(x=550, y=120)
        LL7 = Label(top1, text='Date of Birth:', font=f6, fg='Skyblue').place(x=260, y=160)
        LL8 = Label(top1, text='Course :', font=f6, fg='Skyblue').place(x=550, y=160)
        LL8 = Label(top1, text='State :', font=f6, fg='Skyblue').place(x=550, y=280)
        LL9 = Label(top1, text='Semester:', font=f6, fg='Skyblue').place(x=260, y=200)
        LL10 = Label(top1, text='Batch:', font=f6, fg='Skyblue').place(x=550, y=200)
        LL11 = Label(top1, text='Mobile:', font=f6, fg='Skyblue').place(x=260, y=240)
        LL12 = Label(top1, text='Country:', font=f6, fg='Skyblue').place(x=550, y=240)
        LL13 = Label(top1, text='Drop_Out_Year', font=f6, fg='Skyblue').place(x=260, y=280)
        LL14 = Label(top1, text='RoLL:', font=f6, fg='Skyblue').place(x=260, y=320)
        LL14 = Label(top1, text='Marks:', font=f6, fg='Skyblue').place(x=550, y=320)
        LL14 = Label(top1, text='Reason of Drop_Out:', font=f6, fg='Skyblue').place(x=260, y=360)
        l3 = Label(top1, text="Copyright @ Kundan Kumar & Team", fg='Blue').place(x=220, y=400)

        coun = ['India', 'Nepal', 'Bhutan', 'Afganistan', 'Other']
        bat = ['2017 Onwards', '2018 Onwards', '2019 Onwards']

        EE1 = Entry(top1, textvariable=xx1, width=14, font=f7).place(x=410, y=80)
        EE2 = Entry(top1, textvariable=xx2, width=14, font=f7).place(x=700, y=80)
        EE3 = Entry(top1, textvariable=xx3, width=14, font=f7).place(x=410, y=120)
        EE4 = Entry(top1, textvariable=xx4, width=14, font=f7).place(x=700, y=120)
        EE5 = Entry(top1, textvariable=xx5, width=14, font=f7).place(x=410, y=160)
        c1 = Combobox(top1, values=cour, width=18, textvariable=xx6).place(x=700, y=160)
        xx6.set('Select Course ')
        c2 = Combobox(top1, values=sem, width=18, textvariable=xx7).place(x=410, y=200)
        xx7.set('Select Semester ')

        c3 = Combobox(top1, values=coun, width=18, textvariable=xx10).place(x=700, y=240)
        xx10.set('Select Country ')
        c4 = Combobox(top1, values=bat, width=18, textvariable=xx8).place(x=700, y=200)
        xx8.set('Select Batch ')
        EE9 = Entry(top1, textvariable=xx9, width=14, font=f7).place(x=410, y=240)
        EE11 = Entry(top1, textvariable=xx11, width=14, font=f7).place(x=410, y=280)
        EE11 = Entry(top1, textvariable=xx177, width=14, font=f7).place(x=700, y=280)
        EE12 = Entry(top1, textvariable=xx12, width=14, font=f7).place(x=410, y=320)
        EE13 = Entry(top1, textvariable=xx13, width=14, font=f7).place(x=700, y=320)
        EE14 = Entry(top1, textvariable=xx14, width=14, font=f7)
        EE15 = Entry(top1, textvariable=xx15, width=14, font=f7)
        EE15 = Entry(top1, textvariable=xx178, width=30, font=f7).place(x=480, y=360)
        xx14.set('')
        xx15.set('')

        def image_upload():
            xxx14 = filedialog.askopenfilename(initialdir="/", title="select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
            xx14.set(xxx14)

        def sign_upload():

            xxx15 = filedialog.askopenfilename(initialdir="/", title="select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
            xx15.set(xxx15)

        def take_photo():
            try:
                mkdir('D:\\DataBase Management\\Snap\\')
            except:
                pass

            camera = cv2.VideoCapture(0)
            return_value, \
            image = camera.read()

            cv2.imwrite(('D:\\student DataBase Management\\Snap\\%s.jpg') % str(xx12.get()), image)
            xx14.set(('D:\\student DataBase Management\\Snap\\%s.jpg') % str(xx12.get()))
            del (camera)

        img1 = ImageTk.PhotoImage(Image.open("photo_upload.png"))
        panel = Label(top1, image=img1).place(x=900, y=10)
        img2 = ImageTk.PhotoImage(Image.open("sign.png"))
        pane2 = Label(top1, image=img2).place(x=880, y=270)
        img3 = ImageTk.PhotoImage(Image.open("back.png"))
        pane3 = Label(top1, image=img3).place(x=0, y=0)

        BB1 = Button(top1, text='Add ', bg='Green', fg='white', width=15, font=f4,
                     command=add_record).place(x=70, y=90)
        BB2 = Button(top1, text='Display ', bg='Skyblue', fg='white', width=15, font=f4,
                     command=display).place(x=70, y=130)
        BB3 = Button(top1, text='Search', bg='white', fg='black', width=15, font=f4,
                     command=Search_record).place(x=70, y=170)
        BB5 = Button(top1, text='Update ', bg='black', fg='white', width=15, font=f4,
                     command=update_record).place(x=70, y=210)
        BB4 = Button(top1, text='Delete', bg='orange', fg='white', width=15, font=f4,
                     command=delete_record).place(x=70, y=250)
        BB5 = Button(top1, text='Close', bg='Red', fg='white', width=15, font=f4,
                     command=top1.destroy).place(x=70, y=290)
        BB6 = Button(top1, text='Clear', bg='White', fg='black', width=10, font=f3,
                     command=clear).place(x=770, y=360)
        BB7 = Button(top1, text='Upload Image', bg='White', fg='black', width=15, font=f3,
                     command=image_upload).place(x=860, y=220)
        BB10 = Button(top1, text='Take Pic', bg='Black', fg='White', width=12, font=f3, command=take_photo).place(
            x=1000,
            y=220)
        BB8 = Button(top1, text='Upload Signature', bg='White', fg='black', width=20, font=f3,
                     command=sign_upload).place(x=890, y=350)

        top1.geometry("1150x600+300+100")
        frame = Frame(top1)
        frame.place(x=220, y=460)

        listNodes = Listbox(frame, width=90, height=6, font=Font(family="Time New Roman", size=13, weight="bold"))
        listNodes.pack(side="left", fill="y")

        scrollbar = Scrollbar(frame, orient="vertical")
        scrollbar.config(command=listNodes.yview)
        scrollbar.pack(side="right", fill="y")

        listNodes.config(yscrollcommand=scrollbar.set)
        conn = sqlite3.connect('%s.sqlite' % (database_name))
        cursor = conn.cursor()
        z = 0

        for row in cursor.execute(
                "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,STATE,REASON,IMAGE,SIGN,MARKS   from Student"):
            z += 1
            a11 = row[1] + " " + row[2]
            sss = str(row[0]) + ",  \t\t" + a11 + ',  \t\t' + str(row[5]) + ',  \t\t' + str(row[9]) + ',  \t\t' + str(
                row[7]) + ',  \t\t' + str(row[8]) + ',  \t\t' + str(row[10]) + ', \t\t' + str(row[11]) + ', \t\t' + str(
                row[12] + ',  \t\t' + str(row[15]))
            print(sss)
            listNodes.insert(END, sss)
        conn.commit()
        conn.close()
        LLL2 = Label(top1, text='Number Of Records : %d ' % z, font=f7, fg='green').place(
            x=670, y=400)

        c1 = Canvas(top1, width=20, height=400, bg='White')
        c1.pack(side=RIGHT)
        c1 = Canvas(top1, width=10, height=400, bg='orange')
        c1.pack(side=RIGHT)
        top1.mainloop()

    sq()

    def Feed():
        def School():
            feed_data('school_education_database',
                      ['Science Math English Hindi Social Science', 'Science Math English Urdu Social Science'],
                      ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th'])

        def higher():
            feed_data('higher_education_database', ['Physics and Msths', 'physics and Biology', 'Commerce', 'Arts'],
                      ['11th', '12th'])

        def technical():
            feed_data('Technical_education_database', ['B.Tech', 'M.Tech', 'BSA', 'MCA', 'DCA', 'MBA', 'LAW'],
                      ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th'])

        link1 = Toplevel()
        link1.geometry("500x250+200+100")
        link1.title("Feed Data")
        img1 = ImageTk.PhotoImage(Image.open("data1.jpg"))
        panel = Label(link1, image=img1).place(x=10, y=10)
        f1 = Font(family="Time New Roman", size=12, weight="bold", underline=1)
        f2 = Font(family="Time New Roman", size=15, weight="bold", underline=1)
        f3 = Font(family="Time New Roman", size=10, weight="bold")
        l3 = Label(link1, text=" Adding Data to  Database", fg='green', font=f2).place(x=200, y=10)
        b = Button(link1, text='School Education ', command=School, width=20, font=f1, bg='darkblue', fg='white').place(
            x=300, y=50)
        b = Button(link1, text='Higher Education  ', command=higher, width=20, font=f1, bg='darkred', fg='white').place(
            x=300, y=100)
        b = Button(link1, text='Technical Education  ', command=technical, width=20, font=f1, bg='darkorange',
                   fg='white').place(x=300,
                                     y=150)
        link1.resizable('false', 'false')
        link1.mainloop()

    def analysis():
        def School_a():
            t5 = Toplevel()
            t5.geometry("700x500+200+10")
            f6 = Font(family="Time New Roman", size=12, weight="bold", underline=0)
            conn = sqlite3.connect('school_education_database.sqlite')
            cursor = conn.cursor()
            z = 0
            sta = []
            cor = []
            dro = []
            rea = []
            na = []
            bat = []
            xx10 = StringVar()
            xx11 = StringVar()
            for row in cursor.execute(
                    "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,STATE,REASON,IMAGE,SIGN,MARKS from Student"):

                z += 1
                a2 = row[1] + ' ' + row[2]
                na.append(a2)
                cor.append(row[6])
                bat.append(row[8])

                if row[11] != 'nil' or row[11] != "NIL":
                    dro.append(row[11])
                sta.append(row[12])
                rea.append(row[16])
            print(dro)

            def dis1():
                for i in rea:
                    print(i)

            def dis2():
                t5.destroy()
                conn = sqlite3.connect('school_education_database.sqlite')
                cursor = conn.cursor()
                t6 = Toplevel()
                t6.geometry("700x400+200+10")
                s = xx10.get()
                z1 = 0
                sta = []
                cor = []
                dro = []
                rea = []
                na = []
                bat = []
                for row in cursor.execute(
                        "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,STATE,REASON,IMAGE,SIGN,MARKS from Student where STATE=?",
                        (s,)):
                    z1 += 1
                    a2 = row[1] + ' ' + row[2]
                    na.append(a2)
                    if row[11] != 'nil' or row[11] != "NIL":
                        dro.append(row[11])
                    rea.append(row[16])
                LL2 = Label(t6, text='Database Management', fg='Red', font=f6).place(x=250, y=15)
                LL2 = Label(t6, text='Total Number Of Students Enrolled : %s' % (str(z)), fg='Red', font=f6).place(x=50,
                                                                                                                   y=55)
                conn.commit()
                conn.close()
                LL2 = Label(t6,
                            text='Percentage of Person Qualified            : %s' % (str(((z - len(cor)) / z) * 100)),
                            fg='Red', font=f6).place(x=50, y=255)
                LL2 = Label(t6, text='Percentage of Person DropOut             : %s' % (str(((len(cor)) / z) * 100)),
                            fg='Red', font=f6).place(x=50, y=305)
                LL2 = Label(t6, text='Reason of DropOut            : ', fg='Red', font=f6).place(x=50, y=355)
                b1 = Button(t6, text='Display', command=dis1, width=30, height=1, bg='green', fg='white',
                            font=f3).place(x=320, y=355)
                t6.resizable('false', 'false')
                t6.mainloop()

            def dis3():

                t5.destroy()
                conn = sqlite3.connect('school_education_database.sqlite')
                cursor = conn.cursor()
                t6 = Toplevel()
                t6.geometry("700x400+200+10")
                s12 = xx10.get()
                z1 = 0
                sta = []
                cor = []
                dro = []
                rea = []
                na = []
                bat = []
                for row in cursor.execute(
                        "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,STATE,REASON,IMAGE,SIGN,MARKS from Student where COURSE=?",
                        (s12,)):
                    z1 += 1
                    a2 = row[1] + ' ' + row[2]
                    na.append(a2)
                    if row[11] != 'nil' or row[11] != "NIL":
                        dro.append(row[11])
                    rea.append(row[16])
                LL2 = Label(t6, text='Database Management', fg='Red', font=f6).place(x=250, y=15)
                LL2 = Label(t6, text='Total Number Of Students Enrolled : %s' % (str(z)), fg='Red', font=f6).place(x=50,
                                                                                                                   y=55)
                conn.commit()
                conn.close()
                LL2 = Label(t6,
                            text='Percentage of Person Qualified            : %s' % (str(((z - len(cor)) / z) * 100)),
                            fg='Red', font=f6).place(x=50, y=255)
                LL2 = Label(t6, text='Percentage of Person DropOut             : %s' % (str(((len(cor)) / z) * 100)),
                            fg='Red', font=f6).place(x=50, y=305)
                LL2 = Label(t6, text='Reason of DropOut            : ', fg='Red', font=f6).place(x=50, y=355)
                b1 = Button(t6, text='Display', command=dis1, width=30, height=1, bg='green', fg='white',
                            font=f3).place(x=320, y=355)
                t6.resizable('false', 'false')
                t6.mainloop()
                s12 = xx11.get()

            print(dro)
            LL2 = Label(t5, text='Database Management', fg='Red', font=f6).place(x=250, y=15)
            LL2 = Label(t5, text='Total Number Of Students Enrolled : %s' % (str(z)), fg='Red', font=f6).place(x=50,
                                                                                                               y=55)
            LL2 = Label(t5, text='Total Number Of Dropout : %s' % (str(len(dro))), fg='Red', font=f6).place(x=50, y=105)
            LL2 = Label(t5, text='Total Number Of Courses           : %s' % (str(len(cor))), fg='Red', font=f6).place(
                x=50, y=155)
            LL2 = Label(t5, text='Total Number Drop Out  According to State         :', fg='Red', font=f6).place(x=50,
                                                                                                                 y=205)
            LL2 = Label(t5, text='Total Number Drop Out  According to Course            : %s' % (str(len(dro))),
                        fg='Red', font=f6).place(x=55, y=255)
            LL2 = Label(t5, text='Percentage of Person Qualified            : %s' % (str(((z - len(cor)) / z) * 100)),
                        fg='Red', font=f6).place(x=50, y=305)
            LL2 = Label(t5, text='Percentage of Person DropOut             : %s' % (str(((len(dro)) / z) * 100)),
                        fg='Red', font=f6).place(x=50, y=355)
            LL2 = Label(t5, text='Reason of DropOut            : ', fg='Red', font=f6).place(x=50, y=405)
            b1 = Button(t5, text='Display', command=dis1, width=30, height=1, bg='green', fg='white',
                        font=f3).place(x=320, y=405)
            b1 = Button(t5, text='Display', command=dis2, width=10, height=1, bg='green', fg='white',
                        font=f3).place(x=550, y=205)
            b1 = Button(t5, text='Display', command=dis3, width=10, height=1, bg='green', fg='white',
                        font=f3).place(x=550, y=255)
            c3 = Combobox(t5, values=sta, width=18, textvariable=xx10).place(x=400, y=205)
            xx10.set('Select State ')
            c4 = Combobox(t5, values=cor, width=18, textvariable=xx11).place(x=400, y=255)
            xx11.set('Select Course ')
            conn.commit()
            conn.close()
            t5.resizable('false', 'false')
            t5.mainloop()

        def higher_a():

            t5 = Toplevel()
            t5.geometry("700x500+200+10")
            f6 = Font(family="Time New Roman", size=12, weight="bold", underline=0)
            conn = sqlite3.connect('higher_education_database.sqlite')
            cursor = conn.cursor()
            z = 0
            sta = []
            cor = []
            dro = []
            rea = []
            na = []
            bat = []
            xx10 = StringVar()
            xx11 = StringVar()
            for row in cursor.execute(
                    "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,STATE,REASON,IMAGE,SIGN,MARKS from Student"):

                z += 1
                a2 = row[1] + ' ' + row[2]
                na.append(a2)
                cor.append(row[6])
                bat.append(row[8])
                if row[11] != 'nil' or row[11] != "NIL":
                    dro.append(row[11])
                sta.append(row[12])
                rea.append(row[16])

            def dis1():
                for i in rea:
                    print(i)

            def dis2():
                t5.destroy()
                conn = sqlite3.connect('higher_education_database.sqlite')
                cursor = conn.cursor()
                t6 = Toplevel()
                t6.geometry("700x400+200+10")
                s = xx10.get()
                z1 = 0
                sta = []
                cor = []
                dro = []
                rea = []
                na = []
                bat = []
                for row in cursor.execute(
                        "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,STATE,REASON,IMAGE,SIGN,MARKS from Student where STATE=?",
                        (s,)):
                    z1 += 1
                    a2 = row[1] + ' ' + row[2]
                    na.append(a2)
                    if row[11] != 'nil' or row[11] != "NIL":
                        dro.append(row[11])
                    rea.append(row[16])
                LL2 = Label(t6, text='Database Management', fg='Red', font=f6).place(x=250, y=15)
                LL2 = Label(t6, text='Total Number Of Students Enrolled : %s' % (str(z)), fg='Red', font=f6).place(x=50,
                                                                                                                   y=55)
                conn.commit()
                conn.close()
                LL2 = Label(t6,
                            text='Percentage of Person Qualified            : %s' % (str(((z - len(cor)) / z) * 100)),
                            fg='Red', font=f6).place(x=50, y=255)
                LL2 = Label(t6, text='Percentage of Person DropOut             : %s' % (str(((len(cor)) / z) * 100)),
                            fg='Red', font=f6).place(x=50, y=305)
                LL2 = Label(t6, text='Reason of DropOut            : ', fg='Red', font=f6).place(x=50, y=355)
                b1 = Button(t6, text='Display', command=dis1, width=30, height=1, bg='green', fg='white',
                            font=f3).place(x=320, y=355)
                t6.resizable('false', 'false')
                t6.mainloop()

            def dis3():

                t5.destroy()
                conn = sqlite3.connect('higher_education_database.sqlite')
                cursor = conn.cursor()
                t6 = Toplevel()
                t6.geometry("700x400+200+10")
                s12 = xx10.get()
                z1 = 0
                sta = []
                cor = []
                dro = []
                rea = []
                na = []
                bat = []
                for row in cursor.execute(
                        "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,STATE,REASON,IMAGE,SIGN,MARKS from Student where COURSE=?",
                        (s12,)):
                    z1 += 1
                    a2 = row[1] + ' ' + row[2]
                    na.append(a2)
                    if row[11] != 'nil' or row[11] != "NIL":
                        dro.append(row[11])
                    rea.append(row[16])
                LL2 = Label(t6, text='Database Management', fg='Red', font=f6).place(x=250, y=15)
                LL2 = Label(t6, text='Total Number Of Students Enrolled : %s' % (str(z)), fg='Red', font=f6).place(x=50,
                                                                                                                   y=55)
                conn.commit()
                conn.close()
                LL2 = Label(t6,
                            text='Percentage of Person Qualified            : %s' % (str(((z - len(cor)) / z) * 100)),
                            fg='Red', font=f6).place(x=50, y=255)
                LL2 = Label(t6, text='Percentage of Person DropOut             : %s' % (str(((len(cor)) / z) * 100)),
                            fg='Red', font=f6).place(x=50, y=305)
                LL2 = Label(t6, text='Reason of DropOut            : ', fg='Red', font=f6).place(x=50, y=355)
                b1 = Button(t6, text='Display', command=dis1, width=30, height=1, bg='green', fg='white',
                            font=f3).place(x=320, y=355)
                t6.resizable('false', 'false')
                t6.mainloop()
                s12 = xx11.get()

            print(dro)
            LL2 = Label(t5, text='Database Management', fg='Red', font=f6).place(x=250, y=15)
            LL2 = Label(t5, text='Total Number Of Students Enrolled : %s' % (str(z)), fg='Red', font=f6).place(x=50,
                                                                                                               y=55)
            LL2 = Label(t5, text='Total Number Of Dropout : %s' % (str(len(dro))), fg='Red', font=f6).place(x=50, y=105)
            LL2 = Label(t5, text='Total Number Of Courses           : %s' % (str(len(cor))), fg='Red', font=f6).place(
                x=50, y=155)
            LL2 = Label(t5, text='Total Number Drop Out  According to State         :', fg='Red', font=f6).place(x=50,
                                                                                                                 y=205)
            LL2 = Label(t5, text='Total Number Drop Out  According to Course            : %s' % (str(len(dro))),
                        fg='Red', font=f6).place(x=55, y=255)
            LL2 = Label(t5, text='Percentage of Person Qualified            : %s' % (str(((z - len(cor)) / z) * 100)),
                        fg='Red', font=f6).place(x=50, y=305)
            LL2 = Label(t5, text='Percentage of Person DropOut             : %s' % (str(((len(dro)) / z) * 100)),
                        fg='Red', font=f6).place(x=50, y=355)
            LL2 = Label(t5, text='Reason of DropOut            : ', fg='Red', font=f6).place(x=50, y=405)
            b1 = Button(t5, text='Display', command=dis1, width=30, height=1, bg='green', fg='white',
                        font=f3).place(x=320, y=405)
            b1 = Button(t5, text='Display', command=dis2, width=10, height=1, bg='green', fg='white',
                        font=f3).place(x=550, y=205)
            b1 = Button(t5, text='Display', command=dis3, width=10, height=1, bg='green', fg='white',
                        font=f3).place(x=550, y=255)
            c3 = Combobox(t5, values=sta, width=18, textvariable=xx10).place(x=400, y=205)
            xx10.set('Select State ')
            c4 = Combobox(t5, values=cor, width=18, textvariable=xx11).place(x=400, y=255)
            xx11.set('Select Course ')
            conn.commit()
            conn.close()
            t5.resizable('false', 'false')
            t5.mainloop()

        def technical_a():

            t5 = Toplevel()
            t5.geometry("700x500+200+10")
            f6 = Font(family="Time New Roman", size=12, weight="bold", underline=0)
            conn = sqlite3.connect('Technical_education_database.sqlite')
            cursor = conn.cursor()
            z = 0
            sta = []
            cor = []
            dro = []
            rea = []
            na = []
            bat = []
            xx10 = StringVar()
            xx11 = StringVar()
            for row in cursor.execute(
                    "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,STATE,REASON,IMAGE,SIGN,MARKS from Student"):

                z += 1
                a2 = row[1] + ' ' + row[2]
                na.append(a2)
                cor.append(row[6])
                bat.append(row[8])
                if row[11] != 'nil' or row[11] != "NIL":
                    dro.append(row[11])
                sta.append(row[12])
                rea.append(row[16])

            def dis1():
                for i in rea:
                    print(i)

            def dis2():
                t5.destroy()
                conn = sqlite3.connect('Technical_education_database.sqlite')
                cursor = conn.cursor()
                t6 = Toplevel()
                t6.geometry("700x400+200+10")
                s = xx10.get()
                z1 = 0
                sta = []
                cor = []
                dro = []
                rea = []
                na = []
                bat = []
                for row in cursor.execute(
                        "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,STATE,REASON,IMAGE,SIGN,MARKS from Student where STATE=?",
                        (s,)):
                    z1 += 1
                    a2 = row[1] + ' ' + row[2]
                    na.append(a2)
                    if row[11] != 'nil' or row[11] != "NIL":
                        dro.append(row[11])
                    rea.append(row[16])
                LL2 = Label(t6, text='Database Management', fg='Red', font=f6).place(x=250, y=15)
                LL2 = Label(t6, text='Total Number Of Students Enrolled : %s' % (str(z)), fg='Red', font=f6).place(x=50,
                                                                                                                   y=55)
                conn.commit()
                conn.close()
                LL2 = Label(t6,
                            text='Percentage of Person Qualified            : %s' % (str(((z - len(cor)) / z) * 100)),
                            fg='Red', font=f6).place(x=50, y=255)
                LL2 = Label(t6, text='Percentage of Person DropOut             : %s' % (str(((len(cor)) / z) * 100)),
                            fg='Red', font=f6).place(x=50, y=305)
                LL2 = Label(t6, text='Reason of DropOut            : ', fg='Red', font=f6).place(x=50, y=355)
                b1 = Button(t6, text='Display', command=dis1, width=30, height=1, bg='green', fg='white',
                            font=f3).place(x=320, y=355)
                t6.resizable('false', 'false')
                t6.mainloop()

            def dis3():

                t5.destroy()
                conn = sqlite3.connect('Technical_education_database.sqlite')
                cursor = conn.cursor()
                t6 = Toplevel()
                t6.geometry("700x400+200+10")
                s12 = xx10.get()
                z1 = 0
                sta = []
                cor = []
                dro = []
                rea = []
                na = []
                bat = []
                for row in cursor.execute(
                        "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,STATE,REASON,IMAGE,SIGN,MARKS from Student where COURSE=?",
                        (s12,)):
                    z1 += 1
                    a2 = row[1] + ' ' + row[2]
                    na.append(a2)
                    if row[11] != 'nil' or row[11] != "NIL":
                        dro.append(row[11])
                    rea.append(row[16])
                LL2 = Label(t6, text='Database Management', fg='Red', font=f6).place(x=250, y=15)
                LL2 = Label(t6, text='Total Number Of Students Enrolled : %s' % (str(z)), fg='Red', font=f6).place(x=50,
                                                                                                                   y=55)
                conn.commit()
                conn.close()
                LL2 = Label(t6,
                            text='Percentage of Person Qualified            : %s' % (str(((z - len(cor)) / z) * 100)),
                            fg='Red', font=f6).place(x=50, y=255)
                LL2 = Label(t6, text='Percentage of Person DropOut             : %s' % (str(((len(cor)) / z) * 100)),
                            fg='Red', font=f6).place(x=50, y=305)
                LL2 = Label(t6, text='Reason of DropOut            : ', fg='Red', font=f6).place(x=50, y=355)
                b1 = Button(t6, text='Display', command=dis1, width=30, height=1, bg='green', fg='white',
                            font=f3).place(x=320, y=355)
                t6.resizable('false', 'false')
                t6.mainloop()
                s12 = xx11.get()

            print(dro)
            LL2 = Label(t5, text='Database Management', fg='Red', font=f6).place(x=250, y=15)
            LL2 = Label(t5, text='Total Number Of Students Enrolled : %s' % (str(z)), fg='Red', font=f6).place(x=50,
                                                                                                               y=55)
            LL2 = Label(t5, text='Total Number Of Dropout : %s' % (str(len(dro))), fg='Red', font=f6).place(x=50, y=105)
            LL2 = Label(t5, text='Total Number Of Courses           : %s' % (str(len(cor))), fg='Red', font=f6).place(
                x=50, y=155)
            LL2 = Label(t5, text='Total Number Drop Out  According to State         :', fg='Red', font=f6).place(x=50,
                                                                                                                 y=205)
            LL2 = Label(t5, text='Total Number Drop Out  According to Course            : %s' % (str(len(dro))),
                        fg='Red', font=f6).place(x=55, y=255)
            LL2 = Label(t5, text='Percentage of Person Qualified            : %s' % (str(((z - len(cor)) / z) * 100)),
                        fg='Red', font=f6).place(x=50, y=305)
            LL2 = Label(t5, text='Percentage of Person DropOut             : %s' % (str(((len(dro)) / z) * 100)),
                        fg='Red', font=f6).place(x=50, y=355)
            LL2 = Label(t5, text='Reason of DropOut            : ', fg='Red', font=f6).place(x=50, y=405)
            b1 = Button(t5, text='Display', command=dis1, width=30, height=1, bg='green', fg='white',
                        font=f3).place(x=320, y=405)
            b1 = Button(t5, text='Display', command=dis2, width=10, height=1, bg='green', fg='white',
                        font=f3).place(x=550, y=205)
            b1 = Button(t5, text='Display', command=dis3, width=10, height=1, bg='green', fg='white',
                        font=f3).place(x=550, y=255)
            c3 = Combobox(t5, values=sta, width=18, textvariable=xx10).place(x=400, y=205)
            xx10.set('Select State ')
            c4 = Combobox(t5, values=cor, width=18, textvariable=xx11).place(x=400, y=255)
            xx11.set('Select Course ')
            conn.commit()
            conn.close()
            t5.resizable('false', 'false')
            t5.mainloop()

        def overall_a():

            t5 = Toplevel()
            t5.geometry("700x500+200+10")
            f6 = Font(family="Time New Roman", size=12, weight="bold", underline=0)
            conn = sqlite3.connect('Technical_education_database.sqlite')
            cursor = conn.cursor()
            z1, z2, z3 = 0, 0, 0
            sta = []
            cor = []
            dro = []
            rea = []
            na = []
            bat = []
            xx10 = StringVar()
            xx11 = StringVar()
            for row in cursor.execute(
                    "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,STATE,REASON,IMAGE,SIGN,MARKS from Student"):

                z1 += 1
                a2 = row[1] + ' ' + row[2]
                na.append(a2)
                cor.append(row[6])
                bat.append(row[8])
                if row[11] != 'nil' or row[11] != "NIL":
                    dro.append(row[11])
                sta.append(row[12])
                rea.append(row[16])
            conn.commit()
            conn.close()
            LL2 = Label(t5, text='Total Number Of Students Enrolled in Schooling : %s' % (str(z1)), fg='Red',
                        font=f6).place(x=50, y=55)
            conn = sqlite3.connect('higher_education_database.sqlite')
            cursor = conn.cursor()
            for row in cursor.execute(
                    "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,STATE,REASON,IMAGE,SIGN,MARKS from Student"):

                z2 += 1
                a2 = row[1] + ' ' + row[2]
                na.append(a2)
                cor.append(row[6])
                bat.append(row[8])
                if row[11] != 'nil' or row[11] != "NIL":
                    dro.append(row[11])
                sta.append(row[12])
                rea.append(row[16])
            conn.commit()
            conn.close()
            LL2 = Label(t5, text='Total Number Of Students Enrolled in Higher Study : %s' % (str(z2)), fg='Red',
                        font=f6).place(x=50, y=105)
            conn = sqlite3.connect('school_education_database.sqlite')
            cursor = conn.cursor()
            for row in cursor.execute(
                    "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,DROP_OUT_YEAR,STATE,REASON,IMAGE,SIGN,MARKS from Student"):

                z3 += 1
                a2 = row[1] + ' ' + row[2]
                na.append(a2)
                cor.append(row[6])
                bat.append(row[8])
                if row[11] != 'nil' or row[11] != "NIL":
                    dro.append(row[11])
                sta.append(row[12])
                rea.append(row[16])
            conn.commit()
            conn.close()

            def dis1():
                for i in rea:
                    print(i)

            LL2 = Label(t5, text='Total Number Of Students Enrolled : %s' % (str(z3)), fg='Red', font=f6).place(x=50,
                                                                                                                y=155)
            print(dro)
            LL2 = Label(t5, text='Database Management', fg='Red', font=f6).place(x=250, y=15)
            z = z1 + z2 + z3
            LL2 = Label(t5, text='Total Number Of Students Enrolled : %s' % (str(z)), fg='Red', font=f6).place(x=50,
                                                                                                               y=205)
            LL2 = Label(t5, text='Total Number Of Dropout : %s' % (str(len(dro))), fg='Red', font=f6).place(x=50, y=255)
            LL2 = Label(t5, text='Total Number Of Courses           : %s' % (str(len(cor))), fg='Red', font=f6).place(
                x=50, y=305)
            LL2 = Label(t5, text='Percentage of Person Qualified            : %s' % (str(((z - len(cor)) / z) * 100)),
                        fg='Red', font=f6).place(x=50, y=355)
            LL2 = Label(t5, text='Percentage of Person DropOut             : %s' % (str(((len(dro)) / z) * 100)),
                        fg='Red', font=f6).place(x=50, y=405)
            LL2 = Label(t5, text='Reason of DropOut            : ', fg='Red', font=f6).place(x=50, y=455)
            b1 = Button(t5, text='Display', command=dis1, width=30, height=1, bg='green', fg='white',
                        font=f3).place(x=320, y=455)

            t5.resizable('false', 'false')
            t5.mainloop()

        link.destroy()
        link1 = Toplevel()
        link1.geometry("500x250+200+100")
        link1.title("Analysing Data")
        img1 = ImageTk.PhotoImage(Image.open("data1.jpg"))
        panel = Label(link1, image=img1).place(x=10, y=10)
        f1 = Font(family="Time New Roman", size=12, weight="bold", underline=1)
        f2 = Font(family="Time New Roman", size=15, weight="bold", underline=1)
        f3 = Font(family="Time New Roman", size=10, weight="bold")
        l3 = Label(link1, text=" Studing  Database", fg='green', font=f2).place(x=200, y=10)
        b = Button(link1, text='School Education ', command=School_a, width=20, font=f1, bg='darkblue',
                   fg='white').place(
            x=300, y=50)
        b = Button(link1, text='Higher Education  ', command=higher_a, width=20, font=f1, bg='darkred',
                   fg='white').place(
            x=300, y=100)
        b = Button(link1, text='Technical Education  ', command=technical_a, width=20, font=f1, bg='darkorange',
                   fg='white').place(x=300,
                                     y=150)
        b = Button(link1, text='OverAll Evaluation   ', command=overall_a, width=20, font=f1, bg='skyblue',
                   fg='white').place(x=300,
                                     y=200)
        link1.resizable('false', 'false')
        link1.mainloop()

    link = Tk()
    link.geometry("500x400+200+100")
    link.title("Interlinking Database")
    img1 = ImageTk.PhotoImage(Image.open("data.jpg"))
    panel = Label(link, image=img1).place(x=10, y=10)
    f1 = Font(family="Time New Roman", size=12, weight="bold", underline=1)
    f2 = Font(family="Time New Roman", size=15, weight="bold", underline=1)
    f3 = Font(family="Time New Roman", size=10, weight="bold")
    l3 = Label(link, text=" Master Database", fg='green', font=f2).place(x=150, y=40)
    b = Button(link, text='Feed Data ', command=Feed, width=20, font=f1, bg='darkblue', fg='white').place(x=50, y=200)
    b = Button(link, text='Analyse Data ', command=analysis, width=20, font=f1, bg='darkred', fg='white').place(x=50,
                                                                                                                y=250)
    link.resizable('false', 'false')
    link.mainloop()

def Signup():
    L1 = Label(root, text='                                                                           ', font=f3).place(x=300, y=420)
    try:

        def sign_up():
            sig = sign.get()
            Label(root_signup, text='                                   ').place(x=200, y=180)
            if sig == 'Kundan':
                x = listdir('D:/Face UnLock Face_Data')
                if len(x) == 0:
                    pass
                else:
                    for i in x:
                        os.remove('D:/Face UnLock Face_Data/%s' % i)

                data_path = 'D:/Face UnLock Face_Data/'
                onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
                Labels = []
                for i, files in enumerate(onlyfiles):
                    Labels.append(i)
                Labels = np.asarray(Labels, dtype=np.int32)

                cap = cv2.VideoCapture(0)
                count = 0
                x1 = len(Labels)
                print(x1)

                while True:
                    ret, frame = cap.read()
                    frame = cv2.flip(frame, 1)
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                    n = 0
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
                        n = faces.shape[0]
                        face_img = frame[y:y + h, x:x + w]

                    if n == 0:
                        cv2.putText(frame, 'No Face found', (10, 450), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    else:

                        count += 1
                        face = cv2.resize(face_img, (200, 200))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        cv2.imwrite('D:/Face UnLock Face_Data/user' + str(count + x1) + '.jpg', face)

                        cv2.putText(face, str(count), (5, 180), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow('Face', face)

                    if cv2.waitKey(1) == ord('q') or count == 100:
                        break
                count = 0
                root_signup.destroy()
                cap.release()
                cv2.destroyAllWindows()

            else:
                Label(root_signup, text='Invalid Password').place(x=200, y=180)

        root_signup = Toplevel()
        root_signup.geometry('360x500+900+100')
        img1 = ImageTk.PhotoImage(Image.open("12_lock.jpg"))
        panel = Label(root_signup, image=img1).place(x=1, y=20)
        sign = StringVar()
        l3 = Label(root_signup, text="Hackacthon Battle", fg='brown', font=f1).place(x=70, y=10)
        l3 = Label(root_signup, text=" Sign Up with Face_Lock", fg='darkblue', font=f1).place(x=60, y=40)
        l3 = Label(root_signup, text=" Enter Password ", fg='blue', font=f1).place(x=100, y=380)
        E1 = Entry(root_signup, show='*', textvariable=sign, font=f3).place(x=90, y=420)
        but = Button(root_signup, text='Login', command=sign_up, width=20, height=1, font=f3, bg='green').place(x=80,
                                                                                                                y=460)
        root_signup.resizable('false', 'false')
        root_signup.mainloop()
    except:
        pass

def Face_Unlock():
    try:

        data_path = 'D:/Face UnLock Face_Data/'
        onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

        Training_Data, Labels = [], []

        for i, files in enumerate(onlyfiles):
            image_path = data_path + onlyfiles[i]
            images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            Training_Data.append(np.asarray(images, dtype=np.uint8))
            Labels.append(i)
        if len(Labels) == 0:
            eng = t2s.init()
            try:
                eng.setProperty('rate', 140);
                eng.setProperty('volume', .9)
                eng.say('Firstly You should SignUp With Face ID')
                eng.runAndWait()
            except:
                pass

            o1 = "Message: Firstly You should SignUp With Face ID"
            L1 = Label(root, text=o1, font=f3).place(x=200, y=420)

        else:
            Labels = np.asarray(Labels, dtype=np.int32)

            model = cv2.face.LBPHFaceRecognizer_create()

            model.train(np.asarray(Training_Data), np.asarray(Labels))

            ct = 0
            cap = cv2.VideoCapture(0)
            while True:

                ret, frame = cap.read()
                frame = cv2.flip(frame, 1)
                n = 0

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                    face = gray[y:y + h, x:x + w]
                    face = cv2.resize(face, (200, 200))
                    n = face.shape[0]
                    j, k = model.predict(face)
                    confidence = int(100 * (1 - (k) / 300))

                if n > 0:

                    if k < 50:
                        if confidence > 75:
                            ct += 1
                            cv2.putText(frame, '% Matching' + str(confidence), (20, 450), cv2.FONT_HERSHEY_COMPLEX, 1,
                                        (0, 0, 255), 1)

                            cv2.putText(frame, 'unlocking', (420, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 125), 3)

                        else:
                            ct = 0
                            cv2.putText(frame, "Unknown", (x + w, y + h + 10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0),
                                        1)
                    else:
                        ct = 0
                        cv2.putText(frame, "Unknown", (x + w, y + h + 10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)

                if n == 0:
                    cv2.putText(frame, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

                cv2.imshow('Face unLockIng Application', frame)

                if cv2.waitKey(1) == ord('q') or ct == 20:
                    break

            cap.release()
            cv2.destroyAllWindows()

            if ct == 20:
                eng = t2s.init()
                try:
                    eng.setProperty('rate', 140)
                    eng.setProperty('volume', .9)
                    eng.say('login successfuly. Loading the Content')
                    eng.runAndWait()
                except:
                    pass

                Main()
    except:
        pass

def login():
    s1 = ss1.get()
    s2 = ss2.get()
    if (s1 == 'Kundan' and s2 == 'Singh'):
        eng = t2s.init()
        try:
            eng.setProperty('rate', 140);
            eng.setProperty('volume', .9)
            eng.say('login successfuly. Loading the Content')
            eng.runAndWait()
        except:
            pass

        Main()



    elif s1 == '' and s2 == '':
        eng = t2s.init()
        try:
            eng.setProperty('rate', 140);
            eng.setProperty('volume', .9)
            eng.say('First You should Enter Username and Password.')
            eng.runAndWait()
        except:
            pass

        o1 = "Message: Please Enter Username and Password"
        L1 = Label(root, text=o1, font=f3).place(x=200, y=420)

    else:
        eng = t2s.init()
        try:
            eng.setProperty('rate', 140);
            eng.setProperty('volume', .9)
            eng.say('You have Entered Wrong username or password')
            eng.runAndWait()
        except:
            pass

        o2 = "Please Enter Invalid Username Or Password"
        L2 = Label(root, text=o2, font=f3).place(x=200, y=420)

def win():
    ans1 = messagebox.askyesno("Exit", "DO You Want to Exit")
    if ans1 == True:
        root.quit()

try:
    mkdir('D:/Face UnLock Face_Data/')
except:
    pass

root=Tk()
frame=Frame(root,height=600,width=10).pack(side=LEFT)
img = ImageTk.PhotoImage(Image.open("1.jpg"))
panel = Label(frame, image = img)
panel.pack(side = "right", fill = "both", expand = "yes")


f1 = Font(family="Time New Roman", size=12, weight="bold", underline=1)
f2 = Font(family="Time New Roman", size=15, weight="bold", underline=1)
f3 = Font(family="Time New Roman", size=12, weight="bold")

eng = t2s.init()

def text2speech():
    try:
        eng.setProperty('rate', 140);
        eng.setProperty('volume', .9)
        eng.say('Welcome to Hackathon Battle')
        eng.runAndWait()
    except:
        pass


root.title("Training Project")
l3 = Label(root, text="Master DataBase", fg='brown', font=f1,bg='white').place(x=140, y=30)
l3 = Label(root, text=" Hackacthon Battle", fg='green', font=f1,bg='white').place(x=120, y=70)
l3 = Label(root, text="Enter Username and Password", fg='brown', font=f1,bg='white').place(x=70, y=120)
l3 = Label(root, text="Copyright @ Kundan Kumar ", fg='skyblue',bg='white',font=f3).place(x=550, y=420)
l1 = Label(root, text='Username', fg='brown', font=f1,bg='white').place(x=50, y=160)
l2 = Label(root, text='Password', fg='brown', font=f1,bg='white').place(x=50, y=200)
ss1 = StringVar()
ss2 = StringVar()
e1 = Entry(root, textvariable=ss1).place(x=205, y=165)
e2 = Entry(root, textvariable=ss2, show='*').place(x=205, y=205)
b1 = Button(root, text='Login', command=login, width=15, height=1, bg='skyblue', fg='white', font=f3).place(x=50,y=250)
b2 = Button(root, text='Login_With_Face', command=Face_Unlock, width=15, height=1, bg='green', fg='white', font=f3).place(x=210, y=250)
b1=Button(root,text='Sign_up',width=31,command=Signup,bg='orange',font=f3,height=1).place(x=50,y=290)
b3 = Button(root, text='Exit', command=win, width=31, height=1, font=f3).place(x=50, y=330)
c1 = Canvas(root, width=20, height=400, bg='White')
c1.pack(side=RIGHT)
c1 = Canvas(root, width=10, height=400, bg='orange')
c1.pack(side=RIGHT)

root.geometry("800x450+500+100")

try:
    t = threading.Thread(name='child', target=text2speech, args=())
    if not t.is_alive():
        t.start()
except:
    pass
root.resizable('false','false')
root.mainloop()