import os
# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph
 
def main():
    continua = True
    agirliklar = []
    kruskal=  []
    kenar = []
    addKenar=[]

    while continua:
        os.system('clear')
        print("1 - Köşe Ekle")
        print("2 - Ağırlıkları kenarlarla ekleyin")
        print("3 - Dosyadan Oku")
        print("4 - Kruskal Algoritmasını Çalıştırın")
        print("5 - Ayrılmak\n\n")
        op = input('İstenen seçenek nedir?: ')


        if op == '1':
            print('Köşe ekleme. Çıkmak için 0 girin\n\n')

            ok = True
            while ok:
                v = input('Köşe: ')
                if v == '0':
                    break
                kenar.append(v)


        if op == '2':
            print(kenar)
            print('Ağırlıklar ile kenar ekleme. Çıkmak için 0 girin\n\n')
            print('Exemplo:\A-B: A-B\nPeso: 5\n\n')


            ok = True
            while ok:
                a = input('Dugum1-Dugum2: ')
                p = input('Ağırlık: ')
                print("\n")

                if a == '0' or p == '0':
                    break

                veri = {'a': a, 'p': int(p)}
                agirliklar.append(veri)

        if op == '3':

            dosyaYolu=input("Dosya Yolu : ")
            with open(dosyaYolu, 'r') as f:
                for satir in f.readlines():
                    Kenar=satir[0 : satir.index(':')]
                    Agirlik=satir[satir.index(':')+1 : -1]
                    veri = {'a': Kenar, 'p': int(Agirlik)}
                    agirliklar.append(veri)
            f.closed                
        if op == '4':
            print('Kruskal Algoritmasını Çalıştırma\n\n')
            agirliklar = sorted(agirliklar, key=lambda x: x['p'])
            print("{",end="")
            toplam=0

            for agirlik in agirliklar:
                u = agirlik['a'][0 : agirlik['a'].index('-')]
                v = agirlik['a'][agirlik['a'].index('-')+1 : -1]
                if (not u in addKenar) or (not v in addKenar):
                    print("("+agirlik['a'] + ', ' + str(agirlik['p'])+")",end="")
                    kruskal.append(agirlik)
                    toplam+=int(agirlik['p'])
                    addKenar.append(u)
                    addKenar.append(v)
            print("}")
            print("Toplam uzunluk :"+str(toplam))

            return 0

        if op == '5':
            print('Ayrıl...\n\n')
            return 0
    return 0

if __name__ == '__main__':
    main()