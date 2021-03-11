link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
import time

def test_add_to_bascket(browser):
    '''ищем по уникальному вроде бы селектору, собираем все в список и в Ассерт
    проверяем, что в списке ровно один искомый элемент'''  
    browser.get(link)
    time.sleep(30)
    button_add_to_bascket = browser.find_elements_by_css_selector('.btn\
                                  .btn-lg.btn-primary.btn-add-to-basket')                           
    assert len(button_add_to_bascket) == 1, "No button for Add to bascket"
    