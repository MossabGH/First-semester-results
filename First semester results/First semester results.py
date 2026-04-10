import tkinter as tk


root=tk.Tk()
root.title("First semester results")
root.geometry("500x430+0+45")
root.config(bg='#4dff00')
root.resizable(False,False)
root.iconbitmap("image/imag_1.ico")


lab_licence=tk.Label(root,text="License 1ére Année",bg="#4dff00",font=("Arail",14))
lab_licence.place(x=35,y=73)

#resultants
lab_rés=tk.Label(text="Resultants du semester",bg="#4dff00",font=("Arail",22))
lab_rés.place(x=100,y=10)

lab_exa=tk.Label(text=" Exam ",bg="white",width="10",height="1")
lab_exa.place(x=245,y=75)

lab_td=tk.Label(text="   TD   ",bg="white",width="10",height="1")
lab_td.place(x=325,y=75)


lab_tp=tk.Label(text="   TP   ",bg="white",width="10",height="1")
lab_tp.place(x=405,y=75)

#les modules
lab_chi=tk.Label(text=" Chime 1 ",bg="white",width="32",height="1")
lab_chi.place(x=10,y=100)

lab_math=tk.Label(text=" Mathématique 1 ",bg="white",width="32",height="1")
lab_math.place(x=10,y=160)

lab_phy=tk.Label(text=" Physique 1 ",bg="white",width="32",height="1")
lab_phy.place(x=10,y=130)

lab_info=tk.Label(text=" Informatique 1 ",bg="white",width="32",height="1")
lab_info.place(x=10,y=190)

lab_ang=tk.Label(text=" Langue Anglaise ",bg="white",width="32",height="1")
lab_ang.place(x=10,y=220)

lab_éth=tk.Label(text=" Dimension éthique et déontologique ",bg="white",width="32",height="1")
lab_éth.place(x=10,y=250)

lab_méth=tk.Label(text=" Méthodogie de la rédaction ",bg="white",width="32",height="1")
lab_méth.place(x=10,y=280)

lab_métiers=tk.Label(text=" Les métiers en sciences et Technoologies ",bg="white",width="32",height="1")
lab_métiers.place(x=10,y=310)



#champs de saisie
#chime
def chick_button(*args):
    if entry_chi_exa.get() and entry_chi_td.get() and entry_chi_tp.get() and entry_phy_exa.get() and entry_phy_td.get() and entry_phy_tp.get() and entry_math_exa.get() and entry_math_td.get() and entry_info_exa.get() and entry_info_tp.get() and entry_ang_exa.get() and entry_éth_exa.get() and entry_méth_exa.get() and entry_métiers_exa.get():
        Calculate.config(text="Calculate",command=calcu,bg="#3de222",width="20",height="1",state=tk.NORMAL,fg="#000000")
    else:
        Calculate.config(text="Calculate",command=calcu,bg="#3de222",width="20",height="1",state=tk.DISABLED,fg="#444444")

            
            
            

def delete():
        #chi
        entry_chi_exa.delete(0, tk.END)
        entry_chi_td.delete(0, tk.END)
        entry_chi_tp.delete(0, tk.END)    
        #phy
        entry_phy_exa.delete(0 ,tk.END)
        entry_phy_td.delete(0 ,tk.END)
        entry_phy_tp.delete(0 ,tk.END)
        #math
        entry_math_exa.delete(0 ,tk.END)
        entry_math_td.delete(0 ,tk.END)
        #info
        entry_info_exa.delete(0 ,tk.END)
        entry_info_tp.delete(0 ,tk.END)
        #ebg
        entry_ang_exa.delete(0 ,tk.END)
        #éth
        entry_éth_exa.delete(0 ,tk.END)
        #méth
        entry_méth_exa.delete(0 ,tk.END)
        #métiers
        entry_métiers_exa.delete(0 ,tk.END)
            
## valid_command          
def validate_entry(value):
    try:
        if value is None or value=="":
            return True
        val=float(value)
        if(0<=val<=20):
            return True
        
        
        else:
            return False
    except ValueError:
        return False
valid_command=root.register(validate_entry)




