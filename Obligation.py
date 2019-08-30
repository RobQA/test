from Utils import Utils
from selenium.webdriver.support.wait import WebDriverWait
import random
import time
import urllib.request



co_tt_bl = []
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '17031994', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100011', 'taxType': '1010', 'bl': '900013555017', 'tin': '77778888', 'documentType': '082',
                 'docNumber': '00999999999999999', 'pay': '9999999999999', 'notes': 'fdf2534'})
co_tt_bl.append({'co': '05100011', 'taxType': '1010', 'bl': '900013555017', 'tin': '86915977', 'documentType': '082',
                 'docNumber': '2345', 'pay': '9999999999999', 'notes': 'fdf2534'})
co_tt_bl.append({'co': '05100013', 'taxType': '1011', 'bl': '900013523015', 'tin': '02228898', 'documentType': '088',
                 'docNumber': '2345fgsdfgdffgdg45', 'pay': '99999999999999999',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100015', 'taxType': '1020', 'bl': '900013324018', 'tin': '00008037', 'documentType': '089',
                 'docNumber': '2345fgsdfgdffgdg45', 'pay': '4563456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100016', 'taxType': '1050', 'bl': '900013323010', 'tin': '00092757', 'documentType': '089',
                 'docNumber': '888888888', 'pay': '4563456', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100018', 'taxType': '1510', 'bl': '900013555017', 'tin': '00001182', 'documentType': '081',
                'docNumber': '8888888888', 'pay': '23465785', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100020', 'taxType': '20', 'bl': '900005014015', 'tin': '00471885', 'documentType': '083',
                 'docNumber': '1234215', 'pay': '99999999999999999',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100021', 'taxType': '2010', 'bl': '900005000618', 'tin': '84168159', 'documentType': '088',
                 'docNumber': '1234215', 'pay': '456366666456', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100022', 'taxType': '2011', 'bl': '900005015012', 'tin': '25293353', 'documentType': '082',
                 'docNumber': '2345fgsfsdffgdg45', 'pay': '99999999999999999',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100030', 'taxType': '2040', 'bl': '900005061370', 'tin': '02664656', 'documentType': '083',
                 'docNumber': '1234215', 'pay': '412346456', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100031', 'taxType': '2041', 'bl': '900005061370', 'tin': '47813265', 'documentType': '082',
                 'docNumber': '1234215', 'pay': '99999999999999999',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100032', 'taxType': '2051', 'bl': '900005061370', 'tin': '00891529', 'documentType': '089',
                 'docNumber': '8888888888', 'pay': '4563456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100033', 'taxType': '30', 'bl': '900005168415', 'tin': '05544509', 'documentType': '089',
                 'docNumber': '1234215', 'pay': '45635665345456', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100034', 'taxType': '4510', 'bl': '900005004230', 'tin': '87613918', 'documentType': '082',
                 'docNumber': '009999999999', 'pay': '4563456', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100035', 'taxType': '4511', 'bl': '900005004230', 'tin': '70985319', 'documentType': '088',
                 'docNumber': '1234215', 'pay': '99999999999999999', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100036', 'taxType': '4520', 'bl': '900005004271', 'tin': '37464898', 'documentType': '083',
                 'docNumber': '888888888888', 'pay': '99999999999999999', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100036', 'taxType': '4520', 'bl': '900005004248', 'tin': '27949116', 'documentType': '081',
                 'docNumber': '2345fggsdffgdg45', 'pay': '99999999999999999',
                 'notes': 'fdfgfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh234'})
co_tt_bl.append({'co': '05100040', 'taxType': 'VCT', 'bl': '900005024055', 'tin': '06922436', 'documentType': '082',
                 'docNumber': '66666666666', 'pay': '345634699788', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100041', 'taxType': 'MVT', 'bl': '900293063013', 'tin': '06605211', 'documentType': '083',
                 'docNumber': '0099999999999', 'pay': '56745674567',
                 'notes': 'fdgfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghf234'})
co_tt_bl.append({'co': '05100041', 'taxType': 'MTT', 'bl': '900005014015', 'tin': '05020569', 'documentType': '088',
                 'docNumber': '2345fgsdfffgdg45', 'pay': '2345234537347',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100041', 'taxType': 'MCV', 'bl': '900293063013', 'tin': '01801161', 'documentType': '082',
                 'docNumber': '1234215', 'pay': '4563456', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100041', 'taxType': 'HVT', 'bl': '900005012134', 'tin': '01234557', 'documentType': '089',
                 'docNumber': '2345fgsdsdffgdg45', 'pay': '8888888888',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})


