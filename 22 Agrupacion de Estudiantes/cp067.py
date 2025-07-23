from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ir al reporte del instructor
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions/report?courseid=IS-2025Semestre_1&fsname=Curso_new")
try:
    # Esperar unos segundos a que cargue todo
    time.sleep(5)

    # Buscar el select y seleccionar por VALUE
    select_element = driver.find_element("id", "preview-student")
    select = Select(select_element)
    select.select_by_value("1: mariochampi12@gmail.com")

    time.sleep(1)

    # Hacer clic en el botón Preview as Student
    preview_button = driver.find_element("id", "btn-preview-student")
    preview_button.click()

    print("✅ Se realizó correctamente el preview como Manuel.")
except Exception as e:
    print(f"❌ Ocurrió un error al intentar hacer el preview como estudiante: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
