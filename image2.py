import cv2

# untuk membaca gambar 
image = cv2.imread("/home/meelo/Downloads/cat.jpg")

if image is None:
    print("Gambar tidak ditemukan")
else:
    print("Gambar ditemukan")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# untuk menampilkan gambar
cv2.imshow("Gambar saya", gray_image)

#menunggu tombol ditekan
cv2.waitKey(0)

# menutup semua jendela window
cv2.destroyAllWindows()

