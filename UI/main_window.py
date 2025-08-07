# ui/main_window.py
from tkinter import Tk
import customtkinter as ctk
from PIL import Image, ImageTk
from Controllers.mode_controller import cambiar_modo
from Controllers.cutcopy_controller import copiar_text, borrar_text
from Controllers.aes_controller import cifrar, descifrar, cifrar_archivo, descifrar_archivo
from Controllers.utilities_controller import seleccionar_archivo, accion_checkbox, mostrar_pestana


class AESApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cifrador AES - JESMdev")
        self.geometry("1000x600")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.grid_columnconfigure(0, weight=1)
        self.configure(bg_color="#151515", fg_color="#151515")

        # Contenedor principal
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)

        # Pestaña 1: Textos
        self.frame_texto = ctk.CTkFrame(self.main_frame)
        
        # Pestaña 2: Archivos
        self.frame_archivo = ctk.CTkFrame(self.main_frame)

        # Botones para cambiar pestaña
        self.btn_texto = ctk.CTkButton(
            master=self,
            text="Texto",
            command=lambda:mostrar_pestana(self, self.frame_texto),
            hover=False,   
            font=("Satoshi", 14),
            width=110,
            text_color="#2fa371",                
            fg_color="#151515", 
            bg_color="#151515"  
        )
        self.btn_texto.place(x=32, y=14)

        self.btn_archivo = ctk.CTkButton(
            master=self,
            text="Archivo",
            command=lambda:mostrar_pestana(self, self.frame_archivo),
            hover=False,
            font=("Satoshi", 14),
            width=110,
            text_color="gray",
            fg_color="#151515",
            bg_color="#151515"
        )
        self.btn_archivo.place(x=207, y=14)

        # Mostrar la pestaña inicial
        mostrar_pestana(self, self.frame_texto)

        # CONTENIDO DE LA PESTAÑA 1
        self.inicializar_pestana_texto()

        # CONTENIDO DE LA PESTAÑA 2
        self.inicializar_pestana_archivos()

        # Boton modo: light/dark mode
        # Imagen: light/dark mode Icono
        modo_photo = ctk.CTkImage(
            light_image=Image.open("C:/Program Files/VSCProjects/Python/EncriptadorAES/Assets/moon-stars.png"),
            dark_image=Image.open("C:/Program Files/VSCProjects/Python/EncriptadorAES/Assets/sun.png"),
            size=(20, 20)
        )
        self.btn_modo = ctk.CTkButton(self, text="", image=modo_photo, command=lambda:cambiar_modo(self), width=40, height=40, bg_color="#151515")
        self.btn_modo.place(x=950, y=550)



    def inicializar_pestana_texto(self):        
        # Head Transparente
        self.arriba_frame = ctk.CTkFrame(self.frame_texto, fg_color="transparent")  
        self.arriba_frame.pack(pady=(20, 0))

        # Imagenes
        # Imagen: Fondo
        fondo_photo = ctk.CTkImage(
            light_image=Image.open("C:/Program Files/VSCProjects/Python/EncriptadorAES/Assets/4.png"),
            dark_image=Image.open("C:/Program Files/VSCProjects/Python/EncriptadorAES/Assets/2.png"),
            size=(1000, 600)
        )
        fondo_label = ctk.CTkLabel(self.frame_texto, image=fondo_photo, text="")
        fondo_label.image = fondo_photo # type: ignore
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Imagen: Logo
        self.iconbitmap("C:/Program Files/VSCProjects/Python/EncriptadorAES/Assets/AESLogo.ico")

        # Imagen: Copiar Icono
        copiar_photo = ctk.CTkImage(
            light_image=Image.open("C:/Program Files/VSCProjects/Python/EncriptadorAES/Assets/copy.png"),
            dark_image=Image.open("C:/Program Files/VSCProjects/Python/EncriptadorAES/Assets/copy.png"),
            size=(22, 25)
        )

        # Imagen: Borrar Icono
        borrar_photo = ctk.CTkImage(
            light_image=Image.open("C:/Program Files/VSCProjects/Python/EncriptadorAES/Assets/eraser.png"),
            dark_image=Image.open("C:/Program Files/VSCProjects/Python/EncriptadorAES/Assets/eraser.png"),
            size=(22, 25)
        )

        # Titulo del TextBox: Ingreso
        self.titleBox_lbl = ctk.CTkLabel(self.frame_texto, text="Escribí tu texto aquí:", font=("Satoshi", 16), bg_color="#151515")
        self.titleBox_lbl.place(x=140, y=180)

        # Entrada de texto
        self.entry_texto = ctk.CTkTextbox(self.frame_texto, width=500, height=100, fg_color="transparent", corner_radius=2)
        self.entry_texto.pack(pady=5)
        self.entry_texto.place(x=145, y=216)

        # Boton Texto: Borrar
        self.btn_borrar = ctk.CTkButton(self.frame_texto, width=30, height=30, text="", image=borrar_photo, command=lambda:borrar_text(self), bg_color="#151515")
        self.btn_borrar.place(x=650, y=216)

        self.entry_clave = ctk.CTkEntry(self.frame_texto, placeholder_text="Contraseña de cifrado", show="*", bg_color="#151515")
        self.entry_clave.place(x=145, y=336)
        self.checkBox_clave = ctk.CTkCheckBox(
            master=self.frame_texto,
            text="",
            fg_color="#2fa371",       # color del cuadrado cuando está marcado
            border_color="gray",      # color del borde
            hover_color="#1e1e1e",    # color al pasar el mouse
            checkmark_color="white",  # color del tilde
            font=("Satoshi", 14), 
            bg_color="#151515", 
            command=lambda:accion_checkbox(self)
        )
        self.checkBox_clave.place(x=300, y=338)

        # Botones Principales
        self.frame_botones = ctk.CTkFrame(
            self.frame_texto,
            corner_radius=10,
            bg_color="#151515",     
            border_color="#2fa371", 
            border_width=2
        )
        self.frame_botones.place(x=145, y=370) # 240

        self.btn_cifrar = ctk.CTkButton(self.frame_botones, text="🔐 Cifrar", corner_radius=6, command=lambda:cifrar(self))
        self.btn_cifrar.grid(row=1, column=0, padx=5, pady=5,  sticky="ew")

        self.btn_descifrar = ctk.CTkButton(self.frame_botones, text="🔓 Descifrar", corner_radius=6, command=lambda:descifrar(self))
        self.btn_descifrar.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Titulo del TextBox: Egreso
        self.titleOBox_lbl = ctk.CTkLabel(self.frame_texto, text="Resultado:", font=("Satoshi", 16), bg_color="#151515")
        self.titleOBox_lbl.place(x=140, y=420)

        # Salida
        self.output = ctk.CTkTextbox(self.frame_texto, width=500, height=100, fg_color="transparent", corner_radius=2)
        self.output.pack(pady=(10,0))
        self.output.place(x=145, y=456)

        # Boton Portapapeles: Copiar
        self.btn_copiar = ctk.CTkButton(self.frame_texto, width=30, height=30, text="", image=copiar_photo, command=lambda:copiar_text(self), bg_color="#151515")
        self.btn_copiar.place(x=650, y=456)






    def inicializar_pestana_archivos(self):
        self.arriba_frame = ctk.CTkFrame(self.frame_archivo, fg_color="transparent")  
        self.arriba_frame.pack(pady=(20, 0))

        fondo_photo = ctk.CTkImage(
            light_image=Image.open("C:/Program Files/VSCProjects/Python/EncriptadorAES/Assets/5.png"),
            dark_image=Image.open("C:/Program Files/VSCProjects/Python/EncriptadorAES/Assets/3.png"),
            size=(1000, 600)
        )
        fondo_label = ctk.CTkLabel(self.frame_archivo, image=fondo_photo, text="")
        fondo_label.image = fondo_photo # type: ignore
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.ruta_archivo = ""

        # Etiqueta para mostrar la ruta
        self.ruta_archivo_label = ctk.CTkLabel(self.frame_archivo, text="Ningún archivo seleccionado.", wraplength=500, bg_color="#151515")
        self.ruta_archivo_label.place(x=150, y=230)

        # Botón para seleccionar archivo
        self.seleccionar_btn = ctk.CTkButton(self.frame_archivo, text="Seleccionar archivo", command=lambda:seleccionar_archivo(self), bg_color="#151515")
        self.seleccionar_btn.place(x=150, y=200)

        # Entrada de contraseña
        def toggle_ver_clave():
            if self.checkBox_clave.get():
                self.entry_clave.configure(show="")
            else:
                self.entry_clave.configure(show="*")

        self.entry_clave_a = ctk.CTkEntry(self.frame_archivo, placeholder_text="Contraseña de cifrado", show="*", bg_color="#151515")
        self.entry_clave_a.place(x=145, y=336)
        self.checkBox_clave_a = ctk.CTkCheckBox(
            master=self.frame_archivo,
            text="",
            fg_color="#2fa371",       # color del cuadrado cuando está marcado
            border_color="gray",      # color del borde
            hover_color="#1e1e1e",    # color al pasar el mouse
            checkmark_color="white",  # color del tilde
            font=("Satoshi", 14), 
            bg_color="#151515", 
            command=lambda: toggle_ver_clave()
        )
        self.checkBox_clave_a.place(x=300, y=338)

        # Botones cifrar / descifrar
        self.frame_botones_a = ctk.CTkFrame(
            self.frame_archivo,
            corner_radius=10,
            bg_color="#151515",     
            border_color="#2fa371", 
            border_width=2
        )
        self.frame_botones_a.place(x=145, y=370) # 240
        self.btn_cifrar_a = ctk.CTkButton(self.frame_botones_a, text="🔐 Cifrar Archivo", command=lambda:cifrar_archivo(self))
        self.btn_cifrar_a.grid(row=1, column=0, padx=5, pady=5,  sticky="ew")
        #btn_cifrar.place(x=150,y=400)

        self.btn_descifrar_a = ctk.CTkButton(self.frame_botones_a, text="🔓 Descifrar Archivo", command=lambda:descifrar_archivo(self))
        self.btn_descifrar_a.grid(row=1, column=1, padx=5, pady=5,  sticky="ew")
        #btn_descifrar.place(x=655,y=400)

    
    

    

