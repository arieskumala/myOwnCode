#Caesar Chiper with Python
#Digital Talent Scholarship - Kementerian Komunikasi dan Informatika Republik Indonesia

def caesar_encript(txt, shift):
    result = ""
    for char in txt:
        if char.isalpha() == False:
            result += char
        elif (65 <= ord(char) and ord(char) <= 90):
            result += chr(((ord(char) + shift - 65) % 26) + 65)
        elif (97 <= ord(char) and ord(char) <= 122):
            result += chr(((ord(char) + shift - 97) % 26) + 97)
    return result

def caesar_decript(chiper, shift):
    return caesar_encript(chiper, -shift)

def shuffle_order(txt, order):
    return ''.join([txt[i] for i in order])

def deshuffle_order(sftxt,order):
  return ''.join([sftxt[order.index(i)] for i in range(len(order))])

def send_batch(txt, batch_order, shift):
    while len(txt) % len(batch_order) != 0:
        txt += "_"
    test = ([caesar_encript(txt, shift)[i:i + len(batch_order)] for i in range(0, len(caesar_encript(txt, shift)), len(batch_order))])
    return ([shuffle_order(i, batch_order) for i in test])
    #a = test[-1]
    #if len(a) < len(batch_order):
    #    while len(a) < len(batch_order):
    #        a += "_"
    #    test.remove(test[-1])
    #    test.append(a)


def receive_batch(batch_cpr, batch_order, shift=3):
    batch_txt = [caesar_decript(deshuffle_order(i, batch_order), shift) for i in batch_cpr]
    return ''.join(batch_txt).strip('_')