import tkinter as tk
import copy
from tkinter import *
from tkinter import ttk
import datetime
from PIL import ImageTk , Image
class MyApp:
    def __init__(self):
        self.window=Tk()
        #size window
        self.coefficient=9/10
        self.screen_width=self.window.winfo_screenwidth()+100
        self.screen_height=self.window.winfo_screenheight()
        self.width=int(self.screen_width*self.coefficient)
        self.height=int(self.screen_height*self.coefficient)
        self.title_size=self.automate_size(50)
        self.text_M_size=self.automate_size(30)
        self.text_C_size=self.automate_size(17)
        self.label_text_size=self.automate_size(15)
        self.padding=self.automate_height(100)
        self.height_p=self.automate_height(5)
        self.height_p_c=self.automate_height(10)
        self.width_line=self.automate_width(5)
        #title
        self.title="Cytro"
        #path
        self.logo_path="images/Cytro.ico"
        self.image_path=""
        #color 
        self.button_C_background_color="light blue"
        self.button_C_color="grey"
        self.title_color="#55ffff"
        self.border_color="light blue"
        self.title_font_style="italic bold"
        self.font_style="italic"
        self.background_color="grey"
        self.button_M_background_color="pink"
        self.label_text_color="black"
        self.entry_text_color="black"
        self.label_background_color="light blue"
        self.button_M_color="black"
        self.text_familly="matey"
        #other proprieties
        self.data_entries=[]
        self.current_dd_mm_yy=[]
        self.given_dd_mm_yy=[]
        self.images=[]
        #window
        self.window.title(self.title)
        self.window.iconbitmap(self.logo_path)
        self.window.geometry(f"{self.width}x{self.height}+{(self.screen_width-self.width)//2}+{(self.screen_height*9//10-self.height)//2}")
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
    def create_title(self,this_text:str,por:int)->None:
        por=self.automate_height(por)
        self.canvas.create_text(self.width/2,self.height/por,text=this_text,font=(self.text_familly,self.title_size,self.title_font_style),fill=self.title_color)   
    def create_menu(self):
        # create title 
        self.create_title("Menu",self.height_p)
        #create buttons
        button_calculer=Button(self.canvas,text="Calculer",bg=self.button_M_background_color,fg=self.button_M_color,font=(self.text_familly,self.text_M_size,self.font_style),width=self.automate_width(20),command=self.button_calculer)
        button_historique=Button(self.canvas,text="Historique",bg=self.button_M_background_color,fg=self.button_M_color,font=(self.text_familly,self.text_M_size,self.font_style),width=self.automate_width(20))
        self.canvas.create_window(self.width/2,self.height/5+self.padding,window=button_calculer)
        self.canvas.create_window(self.width/2,self.height/5+2*self.padding,window=button_historique)
        #create border
        self.canvas.create_line(self.width/2-self.automate_width(100),self.height/self.height_p,self.width/2-self.automate_width(300) , self.height/self.height_p,fill=self.border_color,width=self.width_line)
        self.canvas.create_line(self.width/2-self.automate_width(300),self.height/self.height_p-self.automate_height(2),self.width/2-self.automate_width(300),self.height/self.height_p+self.automate_height(303),fill=self.border_color,width=self.width_line)
        self.canvas.create_line(self.width/2-self.automate_width(300),self.height/self.height_p+self.automate_height(300),self.width/2+self.automate_width(300),self.height/self.height_p+self.automate_height(300),fill=self.border_color,width=self.width_line)
        self.canvas.create_line(self.width/2+self.automate_width(300),self.height/self.height_p+self.automate_height(303),self.width/2+self.automate_width(300),self.height/self.height_p-self.automate_height(2),fill=self.border_color,width=self.width_line)
        self.canvas.create_line(self.width/2+self.automate_width(300),self.height/self.height_p,self.width/2+self.automate_width(100) , self.height/self.height_p,fill=self.border_color,width=self.width_line)
    def create_form(self):
        self.current_focus_entry,self.next_focus_entry=-1,-1
        self.index_focus_combobox=-1
        self.entries_form=[] # 0->entry_consommation_RADEEJ 1->entry_prix_RADEEJ 2->entry_etat_initial_compteur 3->entry_etat_final_compteur 4->entry_etat_initial_compteur_Mohcine 5->entry_etat_final_compteur_Mohcine 6->entry_etat_initial_compteur_Mustafa 7->entry_etat_final_compteur_Mustafa
        self.date=[]# 0->day 1->mounth 2->year
        self.create_title("insérer vos informations",self.height_p_c)
        frame_form=Frame(self.canvas,bd=2,relief="raised")
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
        if not self.data_entries :
            self.data_entries=[-1 for _ in range(len(self.entries_form))]
        else :
            for index in range(len(self.data_entries)):
                if self.data_entries[index]>=0:
                    if index==1:
                        self.entries_form[index].delete(0,END)
                        self.entries_form[index].config(fg=self.entry_text_color)
                    self.entries_form[index].insert(0,self.data_entries[index])
        label_line_4=Label(frame_form,text="_____________________________________________________________")
        label_line_4.pack()
        #add ComboBox  date
        self.current_dd_mm_yy=list(reversed(list(map(int,str(datetime.datetime.now()).split()[0].split('-')))))
        if not self.given_dd_mm_yy:
            self.given_dd_mm_yy=copy.copy(self.current_dd_mm_yy)
        frame_date=Frame(frame_form)
        label_date=Label(frame_date,font=(self.text_familly,self.label_text_size,self.font_style),fg=self.label_text_color,bg=self.label_background_color,relief="solid",text="Date (Jour/Mois/Année) : ",width=40)
        label_date.grid(row=0,column=0,padx=20)
        frame_date_combo_box=Frame(frame_date)
        self.date.append(ttk.Combobox(frame_date_combo_box,value=["01","02","03","04","05","06","07","08","09"]+list(range(10,32)),font=(self.text_familly,self.label_text_size,self.font_style),width=7))
        self.date[0].current(self.given_dd_mm_yy[0]-1)
        self.date[0].grid(row=0,column=0)
        self.date.append(ttk.Combobox(frame_date_combo_box,value=["01","02","03","04","05","06","07","08","09","10","11","12"],font=(self.text_familly,self.label_text_size,self.font_style),width=8))
        self.date[1].current(self.given_dd_mm_yy[1]-1)
        self.date[1].grid(row=0,column=1)
        self.date.append(ttk.Combobox(frame_date_combo_box,value=[self.current_dd_mm_yy[2]-1,self.current_dd_mm_yy[2]],font=(self.text_familly,self.label_text_size,self.font_style),width=8,validatecommand=self.check_date_combobox))
        self.date[2].current(1-self.current_dd_mm_yy[2]+self.given_dd_mm_yy[2])
        self.date[2].grid(row=0,column=2)
        frame_date_combo_box.grid(row=0,column=1,padx=10)
        frame_date.pack(pady=15)
        self.canvas.create_window(self.width*4/10,self.height*9/20+self.padding*3/4,window=frame_form)
        #bind the ComboBox
        self.date[0].bind("<Button-1>",self.jj_bind)
        self.date[1].bind("<Button-1>",self.mm_bind)
        self.date[2].bind("<Button-1>",self.yy_bind)
        
        self.date[0].bind("<<ComboboxSelected>>",self.check_date_combobox)
        self.date[1].bind("<<ComboboxSelected>>",self.check_date_combobox)
        self.date[2].bind("<<ComboboxSelected>>",self.check_date_combobox)
        
        for combobox in self.date:
            combobox.bind("<FocusIn>",self.check_date_combobox)
            combobox.bind("<FocusOut>",self.check_date_combobox)
            combobox.bind("<Right>",self.right_combobox)
            combobox.bind("<Left>",self.left_combobox)
            combobox.bind("<Up>",self.up_combobox)
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
        #add images side
        frame_images=Frame(self.canvas)
        label_images=Label(frame_images,font=(self.text_familly,self.label_text_size*4//3,self.font_style),bd=2,bg=self.label_background_color,fg=self.label_text_color,relief="raised",text="Images",width=13)
        label_images.pack()
        frame_listbox_image=Frame(frame_images)
        my_scroll=Scrollbar(frame_listbox_image,orient=VERTICAL)
        my_scroll.pack(fill=Y,side=RIGHT)
        list_box_images=Listbox(frame_listbox_image,font=("Nordic",10,"italic"),width=28,height=28,yscrollcommand=my_scroll.set)
        my_scroll.config(command=list_box_images.yview)
        list_box_images.pack()
        frame_listbox_image.pack(pady=5)
        label_number_images=Label(frame_images,font=(self.text_familly,self.label_text_size,self.font_style),bd=2,bg=self.label_background_color,fg=self.label_text_color,relief="raised",text=f"N° d'images : {len(self.images)}",width=18)
        label_number_images.pack()
        self.canvas.create_window(self.width*9/10-2,self.height*9/20+self.padding*3/4,window=frame_images)
        #create buttons
        button_menu=Button(self.canvas,fg=self.button_C_color,bg=self.button_C_background_color,font=(self.text_familly,self.text_C_size,self.font_style),text="Menu",width=17,command=self.return_to_menu)
        button_ajouter_image=Button(self.canvas,fg=self.button_C_color,bg=self.button_C_background_color,font=(self.text_familly,self.text_C_size,self.font_style),text="Ajouter une image",width=17)
        button_supprimer_image=Button(self.canvas,fg=self.button_C_color,bg=self.button_C_background_color,font=(self.text_familly,self.text_C_size,self.font_style),text="supprimer une image",width=17)
        button_calculer=Button(self.canvas,fg=self.button_C_color,bg=self.button_C_background_color,font=(self.text_familly,self.text_C_size,self.font_style),text="Calculer",width=17)
        self.canvas.create_window(self.width/8,self.height*17/18,window=button_menu)
        self.canvas.create_window(self.width*3/8,self.height*17/18,window=button_ajouter_image)
        self.canvas.create_window(self.width*5/8,self.height*17/18,window=button_supprimer_image)
        self.canvas.create_window(self.width*7/8,self.height*17/18,window=button_calculer)
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
    def jj_bind(self,*args):
        self.check_date_combobox()        
        self.index_focus_combobox=0
    def mm_bind(self,*args):
        self.check_date_combobox()
        self.index_focus_combobox=1
    def yy_bind(self,*args):
        self.check_date_combobox()
        self.index_focus_combobox=2
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
        if self.current_focus_entry==0:
            self.index_focus_combobox=2
            self.date[2].focus()
            return
        self.next_focus_entry=len(self.entries_form)-(len(self.entries_form)-self.current_focus_entry)%len(self.entries_form)-1
        self.entries_form[self.next_focus_entry].focus()
    def down_entry(self,*args):
        if self.current_focus_entry==len(self.entries_form)-1:
            self.index_focus_combobox=0
            self.date[0].focus()
            return
        self.next_focus_entry=(self.current_focus_entry+1)%len(self.entries_form)
        self.entries_form[self.next_focus_entry].focus()
    def left_combobox(self,*args):
        self.date[self.index_focus_combobox].focus()
        if self.index_focus_combobox==0:
            self.next_focus_entry=len(self.entries_form)-1
            self.entries_form[self.next_focus_entry].focus()
            return
        self.index_focus_combobox=2-(3-self.index_focus_combobox)%3
        self.date[self.index_focus_combobox].focus()
    def right_combobox(self,*args):
        self.date[self.index_focus_combobox].focus()
        if self.index_focus_combobox==2:
            self.next_focus_entry=0
            self.entries_form[self.next_focus_entry].focus()
            return
        self.index_focus_combobox=(self.index_focus_combobox+1)%3
        self.date[self.index_focus_combobox].focus()
    def up_combobox(self,*args):
        self.date[self.index_focus_combobox].focus()
        self.next_focus_entry=len(self.entries_form)-1
        self.entries_form[self.next_focus_entry].focus()    

    #button's functions
    def button_calculer(self):
        self.clean_window()
        self.create_form()
    def return_to_menu(self):
        self.next_focus_entry=(self.current_focus_entry+1)%len(self.entries_form)
        self.can_it_be_number(self.entries_form[self.current_focus_entry].get())
        self.clean_window()
        self.create_menu()
    #other
    def check_date_combobox(self,event=[]):
        if self.index_focus_combobox in range(3):
            try :
                value=int(self.date[self.index_focus_combobox].get().strip())
                if self.index_focus_combobox==0 and value not in range(32):
                    raise ValueError("the day should be between 1 and 31 !!")
                if self.index_focus_combobox==1 and value not in range(13):
                    raise ValueError("the mounth should be between 1 and 12")
                if self.index_focus_combobox==2 and value not in set([self.current_dd_mm_yy[2]-1,self.current_dd_mm_yy[2]]):
                    raise ValueError(f"the year should be {self.current_dd_mm_yy[2]-1} or {self.current_dd_mm_yy[2]}")
                self.given_dd_mm_yy[self.index_focus_combobox]=value
            except :
                if self.index_focus_combobox in range(2):
                    self.date[self.index_focus_combobox].current(self.given_dd_mm_yy[self.index_focus_combobox]-1)
                elif self.index_focus_combobox==2:
                    self.date[self.index_focus_combobox].current(1-self.current_dd_mm_yy[2]+self.given_dd_mm_yy[2])
    def clean_window(self):
        self.canvas.destroy()
        self.create_canvas()
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
            return True 
        except:
            if self.next_focus_entry!=self.current_focus_entry and self.current_focus_entry in range(len(self.entries_form)) and self.next_focus_entry in range(len(self.entries_form)) :
                self.data_entries[self.current_focus_entry]=-1
            return False
    def automate_size(self,size:int)->int:
        return int(self.width*self.height*size//1152//648)
    def automate_width(self,width:int)->int:
        return int(self.width*width//1152)
    def automate_height(self,height:int)->int:
        return int(self.height*height//648)
if __name__=="__main__" :
    app=MyApp()
