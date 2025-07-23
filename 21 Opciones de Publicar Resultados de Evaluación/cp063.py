from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ir directamente al link del reporte
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/sessions/result?courseid=IS-2025Semestre_1&fsname=Curso_new&previewas=manuelmariochs@gmail.com")

try:
    # Esperar hasta que el encabezado de la pregunta 1 esté visible
    question_1 = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(@class, 'question-number') and contains(text(), 'Question 1:')]"))
    )

    if question_1:
        print("✅ Se encontró el encabezado 'Question 1:' correctamente.")

except Exception as e:
    print(f"❌ No se pudo encontrar 'Question 1:' - Error: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()

