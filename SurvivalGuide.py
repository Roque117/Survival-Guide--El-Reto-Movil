import tkinter as tk
import random
from tkinter import messagebox

correctasR = 0
actpreg = {}

correctasN = 0
actpregN = {}

correctasS = 0
actpregS = {}

correctasL = 0
actpregL = {}

def Reglas():
    
    Reglas=tk.Toplevel(ventana)
    Reglas.config(bg="Lightcyan")
    Reglas.title("La Cámara de las Reglas")
    Reglas.geometry("600x600")

    Retiqueta = tk.Label(Reglas, text="La Cámara de las Reglas", font=("Arial", 24), bg="Lightcyan")
    Retiqueta.pack(pady=10)

    tk.Label(Reglas, text="Reglas del Salon de clases", font=("Arial", 24))

    CajaR = tk.Text(Reglas, font=("Arial", 8), bg="white")
    CajaR.insert ("1.0","""1. Se requiere 80% de asistencia para tener derecho a evaluación parcial y 80% de trabajos en clase.
2. Se permiten 10 minutos de tolerancia y si el alumno llega después de este tiempo puede permanecer en la clase, pero no se  tomará la asistencia (Solamente en los horarios de inicio: 7:00 a.m. y 14:00 p.m.).
3. Las faltas deberán estar justificadas mediante el correo institucional con un plazo máximo de 24 horas posteriores a la  hora de falta en clase mediante correo del tutor (a), justificantes entregados fuera de la fecha límite permitido no se aceptan,  únicamente se aceptarán recetas médicas y citatorios jurídicos. (De forma física deben ser presentados al tutor para ser  validados y de forma posterior emitidos).
4. Las tareas y trabajos deberán subirlas al Classroom de forma individual y no se recibirán de manera extemporánea. (Salvo  previo justificante validado por el tutor)
5. Las tareas y trabajos presentarlos en tiempo y forma. La demora de un trabajo o tarea sin justificante y/o con justificante  fuera del límite no se aceptan.
6. Utilizar el correo institucional para trabajar bajo la plataforma Google Classroom.
7. El plagio o copia de trabajos y/o exámenes, será condicionado a reprobar a la asignatura y se reportará al área correspondiente.
8. Cualquier deshonestidad académica será sancionada reprobando el parcial sin derecho a examen final.
9. En circunstancia de indisciplina o falta de respeto por parte del alumno hacia docentes, administrativos, compañeros o  cualquier persona perteneciente a la universidad, se realizará una primera llama de atención, si el alumno hace caso omiso tendrá  que abandonar el aula, tres incidencias de este tipo el alumno no tendrá derecho a examen final o parcial.
10. Uso de laptops y/o dispositivos móviles quedará limitado a uso exclusivo de las actividades que así lo requieran.
11. Prohibido el uso de audífonos durante la clase.
12. Prohibido comer y/o tomar líquidos en el salón.
13. Prohibido sentarse encima de las mesas, así como columpiarse en las sillas.
14. Todo tema académico debe ser revisado primeramente por parte del alumno con el docente, de no resolverse, pasar con su  respectivo tutor, y de ser necesario con la coordinación de tutores. En caso de no solucionarse pasar a la dirección del programa  educativo (debe mantenerse este seguimiento de forma obligatoria).
15. Cualquier situación no prevista en el presente reglamento pasar directamente con la dirección del programa educativo.
16. El día destinado a entrega de calificaciones todos los estudiantes deben estar presentes, ese día se entregarán exámenes y se  brindará retroalimentación.
17. Este reglamento entra en vigor después de que se firme o se acepte por la mayoría de los estudiantes asistentes a la primera  sesión de la materia, una vez firmado o aceptado por el 50% más el jefe de grupo, es vigente para todo alumno inscrito en el curso  aunque no esté presente en la primera sesión.""")
    CajaR.pack(pady=10)


    
    def Creglas():
        global pregunta_actual
        Creglas = tk.Toplevel(Reglas)
        Creglas.configure(bg="lightyellow")
        Creglas.title("Cuestionario de La Cámara de las Reglas")
        Creglas.geometry("600x600")
        
        PregR = [
        {"p": "¿Se puede comer en el salón?", "r": False},
        {"p": "¿Se requiere 80% de asistencia?", "r": True},
        {"p": "¿Hay 10 min de tolerancia?", "r": True},
        {"p": "¿El plagio se sanciona con reprobación?", "r": True},
        {"p": "¿Se pueden usar audífonos?", "r": False},
        {"p": "¿Se permite columpiarse en las sillas?", "r": False},
        {"p": "¿Las tareas se entregan por Classroom?", "r": True},
        {"p": "¿El reglamento rige a todos aunque no estén?", "r": True},
        {"p": "¿Se permite beber líquidos en clase?", "r": False},
        {"p": "¿La deshonestidad quita derecho a examen?", "r": True}
        ]
        
        Rmos = tk.Label(Creglas, text="", font=("Arial", 12), bg="Lightyellow")
        Rmos.pack(pady=20)
        
        def campreg():
            global actpreg
            actpreg = random.choice(PregR)
            Rmos.config(text=actpreg["p"])
            

        def verificacion(RespR):
            global correctasR
            
            if RespR == actpreg["r"]:
                correctasR = correctasR + 1
            else:
                correctasR = 0
            
            if correctasR < 2:
                campreg()
            else:
                Rmos.config(text="Bien")
                global boton2
                boton2.config(state="normal")
                Creglas.destroy()
                Reglas.destroy()
                messagebox.showinfo("Nivel 1 Completado", "Se ha desbloqueado El Oráculo de las Notas")
        
        bot1R = tk.Button(Creglas, text="si", font=("Arial", 12), bg="white", command=lambda: verificacion(True))
        bot1R.pack(pady=20)
        
        bot2R = tk.Button(Creglas, text="no", font=("Arial", 12), bg="white", command=lambda: verificacion(False))
        bot2R.pack(pady=20)
        
        campreg()
        
    botonR = tk.Button(Reglas,text="Cuestionario", font=("Arial", 8), bg="white", command=Creglas)
    botonR.pack(pady=50)    
    

