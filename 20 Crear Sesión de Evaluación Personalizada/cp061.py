from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar navegador con perfil instructor
chrome_options = Options()
chrome_options.add_argument(r"--user-data-dir=C:\Users\sailax\chrome_instructor")
chrome_options.add_argument("--profile-directory=Default")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

url = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions/edit?courseid=IS-2025Semestre_1&fsname=Curso_new&editingMode=true"
driver.get(url)

wait = WebDriverWait(driver, 20)

# Paso 1: Esperar y encontrar bloque de Pregunta 3
question_block = wait.until(EC.presence_of_element_located((
    By.XPATH,
    "//div[contains(@class, 'd-flex') and .//span[text()='3'] and .//span[@id='question-type']]"
)))
print("✅ Pregunta 3 encontrada:")
print(question_block.text)

# Paso 2: Click en el botón "Edit" dentro del bloque de la pregunta
edit_button = question_block.find_element(By.XPATH, ".//button[@id='btn-edit-question']")
edit_button.click()
print("🖊️ Clic en botón Edit")

# Paso 3: Hacer clic en el botón desplegable de visibilidad dentro de <tm-visibility-panel>
try:
    # Esperar que el componente tm-visibility-panel esté presente
    visibility_panel = wait.until(EC.presence_of_element_located((By.TAG_NAME, "tm-visibility-panel")))
    
    # Dentro de ese componente, buscar el botón con id="btn-question-visibility"
    visibility_dropdown = visibility_panel.find_element(By.ID, "btn-question-visibility")
    
    # Esperar que el botón sea clickeable y hacer clic
    wait.until(EC.element_to_be_clickable(visibility_dropdown)).click()
    print("✅ Click en botón de visibilidad")

    time.sleep(1)  # Espera corta para que cargue el menú

    # Esperar que aparezca la opción "Custom visibility options..." y hacer clic
    custom_option = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//button[contains(text(), "Custom visibility options...")]'
    )))
    custom_option.click()
    print("✅ Click en 'Custom visibility options...'")

except Exception as e:
    print("❌ Error en el paso de visibilidad:", e)

# Paso 5: Marcar los checkboxes necesarios
labels = [
    "Giver's Team Members can see Answer",
    "Other Students can see Answer",
    "Instructors can see Answer"
]

for label in labels:
    checkbox = wait.until(EC.presence_of_element_located((By.XPATH, f'//input[@type="checkbox" and @aria-label="{label}"]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
    if not checkbox.is_selected():
        checkbox.click()
    print(f"✅ Checkbox marcado: {label}")
    time.sleep(0.5)

print("✅ Todos los checkboxes marcados correctamente.")

driver.quit()