import tkinter as tk
from tkinter import *
from PIL import ImageTk , Image
class MyApp:
    def __init__(self):
        #size window
        self.width=1100
        self.height=self.width*720//1028
        self.title_size=50
        self.text_size=30
        self.label_text_size=15
        self.padding=100
        #title
        self.title="Cytro"
        #path
        self.logo_path="images/Cytro.ico"
        self.image_path=""
        #color 
        self.title_color="#55ffff"
        self.border_color="light blue"
        self.title_font_style="italic bold"
        self.font_style="italic"
        self.background_color="grey"
        self.button_background_color="pink"
        self.label_text_color="black"
        self.entry_text_color="black"
        self.label_background_color="light blue"
        self.button_color="black"
        self.text_familly="matey"
        #window
        self.window=Tk()
        self.window.title(self.title)
        self.window.iconbitmap(self.logo_path)
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False,False)
        self.create_canvas()
        self.create_menu()
        self.window.mainloop()
    def create_canvas(self,add_image:bool=False)->None:
        self.canvas=Canvas(self.window,width=self.width,height=self.height,bg=self.background_color)
        if self.image_path and add_image:
            bg=Image.open(self.image_path)
            bg=bg.resize((self.width,self.height),Image.ANTIALIAS)
            bg=ImageTk.PhotoImage(bg)
            self.canvas.create_image(0,0,image=bg,anchor="nw")
        self.canvas.pack()
    def create_button(self,text:str,this_width:int,this_command="")->Button:
        return Button(self.canvas,text=text,bg=self.button_background_color,fg=self.button_color,font=(self.text_familly,self.text_size,self.font_style),width=this_width,command=this_command)
    def create_title(self,this_text:str,height_porcentage:int)->None:
        self.canvas.create_text(self.width/2,self.height/height_porcentage,text=this_text,font=(self.text_familly,self.title_size,self.title_font_style),fill=self.title_color)
    def create_menu(self):
        # create title 
        self.create_title("Menu",5)
        #create buttons
        self.button_calculer=self.create_button("Calculer",20,self.button_calculer)
        self.button_historique=self.create_button("Historique",20)
        self.canvas.create_window(self.width/2,self.height/5+self.padding,window=self.button_calculer)
        self.canvas.create_window(self.width/2,self.height/5+2*self.padding,window=self.button_historique)
        #create border
        self.canvas.create_line(self.width/2-100,self.height/5,self.width/2-300,self.height/5,fill=self.border_color,width=5)
        self.canvas.create_line(self.width/2-300,self.height/5,self.width/2-300,self.height/5+300,fill=self.border_color,width=5)
        self.canvas.create_line(self.width/2-300,self.height/5+300,self.width/2+300,self.height/5+300,fill=self.border_color,width=5)
        self.canvas.create_line(self.width/2+300,self.height/5+300,self.width/2+300,self.height/5,fill=self.border_color,width=5)
        self.canvas.create_line(self.width/2+300,self.height/5,self.width/2+100,self.height/5,fill=self.border_color,width=5)
    def clean_window(self):
        self.canvas.destroy()
        self.create_canvas()
    def button_calculer(self):
        self.clean_window()
        self.create_form()
    def create_form(self):
        self.current_focus_entry,self.next_focus_entry=-1,-1
        self.entries_form=[] # 0->entry_consommation_RADEEJ 1->entry_prix_RADEEJ 2->entry_etat_initial_compteur 3->entry_etat_final_compteur 4->entry_etat_initial_compteur_Mohcine 5->entry_etat_final_compteur_Mohcine 6->entry_etat_initial_compteur_Mustafa 7->entry_etat_final_compteur_Mustafa
        
        self.create_title("insérer vos informations",10)
        
        frame_form=Frame(self.canvas)

        frame_RADEEJ=Frame(frame_form)
        label_consommation_RADEEJ=Label(frame_RADEEJ,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.label_text_color,bg=self.label_background_color,relief="solid",text="Consommation donnée par la RADEEJ : ",width=40)
        label_consommation_RADEEJ.grid(row=0,column=0,padx=20,pady=20)
        frame_RADEEJ_cons=Frame(frame_RADEEJ)
        self.entries_form.append(Entry(frame_RADEEJ_cons,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.entry_text_color,width=25))
        self.entries_form[0].grid(row=0,column=0)
        label_m_RADEEJ=Label(frame_RADEEJ_cons,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.label_text_color,bg="white",relief="sunken",text=" m³ ")
        label_m_RADEEJ.grid(row=0,column=1)
        frame_RADEEJ_cons.grid(row=0,column=1,padx=10)
        
        #new line
        
        label_prix_RADEEJ=Label(frame_RADEEJ,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.label_text_color,bg=self.label_background_color,relief="solid",text="Prix donné par la RADEEJ : ",width=40)
        label_prix_RADEEJ.grid(row=1,column=0,padx=20)
        frame_RADEEJ_prix=Frame(frame_RADEEJ)
        self.entries_form.append(Entry(frame_RADEEJ_prix,font=(self.text_familly,self.label_text_size,self.font_style),fg="grey",width=25))
        self.entries_form[1].insert(0,"si possible")
        self.entries_form[1].grid(row=0,column=0)
        label_DHs_RADEEJ=Label(frame_RADEEJ_prix,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.label_text_color,bg="white",relief="sunken",text="DHs")
        label_DHs_RADEEJ.grid(row=0,column=1)
        frame_RADEEJ_prix.grid(row=1,column=1,padx=10)
        frame_RADEEJ.pack(pady=5)
        
        label_line_1=Label(frame_form,text="_____________________________________________________________")
        label_line_1.pack()
        
        frame_compteur=Frame(frame_form)
        label_etat_initial=Label(frame_compteur,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.label_text_color,bg=self.label_background_color,relief="solid",text="Etat initial du compteur : ",width=40)
        label_etat_initial.grid(row=0,column=0,padx=20,pady=20)
        frame_compteur_initial=Frame(frame_compteur)
        self.entries_form.append(Entry(frame_compteur_initial,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.entry_text_color,width=25))
        self.entries_form[2].grid(row=0,column=0)
        label_m_etat_initial=Label(frame_compteur_initial,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.label_text_color,bg="white",relief="sunken",text=" m³ ")
        label_m_etat_initial.grid(row=0,column=1)
        frame_compteur_initial.grid(row=0,column=1,padx=10)
        
        #new line
        label_etat_final=Label(frame_compteur,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.label_text_color,bg=self.label_background_color,relief="solid",text="Etat final du compteur : ",width=40)
        label_etat_final.grid(row=1,column=0,padx=20)
        frame_compteur_final=Frame(frame_compteur)
        self.entries_form.append(Entry(frame_compteur_final,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.entry_text_color,width=25))
        self.entries_form[3].grid(row=0,column=0)
        label_m_etat_final=Label(frame_compteur_final,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.label_text_color,bg="white",relief="sunken",text=" m³ ")
        label_m_etat_final.grid(row=0,column=1)
        frame_compteur_final.grid(row=1,column=1,padx=10)
        frame_compteur.pack()
        
        label_line_2=Label(frame_form,text="_____________________________________________________________")
        label_line_2.pack()

        frame_compteur_Mohcine=Frame(frame_form)
        label_etat_initial_Mohcine=Label(frame_compteur_Mohcine,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.label_text_color,bg=self.label_background_color,relief="solid",text="Etat initial du compteur de Mohcine : ",width=40)
        label_etat_initial_Mohcine.grid(row=0,column=0,padx=20,pady=20)
        frame_compteur_initial_Mohcine=Frame(frame_compteur_Mohcine)
        self.entries_form.append(Entry(frame_compteur_initial_Mohcine,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.entry_text_color,width=25))
        self.entries_form[4].grid(row=0,column=0)
        label_m_etat_initial_Mohcine=Label(frame_compteur_initial_Mohcine,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.label_text_color,bg="white",relief="sunken",text=" m³ ")
        label_m_etat_initial_Mohcine.grid(row=0,column=1)
        frame_compteur_initial_Mohcine.grid(row=0,column=1,padx=10)
        
        #new line
        
        label_etat_final_Mohcine=Label(frame_compteur_Mohcine,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.label_text_color,bg=self.label_background_color,relief="solid",text="Etat final du compteur de Mohcine : ",width=40)
        label_etat_final_Mohcine.grid(row=1,column=0,padx=20)
        frame_compteur_Mohcine_final=Frame(frame_compteur_Mohcine)
        self.entries_form.append(Entry(frame_compteur_Mohcine_final,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.entry_text_color,width=25))
        self.entries_form[5].grid(row=0,column=0)
        label_m_etat_final_Mohcine=Label(frame_compteur_Mohcine_final,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.label_text_color,bg="white",relief="sunken",text=" m³ ")
        label_m_etat_final_Mohcine.grid(row=0,column=1)
        frame_compteur_Mohcine_final.grid(row=1,column=1,padx=10)
        frame_compteur_Mohcine.pack()

        label_line_3=Label(frame_form,text="_____________________________________________________________")
        label_line_3.pack()

        frame_compteur_Mustafa=Frame(frame_form)
        label_etat_initial_Mustafa=Label(frame_compteur_Mustafa,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.label_text_color,bg=self.label_background_color,relief="solid",text="Etat initial du compteur de Mustafa : ",width=40)
        label_etat_initial_Mustafa.grid(row=0,column=0,padx=20,pady=20)
        frame_compteur_initial_Mustafa=Frame(frame_compteur_Mustafa)
        self.entries_form.append(Entry(frame_compteur_initial_Mustafa,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.entry_text_color,width=25))
        self.entries_form[6].grid(row=0,column=0)
        label_m_etat_initial_Mustafa=Label(frame_compteur_initial_Mustafa,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.label_text_color,bg="white",relief="sunken",text=" m³ ")
        label_m_etat_initial_Mustafa.grid(row=0,column=1)
        frame_compteur_initial_Mustafa.grid(row=0,column=1,padx=10)
        
        #new line
        
        label_etat_final_Mustafa=Label(frame_compteur_Mustafa,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.label_text_color,bg=self.label_background_color,relief="solid",text="Etat final du compteur de Mustafa : ",width=40)
        label_etat_final_Mustafa.grid(row=1,column=0,padx=20)
        frame_compteur_Mustafa_final=Frame(frame_compteur_Mustafa)
        self.entries_form.append(Entry(frame_compteur_Mustafa_final,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.entry_text_color,width=25))
        self.entries_form[7].grid(row=0,column=0)
        label_m_etat_final_Mustafa=Label(frame_compteur_Mustafa_final,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.label_text_color,bg="white",relief="sunken",text=" m³ ")
        label_m_etat_final_Mustafa.grid(row=0,column=1)
        frame_compteur_Mustafa_final.grid(row=1,column=1,padx=10)        
        frame_compteur_Mustafa.pack()

        label_space=Label(frame_form,text="")
        label_space.pack()
        self.canvas.create_window(self.width*4/10,self.height*9/20+self.padding*3/4,window=frame_form)
        self.data_entries=[-1 for _ in range(len(self.entries_form))]
        #bind the enties to get position
        self.entries_form[0].bind("<Button-1>",self.entry_0)
        self.entries_form[1].bind("<Button-1>",self.entry_1)
        self.entries_form[2].bind("<Button-1>",self.entry_2)
        self.entries_form[3].bind("<Button-1>",self.entry_3)
        self.entries_form[4].bind("<Button-1>",self.entry_4)
        self.entries_form[5].bind("<Button-1>",self.entry_5)
        self.entries_form[6].bind("<Button-1>",self.entry_6)
        self.entries_form[7].bind("<Button-1>",self.entry_7)
        #bind the enties
        for index in range(len(self.entries_form)):
                self.entries_form[index].bind("<FocusIn>",self.focus_in_entry)
                self.entries_form[index].bind("<FocusOut>",self.focus_out_entry)
                self.entries_form[index].bind("<Up>",self.up_entry)
                self.entries_form[index].bind("<Down>",self.down_entry)

    #bind's functions to get position
    def entry_0(self,*args):
        self.next_focus_entry=0
    def entry_1(self,*args):
        self.next_focus_entry=1
    def entry_2(self,*args):
        self.next_focus_entry=2
    def entry_3(self,*args):
        self.next_focus_entry=3
    def entry_4(self,*args):
        self.next_focus_entry=4
    def entry_5(self,*args):
        self.next_focus_entry=5
    def entry_6(self,*args):
        self.next_focus_entry=6
    def entry_7(self,*args):
        self.next_focus_entry=7
        
    #bind's functions
    def focus_in_entry(self,*args)->None:
        self.current_focus_entry,self.next_focus_entry=self.next_focus_entry,-1
        if self.current_focus_entry<0 and self.current_focus_entry>=len(self.entries_form):
            return
        if not self.can_it_be_number(self.entries_form[self.current_focus_entry].get()):
            self.entries_form[self.current_focus_entry].delete(0,END)
            self.entries_form[self.current_focus_entry].config(fg=self.entry_text_color)
    def focus_out_entry(self,*args)->None:
        if self.current_focus_entry<0 and self.current_focus_entry>=len(self.entries_form):
            return
        if not self.entries_form[self.current_focus_entry].get() or not self.can_it_be_number(self.entries_form[self.current_focus_entry].get()):
            self.entries_form[self.current_focus_entry].delete(0,END)
            if self.current_focus_entry==1:
                self.entries_form[self.current_focus_entry].config(fg="grey")
                self.entries_form[self.current_focus_entry].insert(0,"si possible")
        self.current_focus_entry=-1
    def up_entry(self,*args):
        self.next_focus_entry=len(self.entries_form)-(len(self.entries_form)-self.current_focus_entry)%len(self.entries_form)-1
        self.entries_form[self.next_focus_entry].focus()
    def down_entry(self,*args):
        self.next_focus_entry=(self.current_focus_entry+1)%len(self.entries_form)
        self.entries_form[self.next_focus_entry].focus()
    #other
    def can_it_be_number(self,string_to_check:str)->bool:
        try :
            number=float(string_to_check)
            if number<0:
                raise ValueError("ces valeurs devraient etre toujours positive !!")
            number=abs(number)
            if self.next_focus_entry!=self.current_focus_entry and self.current_focus_entry in range(len(self.entries_form)) and self.next_focus_entry in range(len(self.entries_form)) :
                self.data_entries[self.current_focus_entry]=number
                self.entries_form[self.current_focus_entry].delete(0,END)
                self.entries_form[self.current_focus_entry].insert(0,number)
                print(self.data_entries)
            return True 
        except:
            if self.next_focus_entry!=self.current_focus_entry and self.current_focus_entry in range(len(self.entries_form)) and self.next_focus_entry in range(len(self.entries_form)) :
                self.data_entries[self.current_focus_entry]=-1
                print(self.data_entries)
            return False
if __name__=="__main__" :
    app=MyApp()