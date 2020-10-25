string = "Google でサラを調べて"


string = string

print(string)
string2 = ""

string = string.replace("をGoogle で検索して", "").replace("をGoogle で調べて", "").replace("Google で検索して", "").replace("Google で調べて", "").replace(
    "をGoogle で", "").replace("でGoogle を", "").replace(
    "Google で", "").replace("を検索して", "").replace("を調べて", "").replace("検索して", "").replace("調べて", "")