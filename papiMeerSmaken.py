print ('Welkom bij Papi Gelato!')
aantalBolletjes = None
houder = None                           
meer = None
count = None
totaalHorentjes = None
totaalBakjes = None
totaalBolletjes = None
#define variables hier / binnen de class. (zet je dit binnen de class dan krijg je een error)

class Bestelling(object):                   #maak een class met object/self  zodat de variables binnen elkaars function gebruikt kunnen worden 
    count = 0
    aardbei , chocolade , munt , vanille, totaalHorentjes, totaalBakjes , totaalBolletjes= (0,)*7
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
            self.funcMeer()
        elif self.houder in ['b','B''bakje''een bakje']:
            self.houder = 'bakje'
            self.totaalBakjes = self.totaalBakjes + 1
            self.funcMeer()
        else:
            print ('Sorry, dat snap ik niet...')
            return self.funcHouder()

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
        self.berekeningTot = self.berekeningBol + self.berekeningHor + self.berekeningBak
        print (f"""                     
        ---------------["Papi Gelato"]---------------

        Bolletjes	{self.totaalBolletjes} x $1.10  	= ${round(self.berekeningBol,2)}
        Horentjes	{self.totaalHorentjes} x $1.25  	= ${round(self.berekeningHor,2)}
        Bakjes		{self.totaalBakjes} x $0.75       = ${round(self.berekeningBak,2)}
                        ---------- +
        Totaal				= ${round(self.berekeningTot)}                  \n   """)

obj = Bestelling()                                              #maak object en call obj.function, de eerste
obj.funcBolletjes()