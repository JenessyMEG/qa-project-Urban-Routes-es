import time

import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

#Localizadores
class UrbanRoutesPage:
    from_field = (By.ID, 'from')                         #Campo Desde
    to_field = (By.ID, 'to')                             #Campo Hasta
    button_order = (By.CSS_SELECTOR, ".button.round")     #Boton "Pedir Taxi"
    comfort_field = (By.XPATH, "//div[text()='Comfort']") #Opcion Comfort
    phone_number_field = (By.CLASS_NAME, "np-text")       #Campo Telefono
    space_phone_number = (By.ID, "phone")                 #Ventana emergente, campo Phone
    next_button = (By.XPATH, "//button[text()='Siguiente']")  #Boton siguiente
    space_code = (By.ID, "code")                          #Campo del codigo, confirmacion
    confirm_phone_button = (By.XPATH, "//button[text()='Confirmar']") #Boton de confirmar
    down = (By.CLASS_NAME, "tariff-picker.shown")       #Bajar cursor
    credit_field = (By.CLASS_NAME, "pp-button,filled")        #Campo "Tarjeta de Credito"
    credit_card_button = (By.CLASS_NAME, 'pp-plus')           #Boton + (Ventana emergente)
    card_number_field = (By.ID, "number")                   #Ventana emergente, campo agregar num de tarjeta
    cvd = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input")     #Campo de confirmacion
    other_space = (By.CLASS_NAME, "pp-buttons")      #Clic en otro lugar
    add_credit_card_button = (By.XPATH, "//button[text()='Agregar']")        #Boton agregar
    close_credit_button = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/button")       #Boton 2 "X"
    message_field = (By.ID, "comment")                       #Campo de comentario
    blanket_checkbox = (By.CLASS_NAME, "reqs.open")          #Campo Lista desplegable
    tissues_checkbox = (By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")   #Interruptor
    ice_creams_input = (By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]")    #Boton +
    request_taxi_button = (By.CLASS_NAME, "smart-button")     #Boton confirmar "Pedir carro"
    window_info_driver = (By.CLASS_NAME, "order-header-content")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#Metodos
    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def click_taxi(self):
        self.driver.find_element(*self.button_order).click()

    def select_comfort_rate(self):
        self.driver.find_element(*self.comfort_field).click()

    def enter_phone_number(self):
        self.driver.find_element(*self.phone_number_field).click()

    def put_phone_number(self,number):
        self.driver.find_element(*self.space_phone_number).send_keys(number)

    def press_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def code_phone_confirm(self,code):
        self.driver.find_element(*self.space_code).send_keys(code)

    def button_confirm(self):
        self.driver.find_element(*self.confirm_phone_button).click()

    def credit_card_field(self):
        self.driver.find_element(*self.credit_field).click()

    def credit_add_button(self):
        self.driver.find_element(*self.credit_card_button).click()

    def put_number_card(self, card_number):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)

    def put_number_cvd(self, number_cvd):
        self.driver.find_element(*self.cvd).send_keys(number_cvd)

    def other_place(self):
        self.driver.find_element(*self.other_space).click()

    def add_button(self):
        self.driver.find_element(*self.add_credit_card_button).click()

    def close_button(self):
        self.driver.find_element(*self.close_credit_button).click()

    def enter_message(self, message):
        self.driver.find_element(*self.message_field).send_keys(message)

    def deploy_checkbox(self):
        self.driver.find_element(*self.blanket_checkbox).click()

    def check_blanket(self):
        self.driver.find_element(*self.tissues_checkbox).click()

    def enter_ice_cream_quantity(self):
     self.driver.find_element(*self.ice_creams_input).click()

    def request_taxi(self):
        self.driver.find_element(*self.request_taxi_button).click()

    def info_driver(self):
        self.driver.find_element(*self.window_info_driver)

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()

        '''from selenium.webdriver import (DesiredCapabilities)
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)'''

    def test_1_set_route(self):
        self.driver.get(data.urban_routes_url)
        time.sleep(5)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(3)

    def test_clic_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_taxi()
    def test_2_comfort_rate(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort_rate()

    def test_3_enter_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_phone_number()
        phone_number = data.phone_number
        routes_page.put_phone_number(phone_number)
        routes_page.press_next_button()
        phone_code = retrieve_phone_code(driver=self.driver)
        routes_page.code_phone_confirm(phone_code)
        routes_page.button_confirm()
        time.sleep(4)

    def test_4_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.credit_card_field()
        routes_page.credit_add_button()
        number_card = data.card_number
        number_cvd = data.card_code
        routes_page.put_number_card(number_card)
        routes_page.put_number_cvd(number_cvd)
        routes_page.other_place()
        routes_page.add_button()
        routes_page.close_button()
        time.sleep(3)

    def test_5_send_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        text = data.message_for_driver
        routes_page.enter_message(text)

    def test_6_select_tissues(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.deploy_checkbox()
        routes_page.check_blanket()

    def test_7_select_ice(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_ice_cream_quantity()
        routes_page.enter_ice_cream_quantity()

    def test_8_confirm_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_taxi()

    def test_9_driver_info(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.info_driver()

    def test_wait_page(self):
        time.sleep(10)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
