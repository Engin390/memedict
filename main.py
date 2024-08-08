while True:
    meme_dict = {
                "CRINGE": "garip yada utandırıcı birşey",
                "LOL": "katıla katıla gülmek",
                "FAKE": "sahte, gerçek olmayan",
                "TROLL": "şakalamak",
                "BRUH":"yok artık, olacağı belliydi",
                "CREEPY":"korkunç, dehşet verici"
    }

    word = input("anlamadığınız bir kelime girin(büyük harflerle): ")

    if word in meme_dict.keys():
        print("girdiğiniz kelimenin anlamı:",meme_dict[word])
    else:
        print("maalesef aradığınız kelime bu sözlükte bulunmamaktadır...")
