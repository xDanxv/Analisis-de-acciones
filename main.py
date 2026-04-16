import yfinance as yf
import pandas as pd
import pyautogui
import pyperclip
import webbrowser
import time

# 1. Configuración de datos
# Puedes cambiar el ticker por cualquier otro (ej. 'AAPL' para Apple)
ticker = "PETR4.SA" 
datos = yf.Ticker(ticker)

# Descargamos el historial de los últimos 6 meses
tabla = datos.history(period="6mo")
cotizaciones = tabla["Close"]

# 2. Análisis de datos
maxima = round(cotizaciones.max(), 2)
minima = round(cotizaciones.min(), 2)
media = round(cotizaciones.mean(), 2)

# 3. Preparación del mensaje
destinatario = "correo_ejemplo@gmail.com" # Cambia esto por el correo real
asunto = f"Análisis de Acciones - {ticker}"
mi_nombre = "Tu Nombre" # Pon tu nombre aquí

mensaje = f'''
Estimado gestor,

A continuación, detallo el análisis de la acción {ticker} de los últimos 6 meses:

- Cotización Máxima: USD {maxima}
- Cotización Mínima: USD {minima}
- Cotización Media: USD {media}

Quedo atento a cualquier observación o duda.

Saludos, 
{mi_nombre}
'''

# 4. Automatización de envío por Gmail
# Asegúrate de tener tu sesión de Gmail iniciada en el navegador
webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
time.sleep(5) # Esperamos a que cargue la página

pyautogui.PAUSE = 1

# IMPORTANTE: Estas coordenadas (86, 174) dependen de tu resolución de pantalla
# Si el botón "Redactar" no está ahí, deberás ajustarlas.
pyautogui.click(86, 174) 

# Pegar destinatario
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Pegar asunto
pyperclip.copy(asunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Pegar cuerpo del mensaje
pyperclip.copy(mensaje)
pyautogui.hotkey("ctrl", "v")

# Enviar (Ctrl + Enter es el atajo de Gmail para enviar)
pyautogui.hotkey("ctrl", "enter")

print("¡Análisis enviado con éxito!")
