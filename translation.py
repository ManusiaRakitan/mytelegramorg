class Translation(object):
    START_TEXT = """Hi Telaso!
Mau nyari API ID sama HASH kah? 😬
Masukin nomer Telegram lu disini, jangan nomer togel tolol

/start at any stage to re-enter your details"""
    AFTER_RECVD_CODE_TEXT = """Oke Kampang!
Kirim kesini kode yang telah dikirim oleh pihak telegramnya!

kode ini hanya digunakan untuk tujuan mendapatkan ID APP dari my.telegram.org
Jika elu gak percaya sama bot ini, ke my.telegram.org ae sono


/start at any stage to re-enter your details"""
    BEFORE_SUCC_LOGIN = "recieved code. Scarpping web page ..."
    ERRED_PAGE = "something wrongings. failed to get app id. \n\n@ManusiaRakitan"
    CANCELLED_MESG = "Bye! Please re /start the bot conversation"
    IN_VALID_CODE_PVDED = "sorry, but the input does not seem to be a valid Telegram Web-Login code"
    IN_VALID_PHNO_PVDED = "sorry, but the input does not seem to be a valid phone number"
