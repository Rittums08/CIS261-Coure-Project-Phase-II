#Scott Ritz
#CIS261 Course Project Phase III

def getDatesWorked():
    fromdate = input("Please enter your start date in the following format MM/DD/YYYY: ")
    enddate = input("Please enter your end date in the following format MM/DD/YYYY: ")
    return fromdate, enddate

def getEmpName():
    empName = input("Enter Employee Name:  ")
    return empName

def getHoursWorked():
    hours = float(input("Enter Hours: "))
    return hours

def getHourlyRate():
    hourlyRate = float(input("Enter Hourly Rate:  "))
    return hourlyRate

def getTaxRate():
    taxRate = float(input("Enter Tax Rate:  "))
    taxRate = taxRate / 100
    return taxRate

def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    gPay = hours * hourlyRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

def printInfo(empDetailList):
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalnetPay = 0.00
    for empList in empDetailList:
        fromdate = empList[0]
        enddate = empList[1]
        empName = empList[2]
        hours = empList[3]
        hourlyRate = empList[4]
        taxRate = empList[5]
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        print(fromdate, enddate, empName, f"{hours:.2f}", f"{hourlyRate:,.2f}", f"{grosspay:,.2f}", f"{taxRate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
        totalEmployees += 1
        totalHours += hours
        totalGrossPay += grosspay
        totalTax += incometax
        totalnetPay += netpay
        empTotals["totEmp"] = totalEmployees
        empTotals["totHours"] = totalHours
        empTotals["totGross"] = totalGrossPay
        empTotals["totTax"] = totalTax
        empTotals["totNet"] = totalnetPay
        
def printTotals(empTotals):
    print(f'Total Number Of Employees:  {empTotals["totEmp"]}')
    print(f'Total Hours Of Employees:  {empTotals["totHours"]}')
    print(f' Total Gross Pay Of Employees: {empTotals["totGross"]:,.2f}')
    print(f' Total Tax Of Employees: {empTotals["totTax"]:,.2f}')
    print(f' Total Net Pay Of Employees:  {empTotals["totNet"]:,.2f}')
    
def WriteEmployeeInformation(employee):
    file = open("employeeinfo.txt", "a")    
    file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))
    
def GetFromDate():
    valid = False
    fromdate = ""    
    while not valid:
        fromdate = input("Enter From Date (mm/dd/yyyy):  ")
        if (len(fromdate.split('/')) != 3 and fromdate.upper() != 'ALL'):
            print("Invalid date format!!! Please use the correct format of mm/dd/yyy: ")
            
        else:
            valid = True
    return fromdate

def ReadEmployeeInformation(fromdate):
    empDetailList = []
    file = open("employeeinfo.txt", "r")
    data = file.readlines()
    condition = True
    if fromdate.upper() == 'ALL':
        condition = False
    
    for employee in data:
        employee = [x.strip() for x in employee.strip().split("|")]
        if not condition:
            empDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
        else:
            if fromdate == employee[0]:
                empDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
                
    return empDetailList   
     
if __name__ == "__main__":
    empDetailList = []
    empTotals = {}
    while True:
        empName = getEmpName()
        if (empName.lower() == "end"):
            break
        fromdate, enddate = getDatesWorked()
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        print()
        empDetail = EmpDetail = [fromdate, enddate, empName, hours, hourlyRate, taxRate]
        WriteEmployeeInformation(EmpDetail)
        
    print()
    print()
    fromdate = GetFromDate()
    empDetailList = ReadEmployeeInformation(fromdate)
    print()
    printInfo(empDetailList)
    print()
    printTotals(empTotals)
