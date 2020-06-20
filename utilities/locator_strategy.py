
class LocatorStrategy:

    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy

    @staticmethod
    def locator_by_xpath(name):
        locator_strategy = LocatorStrategy(name, 'xpath')
        return locator_strategy

    @staticmethod
    def locator_by_id(name):
        locator_strategy = LocatorStrategy(name, 'id')
        return locator_strategy

    @staticmethod
    def locator_by_css_selector(name):
        locator_strategy = LocatorStrategy(name, 'css_selector')
        return locator_strategy

    @staticmethod
    def locator_by_class_name(name):
        locator_strategy = LocatorStrategy(name, 'class_name')
        return locator_strategy

    @staticmethod
    def locator_by_name(name):
        locator_strategy = LocatorStrategy(name, 'name')
        return locator_strategy

    @staticmethod
    def locator_by_link_text(name):
        locator_strategy = LocatorStrategy(name, 'link_text')
        return locator_strategy

    @staticmethod
    def locator_by_partial_link_text(name):
        locator_strategy = LocatorStrategy(name, 'partial_link_text')
        return locator_strategy
