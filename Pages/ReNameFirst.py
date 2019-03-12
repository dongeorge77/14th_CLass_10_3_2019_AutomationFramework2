class RenameUser:
    def __init__(self,driver):
        self.driver=driver
        self.search_box="//input[@class='filterFieldInput inputFieldWithPlaceholder']"
        #self.clk_user="//*[text()='name, unknown']"
        self.clk_result_xpath="//*[@class='highlightToken']"
        self.first_name_edt="//*[@id='userDataLightBox_firstNameField']"
        self.save_changes="//*[@class='buttonTitle']"

    def user_box(self):
        self.driver.find_element_by_xpath(self.search_box).send_keys("unknown")

    # def clk_user_name(self):
    #     self.driver.find_element_by_xpath(self.clk_user).click()

    def clk_result(self):
        self.driver.find_element_by_xpath(self.clk_result_xpath).click()

    def change_name(self):
        self.driver.find_element_by_xpath(self.first_name_edt).send_keys("test")

    def update_btn(self):
        self.driver.find_element_by_xpath(self.save_changes).click()