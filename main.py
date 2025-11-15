from datetime import datetime

class Hisob:
    def __init__(self, balans):
        self.balans = balans

    def foiz_hisoblash(self):
        pass

    # Python’da overload funksiya parametrlari orqali qilinadi
    def pul_chiqarish(self, summa):
        pass


class OmonatHisobi(Hisob):
    def __init__(self, balans, min_qoldiq=100):
        super().__init__(balans)
        self.min_qoldiq = min_qoldiq

    def foiz_hisoblash(self):
        return self.balans * 0.03

    def pul_chiqarish(self, summa):
        if self.balans - summa < self.min_qoldiq:
            return "Xatolik! Minimal qoldiqdan pastga tushib bo‘lmaydi!"
        self.balans -= summa
        return f"Yangi balans: {self.balans}"


class KreditHisobi(Hisob):
    def foiz_hisoblash(self):
        return self.balans * 0.12

    def pul_chiqarish(self, summa):
        foiz = summa * 0.02
        jami = summa + foiz
        self.balans -= jami
        return f"Foiz bilan yechildi. Yangi balans: {self.balans}"


class InvestitsiyaHisobi(Hisob):
    def foiz_hisoblash(self):
        return self.balans * 0.15

    def pul_chiqarish(self, summa):
        hafta_kuni = datetime.today().weekday()
        if hafta_kuni >= 5:
            return "Faqat ish kunida pul yechish mumkin!"
        self.balans -= summa
        return f"Yangi balans: {self.balans}"


# TEST
hisoblar = [
    OmonatHisobi(1000),
    KreditHisobi(5000),
    InvestitsiyaHisobi(8000)
]

for h in hisoblar:
    print(h.foiz_hisoblash())
