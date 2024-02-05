from selenium import webdriver

# Ścieżka do sterownika przeglądarki, na przykład chromedriver.exe dla Chrome
driver_path = 'ścieżka_do_sterownika/chromedriver.exe'

# Inicjalizacja przeglądarki
driver = webdriver.Chrome(executable_path=driver_path)

# Adres strony do otwarcia
url = 'https://www.example.com'
driver.get(url)

# Znajdź wszystkie elementy, które zawierają literę "a"
elements_with_a = driver.find_elements_by_xpath("//*[contains(text(), 'a')]")

# Wyświetl znalezione elementy
for element in elements_with_a:
    print(element.text)

# Zamknij przeglądarkę
driver.quit()
