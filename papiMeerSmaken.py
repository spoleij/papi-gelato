print ('Welkom bij Papi Gelato! Je mag alle smaken kiezen!')
aantalBolletjes = None
houder = None                           
meer = None
count = None
#define variables hier / binnen de class. (zet je dit binnen de class dan krijg je een error)

class Bestelling(object):                   #maak een class met object/self  zodat de variables binnen elkaars function gebruikt kunnen worden 
    count = 0
    aardbei , chocolade , munt , vanille = (0,)*4
    def funcBolletjes (self):
        try:
            self.aantalBolletjes = int(input ('Hoeveel bolletjes wilt u?\n'))
            if self.aantalBolletjes in [1,2,3]:
                print('toppie joppie')
                self.funcSmaak()
            elif self.aantalBolletjes in [4,5,6,7,8]:
                print(f'Dan krijgt u van mij een bakje met {self.aantalBolletjes} bolletjes')
                self.funcSmaak()
            elif self.aantalBolletjes >8:
                print ('Sorry, zulke grote bakken hebben we niet')
                return self.funcBolletjes()
        except ValueError:
            print ('Sorry, dat snap ik niet...')
            return self.funcBolletjes()

    def funcSmaak (self):                               # HIER AFGEBLEVEN. HOE HERHAAL JE HET VOOR ELK BOLLETJE???

        for i in range (self.aantalBolletjes):
            self.count = self.count +1                  # define de count varible (niet self.count) IN DE CLASS!! ZIE REGEL BOVENAAN
            print (f"""Welke smaak wilt u voor bolletje nummer {self.count}?
            \nA) Aardbei \nC) Chocolade \nM) Munt \nV) Vanille  \n""")
            self.smaak = input()
            if self.smaak in ['a' ,'A', 'aardbei']:
                self.aardbei = self.aardbei + 1
            
            elif self.smaak in ['c' ,'C', 'choco', 'chocolade', 'chocola' ]:
                self.chocolade = self.chocolade + 1
                
            elif self.smaak in ['m', 'M', 'munt' ,'mint', 'pepermunt']:
                self.munt = self.munt + 1
                
            elif self.smaak in ['v', 'V', 'vanille']:
                self.vanille = self.vanille + 1
            
            else:
                print ('Sorry, dat snap ik niet...')
                return self.funcSmaak()
        print (f"""Deze bolletjes krijgt u:\n
                Aardbei         = {self.aardbei}
                Chocolade       = {self.chocolade}
                Munt            = {self.munt}
                Vanille         = {self.vanille}""")
            
        self.funcHouder()        

    def funcHouder (self):
            self.houder = input (f'\nWilt u deze {self.aantalBolletjes} bolletje(s) in: \n A) een hoorntje \n B) een bakje \n')
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