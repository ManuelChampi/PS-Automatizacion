from selenium import webdriver
import time

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ir directamente al link de estudiantes
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/students")

try:
    time.sleep(5)  # Esperar que cargue bien

    # Hacer clic en el botón desplegable (chevron)
    chevron_button = driver.find_element("css selector", "button.chevron")
    chevron_button.click()
    print("✅ Botón desplegable del curso clickeado correctamente.")

except Exception as e:
    print(f"❌ Error durante la automatización: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
