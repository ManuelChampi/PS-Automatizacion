from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ir directamente al link del reporte
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions/edit?courseid=IS-2025Semestre_1&fsname=Curso_new&editingMode=true")

try:
    # Esperar hasta que aparezca cualquier pregunta
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "question-number"))
    )

    # Buscar todos los elementos con clase "question-number"
    question_headers = driver.find_elements(By.CLASS_NAME, "question-number")
    question_4_found = False

    # Verificar si alguno contiene el número 4
    for header in question_headers:
        if "Question 4" in header.text.strip():
            question_4_found = True
            print("✅ Se encontró la Question 4.")
            break

    if not question_4_found:
        print("❌ No se encontró la Question 4.")

except Exception as e:
    print(f"⚠️ Ocurrió un error al verificar las preguntas: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
