# Simulateur de clic en utilisant SELENIUM
1. Installez Python et Selenium en utilisant pip :
```bash
pip install selenium
```
2. Importez les modules Selenium et WebDriver :
```python
from selenium import webdriver
```
3. Ouvrez une instance du navigateur Web (par exemple, Chrome) et naviguez vers la page Web souhaitée :
```python
driver = webdriver.Chrome()
driver.get('https://www.example.com')
```
4. Trouvez l'élément de la page Web sur lequel vous souhaitez cliquer. Vous pouvez utiliser diverses méthodes pour trouver l'élément, telles que find_element_by_id, find_element_by_name, find_element_by_css_selector ou find_element_by_xpath. Par exemple, pour trouver un bouton avec l'ID "submit-button" :
```python
button = driver.find_element_by_id('submit-button')
```
5. Utilisez la méthode click de l'élément pour simuler un clic sur le bouton :
```python
button.click()
```
6. Fermez le navigateur Web lorsque vous avez terminé :
```python
driver.quit()
```
