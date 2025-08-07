# Controllers/mode_controller.py
import customtkinter as ctk

def cambiar_modo(app):
    modo_actual = ctk.get_appearance_mode()

    frame_actual = app.frame_texto if app.frame_texto.winfo_ismapped() else app.frame_archivo

    if modo_actual == "Dark":
        ctk.set_appearance_mode("light")
        app.configure(bg_color="#fff4e7")
        app.titleBox_lbl.configure(bg_color="#fff4e7")
        app.titleOBox_lbl.configure(bg_color="#fff4e7")
        app.frame_botones.configure(bg_color="#fff4e7")
        app.checkBox_clave.configure(bg_color="#fff4e7", hover_color="#e4fec7")
        app.checkBox_clave_a.configure(bg_color="#fff4e7", hover_color="#e4fec7")
        app.entry_clave.configure(bg_color="#fff4e7")
        app.entry_clave_a.configure(bg_color="#fff4e7")
        app.btn_copiar.configure(bg_color="#fff4e7")
        app.btn_modo.configure(bg_color="#fff4e7")
        app.btn_borrar.configure(bg_color="#fff4e7")
        app.frame_botones_a.configure(bg_color="#fff4e7")
        app.seleccionar_btn.configure(bg_color="#fff4e7")
        app.ruta_archivo_label.configure(bg_color="#fff4e7")
        if frame_actual == app.frame_texto:
            app.btn_texto.configure(text_color="#2fa371", fg_color="#fff4e7", bg_color="#fff4e7")
            app.btn_archivo.configure(text_color="gray", fg_color="#e4fec7", bg_color="#e4fec7")
        else:
            app.btn_archivo.configure(text_color="#2fa371", fg_color="#fff4e7", bg_color="#fff4e7")
            app.btn_texto.configure(text_color="gray", fg_color="#e4fec7", bg_color="#e4fec7")
    else:
        ctk.set_appearance_mode("dark")
        app.titleBox_lbl.configure(bg_color="#151515")
        app.titleOBox_lbl.configure(bg_color="#151515")
        app.frame_botones.configure(bg_color="#151515")
        app.checkBox_clave.configure(bg_color="#151515", hover_color="#1e1e1e")
        app.checkBox_clave_a.configure(bg_color="#151515", hover_color="#1e1e1e")
        app.entry_clave.configure(bg_color="#151515")
        app.entry_clave_a.configure(bg_color="#151515")
        app.btn_copiar.configure(bg_color="#151515")
        app.btn_modo.configure(bg_color="#151515")
        app.btn_borrar.configure(bg_color="#151515")
        app.frame_botones_a.configure(bg_color="#151515")
        app.seleccionar_btn.configure(bg_color="#151515")
        app.ruta_archivo_label.configure(bg_color="#151515")
        if frame_actual == app.frame_texto:
            app.btn_texto.configure(text_color="#2fa371", fg_color="#151515", bg_color="#151515")
            app.btn_archivo.configure(text_color="gray", fg_color="#1b1b1b", bg_color="#1b1b1b")
        else:
            app.btn_archivo.configure(text_color="#2fa371", fg_color="#151515", bg_color="#151515")
            app.btn_texto.configure(text_color="gray", fg_color="#1b1b1b", bg_color="#1b1b1b")
