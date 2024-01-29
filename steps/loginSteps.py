from behave import given, when, then
from pages.loginpage import LoginPage


class LoginSteps:

    def define_page_objects(context):
        context.login_page_object = LoginPage(context.web_driver)

    @given("Validate login page")
    def validate_page(context):
        context.login_page_object.validate_login_page_name()
