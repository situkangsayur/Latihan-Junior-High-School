## program hitung nilai

if __name__ == '__main__':

    nilai = 10

    nilai_huruf = ""

    if nilai > 80 :
        nilai_huruf = "A"
    elif nilai >= 70 and nilai < 80: # false/salah dan true/benar ==> salah

        nilai_huruf = "B"
    elif nilai >= 50 and nilai < 70: 
        nilai_huruf = "C"
    elif nilai >= 30 and nilai < 50:
        nilai_huruf = "D"
    else:
        nilai_huruf = "E"

    print(nilai_huruf)