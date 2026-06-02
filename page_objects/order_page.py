from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from locators.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage
from data import TestData

from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):

    @allure.step('Ввод имени')
    def fill_name(self, name):
        self.wait_visibility_of_element(OrderPageLocators.input_name)
        self.click_on_element(OrderPageLocators.input_name)
        self.send_keys_to_input(OrderPageLocators.input_name, name)

    @allure.step('Ввод фамилии')
    def fill_last_name(self, last_name):
        self.click_on_element(OrderPageLocators.input_lastname)
        self.send_keys_to_input(OrderPageLocators.input_lastname, last_name)

    @allure.step('Ввод адреса')
    def fill_address(self, address):
        self.click_on_element(OrderPageLocators.input_address)
        self.send_keys_to_input(OrderPageLocators.input_address, address)

    @allure.step('Ввод телефона')
    def fill_phone(self, phone):
        self.click_on_element(OrderPageLocators.input_phone)
        self.send_keys_to_input(OrderPageLocators.input_phone, phone)

    @allure.step('Выбор станции метро из выпадающего списка')
    def select_metro_station(self):
        self.click_on_element(OrderPageLocators.select_item_in_dropdown_metro)

    @allure.step('Ввод даты доставки')
    def fill_delivery_date(self, date):
        self.wait_visibility_of_element(OrderPageLocators.input_date)
        self.click_on_element(OrderPageLocators.input_date)
        self.send_keys_to_input(OrderPageLocators.input_date, date)

    @allure.step('Выбор срока аренды')
    def select_rental_period(self):
        self.click_on_element(OrderPageLocators.field_rental_period)
        self.click_on_element(OrderPageLocators.dropdown_item_rental_period)

    @allure.step('Выбор цвета самоката: серый')
    def select_grey_scooter_color(self):
        self.click_on_element(OrderPageLocators.checkbox_grey_color_scooter)

    @allure.step('Ввод комментария к заказу')
    def fill_comment(self, comment):
        self.click_on_element(OrderPageLocators.input_comment)
        self.send_keys_to_input(OrderPageLocators.input_comment, comment)

    @allure.step('Нажатие кнопки "Далее"')
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.button_next)

    @allure.step('Нажатие кнопки "Заказать"')
    def click_order_button(self):
        self.click_on_element(OrderPageLocators.button_make_order)

    @allure.step('Подтверждение заказа кнопкой "Да"')
    def confirm_order(self):
        self.wait_visibility_of_element(OrderPageLocators.button_yes_confirm_order)
        self.click_on_element(OrderPageLocators.button_yes_confirm_order)

    @allure.step('Проверка отображения кнопки "Посмотреть статус"')
    def is_check_status_button_displayed(self):
        return self.check_displaying_of_element(OrderPageLocators.button_check_status_of_order)

    @allure.step('Заполнение первой части формы заказа')
    def data_entry_first_form(self, test_data):
        self.fill_name(test_data[0])
        self.fill_last_name(test_data[1])
        self.fill_address(test_data[2])
        self.fill_phone(test_data[4])
        self.click_on_element(OrderPageLocators.input_metro)
        self.send_keys_to_input(OrderPageLocators.input_metro, test_data[3])
        self.select_metro_station()
        self.click_next_button()

    @allure.step('Ввод даты доставки с закрытием календаря')
    def fill_delivery_date(self, date):
        self.wait_visibility_of_element(OrderPageLocators.input_date)
        self.click_on_element(OrderPageLocators.input_date)
        self.send_keys_to_input(OrderPageLocators.input_date, date)
    
        # Нажимаем Enter — это закроет календарь
        self.driver.find_element(*OrderPageLocators.input_date).send_keys(Keys.ENTER)

    @allure.step('Заполнение второй части формы заказа')
    def data_entry_second_form(self, test_data):
        # 1. Вводим дату и закрываем календарь
        self.fill_delivery_date(test_data[5])
    
        # 2. Выбираем срок аренды
        self.select_rental_period()
    
        # 3. Выбираем цвет самоката
        self.select_grey_scooter_color()
    
        # 4. Вводим комментарий
        self.fill_comment(test_data[6])
    
        # 5. Нажимаем "Заказать"
        self.click_order_button()
    
        # 6. Подтверждаем заказ
        self.confirm_order()