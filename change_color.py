import cv2

# Ganti dengan path ke file gambar Anda
image_path = '/home/meelo/Downloads/cat.jpg'

# imread = membaca gambar
# image_path = gambar dari file
image = cv2.imread(image_path)

# Memastikan gambar telah dibaca dengan benar
if image is not None:
    # Koordinat pixel yang ingin diakses
    x, y = 50, 50
    
    # Memastikan koordinat berada dalam batas gambar
    height, width, channels = image.shape
    if x < width and y < height:
        # Mengakses pixel pada posisi (50, 50)
        pixel_value = image[y, x]
        print(f"Pixel value at ({x}, {y}): {pixel_value}")
        
    # Menggambar garis vertikal pada kolom x
        cv2.line(image, (x, 0), (x, height), (0, 255, 0), 1)  # Vertikal, warna hijau
        
        # Menggambar garis horizontal pada baris y
        cv2.line(image, (0, y), (width, y), (255, 0, 0), 1)  # Horizontal, warna hijau
        
        # Menambahkan teks koordinat dan nilai pixel di atas gambar
        text = f"({x}, {y}): {pixel_value}"
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
        

        # Menampilkan gambar
        cv2.imshow('Image with Pixel Info', image)

         # Tombol 'q' untuk keluar dari loop
    while True:
            key = cv2.waitKey(0)  # Tunggu hingga tombol ditekan
            if key == ord('q'):  # Jika tombol 'q' ditekan
                break
    else:
else:
    print("Gambar tidak dapat dibaca.")