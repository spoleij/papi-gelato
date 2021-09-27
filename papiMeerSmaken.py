aantalBolletjes , houder , meer , count , totaalHorentjes , totaalBakjes , totaalBolletjes = (None,)*7
slagroom , sprinkels , caramel , prijsslagroom , prijsCaramel , prijsSprinkels , aantalToppings , totaalToppings = (None,)*8
#define variables hier / binnen de class. (zet je dit binnen de class dan krijg je soms een error ???)

class Bestelling(object):                   #maak een class met object/self  zodat de variables binnen elkaars function gebruikt kunnen worden 
    count = 0
    aardbei , chocolade , munt , vanille, totaalHorentjes, totaalBakjes , totaalBolletjes, slagroom, sprinkels, caramel= (0,)*10
    prijsSlagroom , prijsCaramel , prijsSprinkels , aantalToppings , totaalToppings = (0,)*5
    print ('Welkom bij Papi Gelato!')
    def funcBolletjes (self):
        try:
            self.aantalBolletjes = int(input ('Hoeveel bolletjes wilt u?\n'))
            if self.aantalBolletjes in [1,2,3]:
                print('toppie joppie')
                self.funcSmaak()
            elif self.aantalBolletjes in [4,5,6,7,8]:
                print(f'Dan krijgt u van mij een bakje of horentje met {self.aantalBolletjes} bolletjes')
                self.funcSmaak()
            elif self.aantalBolletjes >8:
                print ('Sorry, zulke grote bakjes/horentjes hebben we niet')
                return self.funcBolletjes()
        except ValueError:
            print ('Sorry, dat snap ik niet...')
            return self.funcBolletjes()
                                                        
    def funcSmaak (self):                               # gefixt! de count variable moest buiten deze def, maar binnen de class!                                                      
        for i in range (self.aantalBolletjes):          # define de count varible (niet self.count) IN DE CLASS!! ZIE REGEL BOVENAAN 
            self.count = self.count +1                  # ik had hier nog niet over global scopes/variables geleerd ^^^^
            print (f"""Welke smaak wilt u voor bolletje nummer {self.count}?
            \nA) Aardbei \nC) Chocolade \nM) Munt \nV) Vanille  \n""")      # error als je opnieuw besteld gaan nummers door?
            self.smaak = input()                                               # gefixt. bij OPNIEUW self.count = 0 gedaan
            if self.smaak in ['a' ,'A', 'aardbei']:
                self.aardbei = self.aardbei + 1             #smaken los gedaan voor het geval dat
                self.totaalBolletjes = self.totaalBolletjes + 1
            
            elif self.smaak in ['c' ,'C', 'choco', 'chocolade', 'chocola' ]:
                self.chocolade = self.chocolade + 1
                self.totaalBolletjes = self.totaalBolletjes + 1
                
            elif self.smaak in ['m', 'M', 'munt' ,'mint', 'pepermunt']:
                self.munt = self.munt + 1
                self.totaalBolletjes = self.totaalBolletjes + 1
                
            elif self.smaak in ['v', 'V', 'vanille']:
                self.vanille = self.vanille + 1
                self.totaalBolletjes = self.totaalBolletjes + 1
            
            else:
                print ('Sorry, dat snap ik niet...')
                return self.funcSmaak()           
        self.funcHouder()        

    def funcHouder (self):
        self.houder = input (f'\nWilt u deze {self.aantalBolletjes} bolletje(s) in: \n A) een hoorntje \n B) een bakje \n')
        if self.houder in ['a', 'A','hoorntje' 'een hoortje' ]:
            self.houder = 'hoorntje'
            self.totaalHorentjes = self.totaalHorentjes + 1
            self.topping()
        elif self.houder in ['b','B''bakje''een bakje']:
            self.houder = 'bakje'
            self.totaalBakjes = self.totaalBakjes + 1
            self.topping()
        else:
            print ('Sorry, dat snap ik niet...')
            return self.funcHouder()
    def topping (self):
            self.welkeTop = input ("Wat voor topping wilt u?: \nA) Geen, \nB) Slagroom, \nC) Sprinkels \nD) Caramel Saus\n")

            if self.welkeTop in ['a' ,'A', 'geen' 'Geen']:
                self.funcMeer()

            elif self.welkeTop in ['b', 'B', 'slagroom', 'Slagroom']:
                self.slagroom = self.slagroom + 1
                self.aantalToppings = self.aantalToppings + 1
                
            elif self.welkeTop in ['c', 'C', 'sprinkels', 'Sprinkels' ,'sprinkles', 'Sprinkles']:
                self.sprinkels = self.sprinkels + 1
                self.prijsSprinkels = self.prijsSprinkels + (self.aantalBolletjes * 0.30)
                self.aantalToppings = self.aantalToppings + 1
                
            elif self.welkeTop in ['d' ,'D', 'caramel' ,'karamel', 'Caramel', 'Karamel', 'karamel saus' ,'Caramel saus']:
                self.caramel = self.caramel + 1
                self.aantalToppings = self.aantalToppings + 1
                if self.houder == 'hoorntje':
                    self.prijsCaramel = self.prijsCaramel + 0.60
                if self.houder == 'bakje':
                    self.prijsCaramel = self.prijsCaramel + 0.90
            
            else:
                print ('Sorry, dat snap ik niet...')
                return self.topping()    
            self.funcMeer()       

    def funcMeer (self):
        self.meer = input (f'Hier is uw {self.houder} met {self.aantalBolletjes} bolletje(s). Wilt u nog meer bestellen? \n(J/N)\n')
        if self.meer in ['j' ,'J' ,'ja', 'Ja', 'JA']:
            self.count = 0
            return self.funcBolletjes()
        if self.meer in ['n' , 'N' , 'nee' , 'Nee' , 'NEE']: #fout in code. als je eerst J doet, dat doet de 2e N het niet. maar de 3e weer wel?
            self.bonnetje()                           
        else:                                           # gefixt! elif vervangen door if.
            print ('Sorry, dat snap ik niet...')
            return self.funcMeer()
                                        # v GEFIXT!! return self.funcBolletjes IPV zonder return ervoor!!!
    def bonnetje (self):                # fout!! hij print een bonnetje voor elke keer dat je nog een keer bolletjes hebt besteld
        self.berekeningBol = self.totaalBolletjes * 1.10
        self.berekeningHor = self.totaalHorentjes * 1.25
        self.berekeningBak = self.totaalBakjes * 0.75
        self.berekeningTot = self.berekeningBol + self.berekeningHor + self.berekeningBak + self.totaalToppings
        self.prijsSlagroom = 0.50 * self.slagroom
        #self.prijsSprinkels
        #self.prijsCaramel
        self.totaalToppings = self.prijsCaramel + self.prijsSlagroom + self.prijsSprinkels
        print (f"""                     
        ---------------["Papi Gelato"]---------------

        Bolletjes	{self.totaalBolletjes} x $1.10  	= ${round(self.berekeningBol,2)}  
        Horentjes	{self.totaalHorentjes} x $1.25  	= ${round(self.berekeningHor,2)}
        Bakjes		{self.totaalBakjes} x $0.75       = ${round(self.berekeningBak,2)}
        Topping         1 x ${self.totaalToppings}        = ${round(self.totaalToppings)}  
                        ---------- +
        Totaal				= ${round(self.berekeningTot)}                  \n   """)
#AFRONDEN LUKT NOG NIET HELEMAAL WANT ALS IETS 0.50 IS KRIJG JE 0. NA DE =


obj = Bestelling()                                              #maak object en call obj.function, de eerste
obj.funcBolletjes()