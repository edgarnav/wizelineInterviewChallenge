from driver_interactions.elementsInteractions import ElementsInteractions


class LoginPage(ElementsInteractions):

    def __init__(self, web_driver):
        super().__init__(web_driver)
        self.web_driver = web_driver

    page_name = "Log in Todoist"

    def validate_login_page_name(self):
        self.verify_page(self.page_name)
