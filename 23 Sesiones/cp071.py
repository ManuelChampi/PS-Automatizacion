from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ir directamente al link de cursos
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/courses")

try:
    # Esperar hasta que se muestre la tabla de cursos (puedes ajustar este ID o clase si cambia)
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table.table-courses"))
    )
    print("✅ Página de cursos cargada correctamente.")

except Exception as e:
    print(f"❌ Error al esperar la carga de la página: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()

