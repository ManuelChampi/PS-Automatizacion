from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ir directamente al link del reporte
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions/edit?courseid=IS-2025Semestre_1&fsname=Curso_new&editingMode=true")

# Esperar a que cargue toda la página (ajustar si es necesario)
time.sleep(5)

# Hacer scroll hacia abajo para asegurarse de que el botón esté visible
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Hacer clic en el botón "Add New Question"
add_question_button = driver.find_element(By.ID, "btn-new-question")
add_question_button.click()

print("✅ Se hizo clic en 'Add New Question'.")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
