# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

#se initializeaza un obiect driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#se acceseaza website-ul dorit
driver.get("https://demoqa.com/text-box")

#maximizez fereastra pentru a putea accesa toate elementele din pagina
driver.maximize_window()

#implicitly wait "obliga" cautarea elementelor timp de 3 secunde
driver.implicitly_wait(1)

#accesez campul de username identificand prin id
full_name_field = driver.find_element(By.CSS_SELECTOR, "#userName")

#Inserez date in campul de username
full_name_field.send_keys("Doe")
time.sleep(1)

#accesez campul de email identificand prin metoda parinte > copil
email_field = driver.find_element(By.CSS_SELECTOR, "div > input[type='email']")

#Inserez date in campul de email
email_field.send_keys("email@email.com")
time.sleep(1)

#accesez campul current adress identificand prin clasa tagului
#fiind 2 elemente care contin clasa form-control il aleg pe primul
#din lista returnata accesand indexul acestuia
current_adress_textarea = driver.find_elements(By.CSS_SELECTOR, "textarea.form-control")[0]

#inserez data in campul current adress
current_adress_textarea.send_keys("Adress")
time.sleep(1)

#accesez campul permanent adress identificand prin clasa tagului
#fiind 2 elemente care contin clasa form-control il aleg pe al doilea
#din lista returnata accesand indexul acestuia
permanent_adress_textarea = driver.find_elements(By.CSS_SELECTOR, "textarea.form-control")[1]

#inserez date in campul permanent adress
permanent_adress_textarea.send_keys("Permanent Adress")
time.sleep(1)

#accesez butonul de submit si dau click
submit_button = driver.find_element(By.CSS_SELECTOR, "#submit")
driver.execute_script("arguments[0].scrollIntoView();", submit_button)
#scriptul de mai sus merge in jos pe pagina pana gaseste elementul cautat
#(daca elementul nu este in prim-plan selenium va arunca o eroare,
# delimitare care la playwright nu exista!)
submit_button.click()

#accesez sectiunea cu valori numita output care apare pe pagina dupa logare
#stochez toate valorile din acea sectiune in variabile pentru a le putea verifica
output_name = driver.find_element(By.CSS_SELECTOR, "div#output > div > #name")
output_email = driver.find_element(By.CSS_SELECTOR, "div#output > div > #email")
output_adress = driver.find_element(By.CSS_SELECTOR, "div#output > div > #currentAddress")
output_permanent_adress = driver.find_element(By.CSS_SELECTOR, "div#output > div > #permanentAddress")

#se acceseaza textul din sectiunea output
#se foloseste metoda split pentru a separa ce este inainte de ":" si ceea ce este dupa
#dat fiindca metoda returneaza o lista cu 2 stringuri in acest caz se acceseaza
#al doilea string, acesta fiind valoarea care ma intereseaza
print(output_name.text.split(":")[1])

#se compara datele de logare scrise in test cu datele din sectiunea output
assert output_name.text.split(":")[1] == "Doe", "Numele introdus nu este corect!"
assert output_email.text.split(":")[1] == "email@email.com", "Email gresit!"
assert output_adress.text.split(":")[1] == "Adress"
assert output_permanent_adress.text.split(":")[1] == "Permanent Adress"

driver.quit()
