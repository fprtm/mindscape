---
title: "2026-08-28-aku-membuat-ai-dari-nol."
source: "https://www.youtube.com/watch?v=WLmY9icEOQk"
author:
  - "[[Fajrul Fx]]"
published: 2025-05-28
created: 2026-08-28
description: "Cobain Dreamina AI di sini: https://bit.ly/fajrulfxmay. Gratis!Di video ini kita akan membuat AI dari nol, dari konsep dasar neuron, perhitungan matematika, sampai implementasinya di coding. Enjoy!"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=WLmY9icEOQk)

Cobain Dreamina AI di sini: https://bit.ly/fajrulfxmay. Gratis!  
Di video ini kita akan membuat AI dari nol, dari konsep dasar neuron, perhitungan matematika, sampai implementasinya di coding. Enjoy!  
  
Source code: https://github.com/fajrulfx/neural\_network  
  
#Dreamina #CapCut #ai #aitools #texttoimage #AIimagegenerator

## Transcript

**0:00** · AI, AI, AI dan AI. AI sekarang ada di mana-mana. Kita mau cari informasi.

**0:07** · Sekali klik pakai AI udah langsung dapat. Hampir semua aplikasi sekarang pun udah punya fitur integrasi AI dan kemudian kita mau bikin gambar pun pakai AI. sekali klik juga udah jadi. AI sekarang sangat-sangat mudah untuk diakses dan karena saking mudahnya untuk diakses, banyak orang yang kemudian enggak sadar terkait dengan proses panjang di balik pengembangan AI ini.

**0:30** · Dianggapnya mungkin sekali klik langsung komputernya tiba-tiba otomatis langsung bisa menghasilkannya. Padahal di balik itu ada sebuah proses yang sangat-sangat kompleks. Ada magic-nya di situ. Nah, di sini biar kita bisa lebih memahami dan mengagumi AI AE dan ini bukan cuman sekedar buw bukan cuman sekedar knowledge prom. Di sini kita akan membuat AI dari nol. Kita bahas mulai dari konsep matematikanya kemudian implementasinya di dalam coding, kemudian proses training-nya sampai kita dapat hasil akhirnya.

**1:01** · Kalau kalian pengin belajar lebih lanjut tentang topik ini, aku menyarankan kalian bisa nonton series videonya Tribuan Brown atau baca bukunya Neural Network and Deep Learning oleh Michael Nilson.

**1:13** · Videonya Tri Blue Brown ini luar biasa bagus ilustrasi-ilustrasinya dan di sini nanti pun aku juga akan pakai banyak beberapa ilustrasi-ilustrasi dari videonya. Kemudian untuk kodenya sendiri aku juga belajar dari bukunya Michael Nelson ini. Oke, sistem AI yang akan kita buat di sini adalah sebuah sistem untuk mendeteksi digit pada tulisan tangan.

**1:34** · Ini adalah sebuah contoh sistem AI yang sangat-sangat sederhana. Tapi sistem ini bisa memberi gambaran lengkap tentang cara kerja di balik AI. Untuk kita manusia melihat angka tulisan tangan adalah sebuah hal yang sangat-sangat mudah untuk dilakukan. Yang karena ini kita sampai enggak sadar bahwa ada sebuah keajaiban yang terjadi di sini.

**1:55** · Otak manusia memiliki jutaan sel neuron yang ketika kita melihat tulisan ini misalnya otak kita bisa memproses gambar yang dilihat dan kemudian mengartikannya sebagai angka dengan tanpa effort. Tapi kalau kita mencoba untuk menulis program komputer untuk memahami ini angka berapa, ini angka berapa, dan seterusnya, ini adalah sebuah proses yang sangat sangat sangat susah.

**2:17** · Misalnya kita bikin program komputer, dia ngecek nih piksel dari masing-masing gambar ini. Oh, kalau pikselnya di sini, di sini, di sini, di sini, maka dia angka 3. Tapi masalahnya untuk setiap tulisan tangan ini kan lokasi pikselnya bakal beda-beda semua kan. Maka program yang ditulis tadi enggak bisa bekerja lagi. Jadi intinya kita enggak bisa mendekati proses memahami angka ini pada komputer dengan program komputer konvensional.