def Notas():
    Notas=tk.Toplevel(ventana)
    Notas.config(bg="Lightcyan")
    Notas.title("El Oráculo de las Notas")
    Notas.geometry("600x600")

    Netiqueta = tk.Label(Notas, text= "El Oráculo de las  Notas", font=("Arial", 24), bg="Lightcyan")
    Netiqueta.pack(pady=10)

    Ncaja = tk.Text(Notas, font=("Arial", 8), bg="white")
    Ncaja.insert("1.0", """PRIMER PARCIAL (1P)
    • Evidencia de Conocimiento: 40%
    • Evidencia de Desempeño: 20%
    • Evidencia de Producto: 30%
    • Proyecto Integrador: 10%
SEGUNDO PARCIAL (2P)
    • Evidencia de Conocimiento: 40%
    • Evidencia de Desempeño: 20%
    • Evidencia de Producto: 30%
    • Proyecto Integrador: 10%
TERCER PARCIAL (3P)
    • Evidencia de Conocimiento: 10%
    • Evidencia de Desempeño: 10%
    • Evidencia de Producto: 30%
    • Proyecto Integrador: 50%""")    
    Ncaja.pack(pady=10)

    def Cnotas():
        Cnotas = tk.Toplevel(Notas)
        Cnotas.config(bg="lightyellow")
        Cnotas.geometry("600x600")
        Cnotas.title("Cuestionario de El Oráculo de las  Notas")
        
        PregN = [
            {"n": "¿Cuanto vale la Evidencia de Conocimiento del Primer Parcial?", "nr": ["40", "cuarenta", "40%"]},
            {"n": "¿Cuanto vale la Evidencia de Conocimiento del Segundo Parcial?", "nr": ["40", "cuarenta", "40%"]},
            {"n": "¿Cuanto vale la Evidencia de Conocimiento del Tercer Parcial?", "nr": ["10", "diez", "10%"]},
            {"n": "¿Cuanto vale la Evidencia de Desempeño del Primer Parcial?", "nr": ["20","veinte", "20%"]},
            {"n": "¿Cuanto vale la Evidencia de Desempeño del Segundo Parcial?", "nr": ["20","veinte", "20%"]},
            {"n": "¿Cuanto vale la Evidencia de Desempeño del Tercer Parcial?", "nr": ["10", "diez", "10%"]},
            {"n": "¿Cuanto vale la Evidencia de Producto del Primer Parcial?", "nr": ["30", "treinta", "30%"]},
            {"n": "¿Cuanto vale la Evidencia de Producto del Segundo Parcial?", "nr": ["30", "treinta", "30%"]},
            {"n": "¿Cuanto vale la Evidencia de Producto del Tercer Parcial?", "nr": ["30", "treinta", "30%"]},
            {"n": "¿Cuanto vale el Proyecto Integrador en el Primer Parcial?", "nr": ["10", "diez", "10%"]},
            {"n": "¿Cuanto vale el Proyecto Integrador en el Segundo Parcial?", "nr": ["10", "diez", "10%"]},
            {"n": "¿Cuanto vale el Proyecto Integrador en el Tercer Parcial?", "nr": ["50","cincuenta", "50%"]}
        ] 
        
        Npreg = tk.Label(Cnotas, text="", font=("Arial", 12), bg="white")
        Npreg.pack(pady="20")
        
        UsuN = tk.Entry(Cnotas, font=("Arial",  12), justify="center")
        UsuN.pack(pady=20)
        
        def CamrespN():
            global actpregN
            actpregN = random.choice(PregN)
            Npreg.config(text=actpregN["n"])
            UsuN.delete(0, tk.END)
        
        def verificacionN():
            global correctasN
            RespN = UsuN.get().lower()
            
            if RespN in actpregN["nr"]:
                correctasN = correctasN + 1
            else:
                correctasN = 0
            
            if correctasN < 2:
                CamrespN()
            else:
                boton3.config(state="normal")
                Cnotas.destroy()
                Notas.destroy()
                messagebox.showinfo("Nivel 2 completado", "Se a desbloqueado Skills a desbloquear")
            
        UsuNbot = tk.Button(Cnotas, text="Enviar", font=("Arial", 12), bg="white", command=verificacionN)
        UsuNbot.pack(pady=20)
        
        CamrespN()
                 
        
        
        

    botonN = tk.Button(Notas, text="Cuestionario", font=("Arial", 12), bg="white", command=Cnotas)
    botonN.pack(pady=50)



