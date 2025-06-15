import tkinter as tk
from tkinter import ttk, messagebox
import math

memoria_figuras = {
    "Cuadrado": {"lado": ""},
    "Rectángulo": {"base": "", "altura": ""},
    "Círculo": {"radio": ""},
    "Triángulo": {"base": "", "altura": "", "lado2": "", "lado3": ""}
}

def guardar_en_memoria():
    figura = combo_figura.get()
    if figura == "Cuadrado":
        memoria_figuras["Cuadrado"]["lado"] = entry_lado.get()
    elif figura == "Rectángulo":
        memoria_figuras["Rectángulo"]["base"] = entry_base.get()
        memoria_figuras["Rectángulo"]["altura"] = entry_altura.get()
    elif figura == "Círculo":
        memoria_figuras["Círculo"]["radio"] = entry_radio.get()
    elif figura == "Triángulo":
        memoria_figuras["Triángulo"]["base"] = entry_base.get()
        memoria_figuras["Triángulo"]["altura"] = entry_altura.get()
        memoria_figuras["Triángulo"]["lado2"] = entry_lado2.get()
        memoria_figuras["Triángulo"]["lado3"] = entry_lado3.get()

def cargar_de_memoria(figura):
    if figura == "Cuadrado":
        entry_lado.delete(0, tk.END)
        entry_lado.insert(0, memoria_figuras["Cuadrado"]["lado"])
    elif figura == "Rectángulo":
        entry_base.delete(0, tk.END)
        entry_base.insert(0, memoria_figuras["Rectángulo"]["base"])
        entry_altura.delete(0, tk.END)
        entry_altura.insert(0, memoria_figuras["Rectángulo"]["altura"])
    elif figura == "Círculo":
        entry_radio.delete(0, tk.END)
        entry_radio.insert(0, memoria_figuras["Círculo"]["radio"])
    elif figura == "Triángulo":
        entry_base.delete(0, tk.END)
        entry_base.insert(0, memoria_figuras["Triángulo"]["base"])
        entry_altura.delete(0, tk.END)
        entry_altura.insert(0, memoria_figuras["Triángulo"]["altura"])
        entry_lado2.delete(0, tk.END)
        entry_lado2.insert(0, memoria_figuras["Triángulo"]["lado2"])
        entry_lado3.delete(0, tk.END)
        entry_lado3.insert(0, memoria_figuras["Triángulo"]["lado3"])

def mostrar_campos(event=None):
    figura_actual = combo_figura.get()
    
    # Guardar valores de la figura anterior antes de cambiar
    if 'figura_anterior' in mostrar_campos.__dict__:
        guardar_en_memoria()
    mostrar_campos.figura_anterior = figura_actual  # Guardar referencia
    
    # Limpiar la interfaz
    for widget in frame_campos.winfo_children():
        widget.grid_remove()
    canvas.delete("all")
    formula.set("")
    
    # Mostrar campos y cargar valores guardados para la nueva figura
    if figura_actual == "Cuadrado":
        label_lado.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_lado.grid(row=0, column=1, padx=5, pady=5)
        cargar_de_memoria("Cuadrado")
    
    elif figura_actual == "Rectángulo":
        label_base.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_base.grid(row=0, column=1, padx=5, pady=5)
        label_altura.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entry_altura.grid(row=1, column=1, padx=5, pady=5)
        cargar_de_memoria("Rectángulo")
    
    elif figura_actual == "Círculo":
        label_radio.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_radio.grid(row=0, column=1, padx=5, pady=5)
        cargar_de_memoria("Círculo")
    
    elif figura_actual == "Triángulo":
        label_base.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_base.grid(row=0, column=1, padx=5, pady=5)
        label_altura.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entry_altura.grid(row=1, column=1, padx=5, pady=5)
        label_lado2.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        entry_lado2.grid(row=2, column=1, padx=5, pady=5)
        label_lado3.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        entry_lado3.grid(row=3, column=1, padx=5, pady=5)
        cargar_de_memoria("Triángulo")


