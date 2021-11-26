from tkinter import*
from tkinter import font
from experta import *

raiz = Tk()
raiz.title("Sistema experto- Tipos de covid")
raiz.config(bg="#f4f7fa")
raiz.resizable(0,0)

mi0Frame = Frame(raiz)#, width="1200", height="700")
mi0Frame.grid(row=0, column=0)
mi0Frame.config(bg="#f4f7fa")
mi3Frame = Frame(raiz)#, width="1200", height="700")
mi3Frame.grid(row=0, column=1)
mi3Frame.config(bg="#f4f7fa")
miFrame = Frame(raiz)#, width="1200", height="700")
miFrame.grid(row=1, column=0)
miFrame.config(bg="#f4f7fa")
mi2Frame = Frame(raiz, highlightbackground="black", highlightthickness=0.5)
mi2Frame.grid(row=1, column=1)
mi2Frame.config(bg="#f4f7fa")

reinicio = 0
#-----------------------------------------------INPUTS DE LOS SÍNTOMAS------------------------------------------------------------
sin0 = Label(miFrame, text="Dolor de cabeza:", bg="#F0F8FF", font=('Century Ghotic', 10, font.BOLD))
sin0.grid(row=0, column=0,padx=10, pady=10,sticky="e")
in_sin0 = Entry(miFrame, width=10, font=('CASTELLAR', 9, font.BOLD), justify='center')
in_sin0.grid(row=0, column=1,padx=10, pady=10)

sin1 = Label(miFrame, text="Perdida del olfato:", bg="#F0F8FF", font=('Century Ghotic', 10, font.BOLD))
sin1.grid(row=1, column=0,padx=10, pady=10,sticky="e")
in_sin1 = Entry(miFrame, width=10, font=('CASTELLAR', 9, font.BOLD), justify='center')
in_sin1.grid(row=1, column=1,padx=10, pady=10)

sin2 = Label(miFrame, text="Dolor muscular:", bg="#F0F8FF", font=('Century Ghotic', 10, font.BOLD))
sin2.grid(row=2, column=0,padx=10, pady=10,sticky="e")
in_sin2 = Entry(miFrame, width=10, font=('CASTELLAR', 9, font.BOLD), justify='center')
in_sin2.grid(row=2, column=1,padx=10, pady=10)

sin3 = Label(miFrame, text="Tos:", bg="#F0F8FF", font=('Century Ghotic', 10, font.BOLD))
sin3.grid(row=3, column=0,padx=10, pady=10,sticky="e")
in_sin3 = Entry(miFrame, width=10, font=('CASTELLAR', 9, font.BOLD), justify='center')
in_sin3.grid(row=3, column=1,padx=10, pady=10)

sin4 = Label(miFrame, text="Dolor de garganta:", bg="#F0F8FF", font=('Century Ghotic', 10, font.BOLD))
sin4.grid(row=4, column=0,padx=10, pady=10,sticky="e")
in_sin4 = Entry(miFrame, width=10, font=('CASTELLAR', 9, font.BOLD), justify='center')
in_sin4.grid(row=4, column=1,padx=10, pady=10)

sin5 = Label(miFrame, text="Dolor en el pecho:", bg="#F0F8FF", font=('Century Ghotic', 10, font.BOLD))
sin5.grid(row=5, column=0,padx=10, pady=10,sticky="e")
in_sin5 = Entry(miFrame, width=10, font=('CASTELLAR', 9, font.BOLD), justify='center')
in_sin5.grid(row=5, column=1,padx=10, pady=10)

sin6 = Label(miFrame, text="Fiebre:", bg="#F0F8FF", font=('Century Ghotic', 10, font.BOLD))
sin6.grid(row=6, column=0,padx=10, pady=10,sticky="e")
in_sin6 = Entry(miFrame, width=10, font=('CASTELLAR', 9, font.BOLD), justify='center')
in_sin6.grid(row=6, column=1,padx=10, pady=10)

sin7 = Label(miFrame, text="Ronquera:", bg="#F0F8FF", font=('Century Ghotic', 10, font.BOLD))
sin7.grid(row=7, column=0,padx=10, pady=10,sticky="e")
in_sin7 = Entry(miFrame, width=10, font=('CASTELLAR', 9, font.BOLD), justify='center')
in_sin7.grid(row=7, column=1,padx=10, pady=10)

