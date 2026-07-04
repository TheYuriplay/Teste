
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

PRIMARY="#2563EB"
SIDEBAR="#111827"
BG="#EEF2F7"

app=ctk.CTk()
app.title("Conducta CRM Demo v0.4")
app.geometry("1400x820")

sidebar=ctk.CTkFrame(app,width=250,corner_radius=0,fg_color=SIDEBAR)
sidebar.pack(side="left",fill="y")

ctk.CTkLabel(sidebar,text="CONDUCTA",font=("Segoe UI",28,"bold")).pack(pady=(20,0))
ctk.CTkLabel(sidebar,text="CRM Demo",text_color="#93C5FD").pack(pady=(0,20))

main=ctk.CTkFrame(app,fg_color=BG)
main.pack(fill="both",expand=True)

header=ctk.CTkFrame(main,height=65,fg_color="white")
header.pack(fill="x",padx=18,pady=18)

title=ctk.CTkLabel(header,text="Dashboard",font=("Segoe UI",24,"bold"),text_color="#111827")
title.pack(side="left",padx=20)

ctk.CTkEntry(header,width=300,placeholder_text="Pesquisar cliente, lead...").pack(side="left",padx=20)
ctk.CTkButton(header,text="+ Novo",width=110,fg_color=PRIMARY).pack(side="right",padx=10)
ctk.CTkLabel(header,text="👤 Admin",text_color="#374151").pack(side="right",padx=20)

content=ctk.CTkFrame(main,fg_color="transparent")
content.pack(fill="both",expand=True,padx=18,pady=(0,18))

pages={}
current=None

def dashboard():
    f=ctk.CTkFrame(content,fg_color="transparent")
    row=ctk.CTkFrame(f,fg_color="transparent")
    row.pack(fill="x")
    info=[("Clientes","18"),("Leads","09"),("Receita","R$ 8.500"),("Conversão","72%")]
    for t,v in info:
        c=ctk.CTkFrame(row,width=240,height=120,fg_color="white")
        c.pack(side="left",padx=8)
        c.pack_propagate(False)
        ctk.CTkLabel(c,text=t,text_color="#6B7280").pack(pady=(18,4))
        ctk.CTkLabel(c,text=v,font=("Segoe UI",28,"bold"),text_color="#111827").pack()

    body=ctk.CTkFrame(f,fg_color="transparent")
    body.pack(fill="both",expand=True,pady=15)

    left=ctk.CTkFrame(body,fg_color="white")
    left.pack(side="left",fill="both",expand=True,padx=(0,8))
    ctk.CTkLabel(left,text="Pipeline",font=("Segoe UI",18,"bold"),text_color="#111827").pack(anchor="w",padx=15,pady=10)
    cols=[("Lead","#DBEAFE"),("Contato","#E0F2FE"),("Proposta","#FEF3C7"),("Cliente","#DCFCE7")]
    line=ctk.CTkFrame(left,fg_color="transparent")
    line.pack(fill="both",expand=True,padx=10,pady=10)
    for name,color in cols:
        col=ctk.CTkFrame(line,width=170,height=260,fg_color=color)
        col.pack(side="left",padx=6)
        col.pack_propagate(False)
        ctk.CTkLabel(col,text=name,font=("Segoe UI",15,"bold"),text_color="#111827").pack(pady=10)
        for txt in ["Empresa Alpha","Clínica Beta"]:
            ctk.CTkLabel(col,text=txt,fg_color="white",corner_radius=8,text_color="#111827").pack(fill="x",padx=8,pady=4)

    right=ctk.CTkFrame(body,width=330,fg_color="white")
    right.pack(side="right",fill="y")
    right.pack_propagate(False)
    ctk.CTkLabel(right,text="Atividades",font=("Segoe UI",18,"bold"),text_color="#111827").pack(anchor="w",padx=15,pady=10)
    for t in ["✓ Proposta enviada","✓ Cliente cadastrado","✓ Reunião 14:00","✓ Renovação contrato"]:
        ctk.CTkLabel(right,text=t,text_color="#374151").pack(anchor="w",padx=15,pady=6)
    return f

def page(name):
    f=ctk.CTkFrame(content,fg_color="white")
    ctk.CTkLabel(f,text=name,font=("Segoe UI",28,"bold"),text_color="#111827").pack(anchor="w",padx=20,pady=20)
    ctk.CTkEntry(f,width=350,placeholder_text=f"Pesquisar em {name.lower()}...").pack(anchor="w",padx=20)
    box=ctk.CTkTextbox(f)
    box.pack(fill="both",expand=True,padx=20,pady=20)
    box.insert("1.0",f"Esta é uma tela demonstrativa de {name}.\n\n• Dados fictícios\n• Interface para apresentação\n• Sem banco de dados")
    return f

pages["Dashboard"]=dashboard()
for p in ["Clientes","Leads","Agenda","Pipeline","Financeiro","Contratos","Configurações"]:
    pages[p]=page(p)

def show(name):
    global current
    if current: current.pack_forget()
    current=pages[name]
    current.pack(fill="both",expand=True)
    title.configure(text=name)

for n in pages:
    ctk.CTkButton(sidebar,text=n,anchor="w",fg_color="transparent",
                  hover_color=PRIMARY,command=lambda x=n:show(x)).pack(fill="x",padx=12,pady=4)

show("Dashboard")
app.mainloop()
