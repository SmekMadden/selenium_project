from pages.product_page import ProductPage
import pytest
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from faker import Faker

# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

# urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
# @pytest.mark.parametrize('link', urls)
@pytest.mark.skip
def test_add_product_to_the_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_cart_link()
    page.cart_click()
    page.solve_quiz_and_get_code()
    page.product_name_in_success_message_is_correct()
    page.cart_total_price_equals_product_price()
    page.success_message_should_disappear()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.cart_click()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.cart_click()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_the_basket()
    basket_page.should_be_basket_empty_message()


@pytest.mark.user_add
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, browser.current_url)
        f = Faker()
        email, password = f.email(), f.password()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    # @pytest.mark.parametrize('link', urls)
    # @pytest.mark.skip
    def test_user_can_add_product_to_the_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_cart_link()
        page.cart_click()
        page.solve_quiz_and_get_code()
        page.product_name_in_success_message_is_correct()
        page.cart_total_price_equals_product_price()
        # page.success_message_should_disappear()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
