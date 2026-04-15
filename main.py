# 11
class Talaba:
    def __init__(self, i, y, k, f):
        self.ism = i
        self.yosh = y
        self.kurs = k
        self.fakultet = f

t1 = Talaba("Ali", 20, 2, "IT")
t2 = Talaba("Vali", 22, 3, "Iqtisod")

print(t1.ism, t1.yosh, t1.kurs, t1.fakultet)
print(t2.ism, t2.yosh, t2.kurs, t2.fakultet)

# 12
class Kitob:
    def __init__(self, n, m, j, n1):
        self.nomi = n
        self.muallif = m
        self.janr = j
        self.narx = n1

k1 = Kitob("O‘tkan kunlar", "Abdulla Qodiriy", "roman", 50000)
k2 = Kitob("Alkimyogar", "Paulo Coelho", "fantastika", 40000)

print(k1.nomi, k1.muallif, k1.janr, k1.narx)
print(k2.nomi, k2.muallif, k2.janr, k2.narx)

# 13
class Telefon:
    def __init__(self, model, rang, xotira, narx):
        self.model = model
        self.rang = rang
        self.xotira = xotira
        self.narx = narx

tel1 = Telefon("iPhone 13", "qora", "128GB", 1200)
tel2 = Telefon("Samsung S21", "oq", "256GB", 950)

print(tel1.model, tel1.rang, tel1.xotira, tel1.narx)
print(tel2.model, tel2.rang, tel2.xotira, tel2.narx)

# 14
class Mashina:
    def __init__(self, marka, rang, yili, narx):
        self.marka = marka
        self.rang = rang
        self.yili = yili
        self.narx = narx

m1 = Mashina("Cobalt", "oq", 2022, 12000)
m2 = Mashina("Malibu", "qora", 2023, 25000)

print(m1.marka, m1.rang, m1.yili, m1.narx)
print(m2.marka, m2.rang, m2.yili, m2.narx)

# 15
class Xodim:
    def __init__(self, ism, yosh, lavozim, maosh):
        self.ism = ism
        self.yosh = yosh
        self.lavozim = lavozim
        self.maosh = maosh

x1 = Xodim("Ali", 25, "Backend developer", 2000)
x2 = Xodim("Vali", 30, "Team lead", 3000)

print(x1.ism, x1.yosh, x1.lavozim, x1.maosh)
print(x2.ism, x2.yosh, x2.lavozim, x2.maosh)

# 16
class Universitet:
    def __init__(self, nomi, shahar, talabalar_soni):
        self.nomi = nomi
        self.shahar = shahar
        self.talabalar_soni = talabalar_soni

u1 = Universitet("TATU", "Toshkent", 20000)
u2 = Universitet("SamDU", "Samarqand", 15000)

print(u1.nomi, u1.shahar, u1.talabalar_soni)
print(u2.nomi, u2.shahar, u2.talabalar_soni)

# 17
class Film:
    def __init__(self, nomi, janr, davomiligi, reyting):
        self.nomi = nomi
        self.janr = janr
        self.davomiligi = davomiligi
        self.reyting = reyting

f1 = Film("Inception", "fantastika", 148, 9)
f2 = Film("Titanic", "drama", 195, 8)

print(f1.nomi, f1.janr, f1.davomiligi, f1.reyting)
print(f2.nomi, f2.janr, f2.davomiligi, f2.reyting)

# 18
class Dokon:
    def __init__(self, n, m, t):
        self.nomi = n
        self.manzil = m
        self.turi = t

d1 = Dokon("Korzinka", "Toshkent", "supermarket")
d2 = Dokon("Havas", "Samarqand", "market")

print(d1.nomi, d1.manzil, d1.turi)
print(d2.nomi, d2.manzil, d2.turi)

# 19
class Hayvon:
    def __init__(self, n, t, y, r):
        self.nomi = n
        self.turi = t
        self.yoshi = y
        self.rang = r

h1 = Hayvon("Rex", "it", 3, "qora")
h2 = Hayvon("Mushukcha", "mushuk", 2, "oq")

print(h1.nomi, h1.turi, h1.yoshi, h1.rang)
print(h2.nomi, h2.turi, h2.yoshi, h2.rang)

# 20
class Kompyuter:
    def __init__(self, p, o, d, n):
        self.protsessor = p
        self.operativ_xotira = o
        self.disk = d
        self.narx = n

k1 = Kompyuter("Intel i5", "8GB", "512GB", 700)
k2 = Kompyuter("Intel i7", "16GB", "1TB", 1200)

print(k1.protsessor, k1.operativ_xotira, k1.disk, k1.narx)
print(k2.protsessor, k2.operativ_xotira, k2.disk, k2.narx)
