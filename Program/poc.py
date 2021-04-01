from tkinter import *
import numpy as np
import pickle
import json

class Window(Frame):

    def resource_path1(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def resource_path2(relative):
        return os.path.join(os.environ.get("_MEIPASS2",os.path.abspath(".")),relative)

    def resource_path3(relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def __init__(self, master=None):
        Frame.__init__(self, master)   
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("POC - Análise Diabetes")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Exit",command=self.client_exit)
        quitButton.place(x=0, y=0)

        self.label1 = Label(self, text="NUMERO GRAVIDEZ")
        self.label1.place(x=0, y=50)
        self.input1 = Entry(self, bd =5)
        self.input1.insert(END, '1')
        self.input1.place(x=150, y=50)

        self.label2 = Label(self, text="GLICOSE")
        self.label2.place(x=0, y=80)
        self.input2 = Entry(self, bd =5)
        self.input2.insert(END, '103')
        self.input2.place(x=150, y=80)

        self.label3 = Label(self, text="PRESSAO_SANGUINEA")
        self.label3.place(x=0, y=110)
        self.input3 = Entry(self, bd =5)
        self.input3.insert(END, '72')
        self.input3.place(x=150, y=110)

        self.label4 = Label(self, text="ESPESSURA_PELE_TRICEPS")
        self.label4.place(x=0, y=140)
        self.input4 = Entry(self, bd =5)
        self.input4.insert(END, '32')
        self.input4.place(x=150, y=140)

        self.label5 = Label(self, text="INSULINA")
        self.label5.place(x=0, y=170)
        self.input5 = Entry(self, bd =5)
        self.input5.insert(END, '190')
        self.input5.place(x=150, y=170)

        self.label6 = Label(self, text="IMC")
        self.label6.place(x=0, y=200)
        self.input6 = Entry(self, bd =5)
        self.input6.insert(END, '67.7')
        self.input6.place(x=150, y=200)

        self.label7 = Label(self, text="FUNCAO_DIABETES")
        self.label7.place(x=0, y=230)
        self.input7 = Entry(self, bd =5)
        self.input7.insert(END, '0.324')
        self.input7.place(x=150, y=230)

        self.label8 = Label(self, text="IDADE")
        self.label8.place(x=0, y=260)
        self.input8 = Entry(self, bd =5)
        self.input8.insert(END, '0.324')
        self.input8.place(x=150, y=260)

        execButton = Button(self, text="Executar",command=self.execmodel)
        execButton.place(x=50, y=0)

    def client_exit(self):
        exit()

    def execmodel(self):
        data = {}
        data['NUMERO_GRAVIDEZ'] = self.input1.get()
        data['GLICOSE'] = self.input2.get()
        data['PRESSAO_SANGUINEA'] = self.input3.get()
        data['ESPESSURA_PELE_TRICEPS'] = self.input4.get()
        data['INSULINA'] = self.input5.get()
        data['IMC'] = self.input6.get()
        data['FUNCAO_DIABETES'] = self.input7.get()
        data['IDADE'] = self.input8.get()
        
        file = open("modelo.pkl",'rb')
        # file = open(self.resource_path("modelo.pkl"),'rb')

        model = pickle.load(file)
        prediction = model.predict(np.array([list(data.values())]))
        output = prediction[0]
        print({'DIABETES': int(output)})

        msgoutput = StringVar()
        textoutput = Message(self, textvariable=msgoutput, relief=RAISED, width=300 )
        msgoutput.set(f"DIABETES: {int(output)}")
        textoutput.place(x=0, y=290)

root = Tk()
root.geometry("400x400")
app = Window(root)
root.mainloop()  