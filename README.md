# Assignment 2 - UNI415 Tim Tujuh
Kode sederhana esp32 melakukan collect data sensor dan mengirim ke dashboard ubidots [Dashboard](https://stem.ubidots.com/app/dashboards/public/dashboard/lvaP28Nk53BCHKAnCaAvYak4ZQhuH_SsENEs8u3-PTM?navbar=true&contextbar=true&datePicker=true&devicePicker=true&displayTitle=true) dan mongodb atlas.

## Tutorial running kode :
- Pastikan laptop dan esp32 berada di jaringan internet yang sama
- Ubah bagian ini di esp32.py menjadi ip laptop Anda :
> SERVER_URL =  "http://172.90.1.26:5000/sensor"
- Pastikan sudah melakukan install depedensi berikut :
> pip install flask pymongo flask-cors
- Jalankan file **server.py**
> python server.py
- Jika berhasil akan menampilkan output
> Running on http://0.0.0.0:5000 (Press CTRL+C to quit)
- Jalankan esp32 setelah server.py berjalan