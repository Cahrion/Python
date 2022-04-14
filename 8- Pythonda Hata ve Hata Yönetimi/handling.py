# error handling => hata yönetimi

while True:
    try: # derlemek için açılan ve hata olursa ekstra kontrol yapan blok
        x = int(input("x: "))
        y = int(input("y: "))
        print(x / y)
        z = y
# except ZeroDivisionError:
#     print("Y'için 0'degeri tanımı tanımsız yapar.")
# except ValueError:
#     print("Sayısal veriye harf eklenmez.")
# except (ZeroDivisionError, ValueError) as e:
#     print("Yanlış veri girdiniz.")
#     print(e)

# except => düzenleme ve hatayı seçme bölümü burada istedigin hatayı veya hepsini seçebilirsiniz.
    except Exception as ex: # exception hata tiplerinin tamamı
        if str(ex) == "division by zero":
            print("Bölme işlerimde 0 kullanılması tanımı tanımsız yapar.")
        else:
            print(f"Hatalı bir kullanım yaptınız: {ex}")
    else:
        break
    finally: # sonlandırıcı bloktur
        print("try except sonlandı.")

