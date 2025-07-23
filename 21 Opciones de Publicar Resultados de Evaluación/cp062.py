from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ir directamente al link del reporte
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/sessions/result?courseid=IS-2025Semestre_1&fsname=Curso_new&previewas=mariochampi12@gmail.com")

try:
    # Esperar que cargue la página principal
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "mainContent"))
    )
    print("Página cargada correctamente.")

    # Desplazarse hacia abajo lentamente
    for _ in range(5):
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)

    print("Desplazamiento hacia abajo completado.")

except Exception as e:
    print(f"Ocurrió un error: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