**2:46** · Makanya di sini kita menggunakan program yang mencoba meniru proses yang terjadi di dalam otak kita. Makanya disebut sebagai artificial intelligence. Dan di sini kita menggunakan model neural network atau jaringan syaraf. By the way, video ini pembahasannya akan agak teknis karena kalau untuk pembahasan yang simpel-simpel itu udah banyak.

**3:06** · Silakan nonton ke sana, Teman-teman.

**3:07** · Sekarang kita bahas yang susah. Atau kalau kalian mau pakai AI secara simpel, sebenarnya enggak perlu paham ini semua juga sih. Kalian bisa sesimpel pakai tool-tool AI yang udah ada sekarang.

**3:18** · Salah satunya adalah Dreamina AI dari CapCut. Dreamina adalah sebuah tool generative AI dari CapCut yang bisa digunakan untuk membuat gambar ataupun video dengan hasil yang sangat-sangat bagus. Di video sebelumnya aku tidak sempat mention tentang Dreamina ini dan sekarang Dreamina udah punya update baru image model yang lebih bagus lagi, image 3.0 yang hasilnya bahkan jauh lebih luar biasa.

**3:43** · Ini adalah contoh hasil gambar dari model image 3.0 dari Dreamina yang jauh lebih realistis dan memiliki resolusi natif sampai 2K. Jadi, detail dan ukurannya bisa lebih besar. Biar lebih jelas, kita bisa langsung cobain aja. Misalnya aku pengin bikin foto Einstein di depan papan tulis, maka aku tinggal cukup nulis aja promnya di sini.

**4:05** · Ini promnya cukup simpel aja dan ini juga support bahasa Indonesia, Teman-teman. Kita pakai model 3.0 yang terbaru dan di sini kita bisa lihat hasilnya yang sangat-sangat bagus.

**4:17** · Tulisan E = MC^-nya pun ini jelas.

**4:21** · Sementara itu, ini perbandingan jika pakai model 2.0 hasilnya juga bagus, tapi model 3.0 ini hasilnya jauh lebih realistis, lebih natural, dan teksnya pun lebih tepat. Model 3.0 dari Dream Mina ini, ini canggih banget, Teman-teman. Dan ini penggunaannya juga sangat fleksibel ya. Misalnya kalian mau pakai buat ilustrasi presentasi, tambahan ilustrasi di video, dan lain sebagainya. Jadi, silakan langsung cobain sendiri aja teman-teman. Driminal linknya ada di deskripsi. ini gratis.

**4:50** · Jadi, langsung cobain aja. Oke, kita kembali lagi ke sistem AI yang akan kita buat. Pertama-tama sebelum kita buat sistem yang kompleks, kita perlu memahami dulu konsep dasar tiap sel neuron. Jadi, misal kita punya jaringan neuron seperti ini, ada tiga input dan ada satu output. Untuk memahaminya bayangkan kayak kita lagi mau ambil keputusan misal mau berangkat nongkrong atau tidak. Maka di sini ada beberapa aspek yang perlu kita perhatikan untuk mengambil keputusan ini. Misalnya, apakah cuacanya cerah?

**5:22** · Apakah teman dekat kamu datang? Apakah jarak tempatnya dekat? Tapi masing-masing pertimbangan ini nilainya enggak sama.

**5:31** · Mereka punya bobotnya masing-masing.

**5:33** · Misalnya cuaca bobotnya tiga, teman dekat datang bobotnya satu, jarak tempatnya dua. Terus batas untuk kita dapat kesimpulan adalah empat misalnya.