def calcular():
    figura = combo_figura.get()
    
    try:
        if figura == "Cuadrado":
            lado = float(entry_lado.get())
            area = lado ** 2
            perimetro = 4 * lado
            dibujar_cuadrado(lado)
            formula.set(f"Área = Lado²\nPerímetro = 4 × Lado")
        
        elif figura == "Rectángulo":
            base = float(entry_base.get())
            altura = float(entry_altura.get())
            area = base * altura
            perimetro = 2 * (base + altura)
            dibujar_rectangulo(base, altura)
            formula.set(f"Área = Base × Altura\nPerímetro = 2 × (Base + Altura)")
        
        elif figura == "Círculo":
            radio = float(entry_radio.get())
            area = math.pi * radio ** 2
            perimetro = 2 * math.pi * radio
            dibujar_circulo(radio)
            formula.set(f"Área = π × Radio²\nPerímetro = 2π × Radio")
        
        elif figura == "Triángulo":
            base = float(entry_base.get())
            altura = float(entry_altura.get())
            lado2 = float(entry_lado2.get())
            lado3 = float(entry_lado3.get())
            area = (base * altura) / 2
            perimetro = base + lado2 + lado3
            dibujar_triangulo(base, altura, lado2, lado3)
            formula.set(f"Área = (Base × Altura) / 2\nPerímetro = Lado1 + Lado2 + Lado3")
        
        resultado.set(f"Área: {area:.2f} | Perímetro: {perimetro:.2f}")
    
    except Exception as e:
        messagebox.showerror("Error", f"Revisa los datos ingresados.\n{e}")

# Funciones para dibujar figuras (ajustadas a escala)
def dibujar_cuadrado(lado):
    canvas.delete("all")
    # Centrar el cuadrado en el Canvas (300x200)
    escala = min(150 / max(lado, 1), 30)  # Ajuste de escala
    x_centro, y_centro = 150, 100  # Centro del Canvas
    x1 = x_centro - (lado * escala) / 2
    y1 = y_centro - (lado * escala) / 2
    x2 = x_centro + (lado * escala) / 2
    y2 = y_centro + (lado * escala) / 2
    canvas.create_rectangle(x1, y1, x2, y2, outline="blue", width=2)
    canvas.create_text(x_centro, y1 - 15, text=f"Lado = {lado}", font=("Arial", 9))

def dibujar_rectangulo(base, altura):
    canvas.delete("all")
    escala = min(120 / max(base, altura, 1), 20)
    x_centro, y_centro = 150, 100
    x1 = x_centro - (base * escala) / 2
    y1 = y_centro - (altura * escala) / 2
    x2 = x_centro + (base * escala) / 2
    y2 = y_centro + (altura * escala) / 2
    canvas.create_rectangle(x1, y1, x2, y2, outline="green", width=2)
    canvas.create_text(x_centro, y1 - 15, text=f"Base = {base}", font=("Arial", 9))
    # Etiqueta de altura a la derecha y centrada verticalmente
    canvas.create_text(x2 + 25, y_centro, text=f"Altura = {altura}", font=("Arial", 9))

def dibujar_circulo(radio):
    canvas.delete("all")
    escala = min(80 / max(radio, 1), 15)
    x_centro, y_centro = 150, 100
    x1 = x_centro - radio * escala
    y1 = y_centro - radio * escala
    x2 = x_centro + radio * escala
    y2 = y_centro + radio * escala
    canvas.create_oval(x1, y1, x2, y2, outline="red", width=2)
    canvas.create_text(x_centro, y1 - 10, text=f"Radio = {radio}", font=("Arial", 9))

def dibujar_triangulo(base, altura, lado2, lado3):
    canvas.delete("all")
    escala = min(100 / max(base, altura, lado2, lado3, 1), 15)
    x_centro, y_centro = 150, 100
    x1 = x_centro - (base * escala) / 2
    y1 = y_centro + (altura * escala) / 2  # Ajuste para triángulo
    x2 = x_centro + (base * escala) / 2
    y2 = y_centro + (altura * escala) / 2
    x3 = x_centro
    y3 = y_centro - (altura * escala) / 2
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, outline="purple", fill="", width=2)
    canvas.create_text(x_centro, y1 + 15, text=f"Base = {base}", font=("Arial", 9))
    canvas.create_text(x3, y3 - 15, text=f"Altura = {altura}", font=("Arial", 9))

