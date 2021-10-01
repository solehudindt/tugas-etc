from room import Room
from character import Enemy
from character import Character
import random

#Inisisai Object
tamu = Room("Tamu")
tamu.set_desc("Mencurigakan, jendela dan pintu terbuka. Bau bawang sangat kuat disini")

keluarga = Room("Keluarga")
keluarga.set_desc("Ruangan ini besar, terdengar samar bunyi Wik-Wik-wiK")

makan = Room("Makan")
makan.set_desc("Baunya enak, ada sisa nasi dan katsu disana")

kerja = Room("Kerja")
kerja.set_desc("Samar terdengar lagu bertempo cepat")

kamar = Room("Kamar")
kamar.set_desc("Banyak barang bertema kartun berserakan dan berbau anyir")

dapur = Room("Dapur")
dapur.set_desc("Aneh, disini tidak tercium bau bumbu dapur.")

#Inisiasi ruangan
tamu.link_room(keluarga, "utara")

keluarga.link_room(tamu, "selatan")
keluarga.link_room(makan, "timur")
keluarga.link_room(kerja, "barat")

kerja.link_room(keluarga, "timur")
kerja.link_room(kamar, "utara")

kamar.link_room(kerja, "selatan")

makan.link_room(keluarga, "barat")
makan.link_room(dapur, "timur")

dapur.link_room(makan, "barat")

#Musuh
dave = Enemy("Dave", "The zombie warrior")
dave.set_conversation("Brwwhhh....")
dave.set_weakness("Cewe")


#Main program
ruang = (keluarga, kerja, kamar, makan, dapur)
ketemu = random.choice(ruang)
random.choice(ruang).set_character(dave)
current_room = tamu
#inhabitant = tamu.set_character(dave)
#inhabitant.describe()
print("Selamat datang di rumah bawang. Semoga kamu beruntung....")

while True:
    print("\n")
    print("Kamu ada di: ")
    current_room.get_info()
    print("\n")
    if current_room == ketemu:
        ketemu.describe()
        print("Selamat kamu bertemu seekor Weaboo!1!1!")
        break
    else:
        command = input("Kearah mana kamu mau pergi?  ")
        current_room = current_room.move(command)