**5:42** · Jadi misalkan cuacanya cerah dan teman dekatmu datang, meskipun jaraknya jauh kamu masih tetap datang. Sementara itu, kalau teman dekatmu datang, jarak tempatnya oke, tapi cuacanya buruk, hasilnya kamu tetap enggak datang. Nah, dalam konsep neuron, angka-angka bobot ini disebutnya sebagai weight. Adapun untuk nilai batasnya disebutnya sebagai bias, weight dan bias. Dan secara matematis hubungannya ditulis seperti ini.

**6:10** · Nilai ini kemudian dinormalisasikan dengan fungsi sigmoid sehingga hasil akhirnya nanti adalah angka antara 0 sampai 1.0 artinya adalah neuronnya tidak aktif. 1 adalah neuronnya sangat aktif dan nanti nilainya bisa di antara keduanya ini. Dengan hanya satu sistem neuron, maka secara praktis enggak banyak yang bisa dilakukan. Makanya dalam praktiknya neural network ini nanti neuronnya akan ada sangat sangat sangat banyak. parameternya pun nanti enggak cuman tiga aja, tapi bisa sampai ratusan bahkan ribuan sampai jutaan.

**6:44** · Kemudian jumlah neuronnya juga ada sangat-sangat banyak sampai berlayer-layer yang jumlah neuron yang makin banyak ini nanti akan membuat sistem ini memiliki sifat yang lebih kompleks sesuai dengan apa yang kita inginkan. Misalkan kita mau memproses gambar tulisan tangan 28 \* 28 piksel, maka di sini jumlah total inputnya adalah 28 \* 28, yaitu 784 input.

**7:08** · Misalnya dari 784 input ini kemudian diproses di layar pertama ada 16 neuron, kemudian di layar kedua ada 16 neuron lagi. Dan hasil akhirnya di sini adalah 10 neuron. Yang ini menunjukkan ketika diaktif ini menunjukkan ini digit berapa.

**7:28** · Misalnya di sini kita coba aja kita tulis saja angka dan dari sini kita lihat dari input di awal dia masuk ke layer pertama. Di layer pertama nanti akan ada beberapa neuron yang aktif.

**7:40** · Kemudian hasilnya nanti lanjut lagi ke layer kedua. Beberapa ada yang aktif lagi ada yang tidak. Sampai di layar yang terakhir kita dapat hasil akhirnya neuron yang aktif yang mana dan itu adalah digit angkanya. Dari hubungan-hubungan sebanyak ini kalau kita total maka jumlah parameternya ini ada banyak banget. Misalnya dari input ke layer pertama masing-masing di sini ada 784 \* 16 neuron berarti 784 \* 16. Layar 1 ke layer 2 16 \* 16. Layer 2 ke layer output 16 \* 10.

**8:13** · Totalnya ada 12.960 koneksi nilai wave. Dan kemudian di masing-masing neuronnya ini mereka memiliki nilai biaya sehingga totalnya kita memiliki sebanyak 13.002 parameter untuk sistem ini. Nah, parameter-parameter ini nilainya nanti perlu disesuaikan agar dia bisa mendeteksi digit seperti yang kita inginkan.

**8:39** · Untuk proses perhitungannya sendiri, jadi untuk masing-masing neuron ini dan koneksinya kita perlu menghitung hasil perhitungan dari semua koneksi yang dia punya. Tentu dari parameter sebanyak ini kalau kita nulisnya manual ini bakal sangat-sangat capek ya, Teman-teman. Makanya notasi ini kemudian disederhanakan menjadi seperti ini. Mungkin sampai sini bakal ada yang tanya kenapa kok di sini ada beberapa layer neuron? Pertanyaan bagus.

**9:06** · Jawabannya adalah agar hasil pemprosesannya lebih tepat. Dengan hanya satu layer saja maka pola dan hasil yang bisa dikenali ini sangat-sangat terbatas. Sementara itu dengan menambah layer kita bisa membuat sistem ini memahami pola yang jauh lebih kompleks lagi. Kita bisa membayangkannya gini.