def mostrar_campos(event=None):
    figura = combo_figura.get()
    for widget in frame_campos.winfo_children():
        widget.grid_remove()
    
    if figura == "Cuadrado":
        label_lado.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_lado.grid(row=0, column=1, padx=5, pady=5)
    
    elif figura == "Rectángulo":
        label_base.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_base.grid(row=0, column=1, padx=5, pady=5)
        label_altura.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entry_altura.grid(row=1, column=1, padx=5, pady=5)
    
    elif figura == "Círculo":
        label_radio.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_radio.grid(row=0, column=1, padx=5, pady=5)
    
    elif figura == "Triángulo":
        label_base.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_base.grid(row=0, column=1, padx=5, pady=5)
        label_altura.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entry_altura.grid(row=1, column=1, padx=5, pady=5)
        label_lado2.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        entry_lado2.grid(row=2, column=1, padx=5, pady=5)
        label_lado3.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        entry_lado3.grid(row=3, column=1, padx=5, pady=5)
    
    canvas.delete("all")
    formula.set("")  # Limpiar fórmula al cambiar figura

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Calculadora de Área y Perímetro")
ventana.geometry("550x650")
ventana.config(bg="#f0f4f8")

# Frame principal
frame_principal = tk.Frame(ventana, bg="#f0f4f8")
frame_principal.pack(pady=10)

# Selección de figura
tk.Label(frame_principal, text="Seleccione la figura:", font=("Arial", 12), bg="#f0f4f8").grid(row=0, column=0, padx=10, pady=5, sticky="w")
combo_figura = ttk.Combobox(frame_principal, values=["Cuadrado", "Rectángulo", "Círculo", "Triángulo"])
combo_figura.grid(row=0, column=1, padx=10, pady=5)
combo_figura.bind("<<ComboboxSelected>>", mostrar_campos)

# Frame para campos de entrada
frame_campos = tk.Frame(ventana, bg="#f0f4f8")
frame_campos.pack(pady=10)

# Campos y etiquetas
label_lado = tk.Label(frame_campos, text="Lado:", bg="#f0f4f8")
entry_lado = tk.Entry(frame_campos)

label_base = tk.Label(frame_campos, text="Base:", bg="#f0f4f8")
entry_base = tk.Entry(frame_campos)

label_altura = tk.Label(frame_campos, text="Altura:", bg="#f0f4f8")
entry_altura = tk.Entry(frame_campos)

label_radio = tk.Label(frame_campos, text="Radio:", bg="#f0f4f8")
entry_radio = tk.Entry(frame_campos)

label_lado2 = tk.Label(frame_campos, text="Lado 2:", bg="#f0f4f8")
entry_lado2 = tk.Entry(frame_campos)

label_lado3 = tk.Label(frame_campos, text="Lado 3:", bg="#f0f4f8")
entry_lado3 = tk.Entry(frame_campos)

# Canvas para dibujos
canvas = tk.Canvas(ventana, width=300, height=200, bg="white", highlightthickness=1, highlightbackground="gray")
canvas.pack(pady=10)

# Frame para fórmulas
frame_formula = tk.Frame(ventana, bg="#f0f4f8")
frame_formula.pack(pady=5)

formula = tk.StringVar()
tk.Label(frame_formula, textvariable=formula, font=("Arial", 10, "italic"), bg="#f0f4f8", fg="navy").pack()

# Botón calcular
tk.Button(ventana, text="Calcular", command=calcular, bg="#007BFF", fg="white", font=("Arial", 11, "bold")).pack(pady=10)

# Resultado
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, font=("Arial", 12, "bold"), fg="green", bg="#f0f4f8").pack(pady=10)


ventana.protocol("WM_DELETE_WINDOW", lambda: [memoria_figuras.clear(), ventana.destroy()])

ventana.mainloop()