entry_chi_exa=tk.Entry(root,width='12',highlightbackground="#4dff00",highlightthickness=1,validate="key",validatecommand=(valid_command,'%P'))
entry_chi_exa.place(x=245,y=100)
entry_chi_exa.bind("<KeyRelease>",chick_button)

entry_chi_td=tk.Entry(root,width='12',highlightbackground="#4dff00",highlightthickness=1,validate="key",validatecommand=(valid_command,'%P'))
entry_chi_td.place(x=325,y=100)
entry_chi_td.bind("<KeyRelease>",chick_button)

entry_chi_tp=tk.Entry(root,width='12',highlightbackground="#4dff00",highlightthickness=1,validate="key",validatecommand=(valid_command,'%P'))
entry_chi_tp.place(x=405,y=100)
entry_chi_tp.bind("<KeyRelease>",chick_button)
#physique
entry_phy_exa=tk.Entry(root,width='12',highlightbackground="#4dff00",highlightthickness=1,validate="key",validatecommand=(valid_command,'%P'))
entry_phy_exa.place(x=245,y=130)
entry_phy_exa.bind("<KeyRelease>",chick_button)

entry_phy_td=tk.Entry(root,width='12',highlightbackground="#4dff00",highlightthickness=1,validate="key",validatecommand=(valid_command,'%P'))
entry_phy_td.place(x=325,y=130)
entry_phy_td.bind("<KeyRelease>",chick_button)

entry_phy_tp=tk.Entry(root,width='12',highlightbackground="#4dff00",highlightthickness=1,validate="key",validatecommand=(valid_command,'%P'))
entry_phy_tp.place(x=405,y=130)
entry_phy_tp.bind("<KeyRelease>",chick_button)
#math

entry_math_exa=tk.Entry(root,width='12',highlightbackground="#4dff00",highlightthickness=1,validate="key",validatecommand=(valid_command,'%P'))
entry_math_exa.place(x=245,y=160)
entry_math_exa.bind("<KeyRelease>",chick_button)

entry_math_td=tk.Entry(root,width='12',highlightbackground="#4dff00",highlightthickness=1,validate="key",validatecommand=(valid_command,'%P'))
entry_math_td.place(x=325,y=160)
entry_math_td.bind("<KeyRelease>",chick_button)
#informatique
entry_info_exa=tk.Entry(root,width='12',highlightbackground="#4dff00",highlightthickness=1,validate="key",validatecommand=(valid_command,'%P'))
entry_info_exa.place(x=245,y=190)
entry_info_exa.bind("<KeyRelease>",chick_button)