**9:24** · Pada sistem digit detection ini misalnya di layar pertama ini berfungsi untuk mendeteksi garis-garis pada digit. Nilai weight dan bias-nya diatur sedemikian rupa sehingga neuronnya akan aktif ketika ada input di bagian tertentu.

**9:38** · Kemudian di layer kedua dia akan memahami pola yang terbentuk dan di layer ketiga ditentukan hasil angkanya.

**9:45** · Berapa jumlah layer yang dibutuhkan, berapa neuron pada tiap layer? Ini akan jadi topik pembahasan tersendiri terkait dengan optimasi sistem neural network-nya. Tapi intinya makin banyak neural network-nya, makin banyak titik-titik dan jaringan koneksinya, maka dia bisa memberikan hasil yang lebih kompleks. Kalau kita implementasikan di coding, kita bisa menulisnya seperti ini. Kita memulai dengan mendefinisikan sebuah kelas bernama network yang nantinya akan menyimpan semua informasi terkait dengan jaringan neuron ini.

**10:14** · Di sini kita mendefinisikan ukuran dari jaringan neuronnya, berapa jumlah layernya, kemudian untuk nilai bias dan weight-nya. Di sini kita mulai dengan nilai random terlebih dahulu. Kemudian kita perlu cara untuk menghitung nilai perkalian antara semua nilai input pada koneksi ini dengan weight-nya masing-masing yang tadi kita tulis dalam formula ini. Di sini kita tulis seperti ini. Dengan sigmoid adalah sebuah fungsi untuk menormalisasikan hasilnya. Nah, sebenarnya dari kode ini sampai sini kita sudah bisa melakukan sebuah proses perhitungan.

**10:46** · Kita bisa masukin nilai input. Kemudian inputnya ini nanti dikalikan dengan semua weight dan bias-nya sampai kita dapat hasil akhirnya. Tapi sayangnya sistem ini masih sangat sangat sangat bodoh karena nilai weight dan bias-nya belum disesuaikan. Makanya kita masuk ke tahap selanjutnya yaitu proses training. Untuk melakukan training di sini kita akan menggunakan amnis dataset.

**11:08** · Mnis data set ini isinya adalah gambar angka tulisan tangan ukuran 28 \* 28 piksel beserta informasi angkanya yang benar yang jumlahnya ada 60.000 data. Jadi dalam proses trainingnya yang perlu dilakukan adalah seperti ini. Kita perlu memasukkan input datanya lalu membiarkan neural network ini melakukan perhitungan dan memberikan hasilnya. Dan hasil yang diberikan ini kemudian dibandingkan dengan hasil yang seharusnya.

**11:37** · Dan di awal-awal bisa dipastikan bahwa hasil yang diberikan oleh sistem ini pasti sangat-sangat jelek. Makanya di sini parameter weight dan bias-nya untuk semua koneksi dan neuronnya perlu diperbaiki. Caranya gimana? Ya tinggal kita lihat aja perbedaan nilai akhirnya atau yang disebut sebagai cost function.

**11:56** · Jadi untuk ngecek seberapa jauh perbedaannya, kita hitung perbedaan masing-masing nilainya dikuadratkan di rata-rata atau weight thated su square atau secara matematis ditulis sebagai berikut. Untuk meminimalisir nilai cos function ini, perbedaan antara hasil akhir dan hasil yang diinginkan, maka kita perlu menghitung nilai turunannya.

**12:18** · Ini pelajaran kalkulus SMA ya. 2/n-nya ini hanya nilai skala aja, nilainya konstan. Enggak penting-penting banget di sini. Jadi kita lupakan aja. Jadi hasil akhirnya kita perlu menghitung nilai ini. Kita hitung perbedaan antara hasil dan nilai yang seharusnya. Agar nilai cost function-nya ini menjadi semakin kecil pada masing-masing weight dan bias ini perlu diubah seperti apa sih di sini? Kemudian kita masuk ke proses back propagation.

