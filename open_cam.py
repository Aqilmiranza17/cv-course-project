import cv2

# Membuka kamera (biasanya 0 adalah kamera default)
cap = cv2.VideoCapture(0)

# Periksa apakah kamera terbuka dengan benar
if not cap.isOpened():
    print("Tidak dapat membuka kamera")
    exit()

while True:
    # Ambil frame dari kamera
    ret, frame = cap.read()

    # Jika frame tidak diambil dengan benar, keluar dari loop
    if not ret:
        print("Tidak dapat menerima frame")
        break

    # Tampilkan frame
    cv2.imshow('Kamera', frame)

    # Tekan 'q' pada keyboard untuk keluar dari loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lepaskan kamera dan tutup semua jendela ketika selesai
cap.release()
cv2.destroyAllWindows()
