import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2

DB_CONFIG = {
    "dbname": "pelucan_ddl.sql",       # Reemplaza con el nombre de tu base de datos
    "user": "postgres",           # Tu usuario de PostgreSQL
    "password": "tu_password",    # Tu contraseña de PostgreSQL
    "host": "localhost",
    "port": "5432"
}

class ListadoMascotasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PELUCAN - Listado de Mascotas")
        self.root.geometry("800x450")
        self.root.config(bg="#f9f9f9")

        titulo_label = tk.Label(
            root, 
            text="Listado General de Mascotas", 
            font=("Arial", 16, "bold"), 
            bg="#f9f9f9", 
            fg="#333333"
        )
        titulo_label.pack(pady=15)

        frame_tabla = tk.Frame(root)
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.columnas = ("id", "nombre", "raza", "edad", "tamano", "duenio")
        self.tree = ttk.Treeview(frame_tabla, columns=self.columnas, show="headings", selectmode="browse")

        self.tree.heading("id", text="ID")
        self.tree.heading("nombre", text="Mascota")
        self.tree.heading("raza", text="Raza")
        self.tree.heading("edad", text="Edad")
        self.tree.heading("tamano", text="Tamaño")
        self.tree.heading("duenio", text="Dueño (Cliente)")

        self.tree.column("id", width=50, anchor=tk.CENTER)
        self.tree.column("nombre", width=130, anchor=tk.W)
        self.tree.column("raza", width=130, anchor=tk.W)
        self.tree.column("edad", width=60, anchor=tk.CENTER)
        self.tree.column("tamano", width=100, anchor=tk.CENTER)
        self.tree.column("duenio", width=200, anchor=tk.W)

        scrollbar = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        frame_botones = tk.Frame(root, bg="#f9f9f9")
        frame_botones.pack(fill=tk.X, padx=20, pady=15)

        btn_actualizar = tk.Button(
            frame_botones, 
            text="Actualizar Lista", 
            command=self.cargar_datos, 
            bg="#4CAF50", 
            fg="white", 
            font=("Arial", 10, "bold"),
            padx=10, 
            pady=5
        )
        btn_actualizar.pack(side=tk.LEFT)

        btn_salir = tk.Button(
            frame_botones, 
            text="Salir", 
            command=root.quit, 
            bg="#f44336", 
            fg="white", 
            font=("Arial", 10, "bold"),
            padx=10, 
            pady=5
        )
        btn_salir.pack(side=tk.RIGHT)

        self.cargar_datos()

    def cargar_datos(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        try:
            conexion = psycopg2.connect(**DB_CONFIG)
            cursor = conexion.cursor()
            query = """
                SELECT 
                    m.id_mascota, 
                    m.nombre, 
                    m.raza, 
                    m.edad, 
                    m.tamano, 
                    c.nombre || ' ' || c.apellido AS duenio
                FROM mascota m
                JOIN cliente c ON m.id_cliente = c.id_cliente
                ORDER BY m.id_mascota ASC;
            """
            cursor.execute(query)
            registros = cursor.fetchall()

            for row in registros:
                self.tree.insert("", tk.END, values=row)

                cursor.close()
            conexion.close()
        except psycopg2.OperationalError as e:
            messagebox.showerror(
                "Error de Conexión", 
                "No se pudo conectar a la base de datos PostgreSQL.\nVerifica los parámetros de conexión (DB_CONFIG).\n\nDetalle: " + str(e)
            )
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al cargar los datos: {str(e)}")
    if __name__ == "__main__":
    root = tk.Tk()
    app = ListadoMascotasApp(root)
    root.mainloop()

        


    