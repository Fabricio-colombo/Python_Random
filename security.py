from selenium import webdriver


driver = webdriver.Chrome()


driver.get("https://www.globo.com/")


campo_de_formulario = driver.find_element_by_name("campo")
campo_de_formulario.send_keys("valor")


botao = driver.find_element_by_id("botao")
botao.click()


resultado = driver.find_element_by_id("resultado").text
if resultado == "sucesso":
    print("Teste bem-sucedido!")
else:
    print("Teste falhou.")


driver.quit()