def Skills():
    Skills=tk.Toplevel(ventana)
    Skills.config(bg="Lightcyan")
    Skills.title("Skills a desbloquear")
    Skills.geometry("600x600")

    Setiqueta = tk.Label(Skills, text= "Skills a desbloquear", font=("Arial", 18), bg="lightcyan")
    Setiqueta.pack(pady=10)

    Scaja = tk.Text(Skills, font=("Arial", 8), bg="white")
    Scaja.insert("1.0", """ OBJETIVO GENERAL
    1.-Aplicación móvil (react)
    2.-Internet público
    3.-APIs
    4.-Servidor web
    5.-Base de datos (SQLite)
     
OBJETIVO ESPECÍFICO
    1.- JS
    2.- React Native
        • Componentes
        • Screens
        • Navegations
        • Comunicación API""")
    Scaja.pack(pady=10)

    def Cskills():
        Cskills = tk.Toplevel(Skills)
        Cskills.config(bg= "lightcyan")
        Cskills.title("Skills a desbloquear")
        Cskills.geometry("600x600")
    
    
        PregS = [
            {"s": "¿Flask está como objetivo específico?", "sr": ["no"]},
            {"s": "¿La base de datos es SQLite?", "sr": ["si"]},
            {"s": "¿Se usa React Native?", "sr": ["si"]},
            {"s": "¿JS es un objetivo específico?", "sr": ["si"]},
            {"s": "¿El servidor es local?", "sr": ["no"]},
            {"s": "¿Navegations es parte de React?", "sr": ["si"]},
            {"s": "¿Se usa Java?", "sr": ["no"]}
        ]
    
        Spreg = tk.Label(Cskills, text="", font=("Arial", 12), bg="white")
        Spreg.pack(pady=20)
    
        bot1S = tk.Button(Cskills, text="si", font=("Arial", 12), bg="white", command=lambda: verificacion(True))
        bot1S.pack(pady=20)
        
        bot2S = tk.Button(Cskills, text="no", font=("Arial", 12), bg="white", command=lambda: verificacion(False))
        bot2S.pack(pady=20)
        
        def campregS():
            global actpregS
            actpregS = random.choice(PregS)
            Spreg.config(text=actpregS["s"])
            
        def verificacion(RespS):
            global correctasS
            
            if RespS == (actpregS["sr"][0] == "si"):
                correctasS = correctasS + 1
            else:
                correctasS = 0
            
            if correctasS < 2:
                campregS()
            else:
                Spreg.config(text="Bien")
                boton4.config(state="normal")
                Cskills.destroy()
                Skills.destroy()
                messagebox.showinfo("Nivel 3 completado", "Se a desbloqueado La Línea del Tiempo")
                
        campregS()
    
    
    botonS = tk.Button(Skills, text="Cuestionario", font=("Arial",12), bg="white", command=Cskills)
    botonS.pack(pady=50)



