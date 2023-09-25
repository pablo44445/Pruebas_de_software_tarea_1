import tkinter as tk
from tkinter import ttk
from agencia import Agencia
from automovil import Automovil
from util import Util

class InterfazAutomotora:
    def __init__(self, root):
        self.root = root
        self.root.title("Automotora")
        self.agencia = Agencia()
        self.vehiculos_por_pagina = 6  # Cambiado a 6 para un diseño 3x2
        self.pagina_actual = 1

        # Crear widgets
        self.label_cantidad = ttk.Label(root, text="Ingrese la cantidad de automóviles:")
        self.label_cantidad.pack()

        self.entry_cantidad = ttk.Entry(root)
        self.entry_cantidad.pack()

        self.boton_generar = ttk.Button(root, text="Generar Automóviles", command=self.generar_vehiculos)
        self.boton_generar.pack()

        self.frame_carrusel = ttk.Frame(root)
        self.frame_carrusel.pack()

        self.frame_paginacion = ttk.Frame(root)
        self.frame_paginacion.pack()

        self.label_pagina = ttk.Label(self.frame_paginacion, text="Página:")
        self.label_pagina.grid(row=0, column=0)

        self.boton_primera_pagina = ttk.Button(self.frame_paginacion, text="<< 1", command=self.ir_a_primera_pagina)
        self.boton_primera_pagina.grid(row=0, column=1)

        self.boton_anterior = ttk.Button(self.frame_paginacion, text="Anterior", command=self.pagina_anterior)
        self.boton_anterior.grid(row=0, column=2)

        self.label_pagina_actual = ttk.Label(self.frame_paginacion, text=str(self.pagina_actual))
        self.label_pagina_actual.grid(row=0, column=3)

        self.boton_siguiente = ttk.Button(self.frame_paginacion, text="Siguiente", command=self.pagina_siguiente)
        self.boton_siguiente.grid(row=0, column=4)

        total_paginas = self.agencia.calcular_total_paginas(self.vehiculos_por_pagina)
        self.boton_ultima_pagina = ttk.Button(self.frame_paginacion, text=f"{total_paginas} >>", command=self.ir_a_ultima_pagina)
        self.boton_ultima_pagina.grid(row=0, column=5)

        self.label_filtro = ttk.Label(self.frame_paginacion, text="Filtrar por precio:")
        self.label_filtro.grid(row=0, column=6)

        self.precio_filtro = tk.StringVar()
        self.precio_filtro.set("0-50000000")  # Rango de precios inicial
        self.filtro_precios = ttk.Combobox(self.frame_paginacion, values=["0-5000000", "5000000-10000000", "10000000-15000000", "15000000-20000000", "20000000-25000000", "25000000-30000000"])
        self.filtro_precios.grid(row=0, column=7)
        self.filtro_precios.bind("<<ComboboxSelected>>", self.aplicar_filtro)

        self.actualizar_carrusel()

    def generar_vehiculos(self):
        cantidad = int(self.entry_cantidad.get())
        self.agencia.generar_automoviles(cantidad)
        self.pagina_actual = 1
        self.actualizar_carrusel()

    def actualizar_carrusel(self):
        vehiculos = self.agencia.obtener_vehiculos_por_pagina(self.pagina_actual, self.vehiculos_por_pagina)
        self.mostrar_vehiculos(vehiculos)

    def mostrar_vehiculos(self, vehiculos):
        # Limpiar el carrusel
        for widget in self.frame_carrusel.winfo_children():
            widget.destroy()

        # Mostrar vehículos en el carrusel
        row = 0
        col = 0
        for automovil in vehiculos:
            info = automovil.obtener_informacion()
            label = ttk.Label(self.frame_carrusel, text=info)
            label.grid(row=row, column=col, padx=10, pady=10, sticky="w")

            # Agregar botón de contacto
            boton_contacto = ttk.Button(self.frame_carrusel, text="Contactar", command=lambda a=automovil: self.contactar_agencia(a))
            boton_contacto.grid(row=row + 1, column=col, padx=10, pady=10)

            col += 1
            if col >= 3:  # Cambiado a 3 para un diseño 3x2
                col = 0
                row += 2

    def pagina_anterior(self):
        if self.pagina_actual > 1:
            self.pagina_actual -= 1
            self.actualizar_carrusel()
        self.label_pagina_actual.config(text=str(self.pagina_actual))

    def pagina_siguiente(self):
        total_paginas = self.agencia.calcular_total_paginas(self.vehiculos_por_pagina)
        if self.pagina_actual < total_paginas:
            self.pagina_actual += 1
            self.actualizar_carrusel()
        self.label_pagina_actual.config(text=str(self.pagina_actual))

    def ir_a_primera_pagina(self):
        self.pagina_actual = 1
        self.actualizar_carrusel()
        self.label_pagina_actual.config(text=str(self.pagina_actual))

    def ir_a_ultima_pagina(self):
        total_paginas = self.agencia.calcular_total_paginas(self.vehiculos_por_pagina)
        self.pagina_actual = total_paginas
        self.actualizar_carrusel()
        self.label_pagina_actual.config(text=str(self.pagina_actual))

    def aplicar_filtro(self, event):
        rango_precio = self.precio_filtro.get()
        precio_min, precio_max = map(int, rango_precio.split("-"))
        vehiculos_filtrados = self.agencia.filtrar_automoviles(precio_min, precio_max)
        self.pagina_actual = 1
        self.actualizar_carrusel()

    def contactar_agencia(self, automovil):
        automovil.contactar_agencia()
        self.actualizar_carrusel()

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Automotora")

        self.interfaz = InterfazAutomotora(root)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()