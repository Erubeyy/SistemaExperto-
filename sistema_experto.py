from experta import *

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
		print("")
		id_tipo = tipo
		tipo_details = get_details(id_tipo)
		tratamientos = get_tratamiento(id_tipo)
		print("")
		print("El tipo más probable que tengas es: \n \nCoronavirus tipo %s" %(id_tipo))
		print("---------------------------------------------------------------------")
		print("\nUna descripción breve del tipo se dará a continuación:\n")
		print(tipo_details+"\n")
		print("Las sugerencias acerca de tratamientos o medicamentos son los siguientes: \n")
		print(tratamientos+"\n")

#def identificar_tipo(dolor_cabeza, perdida_olfato, dolor_muscular, tos, dolor_garganta, dolor_pecho, fiebre, ronquera, perdida_apetito , diarrea, fatiga, confusión, dificultad_respiratoria):
class Covid(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print("Hola, este es un sistema experto que te ayudará a descubrir cuál tipo de covid-19 tienes.")
		print("Para eso tendrás que contestar las siguientes preguntas con un 'si' o un 'no'")
		print("\n ¿Tienes alguno de los siguientes síntomas?:")
		print("")
		yield Fact(action="encontrar_tipo")


	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(dolor_cabeza=W())),salience = 1)
	def sintoma_0(self):
		self.declare(Fact(dolor_cabeza=input("Dolor de cabeza: ")))

	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(perdida_olfato=W())),salience = 1)
	def sintoma_1(self):
		self.declare(Fact(perdida_olfato=input("Perdida del olfato: ")))

	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(dolor_muscular=W())),salience = 1)
	def sintoma_2(self):
		self.declare(Fact(dolor_muscular=input("Dolor muscular: ")))

	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(tos=W())),salience = 1)
	def sintoma_3(self):
		self.declare(Fact(tos=input("Tos: ")))

	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(dolor_garganta=W())),salience = 1)
	def sintoma_4(self):
		self.declare(Fact(dolor_garganta=input("Dolor de garganta: ")))

	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(dolor_pecho=W())),salience = 1)
	def sintoma_5(self):
		self.declare(Fact(dolor_pecho=input("Dolor en el pecho: ")))
	 
	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(fiebre=W())),salience = 1)
	def sintoma_6(self):
		self.declare(Fact(fiebre=input("Fiebre: ")))
	
	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(ronquera=W())),salience = 1)
	def sintoma_7(self):
		self.declare(Fact(ronquera=input("Ronquera: ")))
	
	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(perdida_apetito=W())),salience = 1)
	def sintoma_8(self):
		self.declare(Fact(perdida_apetito=input("Pérdida del apetito: ")))
	
	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(diarrea=W())),salience = 1)
	def sintoma_9(self):
		self.declare(Fact(diarrea=input("Diarrea: ")))
	
	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(fatiga=W())),salience = 1)
	def sintoma_10(self):
		self.declare(Fact(fatiga=input("Fatiga: ")))

	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(confusion=W())),salience = 1)
	def sintoma_11(self):
		self.declare(Fact(confusion=input("Confusión: ")))

	@Rule(Fact(action='encontrar_tipo'), NOT(Fact(dificultad_respiratoria=W())),salience = 1)
	def sintoma_12(self):
		self.declare(Fact(dificultad_respiratoria=input("Dificultad para respirar: ")))

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
		print("")
		id_tipo = tipo
		tipo_details = get_details(id_tipo)
		tratamientos = get_tratamiento(id_tipo)
		print("")
		print("El tipo más probable que tengas es: %s\n" %(id_tipo))
		print("Una descripción breve del tipo se dará a continuación:\n")
		print(tipo_details+"\n")
		print("Las sugerencias acerca de tratamientos o medicamentos son los siguientes: \n")
		print(tratamientos+"\n")

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
		print("\nNo encontramos un tipo de Covid que se relaciones con tus síntomas")
		lis = [dolor_cabeza, perdida_olfato, dolor_muscular, tos, dolor_garganta, dolor_pecho, fiebre, ronquera,perdida_apetito ,diarrea ,fatiga ,confusion ,dificultad_respiratoria]
		max_count = 0
		max_tipo = ""
		for key,val in map_sintomas.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "si"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_tipo = val
		no_coincide(max_tipo)


if __name__ == "__main__":
	preprocess()
	engine = Covid()
	while(1):
		engine.reset()  # Prepare the engine for the execution.
		engine.run()  # Run it!
		print("¿Quisieras diagnosticar otros síntomas?")
		if input() == "no":
			exit()