sin8 = Label(miFrame, text="Pérdida del apetito:", bg="#F0F8FF", font=('Century Ghotic', 10, font.BOLD))
sin8.grid(row=8, column=0,padx=10, pady=10,sticky="e")
in_sin8 = Entry(miFrame, width=10, font=('CASTELLAR', 9, font.BOLD), justify='center')
in_sin8.grid(row=8, column=1,padx=10, pady=10)

sin9 = Label(miFrame, text="Diarrea:", bg="#F0F8FF", font=('Century Ghotic', 10, font.BOLD))
sin9.grid(row=9, column=0,padx=10, pady=10,sticky="e")
in_sin9 = Entry(miFrame, width=10, font=('CASTELLAR', 9, font.BOLD), justify='center')
in_sin9.grid(row=9, column=1,padx=10, pady=10)

sin10 = Label(miFrame, text="Fatiga:", bg="#F0F8FF", font=('Century Ghotic', 10, font.BOLD))
sin10.grid(row=10, column=0,padx=10, pady=10,sticky="e")
in_sin10 = Entry(miFrame, width=10, font=('CASTELLAR', 9, font.BOLD), justify='center')
in_sin10.grid(row=10, column=1,padx=10, pady=10)

sin11 = Label(miFrame, text="Confusión:", bg="#F0F8FF", font=('Century Ghotic', 10, font.BOLD))
sin11.grid(row=11, column=0,padx=10, pady=10,sticky="e")
in_sin11 = Entry(miFrame, width=10, font=('CASTELLAR', 9, font.BOLD), justify='center')
in_sin11.grid(row=11, column=1,padx=10, pady=10)

sin12 = Label(miFrame, text="Dificultad para respirar:", bg="#F0F8FF", font=('Century Ghotic', 10, font.BOLD))
sin12.grid(row=12, column=0,padx=10, pady=10,sticky="e")
in_sin12 = Entry(miFrame, width=10, font=('CASTELLAR', 9, font.BOLD), justify='center')
in_sin12.grid(row=12, column=1,padx=10, pady=10)

#------Cuadros de los resultados--------
tipo_final_lbl = Label(mi2Frame, text="Tipo de covid diagnosticado:", bg="#F0F8FF", font=('Century Ghotic', 10, font.BOLD))
tipo_final_lbl.grid(row=2, column=0,padx=10, pady=10,sticky="n")
tipo_final = Entry(mi2Frame, width=35, justify='center', font=('FELIX TITLING', 10, font.BOLD))
tipo_final.grid(row=3, column=0, padx=1, pady=1)

blank = Label(mi2Frame, bg="#F0F8FF")
blank.grid(row=4, column=0,padx=10, pady=10,sticky="n")

descripcion_tipo_lbl = Label(mi2Frame, text="Descripción del tipo de covid diagnosticado:", bg="#F0F8FF", font=('Century Ghotic', 10, font.BOLD))
descripcion_tipo_lbl.grid(row=5, column=0,padx=10, pady=10,sticky="n")
descripcion_tipo = Text(mi2Frame, width=60, height=10)
descripcion_tipo.grid(row=6, column=0, padx=10, pady=10)

sugerencias_lbl = Label(mi2Frame, text="Sugerencias para tratar la enfermedad:", bg="#F0F8FF", font=('Century Ghotic', 10, font.BOLD))
sugerencias_lbl.grid(row=7, column=0,padx=10, pady=10,sticky="n")
sugerencias = Text(mi2Frame, width=60, height=10)
sugerencias.grid(row=8, column=0, padx=10, pady=10)

#------HEADER--------
head1 = Label(mi0Frame, text="\n\nSÍNTOMAS", bg="#F0F8FF", font=('Elephant', 15))
head1.grid(row=0, column=0, sticky="n")
head1_0 = Label(mi3Frame, text="DIAGNÓSTICO", bg="#F0F8FF", font=('Elephant', 15))
head1_0.grid(row=0, column=0, sticky="n")
head1 = Label(mi0Frame, bg="#F0F8FF")
head1.grid(row=1, column=0, sticky="n")
head2 = Label(mi0Frame, text="  -Introduce un 'si' o un 'no' dependiendo de los síntomas que presentes",
              bg="#F0F8FF", font=('Century Ghotic', 11))
