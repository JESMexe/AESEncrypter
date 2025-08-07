# Controllers/cutvopy_controller.py
import customtkinter as ctk
import pyperclip

def borrar_text(app):
    app.entry_texto.delete("0.0", "end")

def copiar_text(app):
    text = app.output.get("0.0", "end").strip()
    pyperclip.copy(text)