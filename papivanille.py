print ('Welkom bij Papi Gelato! Je mag alle smaken kiezen, zolang je maar vanille ijs kiest!')
aantalBolletjes = None
houder = None                           #define de variables buiten de class/functinons
meer = None

class Bestelling(object):                   #maak een class met object/self  zodat de variables binnen elkaars function gebruikt kunnen worden
    def funcBolletjes (self):
        try:
            self.aantalBolletjes = int(input ('Hoeveel bolletjes wilt u?\n'))
            if self.aantalBolletjes in [1,2,3]:
                print('toppie joppie')
                self.funcHouder()
            elif self.aantalBolletjes in [4,5,6,7,8]:
                print(f'Dan krijgt u van mij een bakje met {self.aantalBolletjes} bolletjes')
                self.funcHouder()
            elif self.aantalBolletjes >8:
                print ('Sorry, zulke grote bakken hebben we niet')
                return self.funcBolletjes()
        except ValueError:
            print ('Sorry, dat snap ik niet...')
            return self.funcBolletjes()
    def funcHouder (self):
        self.houder = input (f'Wilt u deze {self.aantalBolletjes} in: \n A) een hoorntje \n B) een bakje \n')
        if self.houder in ['a', 'A','hoorntje' 'een hoortje' ]:
            self.houder = 'hoorntje'
            self.funcMeer()
        elif self.houder in ['b','B''bakje''een bakje']:
            self.houder = 'bakje'   
            self.funcMeer()
        else:
            print ('Sorry, dat snap ik niet...')
            return self.funcHouder()

    def funcMeer (self):
        self.meer = input (f'Hier is uw {self.houder} met {self.aantalBolletjes} bolletje(s). Wilt u nog meer bestellen? \n(J/N)\n')
        if self.meer in ['j' ,'J' ,'ja', 'Ja', 'JA']:
            self.funcBolletjes()
        elif self.meer in ['n' , 'N' , 'nee' , 'Nee' , 'NEE']:
            print ('Bedankt en tot ziens!')
            return None                                             #fout in code. als je eerst J doet, dat doet de 2e N het niet. maar de 3e weer wel?
        else:
            print ('Sorry, dat snap ik niet...')
            return self.funcMeer()
        self.funcBolletjes()

obj = Bestelling()                                              #maak object en call obj.function, de eerste van de drie
obj.funcBolletjes()