head2.grid(row=2, column=0, sticky="n" )


#-----------------------------------------^^^^^^INPUTS DE LOS SÍNTOMAS^^^^^^------------------------------------------------------


lista_tipos = []
sintomas_tipo = []
map_sintomas = {}
d_desc_map = {}
d_tratamiento_map = {}

def preprocess():
	global lista_tipos,sintomas_tipo,map_sintomas,d_desc_map,d_tratamiento_map
	tipos = open("tipos.txt")
	tipos_t = tipos.read()
	lista_tipos = tipos_t.split("\n")
	tipos.close()
	for tipo in lista_tipos:
		tipo_s_file = open("Sintomas tipo/" + tipo + ".txt")
		tipo_s_data = tipo_s_file.read()
		s_list = tipo_s_data.split("\n")
		sintomas_tipo.append(s_list)
		map_sintomas[str(s_list)] = tipo
		tipo_s_file.close()
		tipo_s_file = open("Descripcion tipo/" + tipo + ".txt")
		tipo_s_data = tipo_s_file.read()
		d_desc_map[tipo] = tipo_s_data
		tipo_s_file.close()
		tipo_s_file = open("Tratamientos tipo/" + tipo + ".txt")
		tipo_s_data = tipo_s_file.read()
		d_tratamiento_map[tipo] = tipo_s_data
		tipo_s_file.close()
	

def identificar_tipo(*arguments):
	lista_sintomas = []
	for sintoma in arguments:
		lista_sintomas.append(sintoma)
	# Handle key error
	return map_sintomas[str(lista_sintomas)]

def get_details(tipo):
	return d_desc_map[tipo]

def get_tratamiento(tipo):
	return d_tratamiento_map[tipo]

def no_coincide(tipo):
        tipo_final.delete("1.0", END)
        descripcion_tipo.delete("1.0", END)
        sugerencias.delete("1.0", END)
        id_tipo = tipo
        tipo_details = get_details(id_tipo)
        tratamientos = get_tratamiento(id_tipo)
        tipo_final.insert("1.0", id_tipo)
        descripcion_tipo.insert("1.0", tipo_details)
        sugerencias.insert("1.0", tratamientos)

