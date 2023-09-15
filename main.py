import smtplib
from email.message import EmailMessage
from tkinter import *

# EMAIL MESSAGE
email = 'lucasdecamposranzani@gmail.com'

with open ('senha.txt') as f:
    senha = f.readlines()
    f.close

senha_do_email = senha[0]

# TKINTER

# Cores
cor1 = '#191b5e'
cor2 = '#ffffff'
cor3 = '#000000'
cor4 = '#f5bd07'

# Criando a Janela
janela = Tk()
janela.title('E-mail Message')
janela.geometry('500x500')
janela.config(bg=cor1)

# Função 
msg = EmailMessage()
def send():
    msg['From'] = 'lucasdecamposranzani@gmail.com'
    msg['To'] = entry_to.get()
    msg['Subject'] = entry_subject.get()
    msg.set_content(text_message.get("1.0",'end-1c'))
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
         smtp.login(email, senha_do_email)
         smtp.send_message(msg)
    

# Title
title = Label(janela, text='Send e-mail', font=('Arial Bold', 30), bg=cor1, fg=cor4)
title.place(x=10, y=10)

# To
label_to = Label(janela, text='Destinatário', font=('Arial Bold', 20), bg=cor1, fg=cor2)
label_to.place(x=20, y=75)

entry_to = Entry(janela, font=('Arial Bold', 15))
entry_to.place(x=20, y=120, width=400, height=30)

# Subject
label_subject = Label(janela, text='Assunto', font=('Arial Bold', 20), bg=cor1, fg=cor2)
label_subject.place(x=20, y=170)

entry_subject = Entry(janela, font=('Arial Bold', 15))
entry_subject.place(x=20, y=210, width=400, height=30)

# mensagem
label_message = Label(janela, text='Mensagem', font=('Arial Bold', 20), bg=cor1, fg=cor2)
label_message.place(x=20, y=260)

text_message = Text(janela, font=('Arial Bold', 15))
text_message.place(x=20, y=300, width=400, height=100)

# Botão
btn = Button(janela, text='Enviar e-mail', font=('Arial Bold', 13), bg=cor4, fg=cor3, width='16', command=send)
btn.place(x=300, y=440)
    
janela.mainloop()