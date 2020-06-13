priority = 2
email = 'arieskumala@gmail.com'

#==========SOAL 1==========
#Graded
def letter_catalog(items, letter='A'):
    pass
    #MULAI KODEMU DI SINI
    newFruit = [x for x in items if x.startswith(letter)]
    return newFruit

print('='*10, "Soal 1", "="*10)
print(letter_catalog(['Apple', 'Avocado', 'Banana', 'Blackberries', 'Blueberries', 'Cherries'], letter='A'))

#==========SOAL 2==========
#Graded
def counter_item(items):
    pass
    #MULAI KODEMU DI SINI
    #membuatnya menjadi huruf kapital dan mengurutkannya
    daftarBuah = []
    for buah in items:
        daftarBuah.append(buah.capitalize())
        daftarBuah.sort()
    #membuat list baru untuk memasukkan buah-buah yang unik dan list jumlah buah
    newList = []
    listCount = []
    for buah in daftarBuah:
        if buah not in newList:
           newList.append(buah)
    for buah in newList:
        sum = daftarBuah.count(buah)
        listCount.append(sum)
    #menggabungkan kedua list dengan built-in zip untuk diubah ke dict
    buahDanJumlah = list(zip(newList, listCount))
    jumlahBuah = dict(buahDanJumlah)
    return jumlahBuah

print('='*10, "Soal 2", "="*10)
print(counter_item(['Apple','Apple','Apple','Blueberries','Blueberries','Blueberries']))

#==========SOAL 3==========
#Graded
# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

#List buah
chart = ['Blueberries', 'Blueberries', 'Blueberries','Grapes','Apple','Apple','Apple','Guava','Jackfruit','Blueberries','Jackfruit']

#MULAI KODEMU DI SINI
fruit_price = dict(zip(fruits,prices))

def total_price(dcounter, fprice):
    pass
    #MULAI KODEMU DI SINI
    total = 0
    for x, y in dcounter.items():
        total += (y*fprice.get(x))
    return total

print('=' * 10, "Soal 3", "=" * 10)
print(total_price(counter_item(chart), fruit_price))

#==========SOAL 4==========
#Graded
def discounted_price(total, discount, minprice=100):
    pass
    #MULAI KODEMU DI SINI
    if total >= minprice:
        totalAkhir = total - (total * (discount/100))
        return totalAkhir
    else:
        return total

print('=' * 10, "Soal 4", "=" * 10)
print(discounted_price(total_price(counter_item(chart),fruit_price),10,minprice=100))

#==========SOAL 5==========
#Graded
def print_summary(items,fprice):
  pass
  a = ""
  # MULAI KODEMU DI SINI
  listPembelian = counter_item(items)
  for x, y in listPembelian.items():
      print(y, x, ":", (y * fprice.get(x)))
  print("total : %s" % total_price(counter_item(items), fprice))
  print("discount price : %r" % discounted_price(total_price(counter_item(items),fprice),10,minprice=100))

print('=' * 10, "Soal 5", "=" * 10)
print_summary(chart, fruit_price)