#def identificar_tipo(dolor_cabeza, perdida_olfato, dolor_muscular, tos, dolor_garganta, dolor_pecho, fiebre, ronquera, perdida_apetito , diarrea, fatiga, confusión, dificultad_respiratoria):
class Covid(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		yield Fact(action="encontrar_tipo")


	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(dolor_cabeza=W())),salience = 1)
	def sintoma_0(self):
		self.declare(Fact(dolor_cabeza=in_sin0.get()))

	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(perdida_olfato=W())),salience = 1)
	def sintoma_1(self):
		self.declare(Fact(perdida_olfato=in_sin1.get()))

	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(dolor_muscular=W())),salience = 1)
	def sintoma_2(self):
		self.declare(Fact(dolor_muscular=in_sin2.get()))

	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(tos=W())),salience = 1)
	def sintoma_3(self):
		self.declare(Fact(tos=in_sin3.get()))

	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(dolor_garganta=W())),salience = 1)
	def sintoma_4(self):
		self.declare(Fact(dolor_garganta=in_sin4.get()))

	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(dolor_pecho=W())),salience = 1)
	def sintoma_5(self):
		self.declare(Fact(dolor_pecho=in_sin5.get()))
	 
	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(fiebre=W())),salience = 1)
	def sintoma_6(self):
		self.declare(Fact(fiebre=in_sin6.get()))
	
	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(ronquera=W())),salience = 1)
	def sintoma_7(self):
		self.declare(Fact(ronquera=in_sin7.get()))
	
	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(perdida_apetito=W())),salience = 1)
	def sintoma_8(self):
		self.declare(Fact(perdida_apetito=in_sin8.get()))
	
	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(diarrea=W())),salience = 1)
	def sintoma_9(self):
		self.declare(Fact(diarrea=in_sin9.get()))
	
	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(fatiga=W())),salience = 1)
	def sintoma_10(self):
		self.declare(Fact(fatiga=in_sin10.get()))

	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(confusion=W())),salience = 1)
	def sintoma_11(self):
		self.declare(Fact(confusion=in_sin11.get()))

	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(dificultad_respiratoria=W())),salience = 1)
	def sintoma_12(self):
		self.declare(Fact(dificultad_respiratoria=in_sin12.get()))

	@Rule(Fact(action='encontrar_tipo'),Fact(dolor_cabeza="si"),Fact(perdida_olfato="si"),Fact(dolor_muscular="si"),Fact(tos="si"),Fact(dolor_garganta="si"),Fact(dolor_pecho="si"),Fact(fiebre="no"),Fact(ronquera="no"),Fact(perdida_apetito="no"),Fact(diarrea="no"),Fact(fatiga="no"),Fact(confusion="no"),Fact(dificultad_respiratoria="no"))
	def tipo_0(self):
		self.declare(Fact(tipo="Gripal sin fiebre"))

	@Rule(Fact(action='encontrar_tipo'),Fact(dolor_cabeza="si"),Fact(perdida_olfato="si"),Fact(dolor_muscular="no"),Fact(tos="si"),Fact(dolor_garganta="si"),Fact(dolor_pecho="no"),Fact(fiebre="si"),Fact(ronquera="si"),Fact(perdida_apetito="si"),Fact(diarrea="no"),Fact(fatiga="no"),Fact(confusion="no"),Fact(dificultad_respiratoria="no"))
	def tipo_1(self):
		self.declare(Fact(tipo="Gripal con fiebre"))

	@Rule(Fact(action='encontrar_tipo'),Fact(dolor_cabeza="si"),Fact(perdida_olfato="si"),Fact(dolor_muscular="no"),Fact(tos="no"),Fact(dolor_garganta="si"),Fact(dolor_pecho="si"),Fact(fiebre="no"),Fact(ronquera="no"),Fact(perdida_apetito="no"),Fact(diarrea="si"),Fact(fatiga="no"),Fact(confusion="no"),Fact(dificultad_respiratoria="no"))
	def tipo_2(self):
		self.declare(Fact(tipo="Gastro Intestinal"))

	@Rule(Fact(action='encontrar_tipo'),Fact(dolor_cabeza="si"),Fact(perdida_olfato="si"),Fact(dolor_muscular="no"),Fact(tos="si"),Fact(dolor_garganta="no"),Fact(dolor_pecho="si"),Fact(fiebre="si"),Fact(ronquera="si"),Fact(perdida_apetito="no"),Fact(diarrea="no"),Fact(fatiga="si"),Fact(confusion="no"),Fact(dificultad_respiratoria="no"))
	def tipo_3(self):
		self.declare(Fact(tipo="Nivel severo uno"))

	@Rule(Fact(action='encontrar_tipo'),Fact(dolor_cabeza="si"),Fact(perdida_olfato="si"),Fact(dolor_muscular="si"),Fact(tos="si"),Fact(dolor_garganta="si"),Fact(dolor_pecho="si"),Fact(fiebre="si"),Fact(ronquera="si"),Fact(perdida_apetito="si"),Fact(diarrea="no"),Fact(fatiga="si"),Fact(confusion="si"),Fact(dificultad_respiratoria="no"))
	def tipo_4(self):
		self.declare(Fact(tipo="Nivel severo dos"))

	@Rule(Fact(action='encontrar_tipo'),Fact(dolor_cabeza="si"),Fact(perdida_olfato="si"),Fact(dolor_muscular="si"),Fact(tos="si"),Fact(dolor_garganta="si"),Fact(dolor_pecho="si"),Fact(fiebre="si"),Fact(ronquera="si"),Fact(perdida_apetito="si"),Fact(diarrea="si"),Fact(fatiga="si"),Fact(confusion="si"),Fact(dificultad_respiratoria="si"))
	def tipo_5(self):
		self.declare(Fact(tipo="Nivel severo tres"))

	@Rule(Fact(action='encontrar_tipo'),Fact(dolor_cabeza="no"),Fact(perdida_olfato="no"),Fact(dolor_muscular="no"),Fact(tos="no"),Fact(dolor_garganta="no"),Fact(dolor_pecho="no"),Fact(fiebre="no"),Fact(ronquera="no"),Fact(perdida_apetito="no"),Fact(diarrea="no"),Fact(fatiga="no"),Fact(confusion="no"),Fact(dificultad_respiratoria="no"))
	def tipo_6(self):
		self.declare(Fact(tipo="No es covid"))

	@Rule(Fact(action='encontrar_tipo'),Fact(tipo=MATCH.tipo),salience = -998)
	def tipo(self, tipo):
            tipo_final.delete("0", END)
            descripcion_tipo.delete("1.0", END)
            sugerencias.delete("1.0", END)
            id_tipo = tipo
            tipo_details = get_details(id_tipo)
            tratamientos = get_tratamiento(id_tipo)
            tipo_final.insert("0", id_tipo)
            descripcion_tipo.insert("1.0", tipo_details)
            sugerencias.insert("1.0",tratamientos)

	@Rule(Fact(action='encontrar_tipo'),
		  Fact(dolor_cabeza=MATCH.dolor_cabeza),
		  Fact(perdida_olfato=MATCH.perdida_olfato),
		  Fact(dolor_muscular=MATCH.dolor_muscular),
		  Fact(tos=MATCH.tos),
		  Fact(dolor_garganta=MATCH.dolor_garganta),
		  Fact(dolor_pecho=MATCH.dolor_pecho),
		  Fact(fiebre=MATCH.fiebre),
		  Fact(ronquera=MATCH.ronquera),
		  Fact(perdida_apetito=MATCH.perdida_apetito),
		  Fact(diarrea=MATCH.diarrea),
		  Fact(fatiga=MATCH.fatiga),
		  Fact(confusion=MATCH.confusion),
		  Fact(dificultad_respiratoria=MATCH.dificultad_respiratoria),NOT(Fact(tipo=MATCH.tipo)),salience = -999)

	def not_matched(self,dolor_cabeza, perdida_olfato, dolor_muscular, tos, dolor_garganta, dolor_pecho, fiebre, ronquera,perdida_apetito ,diarrea ,fatiga ,confusion ,dificultad_respiratoria):
		global reinicio
		if reinicio == 0:
			tipo_final.delete("0", END)
			descripcion_tipo.delete("1.0", END)
			sugerencias.delete("1.0", END)
			tipo_final.insert("0", "Sin coincidencia")
			descripcion_tipo.insert("1.0", "No se encontró un tipo de covid que se relacione con los síntomas presentados")
			sugerencias.insert("1.0", "Se sugiere consultar a un médico que le ayude a descubrir su tipo de enfermedad")
		else:
			reinicio = 0
   

