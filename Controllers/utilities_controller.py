# Controllers/utilities_controller.py
import customtkinter as ctk



def seleccionar_archivo(self):
        ruta = ctk.filedialog.askopenfilename(
            title="Seleccionar archivo",
            filetypes=[("Todos los archivos", "*.*")]
        )
        if ruta:
            self.ruta_archivo = ruta
            self.ruta_archivo_label.configure(text=ruta)



# Entrada de contraseña
def accion_checkbox(self):
    if self.get():
        self.entry_clave.configure(show="")
    else:
        self.entry_clave.configure(show="*")



def mostrar_pestana(self, pestana):
        # Ocultar todos los frames
        for f in [self.frame_texto, self.frame_archivo]:
            f.pack_forget()
    
        # Mostrar el frame actual
        pestana.pack(fill="both", expand=True)

        modo_actual = ctk.get_appearance_mode()

        # Actualizar estilos de botones
        if modo_actual == "Dark":  
            if pestana == self.frame_texto:
                self.btn_texto.configure(text_color="#2fa371", fg_color="#151515", bg_color="#151515")
                self.btn_archivo.configure(text_color="gray", fg_color="#1b1b1b", bg_color="#1b1b1b")
            else:
                self.btn_texto.configure(text_color="gray", fg_color="#1b1b1b", bg_color="#1b1b1b")
                self.btn_archivo.configure(text_color="#2fa371", fg_color="#151515", bg_color="#151515")
        else:
            if pestana == self.frame_texto:
                self.btn_texto.configure(text_color="#2fa371", fg_color="#fff4e7", bg_color="#fff4e7")
                self.btn_archivo.configure(text_color="gray", fg_color="#e4fec7", bg_color="#e4fec7")
            else:
                self.btn_texto.configure(text_color="gray", fg_color="#e4fec7", bg_color="#e4fec7")
                self.btn_archivo.configure(text_color="#2fa371", fg_color="#fff4e7", bg_color="#fff4e7")