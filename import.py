import tkinter as tk
from tkinter import messagebox

def filtrar_palabra():
    # Obtenemos el texto del campo de entrada
    palabra = entrada_palabra.get()

    # Definir los caracteres a eliminar
    caracteres_a_eliminar = ['x', 'y', '.', ',', ' ']

    # Filtrar la palabra
    palabra_filtrada = ''.join(c for c in palabra if c.lower() not in caracteres_a_eliminar)

    # Mostrar la palabra filtrada en la etiqueta
    etiqueta_resultado.config(text=f"Palabra filtrada: {palabra_filtrada}")

    # Activar el botón de copiar
    boton_copiar.config(state=tk.NORMAL)

    return palabra_filtrada

def copiar_al_portapapeles():
    palabra_filtrada = etiqueta_resultado.cget("text").replace("Palabra filtrada: ", "")
    
    if palabra_filtrada:
        root.clipboard_clear()  # Limpiar portapapeles
        root.clipboard_append(palabra_filtrada)  # Agregar al portapapeles
        messagebox.showinfo("Copiado", "La palabra filtrada ha sido copiada al portapapeles.")
    else:
        messagebox.showwarning("Error", "Primero filtra una palabra.")

# Crear la ventana principal
root = tk.Tk()
root.title("Filtrar Palabra")

# Crear la entrada de texto
entrada_palabra = tk.Entry(root, width=30)
entrada_palabra.grid(row=0, column=0, padx=10, pady=10)

# Crear el botón de filtrar
boton_filtrar = tk.Button(root, text="Filtrar", command=filtrar_palabra)
boton_filtrar.grid(row=0, column=1, padx=10, pady=10)

# Etiqueta para mostrar el resultado filtrado
etiqueta_resultado = tk.Label(root, text="Palabra filtrada: ", width=40)
etiqueta_resultado.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Crear el botón de copiar
boton_copiar = tk.Button(root, text="Copiar", state=tk.DISABLED, command=copiar_al_portapapeles)
boton_copiar.grid(row=2, column=0, columnspan=2, pady=10)

# Iniciar la interfaz gráfica
root.mainloop()
