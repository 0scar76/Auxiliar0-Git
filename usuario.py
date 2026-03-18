class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)

    def listarTareas(self):
<<<<<<< HEAD
   for tarea in self.tareas:
       if tarea.estaLista():
           print(f"La tarea {tarea.obtenerNombre()} está lista")
           print(f"La tarea {tarea.obtenerNombre()} no está lista")
=======
    for tarea in self.tareas:
        if tarea.estaLista():
            print(f"[X] {tarea.obtenerNombre()}" )
>>>>>>> b1d67f6f8802f3b7b2e8395c373d3e74d9b0203f
