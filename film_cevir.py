from src.api.omdb import OMDbAPI

def hibrit_film_adi_cevir(film_adi: str, api: OMDbAPI) -> str:
    """
    Film adını İngilizce'ye çevirir.
    Önce yerel eşleştirmeleri kontrol eder, bulamazsa API'yi kullanır.
    """
    # Yerel eşleştirmeler (sadece FilmList.txt'den)
    eslestirmeler = {
        "6 Super Kahraman": "",
        "A Takimi": "",
        "Ailem Robotlara Karsi": "",
        "Alvin and the Chipmunks The Chipwrecked": "",
        "asterix": "",
        "Asterix Obelix Take on Caesar": "",
        "Ata Demirer Tek Kişilik Dev Kadro 2": "",
        "Avatar The Last Airbender S01E01": "",
        "Avengers Ultron": "",
        "Bad Boys Her Zaman Cilgin": "",
        "Başka Bir Sen": "",
        "Başlat": "",
        "Celal ile Ceren": "",
        "Cennetin Krallığı": "",
        "Charlies Angels": "",
        "DeLorean": "",
        "Demir Adam": "",
        "Dogadaki Insan": "",
        "Dogu": "",
        "Dune (1984)": "",
        "En Son Babalar Duyar S01E15": "",
        "Enzo The Racing Art": "",
        "Everyones Hero": "",
        "Everything Theory": "",
        "Final Fantasy XV Kings Sword": "",
        "Five Minarets in New York": "",
        "Ford vs Ferrari": "",
        "Full of Hate": "",
        "GI Joe the Rise of Cobra: First Look": "",
        "GIJoe": "",
        "Guardians of Galaxy": "",
        "Guardians of Galaxy 2": "",
        "Guardians of Galaxy 3": "",
        "Guzel Ve Cirkin": "",
        "Harry Potter Deathly Hallow  Part 2": "",
        "Harry Potter Prisoners Azkaban": "",
        "Hayat Bilgisi": "",
        "Iftarlik Gazoz": "",
        "Jumanji Forest": "",
        "Jumanji New Level": "",
        "Jumanji Vahi Orman": "",
        "Kara Panter": "",
        "Kibar Feyzo": "",
        "Kingsman": "",
        "Kolonya Cumhuriyeti": "",
        "Kurtlar Vadisi Pusu": "",
        "Kutsal Damacana 2": "",
        "E! Online Live from the Red Carpet Men in Black 3": "",
        "Muhteem Yedili": "",
        "Naked Gun 3 The Final Insult": "",
        "Oflu Hocanin Sifresi 2": "",
        "Organize İşler": "",
        "Pokemon: Detective Pikachu (2019)": "",
        "Prens S01E01": "",
        "Rafadan Tayfa: Hayrimator": "",
        "Rons Gone Wrong": "",
        "Sahte Kabadayı": "",
        "Savas Vadisi": "",
        "Selvi Boylum Al Yazmalım": "",
        "Sonic Hedgehog": "",
        "Spoiled": "",
        "Sumelann Sifresi Temel": "",
        "Sümelanın Şifresi 3 Cünyor Temel": "",
        "Sümelanın Şifresi Temel": "",
        "The Fantastic Five": "",
        "The Planets S01E01": "",
        "The Power of Love": "",
        "The Twins Project": "",
        "Tremors 2: Aftershocks": "",
        "Tuts Treasures Hidden Secrets S01E02": "",
        "Umudumuz Şaban": "",
        "Wreck It Ralph Internet": "",
        "Yenilmezler Sonsuzluk Savasi": "",
        "You Are My Everything": "",
        "Çanakkale Yolun Sonu": "",
        "İftarlık Gazoz": "",
    }

    if film_adi in eslestirmeler and eslestirmeler[film_adi]:
        return eslestirmeler[film_adi]

    try:
        return api.film_adi_cevir(film_adi)
    except Exception as e:
        print(f"API hatası: {e}")
        return film_adi 