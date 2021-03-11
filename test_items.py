link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
import time

def test_add_to_bascket(browser):
    '''ищем по уникальному вроде бы селектору, собираем все в список и в Ассерт
    проверяем, что в списке ровно один искомый элемент'''  
    browser.get(link)
    # 15 секунд вполне достаточно вроде, но оставим 30...
    time.sleep(10)
    # селектор .btn-add-to-basket уникальный, я проверил
    button_add_to_bascket = browser.find_elements_by_css_selector('.btn-add-to-basket')                           
    assert len(button_add_to_bascket) == 1, "No button for Add to bascket"
