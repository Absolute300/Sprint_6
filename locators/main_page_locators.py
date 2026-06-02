from selenium.webdriver.common.by import By


class MainPageLocators:
    # Заголовок страницы
    main_header = (By.XPATH, '//div[contains(@class, "Home_Header__iJKdX")]')

    # Раздел "Вопросы о важном"
    faq_section = (By.XPATH, '//div[contains(@class, "Home_FAQ")]')

    # --- ВОПРОСЫ (аккордеон) ---
    # Каждый вопрос теперь ищется по тексту, а не по ID с номером
    faq_questions_items = {
        1: (By.XPATH, '//div[contains(@id, "accordion__heading")]/parent::div[.//text()[contains(., "Сколько это стоит? И как оплатить?")]]'),
        2: (By.XPATH, '//div[contains(@id, "accordion__heading")]/parent::div[.//text()[contains(., "Хочу сразу несколько самокатов! Так можно?")]]'),
        3: (By.XPATH, '//div[contains(@id, "accordion__heading")]/parent::div[.//text()[contains(., "Как рассчитывается время аренды?")]]'),
        4: (By.XPATH, '//div[contains(@id, "accordion__heading")]/parent::div[.//text()[contains(., "Можно ли заказать самокат прямо на сегодня?")]]'),
        5: (By.XPATH, '//div[contains(@id, "accordion__heading")]/parent::div[.//text()[contains(., "Можно ли продлить заказ или вернуть самокат раньше?")]]'),
        6: (By.XPATH, '//div[contains(@id, "accordion__heading")]/parent::div[.//text()[contains(., "Вы привозите зарядку вместе с самокатом?")]]'),
        7: (By.XPATH, '//div[contains(@id, "accordion__heading")]/parent::div[.//text()[contains(., "Можно ли отменить заказ?")]]'),
        8: (By.XPATH, '//div[contains(@id, "accordion__heading")]/parent::div[.//text()[contains(., "Я жизу за МКАДом, привезёте?")]]')
    }

    # --- ОТВЕТЫ (панели) ---
    # Ответы ищем по тексту внутри, а не по номеру панели
    faq_answers_items = {
        1: (By.XPATH, '//div[contains(@id, "accordion__panel") and .//text()[contains(., "Сутки — 400 рублей. Оплата курьеру — наличными или картой.")]]'),
        2: (By.XPATH, '//div[contains(@id, "accordion__panel") and .//text()[contains(., "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.")]]'),
        3: (By.XPATH, '//div[contains(@id, "accordion__panel") and .//text()[contains(., "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.")]]'),
        4: (By.XPATH, '//div[contains(@id, "accordion__panel") and .//text()[contains(., "Только начиная с завтрашнего дня. Но скоро станем расторопнее.")]]'),
        5: (By.XPATH, '//div[contains(@id, "accordion__panel") and .//text()[contains(., "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.")]]'),
        6: (By.XPATH, '//div[contains(@id, "accordion__panel") and .//text()[contains(., "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.")]]'),
        7: (By.XPATH, '//div[contains(@id, "accordion__panel") and .//text()[contains(., "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.")]]'),
        8: (By.XPATH, '//div[contains(@id, "accordion__panel") and .//text()[contains(., "Да, обязательно. Всем самокатов! И Москве, и Московской области.")]]')
    }

    # Кнопки "Заказать"
    order_button_in_main = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button')
    order_button_in_header = (By.XPATH, '//div[@class = "Header_Nav__AGCXC"]//button[text() = "Заказать"]')

    # Логотипы
    header_logo_scooter = (By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]')
    header_logo_yandex = (By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')
    title_of_page = (By.TAG_NAME, 'title')