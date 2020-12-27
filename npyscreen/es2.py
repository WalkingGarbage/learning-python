import npyscreen

class myEmployeeForm(npyscreen.Form):
    def create(self):
        # inserimento nome dell'impiegato
        self.myName        = self.add(npyscreen.TitleText, name='Name')
        # elenco a scelta singola
        self.myDepartment = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=3, name='Department', values = ['Department 1', 'Department 2', 'Department 3'])
        #calendario con selezione data
        self.myDate        = self.add(npyscreen.TitleDateCombo, name='Date Employed')

def myFunction(*args):
    F = myEmployeeForm(name = "New Employee")           #nome del form (finestra)
    F.edit()                                            #persistenza del form
    return "Created record for " + F.myName.value       #output

if __name__ == '__main__':
    print (npyscreen.wrapper_basic(myFunction))