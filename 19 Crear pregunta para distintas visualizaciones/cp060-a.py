from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Ruta al Chrome for Testing del estudiante
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

options.add_argument("--start-maximized")
# URL del estudiante
url = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/sessions/result?courseid=IS-2025Semestre_1&fsname=Curso_new&previewas=manuelmariochs@gmail.com"
driver.get(url)

# Espera a que cargue la página
time.sleep(3)

# Scroll automático hasta el fondo
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Espera para que cargue contenido adicional
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Espera extra por si se carga tarde
time.sleep(2)

# Buscar y hacer clic en todos los botones [more]
buttons = driver.find_elements(By.XPATH, "//button[contains(text(), '[more]')]")
print(f"🔍 Se encontraron {len(buttons)} botones '[more]'. Haciendo clic en cada uno...")

for i, button in enumerate(buttons, start=1):
    try:
        driver.execute_script("arguments[0].scrollIntoView();", button)
        time.sleep(0.5)
        button.click()
        print(f"✅ Botón [{i}] clickeado.")
    except Exception as e:
        print(f"❌ Error al hacer clic en el botón [{i}]: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
