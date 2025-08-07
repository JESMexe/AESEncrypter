# Controllers/aes_controller.py
from Helpers.AES_helper import encrypt, decrypt, encrypt_file, decrypt_file

def cifrar(app):
    texto = app.entry_texto.get("0.0", "end").strip()
    clave = app.entry_clave.get().strip()
    if not texto and not clave:
        app.output.delete("0.0", "end")
        app.output.insert("0.0", "⚠️ Ingresá texto y contraseña.")
        return
    elif not texto:
        app.output.delete("0.0", "end")
        app.output.insert("0.0", "⚠️ Ingresá un texto.")
        return
    elif not clave:
        app.output.delete("0.0", "end")
        app.output.insert("0.0", "⚠️ Ingresá una contraseña.")
        return

    try:
        resultado = encrypt(texto, clave)
        app.output.delete("0.0", "end")
        app.output.insert("0.0", resultado)
    except Exception as e:
        app.output.delete("0.0", "end")
        app.output.insert("0.0", f"Error al cifrar: {e}")

def descifrar(app):
    texto = app.entry_texto.get("0.0", "end").strip()
    clave = app.entry_clave.get().strip()
    if not texto and not clave:
            app.output.delete("0.0", "end")
            app.output.insert("0.0", "⚠️ Ingresá texto y contraseña.")
            return
    elif not texto:
        app.output.delete("0.0", "end")
        app.output.insert("0.0", "⚠️ Ingresá un texto.")
        return
    elif not clave:
        app.output.delete("0.0", "end")
        app.output.insert("0.0", "⚠️ Ingresá una contraseña.")
        return
    
    try:
        resultado = decrypt(texto, clave)
        app.output.delete("0.0", "end")
        app.output.insert("0.0", resultado)
    except Exception as e:
        app.output.delete("0.0", "end")
        app.output.insert("0.0", f"Error al descifrar: {e}")

def cifrar_archivo(self):
    if not self.ruta_archivo:
        self.ruta_archivo_label.configure(text="⚠️ Seleccioná un archivo primero.")
        return

    password = self.entry_clave.get()
    if not password:
        self.ruta_archivo_label.configure(text="⚠️ Ingresá una contraseña.")
        return

    try:
        encrypt_file(self.ruta_archivo, password)
        self.ruta_archivo_label.configure(text="✅ Archivo cifrado exitosamente.")
    except Exception as e:
        self.ruta_archivo_label.configure(text=f"❌ Error al cifrar: {e}")

def descifrar_archivo(self):
    if not self.ruta_archivo:
        self.ruta_archivo_label.configure(text="⚠️ Seleccioná un archivo primero.")
        return

    password = self.entry_clave.get()
    if not password:
        self.ruta_archivo_label.configure(text="⚠️ Ingresá una contraseña.")
        return

    try:
        output_path = self.ruta_archivo.replace(".aes", "") + "_descifrado"
        decrypt_file(self.ruta_archivo, password, output_path)
        self.ruta_archivo_label.configure(text=f"✅ Archivo descifrado: {output_path}")
    except Exception as e:
        self.ruta_archivo_label.configure(text=f"❌ Error al descifrar: {e}")