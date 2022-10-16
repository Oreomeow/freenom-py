import os

# qq mail
MAIL_ADDRESS = str(os.getenv("MAIL_ADDRESS", ""))
MAIL_HOST = str(os.getenv("SMTP_HOST", "smtp.qq.com"))
MAIL_PW = str(os.getenv("MAIL_PW", ""))
MAIL_PORT = int(os.getenv("SMTP_PORT", 465))
MAIL_TO = str(os.getenv("MAIL_TO", ""))
MAIL_USER = str(os.getenv("MAIL_USER", ""))


# free nom
FN_ID = str(os.getenv("FN_ID", ""))
FN_PW = str(os.getenv("FN_PW", ""))