def iniciar_sistema():
    if __name__ == "__main__":
        preprocess()
        engine = Covid()
        engine.reset()
        engine.run()
               
def reiniciar():
    global reinicio
    reinicio = 1
    in_sin0.delete("0", END)
    in_sin1.delete("0", END)
    in_sin2.delete("0", END)
    in_sin3.delete("0", END)
    in_sin4.delete("0", END)
    in_sin5.delete("0", END)
    in_sin6.delete("0", END)
    in_sin7.delete("0", END)
    in_sin8.delete("0", END)
    in_sin9.delete("0", END)
    in_sin10.delete("0", END)
    in_sin11.delete("0", END)
    in_sin12.delete("0", END)
    tipo_final.delete("0", END) 
    descripcion_tipo.delete('1.0', END)
    sugerencias.delete('1.0', END)
    preprocess()
    engine = Covid()
    engine.reset()
    engine.run()               
                
def salir():
    exit()
   
   
#------------------BOTONES---------------------------------------
generarTabla = Button(
    miFrame, 
    text="RESULTADO", 
    command=iniciar_sistema,
    bg="#7fd1ff",
    font=("Eurostile", 10, font.BOLD)
)
generarTabla.grid(row=13, column=1, padx=10, pady=15)

reiniciar = Button(
    mi2Frame, text="REINICIAR", 
    command=reiniciar,
    bg="#7fd1ff",
    font=("Eurostile", 10, font.BOLD)
)
reiniciar.grid(row=9, column=0, padx=10, pady=15)

salir = Button(
    mi2Frame, text="SALIR", 
    command=salir,
    bg="#ea9999",
    font=("Eurostile", 9),
    border='2p'
)
salir.grid(row=10, column=0, padx=10, pady=15)
   
   
raiz.mainloop()