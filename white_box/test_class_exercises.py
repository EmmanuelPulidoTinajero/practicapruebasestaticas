# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import divide, get_grade, is_even, is_triangle, check_number_status, validate_password, calculate_total_discount, calculate_order_total, calculate_items_shipping_cost, validate_login, verify_age, categorize_product, validate_email, validate_credit_card, validate_date, check_flight_eligibility, validate_url, calculate_quantity_discount, check_file_size, check_loan_eligibility, calculate_shipping_cost, grade_quiz, authenticate_user, get_weather_advisory


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")

    def test_check_number_status_is_positive(self):
        self.assertEqual(check_number_status(5), "Positive")

    def check_number_status_is_negative(self):
        self.assertEqual(check_number_status(-3), "Negative")

    def  check_number_status_is_zero(self):
        self.assertEqual(check_number_status(0), "Zero")

    def validate_password_Check_length(self):
        self.assertFalse(validate_password('1abc*'))

    def validate_password__Check_for_at_least_one_uppercase_letter_one_lowercase_letter(self):
        self.assertFalse(validate_password('abcdefghh'))

    def validate_password_ok(self):
        self.assertTrue(validate_password('AbDcdef23*+@'))

    def calculate_total_discount_les_100(self):
        self.assertEqual(calculate_total_discount(99), 0)

    def calculate_total_discount_les_or_equal_500(self):
        self.assertEqual(calculate_total_discount(500), "0.1 * total_amount") 

    def calculate_total_discount_more_500(self):
        self.assertEqual(calculate_total_discount(501), "0.2 * total_amount")

    def  calculate_order_total_lesOrEqual_5(self):
        self.assertEqual(calculate_order_total([{"quantity": 5, "price": 100}]), 500)

    def calculate_order_total_6_10(self):
        self.assertEqual(calculate_order_total([{"quantity": 6, "price": 100}]), 570.0)

    def calculate_order_total_more_10(self):
        self.assertEqual(calculate_order_total([{"quantity": 12, "price": 100}]), 1080.0)

    def calculate_items_shipping_cost_1(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 3}, {"weight": 2}], "standard"), 10)

    def calculate_items_shipping_cost_2(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 7}], "standard"), 15)

    def calculate_items_shipping_cost_3(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 12}], "standard"), 20)

    def calculate_items_shipping_cost_4(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 5}], "express"), 20)

    def calculate_items_shipping_cost_5(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 6}, {"weight": 4}], "express"), 30)

    def calculate_items_shipping_cost_6(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 11}], "express"), 40)

    def validate_login_1(self):
        self.assertEqual(validate_login('emmanuel', 'emmanuel'), "Login Successful")

    def validate_login_2(self):
        self.assertEqual(validate_login('em', 'emmanuel'), "Login Failed")

    def validate_login_3(self):
        self.assertEqual(validate_login('emanuel', 'em'), "Login Failed")

    def verify_age_1(self):
        self.assertEqual(verify_age(25), "Eligible")

    def verify_age_2(self):
        self.assertEqual(verify_age(14), "Not Eligible")

    def categorize_product_1(self):
        self.assertEqual(categorize_product(35), "Category A")

    def categorize_product_2(self):
        self.assertEqual(categorize_product(75), "Category B")

    def categorize_product_3(self):
        self.assertEqual(categorize_product(150), "Category C")

    def categorize_product_4(self):
        self.assertEqual(categorize_product(550), "Category D")

    def validate_email_1(self):
        self.assertEqual(validate_email("jepulidotinajero@gmail.com"),  "Valid Email")

    def validate_email_2(self):
        self.assertEqual(validate_email("jepulidotinajerogmail.com"),  "Invalid Email")

    def validate_email_3(self):
        self.assertEqual(validate_email("jepu"),  "Invalid Email")

    def validate_credit_card_1(self):
        self.assertEqual(validate_credit_card(1234567890123), "Valid Card")


    def validate_credit_card_2(self):
        self.assertEqual(validate_credit_card(1222234567890123), "Valid Card")

    def validate_credit_card_3(self):
        self.assertEqual(validate_credit_card(1267890123), "Invalid Card")

    def validate_credit_card_4(self):
        self.assertEqual(validate_credit_card("abcd"), "Invalid Card")

    def validate_date_1(self):
        self.assertEqual(validate_date(1980, 9, 26), "Valid Date")

    def validate_date_2(self):
        self.assertEqual(validate_date(1880, 9, 26), "Invalid Date")

    def validate_date_3(self):
        self.assertEqual(validate_date(1980, 16, 26), "Invalid Date")

    def validate_date_4(self):
        self.assertEqual(validate_date(1980, 9, 58), "Invalid Date")

    def check_flight_eligibility_1(self):
        self.assertEqual(check_flight_eligibility(23), "Eligible to Book")

    def check_flight_eligibility_2(self):
        self.assertEqual(check_flight_eligibility(65, "frequent_flyer"), "Eligible to Book")

    def check_flight_eligibility_3(self):
        self.assertEqual(check_flight_eligibility(24, "frequent_flyer"), "Eligible to Book")

    def check_flight_eligibility_4(self):
        self.assertEqual(check_flight_eligibility(65), "Not Eligible to Book")

    def validate_url_1(self):
        self.assertEqual(validate_url("https://incluton.com/inicio"), "Valid URL")

    def validate_url_2(self):
        self.assertEqual(validate_url("http://incluton.com/inicio"), "Valid URL")

    def validate_url_3(self):
        self.assertEqual(validate_url("incluton.com/inicio"), "Invalid URL")

    def validate_url_4(self):
        self.assertEqual(validate_url("https://jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjincluton.com/inicio"), "Invalid URL")

    def calculate_quantity_discount_1(self):
        self.assertEqual(self.calculate_quantity_discount(5), "No Discount")
    def calculate_quantity_discount_2(self):
        self.assertEqual(self.calculate_quantity_discount(6), "5% Discount")
    def calculate_quantity_discount_3(self):
        self.assertEqual(self.calculate_quantity_discount(10), "5% Discount")
    def calculate_quantity_discount_4(self):
        self.assertEqual(calculate_quantity_discount(20), "10% Discount")

    def check_file_size_1(self):
        self.assertEqual(check_file_size(128), "Valid File Size")

    def check_file_size_2(self):
        self.assertEqual(check_file_size(-10), "Invalid File Size")

    def check_file_size_3(self):
        self.assertEqual(check_file_size(1048593), "Invalid File Size")

    def check_loan_eligibility_1(self):
        self.assertEqual(check_loan_eligibility(20000), "Not Eligible")



    def check_loan_eligibility_2(self):
        self.assertEqual(check_loan_eligibility(20000), "Not Eligible")

    def check_loan_eligibility_3(self):
        self.assertEqual(check_loan_eligibility(35000), "Secured Loan")

    def check_loan_eligibility_4(self):
        self.assertEqual(check_loan_eligibility(35000, 750), "Standard Loan")

    def check_loan_eligibility_5(self):
        self.assertEqual(check_loan_eligibility(35000, 755), "Premium Loan")


    def calculate_shipping_cost_1(self):
        self.assertEqual(calculate_shipping_cost(1, 9, 9, 9), 5)

    def calculate_shipping_cost_2(self):
        self.assertEqual(calculate_shipping_cost(5, 29, 29, 29), 10)

    def calculate_shipping_cost_2(self):
        self.assertEqual(calculate_shipping_cost(10, 29, 29, 50), 20)

    def grade_quiz_1(self):
        self.assertEqual(grade_quiz(7, 2), "Pass")

    def grade_quiz_2(self):
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def grade_quiz_3(self):
        self.assertEqual(grade_quiz(3, 3), "Fail")

    def authenticate_user_1(self):
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def authenticate_user_2(self):
        self.assertEqual(authenticate_user("emmanu", "emmanuel123"), "User")

    def authenticate_user_3(self):
        self.assertEqual(authenticate_user("emm", "emmanuel123"), "Invalid")

    def authenticate_user_4(self):
        self.assertEqual(authenticate_user("emmanuel", "adbs"), "Invalid")


    def  get_weather_advisory_1(self):
        self.assertEqual(get_weather_advisory(31, 60), "High Temperature and Humidity. Stay Hydrated")

    def  get_weather_advisory_2(self):
        self.assertEqual(get_weather_advisory(-20, 60), "Low Temperature. Bundle Up")

    def  get_weather_advisory_3(self):
        self.assertEqual(get_weather_advisory(90,  10000), "No Specific Advisory")