entry_info_tp=tk.Entry(root,width='12',highlightbackground="#4dff00",highlightthickness=1,validate="key",validatecommand=(valid_command,'%P'))
entry_info_tp.place(x=405,y=190)
entry_info_tp.bind("<KeyRelease>",chick_button)
#Langue Anglaise
entry_ang_exa=tk.Entry(root,width='12',highlightbackground="#4dff00",highlightthickness=1,validate="key",validatecommand=(valid_command,'%P'))
entry_ang_exa.place(x=245,y=220)
entry_ang_exa.bind("<KeyRelease>",chick_button)
#Dimension éthique et déontologique
entry_éth_exa=tk.Entry(root,width='12',highlightbackground="#4dff00",highlightthickness=1,validate="key",validatecommand=(valid_command,'%P'))
entry_éth_exa.place(x=245,y=250)
entry_éth_exa.bind("<KeyRelease>",chick_button)
#Méthodogie de la rédaction
entry_méth_exa=tk.Entry(root,width='12',highlightbackground="#4dff00",highlightthickness=1,validate="key",validatecommand=(valid_command,'%P'))
entry_méth_exa.place(x=245,y=280)
entry_méth_exa.bind("<KeyRelease>",chick_button)
#Les métiers en sciences et Technoologies
entry_métiers_exa=tk.Entry(root,width='12',highlightbackground="#4dff00",highlightthickness=1,validate="key",validatecommand=(valid_command,'%P'))
entry_métiers_exa.place(x=245,y=310)
entry_métiers_exa.bind("<KeyRelease>",chick_button)
def calcu():


    root1=tk.Toplevel()
    root1.title("Academic transcripts")
    root1.geometry("500x600+513+45")
    root1.config(bg='#4dff00')
    root1.resizable(False,False)
    root1.iconbitmap("image/imag_1.ico")
    #chi
    entry_chi_exa1=entry_chi_exa.get()
    entry_chi_td1=entry_chi_td.get()
    entry_chi_tp1=entry_chi_tp.get()
    #phy
    entry_phy_exa1=entry_phy_exa.get()
    entry_phy_td1=entry_phy_td.get()
    entry_phy_tp1=entry_phy_tp.get()
    #math
    entry_math_exa1=entry_math_exa.get()
    entry_math_td1=entry_math_td.get()
    #info
    entry_info_exa1=entry_info_exa.get()
    entry_info_tp1=entry_info_tp.get()
    #ang
    entry_ang_exa1=entry_ang_exa.get()
    #éth
    entry_éth_exa1=entry_éth_exa.get()
    #méth
    entry_méth_exa1=entry_méth_exa.get()
    #métiers
    entry_métiers_exa1=entry_métiers_exa.get()
    

    #------------float------------#
    #chi
    entry_chi_exa1=float(entry_chi_exa1)
    entry_chi_td1=float(entry_chi_td1)
    entry_chi_tp1=float(entry_chi_tp1)
    #phy
    entry_phy_exa1=float(entry_phy_exa1)
    entry_phy_td1=float(entry_phy_td1)
    entry_phy_tp1=float(entry_phy_tp1)
    #MATH
    entry_math_exa1=float(entry_math_exa1)
    entry_math_td1=float(entry_math_td1)
    #info
    entry_info_exa1=float(entry_info_exa1)
    entry_info_tp1=float(entry_info_tp1)
    #ang
    entry_ang_exa1=float(entry_ang_exa1)
    #éth
    entry_éth_exa1=float(entry_éth_exa1)
    #méth
    entry_méth_exa1=float(entry_méth_exa1)
    #métiers
    entry_métiers_exa1=float(entry_métiers_exa1)
    
    #------average------#
    aver_chi=(entry_chi_exa1*0.6)+(entry_chi_td1*0.4)
    aver_chi=round(aver_chi,2)
    aver_phy=(entry_phy_exa1*0.6)+(entry_phy_td1*0.4)
    aver_phy=round(aver_phy,2)
    aver_math=(entry_math_exa1*0.6)+(entry_math_td1*0.4)
    aver_math=round(aver_math,2)
    aver_info=(entry_info_exa1*0.6)+(entry_info_tp1*0.4)
    aver_info=round(aver_info,2)
    u_e_f=(aver_chi*3+aver_phy*3+aver_math*3)/9
    u_e_f=round(u_e_f,2)
    u_e_m=(entry_méth_exa1*1+aver_info*2+entry_phy_tp1*1+entry_chi_tp1*1)/5
    u_e_m=round(u_e_m,2)
    u_e_t=(entry_ang_exa1*1+entry_éth_exa1*1)/2
    u_e_t=round(u_e_t,2)
    u_e_d=entry_métiers_exa1*1
    u_e_d=round(u_e_d,2)
    #---------résultats---------#
    lab_rés=tk.Label(root1,text="Academic transcripts",bg="#4dff00",font=("Arail",22))
    lab_rés.place(x=100,y=10)
    
    lab_exa=tk.Label(root1,text=" Credit ",bg="white",width="10",height="1")
    lab_exa.place(x=245,y=75)

    lab_td=tk.Label(root1,text="  Coef  ",bg="white",width="10",height="1")
    lab_td.place(x=325,y=75)


    lab_tp=tk.Label(root1,text=" Average",bg="white",width="10",height="1")
    lab_tp.place(x=405,y=75)
    
    #---------modules---------#
    lab1_chi=tk.Label(root1,text=" Chime 1 ",bg="white",width="32",height="1")
    lab1_chi.place(x=10,y=100)

    lab1_math=tk.Label(root1,text=" Mathématique 1 ",bg="white",width="32",height="1")
    lab1_math.place(x=10,y=160)

    lab1_phy=tk.Label(root1,text=" Physique 1 ",bg="white",width="32",height="1")
    lab1_phy.place(x=10,y=130)
    
    lab1_u_e_f=tk.Label(root1,text=" (U.E.F)AOOFOOOO1S1 ",bg="white",width="32",height="1")
    lab1_u_e_f.place(x=10,y=190)

    lab1_info=tk.Label(root1,text=" Informatique 1 ",bg="white",width="32",height="1")
    lab1_info.place(x=10,y=220)
    
    lab1_phy_tp=tk.Label(root1,text=" TP Physique 1 ",bg="white",width="32",height="1")
    lab1_phy_tp.place(x=10,y=250)
    
    lab1_chi_tp=tk.Label(root1,text=" TP Chime 1 ",bg="white",width="32",height="1")
    lab1_chi_tp.place(x=10,y=280)
    
    lab1_méth=tk.Label(root1,text=" Méthodogie de la rédaction ",bg="white",width="32",height="1")
    lab1_méth.place(x=10,y=310)
    
    lab1_u_e_m=tk.Label(root1,text=" (U.E.M)AOOMOOOO1S1 ",bg="white",width="32",height="1")
    lab1_u_e_m.place(x=10,y=340)
    
    lab1_ang=tk.Label(root1,text=" Langue Anglaise ",bg="white",width="32",height="1")
    lab1_ang.place(x=10,y=370)

    lab1_éth=tk.Label(root1,text=" Dimension éthique et déontologique ",bg="white",width="32",height="1")
    lab1_éth.place(x=10,y=400)
    
    lab1_u_e_t=tk.Label(root1,text=" (U.E.T)AOOTOOOO1S1 ",bg="white",width="32",height="1")
    lab1_u_e_t.place(x=10,y=430)

    lab1_métiers=tk.Label(root1,text=" Les métiers en sciences et Technoologies ",bg="white",width="32",height="1")
    lab1_métiers.place(x=10,y=460)
    
    lab1_u_e_d=tk.Label(root1,text=" (U.E.D)AOODOOOO1S1 ",bg="white",width="32",height="1")
    lab1_u_e_d.place(x=10,y=490)
    #---lab_résultats----#
    #chhime    
    if(aver_chi>=10):
        lab_aver_chi=tk.Label(root1,text=f'{aver_chi}',fg='green',bg="white",width="10",height="1")
        lab_aver_chi.place(x=405,y=100)
        lab_coef_chi=tk.Label(root1,text='3',width="10",height="1",bg="white")
        lab_coef_chi.place(x=325,y=100)
        lab_cri_chi=tk.Label(root1,text="6",width="10",height="1",bg="white")
        lab_cri_chi.place(x=245,y=100)
        cri_chi=6
    else:
        lab_aver_chi=tk.Label(root1,text=f'{aver_chi}',fg='red',width="10",height="1",bg="white")
        lab_aver_chi.place(x=405,y=100)
        lab_coef_chi=tk.Label(root1,text='3',width="10",height="1",bg="white")
        lab_coef_chi.place(x=325,y=100)
        lab_cri_chi=tk.Label(root1,text="0",width="10",height="1",bg="white")
        lab_cri_chi.place(x=245,y=100)
        cri_chi=0
    #physique
    if(aver_phy>=10):
        lab_aver_phy=tk.Label(root1,text=f'{aver_phy}',fg='green',bg="white",width="10",height="1")
        lab_aver_phy.place(x=405,y=130)
        lab_coef_phy=tk.Label(root1,text='3',width="10",height="1",bg="white")
        lab_coef_phy.place(x=325,y=130)
        lab_cri_phy=tk.Label(root1,text="6",width="10",height="1",bg="white")
        lab_cri_phy.place(x=245,y=130)
        cri_phy=6
    else:
        lab_aver_phy=tk.Label(root1,text=f'{aver_phy}',fg='red',width="10",height="1",bg="white")
        lab_aver_phy.place(x=405,y=130)
        lab_coef_phy=tk.Label(root1,text='3',width="10",height="1",bg="white")
        lab_coef_phy.place(x=325,y=130)
        lab_cri_phy=tk.Label(root1,text="0",width="10",height="1",bg="white")
        lab_cri_phy.place(x=245,y=130)
        cri_phy=0
    #math
    if(aver_math>=10):
        lab_aver_math=tk.Label(root1,text=f'{aver_math}',fg='green',bg="white",width="10",height="1")
        lab_aver_math.place(x=405,y=160)
        lab_coef_math=tk.Label(root1,text='3',width="10",height="1",bg="white")
        lab_coef_math.place(x=325,y=160)
        lab_cri_math=tk.Label(root1,text="6",width="10",height="1",bg="white")
        lab_cri_math.place(x=245,y=160)
        cri_math=6
    else:
        lab_aver_math=tk.Label(root1,text=f'{aver_math}',fg='red',width="10",height="1",bg="white")
        lab_aver_math.place(x=405,y=160)
        lab_coef_math=tk.Label(root1,text='3',width="10",height="1",bg="white")
        lab_coef_math.place(x=325,y=160)
        lab_cri_math=tk.Label(root1,text="0",width="10",height="1",bg="white")
        lab_cri_math.place(x=245,y=160)
        cri_math=0
    #u_e_f
    cri_u_e_f=cri_math+cri_phy+cri_chi
    if(u_e_f>=10):
        lab_u_e_f=tk.Label(root1,text=f'{u_e_f}',fg='green',bg="white",width="10",height="1")
        lab_u_e_f.place(x=405,y=190)
        lab_coef_u_e_f=tk.Label(root1,text='9',width="10",height="1",bg="white")
        lab_coef_u_e_f.place(x=325,y=190)
        lab_cri_u_e_f=tk.Label(root1,text=f"{cri_u_e_f}/18",width="10",height="1",bg="white")
        lab_cri_u_e_f.place(x=245,y=190)
        
    else:
        lab_u_e_f=tk.Label(root1,text=f'{u_e_f}',fg='red',width="10",height="1",bg="white")
        lab_u_e_f.place(x=405,y=190)
        lab_coef_u_e_f=tk.Label(root1,text='9',width="10",height="1",bg="white")
        lab_coef_u_e_f.place(x=325,y=190)
        lab_cri_u_e_f=tk.Label(root1,text=f"{cri_u_e_f}/18",width="10",height="1",bg="white")
        lab_cri_u_e_f.place(x=245,y=190)
    #informatique
    if(aver_info>=10):
        lab_aver_info=tk.Label(root1,text=f'{aver_info}',fg='green',bg="white",width="10",height="1")
        lab_aver_info.place(x=405,y=220)
        lab_coef_info=tk.Label(root1,text='2',width="10",height="1",bg="white")
        lab_coef_info.place(x=325,y=220)
        lab_cri_info=tk.Label(root1,text="4",width="10",height="1",bg="white")
        lab_cri_info.place(x=245,y=220)
        cri_info=4
    else:
        lab_aver_info=tk.Label(root1,text=f'{aver_info}',fg='red',width="10",height="1",bg="white")
        lab_aver_info.place(x=405,y=220)
        lab_coef_info=tk.Label(root1,text='2',width="10",height="1",bg="white")
        lab_coef_info.place(x=325,y=220)
        lab_cri_info=tk.Label(root1,text="0",width="10",height="1",bg="white")
        lab_cri_info.place(x=245,y=220)
        cri_info=0
    #TP physique
    if(entry_phy_tp1>=10):
        lab_phy_tp=tk.Label(root1,text=f'{entry_phy_tp1}',fg='green',bg="white",width="10",height="1")
        lab_phy_tp.place(x=405,y=250)
        lab_coef_phy_tp=tk.Label(root1,text='1',width="10",height="1",bg="white")
        lab_coef_phy_tp.place(x=325,y=250)
        lab_cri_phy_tp=tk.Label(root1,text="2",width="10",height="1",bg="white")
        lab_cri_phy_tp.place(x=245,y=250)
        cri_phy_tp=2
    else:
        lab_phy_tp=tk.Label(root1,text=f'{entry_phy_tp1}',fg='red',width="10",height="1",bg="white")
        lab_phy_tp.place(x=405,y=250)
        lab_coef_phy_tp=tk.Label(root1,text='1',width="10",height="1",bg="white")
        lab_coef_phy_tp.place(x=325,y=250)
        lab_cri_phy_tp=tk.Label(root1,text="0",width="10",height="1",bg="white")
        lab_cri_phy_tp.place(x=245,y=250)
        cri_phy_tp=0
    #TP chime
    if(entry_chi_tp1>=10):
        lab_chi_tp=tk.Label(root1,text=f'{entry_chi_tp1}',fg='green',bg="white",width="10",height="1")
        lab_chi_tp.place(x=405,y=280)
        lab_coef_chi_tp=tk.Label(root1,text='1',width="10",height="1",bg="white")
        lab_coef_chi_tp.place(x=325,y=280)
        lab_cri_chi_tp=tk.Label(root1,text="2",width="10",height="1",bg="white")
        lab_cri_chi_tp.place(x=245,y=280)
        cri_chi_tp=2
    else:
        lab_chi_tp=tk.Label(root1,text=f'{entry_chi_tp1}',fg='red',width="10",height="1",bg="white")
        lab_chi_tp.place(x=405,y=280)
        lab_coef_chi_tp=tk.Label(root1,text='1',width="10",height="1",bg="white")
        lab_coef_chi_tp.place(x=325,y=280)
        lab_cri_chi_tp=tk.Label(root1,text="0",width="10",height="1",bg="white")
        lab_cri_chi_tp.place(x=245,y=280)
        cri_chi_tp=0
    #métho
    if(entry_méth_exa1>=10):
        lab_méth=tk.Label(root1,text=f'{entry_méth_exa1}',fg='green',bg="white",width="10",height="1")
        lab_méth.place(x=405,y=310)
        lab_coef_méth=tk.Label(root1,text='1',width="10",height="1",bg="white")
        lab_coef_méth.place(x=325,y=310)
        lab_cri_méth=tk.Label(root1,text="1",width="10",height="1",bg="white")
        lab_cri_méth.place(x=245,y=310)
        cri_méth=1
    else:
        lab_méth=tk.Label(root1,text=f'{entry_méth_exa1}',fg='red',width="10",height="1",bg="white")
        lab_méth.place(x=405,y=310)
        lab_coef_méth=tk.Label(root1,text='1',width="10",height="1",bg="white")
        lab_coef_méth.place(x=325,y=310)
        lab_cri_méth=tk.Label(root1,text="0",width="10",height="1",bg="white")
        lab_cri_méth.place(x=245,y=310)
        cri_méth=0
    #u_e_m
    cri_u_e_m=cri_méth+cri_phy_tp+cri_chi_tp+cri_info
    if(u_e_m>=10):
        lab_u_e_m=tk.Label(root1,text=f'{u_e_m}',fg='green',bg="white",width="10",height="1")
        lab_u_e_m.place(x=405,y=340)
        lab_coef_u_e_m=tk.Label(root1,text='5',width="10",height="1",bg="white")
        lab_coef_u_e_m.place(x=325,y=340)
        lab_cri_u_e_m=tk.Label(root1,text=f"{cri_u_e_m}/9",width="10",height="1",bg="white")
        lab_cri_u_e_m.place(x=245,y=340)
        
    else:
        lab_u_e_f=tk.Label(root1,text=f'{u_e_f}',fg='red',width="10",height="1",bg="white")
        lab_u_e_f.place(x=405,y=340)
        lab_coef_u_e_f=tk.Label(root1,text='5',width="10",height="1",bg="white")
        lab_coef_u_e_f.place(x=325,y=340)
        lab_cri_u_e_f=tk.Label(root1,text=f"{cri_u_e_f}/9",width="10",height="1",bg="white")
        lab_cri_u_e_f.place(x=245,y=340)
    #ang
    if(entry_ang_exa1>=10):
        lab_ang=tk.Label(root1,text=f'{entry_ang_exa1}',fg='green',bg="white",width="10",height="1")
        lab_ang.place(x=405,y=370)
        lab_coef_ang=tk.Label(root1,text='1',width="10",height="1",bg="white")
        lab_coef_ang.place(x=325,y=370)
        lab_cri_ang=tk.Label(root1,text="1",width="10",height="1",bg="white")
        lab_cri_ang.place(x=245,y=370)
        cri_ang=1
    else:
        lab_ang=tk.Label(root1,text=f'{entry_ang_exa1}',fg='red',width="10",height="1",bg="white")
        lab_ang.place(x=405,y=370)
        lab_coef_ang=tk.Label(root1,text='1',width="10",height="1",bg="white")
        lab_coef_ang.place(x=325,y=370)
        lab_cri_ang=tk.Label(root1,text="0",width="10",height="1",bg="white")
        lab_cri_ang.place(x=245,y=370)
        cri_ang=0
    #éth
    if(entry_éth_exa1>=10):
        lab_éth=tk.Label(root1,text=f'{entry_éth_exa1}',fg='green',bg="white",width="10",height="1")
        lab_éth.place(x=405,y=400)
        lab_coef_éth=tk.Label(root1,text='1',width="10",height="1",bg="white")
        lab_coef_éth.place(x=325,y=400)
        lab_cri_éth=tk.Label(root1,text="1",width="10",height="1",bg="white")
        lab_cri_éth.place(x=245,y=400)
        cri_éth=1
    else:
        lab_éth=tk.Label(root1,text=f'{entry_éth_exa1}',fg='red',width="10",height="1",bg="white")
        lab_éth.place(x=405,y=400)
        lab_coef_éth=tk.Label(root1,text='1',width="10",height="1",bg="white")
        lab_coef_éth.place(x=325,y=400)
        lab_cri_éth=tk.Label(root1,text="0",width="10",height="1",bg="white")
        lab_cri_éth.place(x=245,y=400)
        cri_éth=0
    #u_e_t
    cri_u_e_t=cri_ang+cri_éth
    if(u_e_t>=10):
        lab_u_e_t=tk.Label(root1,text=f'{u_e_t}',fg='green',bg="white",width="10",height="1")
        lab_u_e_t.place(x=405,y=430)
        lab_coef_u_e_t=tk.Label(root1,text='2',width="10",height="1",bg="white")
        lab_coef_u_e_t.place(x=325,y=430)
        lab_cri_u_e_t=tk.Label(root1,text=f"{cri_u_e_t}/2",width="10",height="1",bg="white")
        lab_cri_u_e_t.place(x=245,y=430)
        
    else:
        lab_u_e_t=tk.Label(root1,text=f'{u_e_t}',fg='red',width="10",height="1",bg="white")
        lab_u_e_t.place(x=405,y=430)
        lab_coef_u_e_t=tk.Label(root1,text='2',width="10",height="1",bg="white")
        lab_coef_u_e_t.place(x=325,y=430)
        lab_cri_u_e_t=tk.Label(root1,text=f"{cri_u_e_t}/2",width="10",height="1",bg="white")
        lab_cri_u_e_t.place(x=245,y=430)
    #métiers
    if(entry_métiers_exa1>=10):
        lab_métiers=tk.Label(root1,text=f'{entry_métiers_exa1}',fg='green',bg="white",width="10",height="1")
        lab_métiers.place(x=405,y=460)
        lab_coef_métiers=tk.Label(root1,text='1',width="10",height="1",bg="white")
        lab_coef_métiers.place(x=325,y=460)
        lab_cri_métiers=tk.Label(root1,text="1",width="10",height="1",bg="white")
        lab_cri_métiers.place(x=245,y=460)
        cri_métiers=1
    else:
        lab_métiers=tk.Label(root1,text=f'{entry_métiers_exa1}',fg='red',width="10",height="1",bg="white")
        lab_métiers.place(x=405,y=460)
        lab_coef_métiers=tk.Label(root1,text='1',width="10",height="1",bg="white")
        lab_coef_métiers.place(x=325,y=460)
        lab_cri_métiers=tk.Label(root1,text="0",width="10",height="1",bg="white")
        lab_cri_métiers.place(x=245,y=460)
        cri_métiers=0
    #u_e_m
    cri_u_e_d=cri_métiers
    if(u_e_m>=10):
        lab_u_e_d=tk.Label(root1,text=f'{u_e_d}',fg='green',bg="white",width="10",height="1")
        lab_u_e_d.place(x=405,y=490)
        lab_coef_u_e_d=tk.Label(root1,text='1',width="10",height="1",bg="white")
        lab_coef_u_e_d.place(x=325,y=490)
        lab_cri_u_e_d=tk.Label(root1,text=f"{cri_u_e_d}/1",width="10",height="1",bg="white")
        lab_cri_u_e_d.place(x=245,y=490)
        
    else:
        lab_u_e_d=tk.Label(root1,text=f'{u_e_t}',fg='red',width="10",height="1",bg="white")
        lab_u_e_d.place(x=405,y=490)
        lab_coef_u_e_d=tk.Label(root1,text='1',width="10",height="1",bg="white")
        lab_coef_u_e_d.place(x=325,y=490)
        lab_cri_u_e_d=tk.Label(root1,text=f"{cri_u_e_d}/1",width="10",height="1",bg="white")
        lab_cri_u_e_d.place(x=245,y=490)
    #credit_tot
    credit=cri_u_e_f+cri_u_e_m+cri_u_e_t+cri_u_e_d
    average_s1=(u_e_f*9+u_e_m*5+u_e_t*2+u_e_d*1)/17
    average_s1=round(average_s1,2)
    lab_licence=tk.Label(root1,text="Licence 1ére Année",bg="#4dff00",font=("Arail",14))    
    lab_licence.place(x=35,y=73)
    if(average_s1>=10):
        lab_average_s1=tk.Label(root1,text=f"Average semestre : {average_s1} ",width="32",height="1",bg="#2bea29")
        lab_average_s1.place(x=10,y=520)
    else:
        lab_average_s1=tk.Label(root1,text=f"Average semestre : {average_s1} ",width="32",height="1",bg="#fc5144")
        lab_average_s1.place(x=10,y=520)
        
    if(average_s1>=10):
        lab_credit=tk.Label(root1,text=f"Credits : 30 ",width="34",height="1",bg="#2bea29")
        lab_credit.place(x=245,y=520)
    else:
        if(credit>=15):
            lab_credit=tk.Label(root1,text=f"Credits : {credit}",width="34",height="1",bg="#2bea29")
            lab_credit.place(x=245,y=520)
        else:
            lab_credit=tk.Label(root1,text=f"Credits : {credit}",width="34",height="1",bg="#fc5144")
            lab_credit.place(x=245,y=520)
    
    if(average_s1>=10):
        lab_des=tk.Label(root1,text=f"Decision : Pas Ajourné(e)",width="32",height="1",fg="black",bg="#2bea29")
        lab_des.place(x=10,y=550)
    else:
        lab_des=tk.Label(root1,text=f"Decision : ajourné(e)",width="32",height="1",fg="black",bg="#fc5144")
        lab_des.place(x=10,y=550)
         
    root1.mainloop()
#button  delete   
delet=tk.Button(text="Delete",command=delete,bg="#ec2a0c",width="20",height="1")
delet.place(x=300,y=350)


#button Calculate
Calculate=tk.Button(text="Calculate",command=calcu,bg="#3de222",width="20",height="1",state=tk.DISABLED,fg="#444444")
Calculate.place(x=50,y=350)
def réaliser_par():
    root2 = tk.Toplevel()
    root2.title("Réaliser par")
    root2.geometry("250x150+350+200")
    root2.config(bg='#4dff00')
    root2.resizable(False,False)
    root2.iconbitmap("image/imag_1.ico")
    
    



    root2.mainloop()
#buttn  Réaliser par
MOUS=tk.Label(text="MossabGH",bg="#4dff00",font=("Impact", 15))
MOUS.place(x=3,y=402)

root.mainloop()




