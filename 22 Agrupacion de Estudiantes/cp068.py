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

    # 2️⃣ Preview como INSTRUCTOR
    select_instructor = Select(driver.find_element("id", "preview-instructor"))
    select_instructor.select_by_value("0: mchampis@unsa.edu.pe")
    time.sleep(1)
    driver.find_element("id", "btn-preview-instructor").click()
    print("✅ Preview como instructor hecho correctamente.")

except Exception as e:
    print(f"❌ Error durante la automatización: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
