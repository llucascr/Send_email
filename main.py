import os
import smtplib
from email.message import EmailMessage
from tkinter import *

# EMAIL MESSAGE
email = 'lucasdecamposranzani@gmail.com'

with open ('senha.txt') as f:
    senha = f.readlines()
    
    f.close

senha_do_email = senha[0]

msg = EmailMessage()
msg['Subject'] = 'Enviando e-mail com Python'
msg['From'] = 'lucasdecamposranzani@gmail.com'
msg['To'] = 'lucasdecamposranzani@gmail.com'
msg.set_content('Segue o relatório diário')

# Enviando e-mail
def send():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email, senha_do_email)
        smtp.send_message(msg)


# TKINTER

# Cores
cor1 = '#191b5e'
cor2 = '#ffffff'
cor3 = '#000000'
cor4 = '#f5bd07'

# Criando a Janela
janela = Tk()
janela.title('E-mail Message')
janela.geometry('800x500')
janela.config(bg=cor1)

# Title
title = Label(janela, text='Send e-mail', font=('Arial Bold', 30), bg=cor1, fg=cor4)
title.place(x=10, y=10)

# Botão
btn = Button(janela, text='Enviar e-mail', font=('Arial Bold', 13), bg=cor4, fg=cor3, width='16', command=send)
btn.place(x=600, y=400)

# Subject
label_subject = Label(janela, text='Subject', font=('Arial Bold', 20), bg=cor1, fg=cor2)
label_subject.place(x=20, y=75)

entrey_subject = Entry(janela, font=('Arial Bold', 15))
entrey_subject.place(x=20, y=120, width=400, height=30)

# From
# label_from = Label(janela, text='From', font=('Arial Bold', 20), bg=cor1, fg=cor2)
# label_from.place(x=20, y=170)

# entrey_from = Entry(janela, font=('Arial Bold', 15))
# entrey_from.place(x=20, y=210, width=400, height=30)
    
janela.mainloop()