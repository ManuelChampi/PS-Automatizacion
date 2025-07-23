from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ir directamente a la página de sesiones
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions")

try:
    # Esperar a que el botón esté presente y hacer clic
    btn_add_session = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "btn-add-session"))
    )
    btn_add_session.click()
    print("✅ Se hizo clic en 'Add New Feedback Session'.")

except Exception as e:
    print(f"❌ Error al hacer clic en el botón: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
