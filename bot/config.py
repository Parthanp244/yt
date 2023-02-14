import os


class Config:

    BOT_TOKEN = "5659957974:AAGClSa1IPgr8fNDJ5BoI05urUvTPFbcTmQ"

    SESSION_NAME = ":memory:"

    API_ID = "5948230"

    API_HASH = "dd19a00b085a219421a3717d0ae9c0d0"

    CLIENT_ID = "615235511058-069l2a67jlqhred7f4g8glecdq4pou7l.apps.googleusercontent.com"

    CLIENT_SECRET = "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"

    BOT_OWNER = "1237712948"

    AUTH_USERS_TEXT = "AUTH_USERS"

    AUTH_USERS = [BOT_OWNER, 754495556] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = "unlisted"
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