def LineaTiempo():
    Tiempo = tk.Toplevel (ventana)
    Tiempo.config(bg= "lightcyan")
    Tiempo.title("La Línea del Tiempo")
    Tiempo.geometry("600x600")

    Tetiqueta= tk.Label(Tiempo, text="La Línea del Tiempo:", font=("Arial", 18), bg="white")
    Tetiqueta.pack(pady=10)

    Tcaja = tk.Text(Tiempo, font=("Arial", 8),bg="white")
    Tcaja.insert("1.0", """Exámenes:
•	Primer Parcial.- 02-06-26
•	Segundo Parcial.- 07-07-26
•	Tercer Parcial.- 11-08-26
•	Final.- 17-08-26

•   Dias NO Laborables: 15-06-26

•   Vacaciones: 20-07-26 a 24-07-26""")
    Tcaja.pack(pady=10)


    def Cuesttiempo():
        Ctiempo = tk.Toplevel(ventana)
        Ctiempo.config(bg="lightyellow")
        Ctiempo.title("Cuestionario de La Línea del Tiempo")
        Ctiempo.geometry("600x600")
        
        PregS = [
            {"s": "¿El primer parcial es el 02-06-26?", "sr": ["si"]},
            {"s": "¿El segundo parcial es el 07-07-26?", "sr": ["si"]},
            {"s": "¿El tercer parcial es el 11-08-26?", "sr": ["si"]},
            {"s": "¿El examen final es el 17-08-26?", "sr": ["si"]},
            {"s": "¿El 15-06-26 es un día no laborable?", "sr": ["si"]},
            {"s": "¿Las vacaciones son del 20-07-26 al 24-07-26?", "sr": ["si"]},
            {"s": "¿El examen final es el 17-09-26?", "sr": ["no"]},
            {"s": "¿El primer parcial es el 02-07-26?", "sr": ["no"]},
            {"s": "¿El segundo parcial es el 07-08-26?", "sr": ["no"]},
            {"s": "¿El tercer parcial es el 11-09-26?", "sr": ["no"]}
        ]   
        
        Spreg = tk.Label(Ctiempo, text="", font=("Arial", 12), bg="white")
        Spreg.pack(pady=20)
        
        bot1S = tk.Button(Ctiempo, text="si", font=("Arial", 12), bg="white", command=lambda: verificacion(True))
        bot1S.pack(pady=20)
        
        bot2S = tk.Button(Ctiempo, text="no", font=("Arial", 12), bg="white", command=lambda: verificacion(False))
        bot2S.pack(pady=20)
        
        def campregS():
            global actpregL
            actpregL = random.choice(PregS)
            Spreg.config(text=actpregL["s"])
            
        def verificacion(RespS):
            global correctasL
            
            if RespS == (actpregL["sr"][0] == "si"):
                correctasL = correctasL + 1
            else:
                correctasL = 0
            
            if correctasL < 2:
                campregS()
            else:
                Spreg.config(text="Bien")
                Ctiempo.destroy()
                Tiempo.destroy()
                messagebox.showinfo("Nivel 4 completado", "Se a completado Todo el juego")
                
        campregS()
        
    botonT = tk.Button(Tiempo, text="Cuestionario", font=("Arial", 8), bg="white", command=Cuesttiempo)
    botonT.pack(pady=50)


ventana=tk.Tk()
ventana.config(bg="black")
ventana.title("Survival Guide")
ventana.geometry("600x600")

etiqueta = tk.Label(ventana, text="--SURVIVAL GUIDE--", font=("Arial", 24), bg="black", fg="white")
etiqueta.pack(pady=(0, 20))

Boton1=tk.Button(ventana, text="La Cámara de las Reglas", font=("Arial", 16), bg="Red", command=Reglas, fg="white")
Boton1.pack(pady=10)

boton2=tk.Button(ventana, text="El Oráculo de las Notas", font=("Arial", 16), bg="blue", command=Notas, fg="white", state="disabled")
boton2.pack(pady=10)

boton3=tk.Button(ventana, text="Skills a desbloquear", font=("Arial", 16), bg="green", command=Skills, fg="white", state="disabled")
boton3.pack(pady=10)

boton4=tk.Button(ventana, text="La Línea del Tiempo", font=("Arial", 16), bg="orange", command=LineaTiempo, fg="white", state="disabled")
boton4.pack(pady=10)

ventana.mainloop()

