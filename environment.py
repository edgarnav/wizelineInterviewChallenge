from driver_interactions.initWebDriver import InitWebDriver
from driver_interactions.elementsInteractions import ElementsInteractions
import configurations.configurationsFile as Configurations


def before_all(context):
    context.init_web_driver = InitWebDriver.init_web_driver()
    context.elements_interactions = ElementsInteractions(context.init_web_driver)
    context.elements_interactions.open_web_page(Configurations.url)
