from crawler.init.init import InitSelenium

class CommonUtilities(InitSelenium):
    def execute_script(self, link_user: str):
        print("CommonUtilities class")
        pass

    def check_block(self):
        return "Temporarily Blocked" in self.driver.page_source

    def check_height(self):
        new_height = self.driver.execute_script("return document.body.scrollHeight")
        return new_height != self.old_height

    def scroll(self):
        self.current_scrolls = 0

        while (True):
            try:
                if self.current_scrolls == self.total_scrolls:
                    return

                self.old_height = self.driver.execute_script("return document.body.scrollHeight")
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                WebDriverWait(self.driver, self.scroll_time, 0.05).until(lambda driver: self.check_height())
                self.current_scrolls += 1
            except TimeoutException:
                break

        return
  

if __name__ == "__main__":
    test = CommonUtilities("test", "test")
    test.execute_script()
    test.quit()