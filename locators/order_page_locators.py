from selenium.webdriver.common.by import By


class MainPageLocators:
    # Заголовок страницы
    main_header = (By.XPATH, '//div[contains(@class, "Home_Header__iJKdX")]')

    # Раздел "Вопросы о важном"
    faq_section = (By.XPATH, '//div[contains(@class, "Home_FAQ")]')

    # --- ВОПРОСЫ (аккордеон) ---
    # Каждый вопрос теперь ищется по тексту, а не по ID с номером
    faq_questions_items = {
        1: (By.XPATH, '//div[contains(@id, "accordion__heading")]/parent::div[.//text()[contains(., "Сколько это стоит? Как оплатить?")]]'),
        2: (By.XPATH, '//div[contains(@id, "accordion__heading")]/parent::div[.//text()[contains(., "Хочу сразу несколько самокатов Так можно?")]]'),
        3: (By.XPATH, '//div[contains(@id, "accordion__heading")]/parent::div[.//text()[contains(., "Как рассчитывается время аренды?")]]'),
        4: (By.XPATH, '//div[contains(@id, "accordion__heading")]/parent::div[.//text()[contains(., "Можно ли продлить аренду или вернуть самокат раньше?")]]'),
        5: (By.XPATH, '//div[contains(@id, "accordion__heading")]/parent::div[.//text()[contains(., "Вы привозите зарядку вместе с самокатом?")]]'),
        6: (By.XPATH, '//div[contains(@id, "accordion__heading")]/parent::div[.//text()[contains(., "Можно ли купить такой же самокат?")]]'),
        7: (By.XPATH, '//div[contains(@id, "accordion__heading")]/parent::div[.//text()[contains(., "Что входит в комплектации самоката?")]]'),
        8: (By.XPATH, '//div[contains(@id, "accordion__heading")]/parent::div[.//text()[contains(., "Сколько времени длится зарядка?")]]')
    }

    # --- ОТВЕТЫ (панели) ---
    # Ответы ищем по тексту внутри, а не по номеру панели
    faq_answers_items = {
        1: (By.XPATH, '//div[contains(@id, "accordion__panel") and .//text()[contains(., "Два варианта. Первый — доставка сразу на дом")]]'),
        2: (By.XPATH, '//div[contains(@id, "accordion__panel") and .//text()[contains(., "Пока что у нас так: один заказ — один самокат")]]'),
        3: (By.XPATH, '//div[contains(@id, "accordion__panel") and .//text()[contains(., "Расчёт минут идёт с момента подтверждения заказа")]]'),
        4: (By.XPATH, '//div[contains(@id, "accordion__panel") and .//text()[contains(., "Да, всегда можно изменить заказ")]]'),
        5: (By.XPATH, '//div[contains(@id, "accordion__panel") and .//text()[contains(., "Самокат приезжает к вам заряженным")]]'),
        6: (By.XPATH, '//div[contains(@id, "accordion__panel") and .//text()[contains(., "Да, самокат можно купить на сайте")]]'),
        7: (By.XPATH, '//div[contains(@id, "accordion__panel") and .//text()[contains(., "Самокат, зарядное устройство и инструкция")]]'),
        8: (By.XPATH, '//div[contains(@id, "accordion__panel") and .//text()[contains(., "Зарядка самоката занимает 4 часа")]]')
    }

    # Кнопки "Заказать"
    order_button_in_main = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button')
    order_button_in_header = (By.XPATH, '//div[@class = "Header_Nav__AGCXC"]//button[text() = "Заказать"]')

    # Логотипы
    header_logo_scooter = (By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]')
    header_logo_yandex = (By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')
    title_of_page = (By.TAG_NAME, 'title')