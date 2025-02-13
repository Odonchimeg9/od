buten_ner = input("Таны бүтэн нэр: ")
tovch_ner = input("Таны товчилсон нэр: ")

index = int(input(f"Таны бүтэн нэрэнд таны товчилсон нэрийн ямар дугаарт байгаа үсгийг хайх вэ?: "))

if 0 <= index < len(tovch_ner):  
    usug = tovch_ner[index]
    bairlal = buten_ner.find(usug)
    print(f"{index} дугаар дахь үсэг '{usug}' {bairlal} дугаар дээр олдлоо.")
else:
    print(f"{index} дугаар дахь үсэг -1 дугаар дээр олдлоо.")  
