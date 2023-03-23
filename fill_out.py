import random
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


class InputBoxHandler:
    def __init__(self, driver):
        self.driver = driver

    def handle_input_boxes_by_tag_name(self, tag_name):
        # Find all input boxes on the webpage by tag name
        input_boxes = self.driver.find_elements(By.TAG_NAME, tag_name)




        # Loop through each input box and fill out its value or select it if it's a checkbox
        for input_box in input_boxes:
            # time.sleep(.2)
            if input_box.get_attribute("type") == "text" or input_box.get_attribute("type") == "tel":
                # Scroll to the input box if it's not in view
                actions = ActionChains(self.driver)
                actions.move_to_element(input_box).perform()

                # Click on the input box to focus it
                input_box.click()

                # Generate a random string of length 8 with at least one number
                random_chars =  string.digits
                random_string = ''.join(random.choice(random_chars)
                                        for _ in range(7))
                random_string += random.choice(string.digits)

                input_box.send_keys(random_string)

            elif input_box.get_attribute("type") == "checkbox":
                #return a random boolean
                random_boolean = random.choice([True, False, False, False])

                parent_element = input_box.find_element(By.XPATH, "..")
                parent_of_parent_element = parent_element.find_element(By.XPATH, "..")
                parent_of_parent_of_parent_element = parent_of_parent_element.find_element(By.XPATH, "..")

                #now get the p tag in the parent of the parent element
                p_tag = parent_of_parent_of_parent_element.find_element(By.TAG_NAME, "p").text




                if   p_tag.lower() == "yes" or random_boolean and p_tag.lower() != "no" or p_tag.lower() == "insurance" or p_tag.lower() == "normal":
                    # Scroll to the checkbox if it's not in view
                    actions = ActionChains(self.driver)
                    actions.move_to_element(input_box).perform()

                    # Click on the checkbox to select it

                    input_box.click()

    def find_new_inputs_and_fill(self, tag_name):
        # now grab all the text boxes again to compensate for the new ones that have been added
        # Find all input boxes on the webpage by tag name
        # Fill in only the ones that are not already filled in
        input_boxes = self.driver.find_elements(By.TAG_NAME, tag_name)
        for input_box in input_boxes:
            if input_box.get_attribute("value") == "" or input_box.get_attribute("value") == None or input_box.get_attribute("value") == " ":
                # Scroll to the input box if it's not in view
                actions = ActionChains(self.driver)
                actions.move_to_element(input_box).perform()

                # Click on the input box to focus it
                input_box.click()

                # Generate a random string of length 8 with at least one number
                random_chars = string.ascii_lowercase + string.digits
                random_string = ''.join(random.choice(random_chars)
                                        for _ in range(7))
                random_string += random.choice(string.digits)

                input_box.send_keys(random_string)

                #try to add item to list if button is present



            elif input_box.get_attribute("type") == "checkbox" and input_box.get_attribute("checked") == None:
                print(input_box.get_attribute("checked"))
                #return a random boolean
                random_boolean = random.choice([True, False, False, False])
                parent_element = input_box.find_element(By.XPATH, "..")
                parent_of_parent_element = parent_element.find_element(By.XPATH, "..")
                parent_of_parent_of_parent_element = parent_of_parent_element.find_element(By.XPATH, "..")

                #now get the p tag in the parent of the parent element
                p_tag = parent_of_parent_of_parent_element.find_element(By.TAG_NAME, "p").text
                if p_tag.lower() == "yes" or random_boolean and p_tag.lower() != "no" or p_tag.lower() == "insurance" or p_tag.lower() == "normal":
                    # Scroll to the checkbox if it's not in view
                    actions = ActionChains(self.driver)
                    actions.move_to_element(input_box).perform()

                    # Click on the checkbox to select it
                    input_box.click()





    def sign_in_to_account(self, email, password):
        time.sleep(2)
        # click email input to log in
        email_input = self.driver.find_element(
            By.CSS_SELECTOR, "#email > input")
        # fill in keys for email and password'
        email_input.send_keys(email)
        password_input = self.driver.find_element(
            By.CSS_SELECTOR, "#password > input")
        password_input.send_keys(password)
        # click on the button to log in
        login_button = self.driver.find_element(
            By.CSS_SELECTOR, "#__next > div > div > div:nth-child(7) > button")
        login_button.click()
        time.sleep(2)

    def create_an_account(self, email, password):
        time.sleep(2)
        # click on the button to create an account
        create_account_button = self.driver.find_element(
            By.CSS_SELECTOR, "#__next > div > div > p:nth-child(6)").click()

        time.sleep(2)
        # click email input to log in
        email_input = self.driver.find_element(
            By.CSS_SELECTOR, "#email > input")
        # fill in keys for email and password'
        email_input.send_keys(email)
        password_input = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div/div[2]/input")
        password_input.send_keys(password)
        confirm_password_input = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div/div[3]/input")
        confirm_password_input.send_keys(password)
        # click on the button to create an account
        create_account_button = self.driver.find_element(
            By.CSS_SELECTOR, "#__next > div > div > div:nth-child(6) > button")
        create_account_button.click()

    def start_NPP(self):
        time.sleep(3)
        fill_out_button = self.driver.find_element(
            By.CSS_SELECTOR, "#__next > div > div > div.flex.flex-col.items-center.justify-center > button")
        fill_out_button.click()
        time.sleep(4)

    def create_email(self):
        # create a random email
        random_chars = string.ascii_lowercase + string.digits
        random_string = ''.join(random.choice(random_chars)
                                for _ in range(7))
        random_string += random.choice(string.digits)
        email = 'zzz' +random_string + "@gmail.com"
        #create a file to store the email
        file = open("accounts.txt", "a")
        file.write("\n" + 'email:'+ email + "\n" + 'password: 123456' + "\n" + "\n")

        return email

    def submit_packet(self):
        #scroll to buttons and click
        actions = ActionChains(self.driver)
        button1 = self.driver.find_element(By.CSS_SELECTOR, "#__next > div > main > section:nth-child(21) > div > div > div.bg-\[\#c3969600\].undefined.undefined.my-20.flex.w-full.flex-col.items-center.justify-center.text-center > button")

        actions.move_to_element(button1).perform()
        button1.click()

        button2 = self.driver.find_element(By.CSS_SELECTOR, "#__next > div > main > div:nth-child(25) > button")

        actions.move_to_element(button2).perform()
        button2.click()

        button3 = self.driver.find_element(By.CSS_SELECTOR, "#__next > div > main > div:nth-child(27) > button")

        actions.move_to_element(button3).perform()
        button3.click()



        button4 = self.driver.find_element(By.CSS_SELECTOR, "#__next > div > main > section:nth-child(34) > div > div > div.bg-\[\#c3969600\].undefined.undefined.my-20.flex.w-full.flex-col.items-center.justify-center.text-center > button")

        actions.move_to_element(button4).perform()
        button4.click()

        checkBox1 = self.driver.find_element(By.CSS_SELECTOR, "#patientMedicalReviewSignature > div.undefined.undefined.undefined.my-\[1px\].flex.grid-cols-2.flex-row > div:nth-child(1) > div > input")
        actions.move_to_element(checkBox1).perform()
        checkBox1.click()

        checkBox2 = self.driver.find_element(By.CSS_SELECTOR, "#advancedDirectivesLivingWill > div.undefined.undefined.undefined.my-\[1px\].flex.grid-cols-2.flex-row > div:nth-child(1) > div > input")
        actions.move_to_element(checkBox2).perform()
        checkBox2.click()

        checkBox3 = self.driver.find_element(By.CSS_SELECTOR, "#hippa > div.undefined.undefined.undefined.my-\[1px\].flex.grid-cols-2.flex-row > div:nth-child(1) > div > input")
        actions.move_to_element(checkBox3).perform()
        checkBox3.click()

        checkBox4 = self.driver.find_element(By.CSS_SELECTOR, "#financialPolicy > div > div.undefined.undefined.undefined.my-\[1px\].flex.grid-cols-2.flex-row > div:nth-child(1) > div > input")
        actions.move_to_element(checkBox4).perform()
        checkBox4.click()




        time.sleep(2)
        submit_button = self.driver.find_element(
            By.CSS_SELECTOR, "#__next > div > main > div.mt-10.flex.flex-col.items-center.justify-center > button")
        submit_button.click()






if __name__ == "__main__":
    print(InputBoxHandler.create_email(self=None))
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/PatientPage")
    # input("Press Enter to continue...")
    time.sleep(2)
    fill_out_packet = InputBoxHandler(driver)
    fill_out_packet.create_an_account(
       email=fill_out_packet.create_email(), password="123456")
    fill_out_packet.start_NPP(

    )

    fill_out_packet.handle_input_boxes_by_tag_name("input")
    input("Press Enter to continue...")


