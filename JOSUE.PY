import tkinter as tk

# Función para procesar el formulario
def submit_form():
    NOMBRE_COMPLETO = name_entry.get()
    CORREO_ELECTRONICO = email_entry.get()
    DESCRIPCION = message_text.get("1.0", "end-1c")
    
    # Aquí puedes agregar la lógica para procesar los datos del formulario
    print(f"NOMBRE_COMPLETO: {NOMBRE_COMPLETO}")
    print(f"CORREO_ELECTRONICO: {CORREO_ELECTRONICO}")
    print(f"DESCRIPCION : {DESCRIPCION}")
    
    # Limpiar los campos del formulario
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    message_text.delete("1.0", tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("FORMULARIO")

# Crear los widgets del formulario
name_label = tk.Label(root, text="NOMBRE COMPLETO")
name_entry = tk.Entry(root)

email_label = tk.Label(root, text="CORREO ELECTRONICO:")
email_entry = tk.Entry(root)

message_label = tk.Label(root, text="DESCRIPCION :")
message_text = tk.Text(root, height=5, width=30)

submit_button = tk.Button(root, text="GUARDAR", command=submit_form)

# Organizar los widgets en la ventana
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry.grid(row=0, column=1, padx=10, pady=10)

email_label.grid(row=1, column=0, padx=10, pady=10)
email_entry.grid(row=1, column=1, padx=10, pady=10)

message_label.grid(row=2, column=0, padx=10, pady=10)
message_text.grid(row=2, column=1, padx=10, pady=10)

submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()

