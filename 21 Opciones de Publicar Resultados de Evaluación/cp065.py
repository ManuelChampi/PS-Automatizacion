from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ir directamente al link del formulario de edición
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions/edit?courseid=IS-2025Semestre_1&fsname=Curso_new&editingMode=true")

try:
    # Esperar a que aparezca el span con "2" dentro del h2
    question_2_span = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//h2[contains(@class, 'question-number')]//span[@id='question-number' and text()='2']"))
    )

    if question_2_span:
        print("✅ Se encontró correctamente el encabezado 'Question 2'.")

except Exception as e:
    print(f"❌ No se encontró el encabezado 'Question 2'. Error: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
