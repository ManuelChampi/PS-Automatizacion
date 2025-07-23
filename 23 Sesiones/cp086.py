from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ir a la URL del reporte de la sesión
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions/report?courseid=IS-2025Semestre_1&fsname=Curso_new")

try:
    wait = WebDriverWait(driver, 10)

    # Buscar el elemento que contiene la fecha única (results visible from)
    result_visible_element = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//p[contains(@class, 'form-control-static') and contains(text(), 'Thu, 17 Jul, 2025, 10:00 PM')]")
    ))

    for elem in result_visible_element:
        print("✅ Results visible from:")
        print(elem.text.strip())

except Exception as e:
    print(f"❌ Ocurrió un error al buscar la fecha de visibilidad de resultados: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
