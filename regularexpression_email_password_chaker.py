import re

pattern_email = re.compile(
    r"(^[a-zA-Z0-9-%$._+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
pattern_password = re.compile(r"^[a-zA-Z0-9-%$#@]{8,}")

email = "BBBiiiHHHkkkah@ugfdiuf.sdjsldfj"
password = "sdsasdasdal"

eml = pattern_email.search(email)
paswr = pattern_password.search(password)

print(eml)
print(paswr)
