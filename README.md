[README.MD.txt](https://github.com/user-attachments/files/26802680/README.MD.txt)


# Automatización de Análisis de Acciones

Este proyecto automatiza la extracción de datos financieros, realiza cálculos estadísticos y envía un reporte por correo electrónico.

##  Funcionalidades
- Extracción de datos en tiempo real con `yfinance`.
- Análisis de cotizaciones (Máxima, Mínima y Media) con `pandas`.
- Envío automatizado de reportes vía Gmail usando `pyautogui`.

## 🛠 Tecnologías
- Python 3.12+
- Pandas / YFinance
- PyAutoGUI / Pyperclip

## ¿Como usarlo?
Para ejecutar este proyecto en tu computadora, sigue estos pasos:

**Clonar el repositorio o descargar los archivos:**
   Si tienes Git: `git clone https://github.com/TuUsuario/analisis-de-acciones.git`

**Instalar las librerías necesarias:**
   Abre una terminal en la carpeta del proyecto y ejecuta:
   ```bash
   pip install -r requirements.txt

##Nota importante
Nota importante: Este script utiliza PyAutoGUI para automatizar clics en el navegador. Las coordenadas de los clics en el archivo main.py están configuradas para una resolución de pantalla específica. Es posible que necesites ajustar los valores en pyautogui.click(x, y) para que coincidan con tu monitor y la posición del botón "Redactar" en Gmail.

## 💡 Lo que aprendí
Desarrollé este script para practicar la integración de APIs financieras y la automatización de interfaces de usuario (GUI), mejorando la eficiencia en el reporte de datos.
