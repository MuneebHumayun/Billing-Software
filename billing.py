from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#B3FFAB,#ff99cc"
        title=Label(self.root,text="Billing Software",font=("Regular 400",30,"bold"),bg=bg_color,fg="white")
        title.place(x=0,y=0,relwidth=1)

        #=======Variables===========
        #========Stationary===========
        self.pencil=IntVar()
        self.scale=IntVar()
        self.marker=IntVar()
        self.pen=IntVar()
        self.ink=IntVar()
        self.remover=IntVar()
        self.box=IntVar()

        #========grocery=========
        self.wheat=IntVar()
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.pulses=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        self.milk=IntVar()
        
        #=======baverages========
        self.pepsi=IntVar()
        self.svnup=IntVar()
        self.marinda=IntVar()
        self.dew=IntVar()
        self.sprite=IntVar()
        self.slice=IntVar()
        self.nesfruta=IntVar()

        #========total and tax======
        self.stationary_price=StringVar()
        self.grocery_price=StringVar()
        self.baverages_price=StringVar()

        self.stationary_tax=StringVar()
        self.grocery_tax=StringVar()
        self.baverages_tax=StringVar()

        #======customer=========
        self.c_name=StringVar()
        self.c_phn=StringVar()

        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()

        
        #=====Customer Detail Frame=======
        F1=LabelFrame(self.root,text="Customer Details",font=("Regular 400",12,"bold"),bg=bg_color,fg="white")
        F1.place(x=0,y=70,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",font=("Regular 400",15,"bold"),bg=bg_color,fg="white").grid(row=0,column=0, padx=20, pady=5)
        cname_txt=Entry(F1, width=20,textvariable=self.c_name, font="arial 13").grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl=Label(F1,text="Customer Phone No.",font=("Regular 400",15,"bold"),bg=bg_color,fg="white").grid(row=0,column=2, padx=20, pady=5)
        cphn_txt=Entry(F1, width=20, textvariable=self.c_phn, font="arial 13").grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl=Label(F1,text="Bill Number",font=("Regular 400",15,"bold"),bg=bg_color,fg="white").grid(row=0,column=4, padx=20, pady=5)
        c_bill_txt=Entry(F1, width=20, textvariable=self.search_bill, font="arial 13").grid(row=0, column=5, pady=5, padx=10)

        bill_btn=Button(F1, command=self.find_bill,text="Search", width=12, font="arial 12 bold", bg="#016A6A", fg="white").grid(row=0, column=6)
    #=====Stationary Item Frame======
        F2=LabelFrame(self.root,text="Stationary Items",font=("Regular 400",12,"bold"),bg=bg_color,fg="white")
        F2.place(x=5,y=150,width=330,height=380)
        
        lbl_pencil=Label(F2,text="Pencil",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_pencil.grid(row=0,column=0,pady=10,padx=10,sticky="w") 

        txt_pencil=Entry(F2,width=15, textvariable=self.pencil,font=("Segeo UI",16,"bold"))
        txt_pencil.grid(row=0,column=1,pady=10,padx=10,sticky="w") 

        lbl_scale=Label(F2,text="Scale",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_scale.grid(row=2,column=0,pady=10,padx=10,sticky="w") 

        txt_scale=Entry(F2,width=15,textvariable=self.scale,font=("Segeo UI",16,"bold"))
        txt_scale.grid(row=2,column=1,pady=10,padx=10,sticky="w")

        lbl_marker=Label(F2,text="Marker",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_marker.grid(row=3,column=0,pady=10,padx=10,sticky="w") 

        txt_marker=Entry(F2,width=15,textvariable=self.marker,font=("Segeo UI",16,"bold"))
        txt_marker.grid(row=3,column=1,pady=10,padx=10,sticky="w")

        lbl_pen=Label(F2,text="Pen",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_pen.grid(row=4,column=0,pady=10,padx=10,sticky="w") 

        txt_pen=Entry(F2,width=15,textvariable=self.pen,font=("Segeo UI",16,"bold"))
        txt_pen.grid(row=4,column=1,pady=10,padx=10,sticky="w")

        lbl_ink=Label(F2,text="Ink",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_ink.grid(row=5,column=0,pady=10,padx=10,sticky="w") 

        txt_ink=Entry(F2,width=15,textvariable=self.ink,font=("Segeo UI",16,"bold"))
        txt_ink.grid(row=5,column=1,pady=10,padx=10,sticky="w")

        lbl_remover=Label(F2,text="Remover",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_remover.grid(row=6,column=0,pady=10,padx=10,sticky="w") 

        txt_remover=Entry(F2,width=15,textvariable=self.remover,font=("Segeo UI",16,"bold"))
        txt_remover.grid(row=6,column=1,pady=10,padx=10,sticky="w")

        lbl_box=Label(F2,text="Box",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_box.grid(row=7,column=0,pady=10,padx=10,sticky="w") 

        txt_box=Entry(F2,width=15,textvariable=self.box,font=("Segeo UI",16,"bold"))
        txt_box.grid(row=7,column=1,pady=10,padx=10,sticky="w")

        #=====Grocery Frame======
        F3=LabelFrame(self.root,text="Grocery",font=("Regular 400",12,"bold"),bg=bg_color,fg="white")
        F3.place(x=340,y=150,width=325,height=380)
        
        lbl_rice=Label(F3,text="Rice",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_rice.grid(row=0,column=0,pady=10,padx=10,sticky="w") 

        txt_rice=Entry(F3,width=15,textvariable=self.rice,font=("Segeo UI",16,"bold"))
        txt_rice.grid(row=0,column=1,pady=10,padx=10,sticky="w") 

        lbl_oil=Label(F3,text="Food Oil",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_oil.grid(row=2,column=0,pady=10,padx=10,sticky="w") 

        txt_oil=Entry(F3,width=15,textvariable=self.food_oil,font=("Segeo UI",16,"bold"))
        txt_oil.grid(row=2,column=1,pady=10,padx=10,sticky="w")

        lbl_pulses=Label(F3,text="Pulses",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_pulses.grid(row=3,column=0,pady=10,padx=10,sticky="w") 

        txt_pulses=Entry(F3,width=15,textvariable=self.pulses,font=("Segeo UI",16,"bold"))
        txt_pulses.grid(row=3,column=1,pady=10,padx=10,sticky="w")

        lbl_wheat=Label(F3,text="Wheat",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_wheat.grid(row=4,column=0,pady=10,padx=10,sticky="w") 

        txt_wheat=Entry(F3,width=15,textvariable=self.wheat,font=("Segeo UI",16,"bold"))
        txt_wheat.grid(row=4,column=1,pady=10,padx=10,sticky="w")

        lbl_sugar=Label(F3,text="Sugar",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_sugar.grid(row=5,column=0,pady=10,padx=10,sticky="w") 

        txt_sugar=Entry(F3,width=15,textvariable=self.sugar,font=("Segeo UI",16,"bold"))
        txt_sugar.grid(row=5,column=1,pady=10,padx=10,sticky="w")

        lbl_tea=Label(F3,text="Tea",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_tea.grid(row=6,column=0,pady=10,padx=10,sticky="w") 

        txt_tea=Entry(F3,width=15,textvariable=self.tea,font=("Segeo UI",16,"bold"))
        txt_tea.grid(row=6,column=1,pady=10,padx=10,sticky="w")

        lbl_milk=Label(F3,text="Milk",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_milk.grid(row=7,column=0,pady=10,padx=10,sticky="w") 

        txt_milk=Entry(F3,width=15,textvariable=self.milk,font=("Segeo UI",16,"bold"))
        txt_milk.grid(row=7,column=1,pady=10,padx=10,sticky="w")

         #=====Baverages Frame======
        F4=LabelFrame(self.root,text="Baverages",font=("Regular 400",12,"bold"),bg=bg_color,fg="white")
        F4.place(x=670,y=150,width=325,height=380)
        
        lbl_pepsi=Label(F4,text="Pepsi",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_pepsi.grid(row=0,column=0,pady=10,padx=10,sticky="w") 

        txt_pepsi=Entry(F4,width=15,textvariable=self.pepsi,font=("Segeo UI",16,"bold"))
        txt_pepsi.grid(row=0,column=1,pady=10,padx=10,sticky="w") 

        lbl_7up=Label(F4,text="7Up",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_7up.grid(row=2,column=0,pady=10,padx=10,sticky="w") 

        txt_7up=Entry(F4,width=15,textvariable=self.svnup,font=("Segeo UI",16,"bold"))
        txt_7up.grid(row=2,column=1,pady=10,padx=10,sticky="w")

        lbl_marinda=Label(F4,text="Marinda",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_marinda.grid(row=3,column=0,pady=10,padx=10,sticky="w") 

        txt_marinda=Entry(F4,width=15,textvariable=self.marinda,font=("Segeo UI",16,"bold"))
        txt_marinda.grid(row=3,column=1,pady=10,padx=10,sticky="w")

        lbl_dew=Label(F4,text="Dew",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_dew.grid(row=4,column=0,pady=10,padx=10,sticky="w") 

        txt_dew=Entry(F4,width=15,textvariable=self.dew,font=("Segeo UI",16,"bold"))
        txt_dew.grid(row=4,column=1,pady=10,padx=10,sticky="w")

        lbl_sprite=Label(F4,text="Sprite",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_sprite.grid(row=5,column=0,pady=10,padx=10,sticky="w") 

        txt_sprite=Entry(F4,width=15,textvariable=self.sprite,font=("Segeo UI",16,"bold"))
        txt_sprite.grid(row=5,column=1,pady=10,padx=10,sticky="w")

        lbl_slice=Label(F4,text="Slice",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_slice.grid(row=6,column=0,pady=10,padx=10,sticky="w") 

        txt_slice=Entry(F4,width=15,textvariable=self.slice,font=("Segeo UI",16,"bold"))
        txt_slice.grid(row=6,column=1,pady=10,padx=10,sticky="w")

        lbl_nes=Label(F4,text="Nesfruta",bg=bg_color,fg="white",font=("Segeo UI",16,"bold"))
        lbl_nes.grid(row=7,column=0,pady=10,padx=10,sticky="w") 

        txt_nes=Entry(F4,width=15,textvariable=self.nesfruta,font=("Segeo UI",16,"bold"))
        txt_nes.grid(row=7,column=1,pady=10,padx=10,sticky="w")

        F5=Frame(self.root, bd=4, relief=GROOVE)
        F5.place(x=1000,y=150,width=340,height=380)
        bill_title=Label(F5,text="Bill Receipt",font="arial 15 bold").pack(fill=X)
        scroll_y=Scrollbar(F5, orient=VERTICAL)
        self.txtrcpt=Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtrcpt.yview)
        self.txtrcpt.pack(fill=BOTH,expand=1)

        #===========buttonframe============
        F6=LabelFrame(self.root,text="Bill Menu",font=("Regular 400",12,"bold"),bg=bg_color,fg="white")
        F6.place(x=0,y=540,relwidth=1,height=155)
        m1=Label(F6,text="Total Stationary Price",bg=bg_color,fg="white",font=("Segeo UI",15,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        txt_m1=Entry(F6,width=12,textvariable=self.stationary_price,font=("Segeo UI",14,"bold"))
        txt_m1.grid(row=0,column=1,pady=10,padx=10,sticky="w")

        m2=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("Segeo UI",15,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        txt_m2=Entry(F6,width=12,textvariable=self.grocery_price,font=("Segeo UI",14,"bold"))
        txt_m2.grid(row=2,column=1,pady=10,padx=10,sticky="w")

        m3=Label(F6,text="Total Baverages Price",bg=bg_color,fg="white",font=("Segeo UI",15,"bold")).grid(row=3,column=0,padx=20,pady=1,sticky="w")
        txt_m3=Entry(F6,width=12,textvariable=self.baverages_price,font=("Segeo UI",14,"bold"))
        txt_m3.grid(row=3,column=1,pady=10,padx=10,sticky="w")

        c1=Label(F6,text="Stationary Tax",bg=bg_color,fg="white",font=("Segeo UI",15,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        txt_c1=Entry(F6,width=12,textvariable=self.stationary_tax,font=("Segeo UI",14,"bold"))
        txt_c1.grid(row=0,column=3,pady=10,padx=10,sticky="w")

        c2=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("Segeo UI",15,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        txt_c2=Entry(F6,width=12,textvariable=self.grocery_tax,font=("Segeo UI",14,"bold"))
        txt_c2.grid(row=2,column=3,pady=10,padx=10,sticky="w")

        c3=Label(F6,text="Baverages Tax",bg=bg_color,fg="white",font=("Segeo UI",15,"bold")).grid(row=3,column=2,padx=20,pady=1,sticky="w")
        txt_c3=Entry(F6,width=12,textvariable=self.baverages_tax,font=("Segeo UI",14,"bold"))
        txt_c3.grid(row=3,column=3,pady=10,padx=10,sticky="w")

        btn_f=Frame(F6, bg="cadetblue")
        btn_f.place(x=750, width=580, height=125)

        total_btn=Button(btn_f,command=self.total,text="Total",bg="#016A6A",fg="white",pady=10,width=10,font="arial 14 bold").grid(row=0,column=0,pady=30,padx=5)
        GBill_btn=Button(btn_f,command=self.bill_reciept,text="Generate Bill",bg="#016A6A",fg="white",pady=10,width=10,font="arial 14 bold").grid(row=0,column=1,pady=30,padx=5)
        clear_btn=Button(btn_f,command=self.clear,text="Clear",bg="#016A6A",fg="white",pady=10,width=10,font="arial 14 bold").grid(row=0,column=2,pady=30,padx=5)
        exit_btn=Button(btn_f,command=self.Exit_App,text="Exit",bg="#016A6A",fg="white",pady=10,width=10,font="arial 14 bold").grid(row=0,column=3,pady=30,padx=5)
        self.welcome_bill()
    def total(self):
        self.s_pl=self.pencil.get()*15
        self.s_s=self.scale.get()*20
        self.s_m=self.marker.get()*10
        self.s_pn=self.pen.get()*50
        self.s_r=self.remover.get()*25
        self.s_i=self.ink.get()*40
        self.s_b=self.box.get()*50
        self.total_stationary_price=float(
                                         self.s_pl+
                                         self.s_s+
                                         self.s_m+
                                         self.s_pn+
                                         self.s_r+
                                         self.s_i+
                                         self.s_b
                                         )    
        self.stationary_price.set("Rs. "+str(self.total_stationary_price))
        self.stationary_tax.set("Rs. "+str(round((self.total_stationary_price*0.05),2)))
        
        self.g_r=self.rice.get()*130
        self.g_f_o=self.food_oil.get()*200
        self.g_w=self.wheat.get()*70
        self.g_p=self.pulses.get()*150
        self.g_su=self.sugar.get()*80
        self.g_t=self.tea.get()*100
        self.g_mi=self.milk.get()*120
        self.total_grocery_price=float(
                                      self.g_r+
                                      self.g_f_o+
                                      self.g_w+
                                      self.g_p+
                                      self.g_su+
                                      self.g_t+
                                      self.g_mi
                                      )    
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.grocery_tax.set("Rs. "+str(round((self.total_grocery_price*0.05),2)))

        self.b_pep=self.pepsi.get()*90
        self.b_up=self.svnup.get()*90
        self.b_d=self.dew.get()*90
        self.b_sp=self.sprite.get()*90
        self.b_mn=self.marinda.get()*90
        self.b_sl=self.slice.get()*110
        self.b_nf=self.nesfruta.get()*150
        self.total_baverages_price=float(
                                        self.b_pep+
                                        self.b_up+
                                        self.b_d+
                                        self.b_sp+
                                        self.b_mn+
                                        self.b_sl+
                                        self.b_nf
                                        )    
        self.baverages_price.set("Rs. "+str(self.total_baverages_price))
        self.baverages_tax.set("Rs. "+str(round((self.total_baverages_price*0.05),2)))                         
        
        self.total__bill=float( self.total_stationary_price+
                               self.total_grocery_price+
                               self.total_baverages_price
                            )  


    def welcome_bill(self):
        self.txtrcpt.delete('1.0', END)
        self.txtrcpt.insert(END,"\tWelcome MMH Developer Retail\n")
        self.txtrcpt.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtrcpt.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtrcpt.insert(END,f"\n Phone Number : {self.c_phn.get()}")
        self.txtrcpt.insert(END,f"\n======================================")
        self.txtrcpt.insert(END,f"\n Products\t\tQuantity\t\tPrice")
        self.txtrcpt.insert(END,f"\n======================================")


    def bill_reciept(self):
        if self.c_name.get()=="" and self.c_phn.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.stationary_price.get()=="" and self.grocery_price.get()=="" and self.baverages_price.get()=="":
              messagebox.showerror("Error","No product selected")   
        else:
            self.welcome_bill()

    #======Stationary=======
        if self.pencil.get()!=0:
            self.txtrcpt.insert(END,f"\n Pencil\t\t{self.pencil.get()}\t\t{self.s_pl}")
        
        if self.scale.get()!=0:
            self.txtrcpt.insert(END,f"\n Scale\t\t{self.scale.get()}\t\t{self.s_s}")

        if self.marker.get()!=0:
            self.txtrcpt.insert(END,f"\n Marker\t\t{self.marker.get()}\t\t{self.s_m}")

        if self.pen.get()!=0:
            self.txtrcpt.insert(END,f"\n Pen\t\t{self.pen.get()}\t\t{self.s_pn}")

        if self.remover.get()!=0:
            self.txtrcpt.insert(END,f"\n Remover\t\t{self.remover.get()}\t\t{self.s_r}")

        if self.ink.get()!=0:
            self.txtrcpt.insert(END,f"\n Ink\t\t{self.ink.get()}\t\t{self.s_i}")

        if self.box.get()!=0:
            self.txtrcpt.insert(END,f"\n Box\t\t{self.box.get()}\t\t{self.s_b}")
    #======grocery=============
        if self.rice.get()!=0:
            self.txtrcpt.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r}")
        
        if self.food_oil.get()!=0:
            self.txtrcpt.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_o}")
        
        if self.wheat.get()!=0:
            self.txtrcpt.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w}")
        
        if self.pulses.get()!=0:
            self.txtrcpt.insert(END,f"\n Pulses\t\t{self.pulses.get()}\t\t{self.g_p}")

        if self.sugar.get()!=0:
            self.txtrcpt.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_su}")
        
        if self.tea.get()!=0:
            self.txtrcpt.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t}")

        if self.milk.get()!=0:
            self.txtrcpt.insert(END,f"\n Milk\t\t{self.milk.get()}\t\t{self.g_mi}")
    
    #=======baverages=========
        if self.pepsi.get()!=0:
            self.txtrcpt.insert(END,f"\n Pepsi\t\t{self.pepsi.get()}\t\t{self.b_pep}")
        
        if self.svnup.get()!=0:
            self.txtrcpt.insert(END,f"\n 7up\t\t{self.svnup.get()}\t\t{self.b_up}")
        
        if self.marinda.get()!=0:
            self.txtrcpt.insert(END,f"\n Marinda\t\t{self.marinda.get()}\t\t{self.b_mn}")

        if self.sprite.get()!=0:
            self.txtrcpt.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.b_sp}")

        if self.dew.get()!=0:
            self.txtrcpt.insert(END,f"\n Dew\t\t{self.dew.get()}\t\t{self.b_d}")

        if self.slice.get()!=0:
            self.txtrcpt.insert(END,f"\n Slice\t\t{self.slice.get()}\t\t{self.b_sl}")

        if self.nesfruta.get()!=0:
            self.txtrcpt.insert(END,f"\n Nesfruta\t\t{self.nesfruta.get()}\t\t{self.b_nf}")

        self.txtrcpt.insert(END,f"\n--------------------------------------")
        if self.stationary_tax.get()!='Rs. 0.0':
            self.txtrcpt.insert(END,f"\n Stationary Tax\t\t\t{self.stationary_tax.get()}")
        if self.grocery_tax.get()!='Rs. 0.0':
            self.txtrcpt.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
        if self.baverages_tax.get()!='Rs. 0.0':
            self.txtrcpt.insert(END,f"\n Baverages Tax\t\t\t{self.baverages_tax.get()}")
            self.txtrcpt.insert(END,f"\n--------------------------------------")
            self.txtrcpt.insert(END,f"\n Total Bill : \t\t\t Rs. {str(self.total__bill)}")    
            self.txtrcpt.insert(END,f"\n--------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtrcpt.get("1.0",END)
            f1=open("Bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No : {self.bill_no.get()} saved successfully")
        else:
            return
    
    def find_bill(self):
        present="no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"Bills/{i}","r")
                self.txtrcpt.delete('1.0',END)
                for d in f1:
                    self.txtrcpt.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
                messagebox.showerror("Error","Invalid Bill No.")



    def clear(self):
        self.pencil.set("")
        self.scale.set("")
        self.marker.set("")
        self.pen.set("")
        self.ink.set("")
        self.remover.set("")
        self.box.set("")

        #========grocery=========
        self.wheat.set("")
        self.rice.set("")
        self.food_oil.set("")
        self.pulses.set("")
        self.sugar.set("")
        self.tea.set("")
        self.milk.set("")
        
        #=======baverages========
        self.pepsi.set("")
        self.svnup.set("")
        self.marinda.set("")
        self.dew.set("")
        self.sprite.set("")
        self.slice.set("")
        self.nesfruta.set("")

        #========total and tax======
        self.stationary_price.set("")
        self.grocery_price.set("")
        self.baverages_price.set("")

        self.stationary_tax.set("")
        self.grocery_tax.set("")
        self.baverages_tax.set("")
        self.c_name.set("")
        self.c_phn.set("")
        self.bill_no.set("")
        self.search_bill.set("")
        self.welcome_bill()

    def Exit_App(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy



root=Tk()
obj=Bill_App(root)
root.mainloop()