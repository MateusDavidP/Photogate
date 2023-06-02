import customtkinter as ctk
from photogate import *

distancia = int(input())
arquivo = r"C:\Users\User\OneDrive - Etec Centro Paula Souza\Desktop\Arquivos photogata\Photogate\Computação\tempos.CSV"
voltas = leitura_arquivo(arquivo)
voltas = calculo_acrescimos(voltas)
voltas = calculo_velocidades(distancia, voltas)



app = ctk.CTk()
app.geometry('400x400')
frame1 = ctk.CTkScrollableFrame(
    app,
    width= 200,
    height=  200
)

for x,y in zip(['Voltas', 'Tempo (Segundos)', 'Acréscimo (Segundos)', 'Vel. Ints (m/s)' ], [0,1,2,3]):
    entry = ctk.CTkEntry(app,justify='center')
    entry.insert(y,x)


for x,y in zip(voltas,[0,1,2,3]):
    entry = ctk.CTkEntry(app,justify='center')
    entry.insert(y,x[y])
    entry.configure(state='readonly')


app.mainloop()