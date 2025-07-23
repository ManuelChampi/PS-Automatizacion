from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ir directamente al link del reporte
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions/report?courseid=IS-2025Semestre_1&fsname=Curso_new")

try:
    time.sleep(5)

    # 3️⃣ Hacer clic en el botón "Expand All" para ver respuestas de los alumnos
    time.sleep(3)
    driver.find_element("id", "btn-expand-all").click()
    print("✅ Botón 'Collapse All' fue clickeado.")

except Exception as e:
    print(f"❌ Error durante la automatización: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
