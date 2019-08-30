from selenium import webdriver


from Logout import Logout
from Roles import Roles
from SearchFillAll import SearchFillAll
from Payroll import Payroll
from TestGroup import TestGroup
from TestCase import TestCase
from Obligation import Obligation
from IncreaseOverpayment import IncreaseOverpayment
from DecreaseOverpayment import DecreaseOverpayment
from SetOff import SetOff
from FreezeUnFreeze import FreezeUnFreeze
from ViewOverpaymentsDebts import ViewOverpaymentsDebts
from Utils import Utils

driver = webdriver.Chrome()
driver.implicitly_wait(1)
Utils.driver = driver

createObligationSteps = [
    {'func': Utils.login, 'args': [Roles.CAP_QART]},
    {'func': Obligation.create_obligation, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

Ob_Cr = TestCase('CREATE-OBLIGATION', createObligationSteps, '')

updateObligationSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Obligation.create_obligation, 'args': None},
    {'func': Obligation.update_obligation, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

Ob_Up = TestCase('UPDATE-OBLIGATION', updateObligationSteps, '')

PayFromOverpaymentSteps = [
    #{'func': Utils.login, 'args': [Roles.CAP_QART]},
    {'func': Obligation.create_obligation, 'args': None},
    {'func': Logout.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CAP_ALL]},
    {'func': Obligation.obligation_allow, 'args': None},
    {'func': Logout.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CAP_QART]},
    {'func': Obligation.pay_from_overpayment, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]
Pa_Ov = TestCase('PAY-FROM-OVERPAYMENT', PayFromOverpaymentSteps, '')

ObligationCancelSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Obligation.create_obligation, 'args': None},
    {'func': Obligation.obligation_cancel, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]
Ob_Ca = TestCase('OBLIGATION-CANCEL', ObligationCancelSteps, '')

CreatePayrollForObligationSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Obligation.create_obligation, 'args': None},
    {'func': Obligation.create_payroll_for_obligation, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

Cr_Py_Ob = TestCase('CREATE-PAYROLL-FOR-OBLIGATION', CreatePayrollForObligationSteps, '')

CreatePayrollSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Payroll.create_payroll, 'args': None},
    #{'func': Utils.close_browser, 'args': None},
]

Cr_Py = TestCase('CREATE-PAYROLL', CreatePayrollSteps, '')

UpdatePayrollSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Payroll.create_payroll, 'args': None},
    {'func': Payroll.update_payroll, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

Up_Py = TestCase('UPDATE_PAYROLL', UpdatePayrollSteps, '')

PayPayrollAndConfirmSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Payroll.create_payroll, 'args': None},
    {'func': Payroll.pay_payroll, 'args': None},
    {'func': Payroll.confirm_pay, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

Pa_Py_Co = TestCase('PAY-PAYROLL-AND-CONFIRM', PayPayrollAndConfirmSteps, '')

CancelPayrollSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Payroll.create_payroll, 'args': None},
    {'func': Payroll.cancel_payroll, 'args': None}
    #{'func': Utils.close_browser, 'args': None}
]

Ca_Py = TestCase('CANCEL-PAYROLL', CancelPayrollSteps, '')

IncreaseOverpaymentSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': IncreaseOverpayment.increase_overpayment, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

In_Ov = TestCase('INCREASE-OVERPAYMENT', IncreaseOverpaymentSteps, '')

DecreaseOverpaymentSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': DecreaseOverpayment.decrease_overpayment, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

De_Ov = TestCase('DECREASE-OVERPAYMENT', DecreaseOverpaymentSteps, '')

ViewObligationSteps = [
    # {'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Obligation.view_obligation, 'args': None},
    # {'func': Utils.close_browser, 'args': None}
]

Vw_Ob = TestCase('VIEW-OBLIGATION', ViewObligationSteps, '')

ViewAndPrint99993Steps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Obligation.view_and_print_99993, 'args': None}
    #{'func': Utils.close_browser, 'args': None}
]
Vw_Pr_93 = TestCase('VIEW-AND-PRINT-99993', ViewAndPrint99993Steps, '')

PrintPayrollSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Payroll.print_payroll, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

Pr_Py = TestCase('PRINT-PAYROLL', PrintPayrollSteps, '')

SearchFillAllSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': SearchFillAll.search_fill_all, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

Se_All = TestCase('SEARCH-FILL-ALL', SearchFillAllSteps, '')

ObligationCreateBarSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Obligation.obligation_create_bar, 'args': None},
    # {'func': Utils.close_browser, 'args': None}
]

Ob_Cr_Bar = TestCase('OBLIGATION-CREATE-BAR', ObligationCreateBarSteps, '')

PayrollCreateBarSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Payroll.payroll_create_bar, 'args': None},
    # {'func': Utils.close_browser, 'args': None}
]

Py_Cr_Bar = TestCase('PAYROLL-CREATE-BAR', PayrollCreateBarSteps, '')

SetOffSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': SetOff.set_off, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

Set_Off = TestCase('SET-OFF', SetOffSteps, '')

UnFreezeSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': FreezeUnFreeze.un_freeze, 'args': None},
    {'func': Utils.close_browser, 'args': None}
]

#TestCase('UN-FREEZE', UnFreezeSteps, '').run()

ViewOverpaymentsDebtsSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': ViewOverpaymentsDebts.view_overpayments_debts, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

Vw_Op_Db = TestCase('VIEW-OVERPAYMENTS-DEBTS', ViewOverpaymentsDebtsSteps, '')

HistoryObligationPrint99993Steps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Obligation.history_obligation_print_99993, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

Hi_Ob_Pr_93 = TestCase('HISTORY-OBLIGATION-PRINT=99993', HistoryObligationPrint99993Steps, '')

HistoryPayrollPrintSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Payroll.history_payroll_print, 'args': None},
    #{'func': Utils.close_browser, 'args': None}

]

Hi_Py_Pr = TestCase('HISTORY-PAYROLL-PRINT', HistoryPayrollPrintSteps, '')

View00000PayrollPrintSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Payroll.view_00000_payroll_print, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

Vw_0_Py_Pr = TestCase('VIEW-ACTUAL-PAYMENT', View00000PayrollPrintSteps, '')

AriaControlsObSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Obligation.aria_controls_ob, 'args': None},
    #{'func': Utils.close_browser, 'args': None}

]

Ar_Co_Ob = TestCase('ARIA_CONTROLS_OB', AriaControlsObSteps, '')

AriaControlsPySteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Payroll.aria_controls_py, 'args': None},
    #{'func': Utils.close_browser, 'args': None}

]

Ar_Co_Py = TestCase('ARIA_CONTROLS_PY', AriaControlsPySteps, '')

Open_By_NumberSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Obligation.open_by_number, 'args': None},
    #{'func': Utils.close_browser, 'args': None}

]

Op_By_Nm = TestCase('OPEN_BY_NUMBER', Open_By_NumberSteps, '')

PayrollPrintViewActualPaymentViewReallocationsSteps = [
    #{'func': Utils.login, 'args': [Roles.ADMIN]},
    {'func': Payroll.payroll_print_view_actual_payment_view_reallocations, 'args': None},
    #{'func': Utils.close_browser, 'args': None}

]

Py_Pr_Vw_Ac = TestCase('PAYROLL_PRINT_VIEW_ACTUAL_PAYMENTS_VIEW_REALLOCATION', PayrollPrintViewActualPaymentViewReallocationsSteps, '')


TestGroup('TEST_CROUP_QART_ROLL',
          [Ob_Cr, Ob_Up, Pa_Ov, Ob_Ca, Cr_Py_Ob, Cr_Py, Up_Py, Pa_Py_Co, Ca_Py, In_Ov, De_Ov, Vw_Ob, Pr_Py, Se_All,
           Ob_Cr_Bar, Py_Cr_Bar, Set_Off, Vw_Pr_93, Vw_Op_Db, Hi_Ob_Pr_93, Hi_Py_Pr, Vw_0_Py_Pr, Ar_Co_Py, Ar_Co_Ob,
           Py_Pr_Vw_Ac, Op_By_Nm])

