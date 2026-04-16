# 📈 Automatización de Análisis de Acciones / Stock Analysis Automation

> [🇪🇸 Español](#español) | [🇺🇸 English](#english)

---

<a name="español"></a>
## 🇪🇸 Descripcion en Español

## Este proyecto automatiza la extracción de datos financieros, realiza cálculos estadísticos y envía un reporte por correo electrónico.

### Funcionalidades
* Extracción de datos en tiempo real con `yfinance`.
* Análisis de cotizaciones (Máxima, Mínima y Media) con `pandas`.
* Envío automatizado de reportes vía Gmail usando `pyautogui`.

### 🛠️ Tecnologías
* Python 3.12+
* Pandas / YFinance
* PyAutoGUI / Pyperclip

### ¿Como usarlo?
Para ejecutar este proyecto en tu computadora, sigue estos pasos:

**Clonar el repositorio o descargar los archivos:**
   Si tienes Git: `git clone https://github.com/TuUsuario/analisis-de-acciones.git`

**Instalar las librerías necesarias:**
   Abre una terminal en la carpeta del proyecto y ejecuta: pip install -r requirements.txt

##Nota importante
Este script utiliza PyAutoGUI para automatizar clics en el navegador. Las coordenadas de los clics en el archivo main.py están configuradas para una resolución de pantalla específica. Es posible que necesites ajustar los valores en pyautogui.click(x, y) para que coincidan con tu monitor y la posición del botón "Redactar" en Gmail.

## 💡 Lo que aprendí
Desarrollé este script para practicar la integración de APIs financieras y la automatización de interfaces de usuario (GUI), mejorando la eficiencia en el reporte de datos.




---

<a name="english"></a>
## 🇺🇸 Description in English

📈 Financial Analysis Automation
This project automates financial data extraction, performs statistical calculations, and sends a report via email.

Features
Real-time data extraction using yfinance.

Stock quote analysis (High, Low, and Average) with pandas.

Automated report delivery via Gmail using pyautogui.

🛠️ Technologies
Python 3.12+

Pandas / YFinance

PyAutoGUI / Pyperclip

How to use it?
To run this project on your computer, follow these steps:

Clone the repository or download the files:
If you have Git: git clone https://github.com/YourUser/stock-analysis.git

Install the necessary libraries:
Open a terminal in the project folder and run: pip install -r requirements.txt

⚠️ Important Note
This script uses PyAutoGUI to automate browser clicks. The click coordinates in the main.py file are configured for a specific screen resolution. You may need to adjust the values in pyautogui.click(x, y) to match your monitor and the position of the "Compose" button in Gmail.

💡 What I learned
I developed this script to practice financial API integration and graphical user interface (GUI) automation, improving efficiency in data reporting.