class Obligation:

    @staticmethod
    def x(obj):
        return {
            'customsOfficeCode': obj['co'],
            'payeeId': obj['tin'],
            'documentCode': obj['documentType'],
            'documentReferenceNumber': obj['docNumber'],
            'taxCode': obj['taxType'],
            'budgetAccount': obj['bl'],
            'amount': obj['pay'],
            'notes': obj['notes'],
            #'operationCreate': None,
            #'confirmOper': None
        }

    @staticmethod
    def create_obligation():
        driver = Utils.driver
        driver.get("https://uatapp3.fipsoft.com/cap/obligation/create?lang=ru")
        Utils.check_select('iff', 0)
        Utils.set_date('documentDate', '17/01/2018')
        Utils.set_date('dueDate', '17/01/2018')
        rInt = random.randint(0, len(co_tt_bl)-1)
        Utils.fill_form(Obligation.x(co_tt_bl[rInt]))
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationCreate').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()



    ###################################################################################################################

    updateObligationFormData = {
        'amount': '1',
        'notes': 'r234123f',
        #'operationUpdate': None,
        #'confirmOper': None
    }

    @staticmethod
    def update_obligation():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.driver.find_element_by_id('clearCriteria').click()
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationUpdateClass').click()
        Utils.driver.find_element_by_id('amount').clear()
        Utils.driver.find_element_by_id('notes').clear()
        Utils.fill_form(Obligation.updateObligationFormData)
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationUpdate').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()

    ###################################################################################################################

    obligationCancelFormData = {
        #'confirmOper': None
    }

    @staticmethod
    def obligation_cancel():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.driver.find_element_by_id('clearCriteria').click()
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationCancelCreatedClass').click()
        Utils.fill_form(Obligation.obligationCancelFormData)
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()


    ###################################################################################################################

    obligationAllowFormData = {
        #'confirmOper': None
    }

    @staticmethod
    def obligation_allow():
        driver = Utils.driver
        driver.get("https://uatapp3.fipsoft.com/cap/?lang=ru")
        time.sleep(1)
        Utils.driver.find_element_by_id('clearCriteria').click()
        time.sleep(1)
        Utils.driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        Utils.driver.find_element_by_class_name('operationApproveClass').click()
        time.sleep(1)
        Utils.fill_form(Obligation.obligationAllowFormData)
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()




    ###################################################################################################################

    @staticmethod
    def view_obligation():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.driver.find_element_by_id('clearCriteria').click()
        WebDriverWait(Utils.driver, 5).until(
            Utils.wait_for_ajax_complete, "Timeout waiting for page to load")
        driver.find_element_by_class_name('glyphicon-eye-open').click()

    ###################################################################################################################

    mode_Of_Payment = ['БЗ', 'БН', 'НР', 'ПК', 'ПС']
    createPayrollForObligationFormData = {
        'modeOfPayment':  mode_Of_Payment[random.randint(0, len(mode_Of_Payment)-1)],
        'bankBranch': '16605',
        'bankAccount': '2341234',
        'notes': '123',
        #'operationCreate': None,
        #'confirmOper': None

    }

    @staticmethod
    def create_payroll_for_obligation():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.driver.find_element_by_id('clearCriteria').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        element = driver.find_element_by_css_selector(".operationAddPaymentOrderClass")
        time.sleep(1)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        Utils.fill_form(Obligation.createPayrollForObligationFormData)
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationCreate').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()


    ###################################################################################################################

    payFromOverpaymentFormData = {
        'overPayments[0].amountToUse': '99999999999999999',
        #'operationPayFromOverpayment': None,
        #'confirmOper': None
    }

    @staticmethod
    def pay_from_overpayment():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.driver.find_element_by_id('clearCriteria').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        element = driver.find_element_by_css_selector(".operationPayFromOverpaymentClass")
        time.sleep(1)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        Utils.fill_form(Obligation.payFromOverpaymentFormData)
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationPayFromOverpayment').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()


    ###################################################################################################################

    viewAndPrint99993FormData = {
        'clearCriteria': None,
        'documentCode': '09035',
        'searchObligations': None

    }

    @staticmethod
    def view_and_print_99993():
        driver = Utils.driver
        Utils.fill_form(Obligation.viewAndPrint99993FormData)
        WebDriverWait(Utils.driver, 5).until(
            Utils.wait_for_ajax_complete, "Timeout waiting for page to load")
        element = driver.find_element_by_css_selector("#obligationsTable .glyphicon-eye-open")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('cancel').click()
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        driver.find_element_by_class_name('clearCriteria').click()

    ###################################################################################################################

    historyObligationPrint99993FormData = {
        'documentCode': '09035',
        'searchObligations': None,

    }

    @staticmethod
    def history_obligation_print_99993():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.fill_form(Obligation.historyObligationPrint99993FormData)
        WebDriverWait(Utils.driver, 5).until(
            Utils.wait_for_ajax_complete, "Timeout waiting for page to load")  # Дождаться завершения ajax
        element = driver.find_element_by_css_selector("#obligationsTable .glyphicon-time")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector("#obligationsTable .operationLink")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('cancel').click()
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        driver.find_element_by_class_name('clearCriteria').click()

    ###################################################################################################################

    viewAndPrint09013FormData = {
        'clearCriteria': None,
        'documentCode': '09013',
        'searchObligations': None

    }

    @staticmethod
    def view_and_print_09013():
        driver = Utils.driver
        Utils.fill_form(Obligation.viewAndPrint09013FormData)
        WebDriverWait(Utils.driver, 5).until(
            Utils.wait_for_ajax_complete, "Timeout waiting for page to load")
        element = driver.find_element_by_css_selector("#obligationsTable .glyphicon-eye-open")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('cancel').click()
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        driver.find_element_by_class_name('clearCriteria').click()

    ###################################################################################################################

    historyObligationPrint09013FormData = {
        'documentCode': '09013',
        'searchObligations': None,

    }

    @staticmethod
    def history_obligation_print_09013():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.fill_form(Obligation.historyObligationPrint09013FormData)
        WebDriverWait(Utils.driver, 5).until(
            Utils.wait_for_ajax_complete, "Timeout waiting for page to load")  # Дождаться завершения ajax
        element = driver.find_element_by_css_selector("#obligationsTable .glyphicon-time")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector("#obligationsTable .operationLink")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('cancel').click()
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        driver.find_element_by_class_name('clearCriteria').click()

    ###################################################################################################################

    obligationCreateBarFormData = {
        # 'createObligation': None,
        'customsOfficeCode': '05100010',
        'payeeId': '17031994',
        'documentCode': '088',
        'documentDate': '13012018',
        'documentReferenceNumber': '1234',
        'taxCode': '10',
        'budgetAccount': '900013323010',
        'amount': '12346',
        'dueDate': '18012018',
        'notes': '17034534',
        'operationCreate': None,
        'confirmOper': None
    }

    @staticmethod
    def obligation_create_bar():
        driver = Utils.driver
        # driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.driver.find_element_by_id('clearCriteria').click()
        driver.find_element_by_class_name('createObligation').click()
        Utils.check_select('iff', 1)
        Utils.set_date('documentDate', '17/01/2018')
        Utils.set_date('dueDate', '17/01/2018')
        rInt = random.randint(0, len(co_tt_bl) - 1)
        Utils.fill_form(Obligation.x(co_tt_bl[rInt]))

    ###################################################################################################################

    @staticmethod
    def aria_controls_ob():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.check_select('obligationsTable_length', 3)
        WebDriverWait(Utils.driver, 5).until(
            Utils.wait_for_ajax_complete, "Timeout waiting for page to load")
        Utils.check_select('obligationsTable_length', 2)
        WebDriverWait(Utils.driver, 5).until(
            Utils.wait_for_ajax_complete, "Timeout waiting for page to load")
        Utils.check_select('obligationsTable_length', 1)
        WebDriverWait(Utils.driver, 5).until(
            Utils.wait_for_ajax_complete, "Timeout waiting for page to load")
        Utils.check_select('obligationsTable_length', 0)

    ###################################################################################################################

    document_Code = ['02019', '05013', '09013', '99991', '09035']
    openByNumberFormData = {
        'documentCode': document_Code[random.randint(0, len(document_Code) - 1)],
        'searchObligations': None
    }

    @staticmethod
    def open_by_number():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.fill_form(Obligation.openByNumberFormData)
        WebDriverWait(Utils.driver, 5).until(
            Utils.wait_for_ajax_complete, "Timeout waiting for page to load")  # Дождаться завершения ajax
        driver.find_element_by_css_selector("#obligationsTable tbody tr:first-child td:nth-child(8) a").click()
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')

    ###################################################################################################################

    createPayrollsFormData = {
        'customsOfficeCode': '05100010',
        'payeeId': '17031994',
        'documentCode': '088',
        'documentDate': '13012018',
        'documentReferenceNumber': '1234',
        'taxCode': '10',
        'budgetAccount': '900013323010',
        'amount': '12346',
        'dueDate': '18012018',
        'notes': '17034534',
    }

    searchForCreateFormData = {
        'payeeId': '17031994',
    }

    @staticmethod
    def create_payrolls():
        driver = Utils.driver
        driver.get("https://uatapp3.fipsoft.com/cap/obligation/create/?lang=ru")
        Utils.fill_form(Obligation.createPayrollsFormData)
        Utils.set_date('documentDate', '17/01/2018')
        Utils.set_date('dueDate', '17/01/2018')
        Utils.driver.find_element_by_id('operationCreate').click()
        Utils.driver.find_element_by_id('confirmOper').click()
        Utils.fill_form(Obligation.searchForCreateFormData)
        Utils.check_select('iff', 1)
        Utils.check_select('status', 4)
        Utils.driver.find_element_by_id('searchObligations').click()
        WebDriverWait(Utils.driver, 5).until(
            Utils.wait_for_ajax_complete, "Timeout waiting for page to load")
        #driver.find_element_by_css_selector("#obligationsTable tbody tr:first-child td:nth-child(2)").click()
        driver.find_element_by_css_selector('createdColor')

