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

wait = WebDriverWait(driver, 20)

# Esperar a que el botón "Copy Question" esté visible y clickeable
copy_btn = wait.until(EC.element_to_be_clickable((By.ID, "btn-copy-question")))

# Hacer scroll hasta el botón y hacer clic
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", copy_btn)
copy_btn.click()

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
