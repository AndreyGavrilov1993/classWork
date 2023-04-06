spisok = {"Boba": {"Phone": "8 564 317 23 64", "Email": "sabaka@mail.com", "Town": "Novosibirsk"},
          "Igor": {"Phone": "8 615 837 73 39", "Email": "igorek@gmail.com", "Town": "Kirgistan"},
          "Evgeniy": {"Phone": "8 839 019 83 71", "Email": "ququha@mail.com", "Town": "daleko"}}
peremenaya = spisok[input("Введите имя (Boba/Igor/Evgeniy): ")][input("Введите данные(Phone/Email/Town): ")]
print(peremenaya)