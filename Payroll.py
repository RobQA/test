from Utils import Utils
from selenium.webdriver.support.wait import WebDriverWait
import random
import time


co_tt_bl = []
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'modeOfPayment': 'БН', 'bankBranch': '00000',
                 'tin': '17031994', 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append(
    {'co': '05100011', 'taxType': '1010', 'bl': '900013555017', 'modeOfPayment': 'БЗ', 'bankBranch': '90000',
     'tin': '77778888', 'docNumber': '0099999999999999999999999', 'pay': '9999999999999', 'notes': 'fdf2534'})
co_tt_bl.append(
    {'co': '05100011', 'taxType': '1010', 'bl': '900013555017', 'modeOfPayment': 'ПК', 'bankBranch': '19300',
     'tin': '86915977', 'docNumber': '2345', 'pay': '9999999999999', 'notes': 'fdf2534'})
co_tt_bl.append(
    {'co': '05100013', 'taxType': '1011', 'bl': '900013523015', 'modeOfPayment': 'БЗ', 'bankBranch': '25000',
     'tin': '02228898', 'docNumber': '2345fgsdfgdfg2hghghgfsdffgdg45', 'pay': '99999999999999999',
     'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append(
    {'co': '05100015', 'taxType': '1020', 'bl': '900013324018', 'modeOfPayment': 'БН', 'bankBranch': '24100',
     'tin': '00008037', 'docNumber': '2345fgsdfgdfg2hghghgfsdffgdg45', 'pay': '4563456',
     'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append(
    {'co': '05100016', 'taxType': '1050', 'bl': '900013323010', 'modeOfPayment': 'БЗ', 'bankBranch': '23500',
     'tin': '00092757', 'docNumber': '888888888', 'pay': '4563456', 'notes': 'fdf234'})
co_tt_bl.append(
    {'co': '05100017', 'taxType': '1090', 'bl': '900013576013', 'modeOfPayment': 'ПК', 'bankBranch': '22000',
     'tin': '003646445', 'docNumber': '0099999999999999999999999', 'pay': '4563456', 'notes': 'fdf234'})
co_tt_bl.append(
    {'co': '05100018', 'taxType': '1510', 'bl': '900013555017', 'modeOfPayment': 'БЗ', 'bankBranch': '21400',
     'tin': '00001182', 'docNumber': '8888888888', 'pay': '23465785', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100020', 'taxType': '20', 'bl': '900005014015', 'modeOfPayment': 'БН', 'bankBranch': '20500',
                 'tin': '00471885', 'docNumber': '1234215', 'pay': '99999999999999999',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append(
    {'co': '05100021', 'taxType': '2010', 'bl': '900005000618', 'modeOfPayment': 'БЗ', 'bankBranch': '10300',
     'tin': '84168159', 'docNumber': '1234215', 'pay': '456366666456', 'notes': 'fdf234'})
co_tt_bl.append(
    {'co': '05100022', 'taxType': '2011', 'bl': '900005015012', 'modeOfPayment': 'ПК', 'bankBranch': '25300',
     'tin': '25293353', 'docNumber': '2345fgsdfgdfg2hghghgfsdffgdg45', 'pay': '99999999999999999',
     'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append(
    {'co': '05100030', 'taxType': '2040', 'bl': '900005061370', 'modeOfPayment': 'БЗ', 'bankBranch': '24700',
     'tin': '02664656', 'docNumber': '1234215', 'pay': '412346456', 'notes': 'fdf234'})
co_tt_bl.append(
    {'co': '05100031', 'taxType': '2041', 'bl': '900005061370', 'modeOfPayment': 'НР', 'bankBranch': '23800',
     'tin': '47813265', 'docNumber': '1234215', 'pay': '99999999999999999',
     'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append(
    {'co': '05100032', 'taxType': '2051', 'bl': '900005061370', 'modeOfPayment': 'БЗ', 'bankBranch': '22300',
     'tin': '00891529', 'docNumber': '8888888888', 'pay': '4563456',
     'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100033', 'taxType': '30', 'bl': '900005168415', 'modeOfPayment': 'БН', 'bankBranch': '21700',
                 'tin': '05544509', 'docNumber': '1234215', 'pay': '45635665345456', 'notes': 'fdf234'})
co_tt_bl.append(
    {'co': '05100034', 'taxType': '4510', 'bl': '900005004230', 'modeOfPayment': 'БЗ', 'bankBranch': '20800',
     'tin': '87613918', 'docNumber': '0099999999999999999999999', 'pay': '4563456', 'notes': 'fdf234'})
co_tt_bl.append(
    {'co': '05100035', 'taxType': '4511', 'bl': '900005004230', 'modeOfPayment': 'НР', 'bankBranch': '18100',
     'tin': '70985319', 'docNumber': '1234215', 'pay': '99999999999999999', 'notes': 'fdf234'})
co_tt_bl.append(
    {'co': '05100036', 'taxType': '4520', 'bl': '900005004271', 'modeOfPayment': 'БЗ', 'bankBranch': '17500',
     'tin': '37464898', 'docNumber': '888888888888', 'pay': '99999999999999999', 'notes': 'fdf234'})
co_tt_bl.append(
    {'co': '05100036', 'taxType': '4520', 'bl': '900005004248', 'modeOfPayment': 'БН', 'bankBranch': '16600',
     'tin': '27949116', 'docNumber': '2345fgsdfgdfg2hghghgfsdffgdg45', 'pay': '99999999999999999',
     'notes': 'fdfgfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh234'})
co_tt_bl.append({'co': '05100040', 'taxType': 'VCT', 'bl': '900005024055', 'modeOfPayment': 'БЗ', 'bankBranch': '16300',
                 'tin': '06922436', 'docNumber': '66666666666', 'pay': '345634699788', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100041', 'taxType': 'MVT', 'bl': '900293063013', 'modeOfPayment': 'НР', 'bankBranch': '16000',
                 'tin': '06605211', 'docNumber': '0099999999999999999999999', 'pay': '56745674567',
                 'notes': 'fdgfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghf234'})
co_tt_bl.append({'co': '05100041', 'taxType': 'MTT', 'bl': '900005014015', 'modeOfPayment': 'БЗ', 'bankBranch': '15700',
                 'tin': '05020569', 'docNumber': '2345fgsdfgdfg2hghghgfsdffgdg45', 'pay': '2345234537347',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100041', 'taxType': 'MCV', 'bl': '900293063013', 'modeOfPayment': 'ПК', 'bankBranch': '11800',
                 'tin': '01801161', 'docNumber': '1234215', 'pay': '4563456', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100041', 'taxType': 'HVT', 'bl': '900005012134', 'modeOfPayment': 'БЗ', 'bankBranch': '11500',
                 'tin': '01234557', 'docNumber': '2345fgsdfgdfg2hghghgfsdffgdg45', 'pay': '8888888888',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})


class Payroll:

    @staticmethod
    def x(obj):
        return {
            'customsOfficeCode': obj['co'],
            'payeeId': obj['tin'],
            'taxCode': obj['taxType'],
            'budgetAccount': obj['bl'],
            'modeOfPayment': obj['modeOfPayment'],
            'bankBranch': obj['bankBranch'],
            'bankAccount': '26745674546',
            'amount': obj['pay'],
            'notes': obj['notes'],
            #'operationCreate': None,
            #'confirmOper': None
        }

    @staticmethod
    def create_payroll():
        driver = Utils.driver
        driver.get("https://uatapp3.fipsoft.com/cap/payment/create?lang=ru")
        Utils.check_select('iff', 0)
        rInt = random.randint(0, len(co_tt_bl) - 1)
        Utils.fill_form(Payroll.x(co_tt_bl[rInt]))
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationCreate').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()

        ###############################################################################################################

    updatePayrollFormData = {
        'modeOfPayment': 'БЗ',
        'bankBranch': '123123123123',
        'bankAccount': '41234',
        'amount': '1',
        'notes': '12341',
        #'operationUpdate': None,
        #'confirmOper': None
    }

    @staticmethod
    def update_payroll():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.driver.find_element_by_id('clearCriteria').click()
        element = driver.find_element_by_css_selector("#paymentsTable .dropdown-toggle")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector("#paymentsTable .operationUpdateClass")
        driver.execute_script("arguments[0].click();", element)
        Utils.driver.find_element_by_id('modeOfPayment').clear()
        Utils.driver.find_element_by_id('bankBranch').clear()
        Utils.driver.find_element_by_id('bankAccount').clear()
        Utils.driver.find_element_by_id('amount').clear()
        Utils.driver.find_element_by_id('notes').clear()
        Utils.fill_form(Payroll.updatePayrollFormData)
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationUpdate').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()

        ###############################################################################################################

    cancelPayrollFormData = {
        #'confirmOper': None
    }

    @staticmethod
    def cancel_payroll():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.driver.find_element_by_id('clearCriteria').click()
        element = driver.find_element_by_css_selector("#paymentsTable .dropdown-toggle")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector("#paymentsTable .operationCancelCreatedClass")
        driver.execute_script("arguments[0].click();", element)
        Utils.fill_form(Payroll.cancelPayrollFormData)
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()

        ###############################################################################################################

    confirmPayrollFormData = {
        'confirmationNumber': '12341234',
        'notes': '12312',
        #'operationConfirm': None,
        #'confirmOper': None
    }

    @staticmethod
    def confirm_pay():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.driver.find_element_by_id('clearCriteria').click()
        element = driver.find_element_by_css_selector("#paymentsTable .dropdown-toggle")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('operationConfirmClass').click()
        Utils.fill_form(Payroll.confirmPayrollFormData)
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationConfirm').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()

        ###############################################################################################################

    payPayrollFormData = {
        'paidAmount': '99999999999999999',
        'paymentDocumentNumber': '1432',
        'notes': '131234',
        #'operationPay': None,
        #'confirmOper': None
    }

    @staticmethod
    def pay_payroll():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.driver.find_element_by_id('clearCriteria').click()
        element = driver.find_element_by_css_selector("#paymentsTable .dropdown-toggle")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('operationPayClass').click()
        Utils.fill_form(Payroll.payPayrollFormData)
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationPay').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()

        ###############################################################################################################

    @staticmethod
    def print_payroll():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.driver.find_element_by_id('clearCriteria').click()
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-print")
        driver.execute_script("arguments[0].click();", element)

        ###############################################################################################################

    @staticmethod
    def history_payroll_print():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-time")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector("#paymentsTable .operationLink")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('btn').click()

        ###############################################################################################################

    payrollCreateBarFormData = {
        'customsOfficeCode': '05100010',
        'payeeId': '17031994',
        'taxCode': '10',
        'budgetAccount': '900013323010',
        'modeOfPayment': 'БЗ',
        'bankBranch': '34523452345',
        'bankAccount': '26745674546',
        'amount': '534523452',
        'notes': '17031994',
        #'operationCreate': None,
        #'confirmOper': None
    }

    @staticmethod
    def payroll_create_bar():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.driver.find_element_by_id('clearCriteria').click()
        driver.find_element_by_class_name('createPayment').click()
        Utils.check_select('iff', 0)
        rInt = random.randint(0, len(co_tt_bl) - 1)
        Utils.fill_form(Payroll.x(co_tt_bl[rInt]))
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationCreate').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()

        ###############################################################################################################

    view00000PayrollPrintFormData = {
        'showHideCriteria': None,
        'bankAccount': '000000000000',
        'searchPayments': None,
    }

    @staticmethod
    def view_00000_payroll_print():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.fill_form(Payroll.view00000PayrollPrintFormData)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-eye-open")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('btn').click()

        ###############################################################################################################

    @staticmethod
    def aria_controls_py():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.check_select('paymentsTable_length', 3)
        WebDriverWait(Utils.driver, 5).until(
            Utils.wait_for_ajax_complete, "Timeout waiting for page to load")
        Utils.check_select('paymentsTable_length', 2)
        WebDriverWait(Utils.driver, 5).until(
            Utils.wait_for_ajax_complete, "Timeout waiting for page to load")
        Utils.check_select('paymentsTable_length', 1)
        WebDriverWait(Utils.driver, 5).until(
            Utils.wait_for_ajax_complete, "Timeout waiting for page to load")
        Utils.check_select('paymentsTable_length', 0)

        ###############################################################################################################

    payrollPrintViewActualPaymentViewReallocationsFormData = {
        'bankBranch': '00000',
        'bankAccount': '000000000000',
        'searchPayments': None

    }

    @staticmethod
    def payroll_print_view_actual_payment_view_reallocations():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-eye-open")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_partial_link_text('Распечатать').click()
        #driver.find_element_by_partial_link_text('Просмотр фактической оплаты').click()
        driver.find_element_by_partial_link_text('Просмотр зачетов').click()
        driver.find_element_by_partial_link_text('Распечатать').click()



