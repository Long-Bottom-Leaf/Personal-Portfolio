import datetime

def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr


def FComma2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:,.2f}".format(Value)

    return ValueStr


def FComma0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:,.0f}".format(Value)

    return ValueStr


def FNumber0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.0f}".format(Value)

    return ValueStr


def FNumber1(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.1f}".format(Value)

    return ValueStr


def FNumber2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.2f}".format(Value)

    return ValueStr


def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr


def FDateM(DateValue):
    # Function will accept a value and format it to dd-Mon-yy.

    DateValueStr = DateValue.strftime("%d-%b-%y")

    return DateValueStr


def FDateL(DateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.

    DateValueStr = DateValue.strftime("%A, %B %d, %Y")

    return DateValueStr

def FPhone14(PhoneNumber):
    # Function to format the phone number to (###) ###-####

    Phone14 = "(" + PhoneNumber[0:3] + ") " + PhoneNumber[3:6] + "-" + PhoneNumber[6:10]

    return Phone14

def GetPayDue(InvoiceDate):
    # Determine the payment date based on 20 days after the invoice date
    # or the first day of the next month - whichever is later.
 
    Pay20Date = InvoiceDate + datetime.timedelta(days=20)
    PurYear = InvoiceDate.year
    PurMonth = InvoiceDate.month
    PurDay = InvoiceDate.day
 
    PayYear = PurYear
    PayMonth = PurMonth + 1
    if PayMonth == 13:
        PayMonth -= 12
        PayYear += 1
    PayDay = 1
    PayFirstDate = datetime.datetime(PayYear, PayMonth, PayDay)
 
    if Pay20Date > PayFirstDate:
        PayDate = Pay20Date
    else:
        PayDate = PayFirstDate
 
    return PayDate

