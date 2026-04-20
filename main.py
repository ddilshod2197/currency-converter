class Talaba:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya
        self.baholar = []

class Fan:
    def __init__(self, nom):
        self.nom = nom
        self.baholar = []

class Tizim:
    def __init__(self):
        self.talabalar = []
        self.fanlar = []

    def qosh_talaba(self, talaba):
        self.talabalar.append(talaba)

    def qosh_fan(self, fan):
        self.fanlar.append(fan)

    def qosh_baho(self, talaba, fan, baho):
        talaba.baholar.append((fan, baho))
        fan.baholar.append(baho)

    def otr_baho(self, talaba):
        if talaba.baholar:
            baholar = [baho for fan, baho in talaba.baholar]
            return sum(baholar) / len(baholar)
        else:
            return 0

    def eng_yaxshi_talaba(self):
        if self.talabalar:
            eng_yaxshi = max(self.talabalar, key=lambda talaba: sum(baho for fan, baho in talaba.baholar))
            return eng_yaxshi
        else:
            return None

    def fan_statistika(self, fan):
        if fan.baholar:
            baholar = fan.baholar
            otr_baho = sum(baholar) / len(baholar)
            eng_yaxshi = max(baholar)
            eng_yaxshi_talaba = max(self.talabalar, key=lambda talaba: talaba.baholar.count((fan, eng_yaxshi)))
            return {
                'O\'rtacha baho': otr_baho,
                'Eng yaxshi baho': eng_yaxshi,
                'Eng yaxshi talaba': eng_yaxshi_talaba.ism + ' ' + eng_yaxshi_talaba.familiya
            }
        else:
            return None

tizim = Tizim()

talaba1 = Talaba('Ali', 'Valiyev')
talaba2 = Talaba('Vali', 'Valiyev')
talaba3 = Talaba('Hasan', 'Hasanov')

fan1 = Fan('Matematika')
fan2 = Fan('Fizika')

tizim.qosh_talaba(talaba1)
tizim.qosh_talaba(talaba2)
tizim.qosh_talaba(talaba3)

tizim.qosh_fan(fan1)
tizim.qosh_fan(fan2)

tizim.qosh_baho(talaba1, fan1, 90)
tizim.qosh_baho(talaba1, fan2, 80)
tizim.qosh_baho(talaba2, fan1, 95)
tizim.qosh_baho(talaba2, fan2, 85)
tizim.qosh_baho(talaba3, fan1, 70)
tizim.qosh_baho(talaba3, fan2, 60)

print('O\'rtacha baho:', tizim.otr_baho(talaba1))
print('Eng yaxshi talaba:', tizim.eng_yaxshi_talaba().ism + ' ' + tizim.eng_yaxshi_talaba().familiya)

print('Matematika fan statistikasi:')
print(tizim.fan_statistika(fan1))

print('Fizika fan statistikasi:')
print(tizim.fan_statistika(fan2))