**12:46** · Intinya back propagation ini akan ngecek untuk masing-masing parameter ini mereka perlu diubah seperti apa agar hasil akhirnya lebih mendekati nilai yang tepat. Back propagation ini bisa dibilang adalah inti dari neural network. Dan makanya untuk back propagation ini sebenarnya topiknya jauh lebih kompleks ya, Teman-teman. Ada banyak parameter yang bisa disesuaikan tapi untuk di video ini kita cukupkan untuk sampai sini saja.

**13:12** · Dan ya, setelah kita tahu pada masing-masing parameter weight and bias ini perlu diubah seperti apa, ya sudah implementasi selanjutnya tinggal diubah aja nilainya sampai kemudian cost function-nya menjadi semakin semakin semakin kecil yang artinya sistem neural network ini bisa menjadi semakin akurat.

**13:30** · Di dalam kode kita mengimplementasikannya seperti ini.

**13:33** · Menghitung nilai cost derivatif, nilai back propagation, kemudian kita update parameternya.

**13:39** · Sampai sini semua keperluan yang dibutuhkan udah terpenuhi, kodenya udah ada semua. Maka kita langsung masuk ke proses training. Untuk memulai proses training di sini kita memulai dengan mendefinisikan dulu bentuk jaringannya.

**13:52** · Di sini kita punya misalnya 784 16 10.

**13:56** · Kemudian data set-nya kita buka dan ya kita langsung panggil aja metode function untuk melakukan proses training seperti ini. Di sini pun ada beberapa parameter training yang bisa kita masukkan dan ya di sini proses training-nya udah mulai berjalan. Ini EPCH ini nunjukin pengulangan proses training-nya dan dari sini hanya dalam beberapa percobaan aja kita sudah dapat nilai akurasi yang cukup tinggi. Artinya sistem neural network yang baru aja kita bangun dan kita training ini dia udah berhasil mendeteksi nilai digit dengan akurasi 95%.

**14:28** · Dia benar 95%-nya. Sekarang data hasil training-nya kita coba untuk tes. Di sini aku bikin sebuah program sederhana untuk aku bisa nulis digit. Kemudian dia akan ngecek hasilnya dan juga menunjukkan distribusi nilai neuron pada layer output. Misal nulis angka 3, kita cek digit dan kita pun dapat hasilnya, Teman-teman. Benar. Nulis angka 8. Kita cek benar lagi hasilnya.

**14:55** · Di sini pun kita bisa melihat nilai distribusi aktivasi neuron output-nya yang mana kadang ada yang nilai output-nya hanya ada di satu angka aja. Tapi ada juga misalnya angkanya ini agak enggak jelas di sini neuronnya kesulitan dia mendeteksinya. Makanya ada beberapa nilai yang aktif bahkan ada juga yang dia ngacau seperti ini. Yang pasti ini hasilnya udah bagus banget loh dengan kode sesedikit ini, sesimpel ini.

**15:25** · Kemudian waktu trainingnya juga sangat-sangat sebentar. Enggak ada 5 menit by the way ini tadi. Tapi hasilnya udah sangat-sangat bagus. Dan ya di sini kita sudah berhasil untuk membuat sistem AI untuk mendeteksi nilai digit pada tulisan tangan. Well, ini masih dasar banget sebenarnya. Di sini pun tadi ada beberapa detail yang masih aku skip misalnya kayak back propagation, kemudian gradien desain dan lain sebagainya. Silakan itu nanti kalian ulik sendiri. Kalau kalian pengin belajar lebih lanjut silakan tonton seriesnya Tri Blue and Brown atau bukunya Michael Nilson.

**15:59** · Dan aku ingatkan teman-teman kalau kalian pengin belajar tentang AI yang seperti ini yang real AI ya, bukan hanya sekedar cara menggunakan AI. Di sini kalian seenggaknya minimal harus lebih familiar sama notasi-notasi matematika.

**16:13** · Dan itu dulu saja teman-teman untuk video kali ini. Kalau kalian ada tambahan, ada pertanyaan, silakan tulis saja di kolom komentar. Kita ketemu di video selanjutnya. Terima kasih. Yeah.