# LAPORAN PRAKTIKUM PENGEMBANGAN APLIKASI WEB
## MODUL 1: PENGENALAN HTML (TINGKAT DASAR & LANJUT)

**Program Studi S1 Sistem Informasi - Telkom University Surabaya**  
**Tahun Akademik 2026**

---

### IDENTITAS MAHASISWA
* **Nama Mahasiswa:** [Nama Anda]
* **NIM:** [NIM Anda]
* **Kelas:** S1 Sistem Informasi
* **Mata Kuliah:** Praktikum Pengembangan Aplikasi Web (Modul 1)
* **Dosen Pengampu:** Purnama Anaking, S.Kom., M.Kom.

---

## BAB I: PENDAHULUAN

### 1.1 Latar Belakang
Hypertext Markup Language (HTML) merupakan bahasa markah standar yang digunakan untuk membuat dan menyusun struktur halaman web. Melalui HTML, pengembang dapat menyusun teks, tautan, berkas multimedia (gambar, audio, video), hingga formulir interaktif yang dapat dirender oleh peramban (browser). Penguasaan dasar-dasar HTML, mulai dari hierarki dokumen, elemen semantik modern (HTML5), hingga manajemen masukan pengguna melalui form, merupakan pondasi fundamental bagi mahasiswa Sistem Informasi dalam merancang dan mengembangkan aplikasi web yang terstandarisasi.

### 1.2 Tujuan Praktikum
1. Mahasiswa memahami struktur dasar sebuah dokumen HTML (`<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`).
2. Mahasiswa mampu menerapkan elemen dasar pemformatan teks, daftar berbutir (*list*), tautan (*link*), multimedia, dan tabel bersarang (*nested table*).
3. Mahasiswa mampu mengimplementasikan elemen Semantic HTML5 (`<header>`, `<nav>`, `<main>`, `<article>`, `<aside>`, `<footer>`) serta penyematan konten eksternal melalui `<iframe>`.
4. Mahasiswa mampu merancang antarmuka formulir data interaktif menggunakan `<fieldset>`, `<legend>`, `<input>`, `<select>`, dan `<textarea>`.
5. Mahasiswa mampu mempublikasikan halaman web ke platform hosting publik (GitHub Pages / Vercel).

---

## BAB II: DASAR TEORI

### 2.1 Perilaku Elemen: Block-Level vs Inline-Level
* **Block-level Element:** Elemen yang selalu diawali pada baris baru dan mengambil seluruh lebar horizontal yang tersedia pada kontainer induknya (contoh: `<div>`, `<p>`, `<h1>`–`<h6>`, `<table>`, `<form>`).
* **Inline-level Element:** Elemen yang hanya menggunakan lebar horizontal selebar konten yang dimilikinya dan tidak memulai baris baru (contoh: `<span>`, `<a>`, `<strong>`, `<em>`, `<img>`).

### 2.2 Tabel Bersarang (Nested Table)
Tabel bersarang (*nested table*) adalah teknik menempatkan elemen tabel di dalam sel (`<td>`) dari tabel lain. Teknik ini sangat berguna dalam menyusun tata letak berbasis baris dan kolom yang memiliki jumlah pembagian kolom berbeda di tiap barisnya tanpa terpengaruh oleh lebar kolom baris lainnya.

### 2.3 Semantic HTML5
HTML5 memperkenalkan elemen semantik yang memberikan arti kontekstual terhadap struktur halaman web. Tag semantik mempermudah pembacaan kode oleh pengembang, peramban, *screen reader* (aksesibilitas), serta mesin pencari (*Search Engine Optimization* / SEO). Tag utama mencakup:
* `<header>`: Bagian kepala dokumen atau navigasi.
* `<nav>`: Sekumpulan tautan navigasi utama.
* `<main>`: Wadah isi konten utama halaman.
* `<article>`: Bagian konten mandiri yang dapat didistribusikan secara terpisah (misal artikel berita).
* `<aside>`: Bagian pelengkap yang terkait secara tidak langsung dengan konten utama (sidebar).
* `<footer>`: Bagian kaki halaman yang berisi informasi hak cipta, kontak, atau tautan tambahan.

### 2.4 Elemen Form dan Kontrol Input
Formulir web dibangun dengan tag `<form>` dan diproteksi pengelompokannya menggunakan `<fieldset>` serta `<legend>`. Input dikontrol melalui berbagai atribut seperti `type` (`text`, `email`, `password`, `file`, `radio`, `checkbox`), atribut status (`readonly`, `disabled`, `required`), serta elemen masukan berskala seperti `<select>` dan `<textarea>`.

---

## BAB III: IMPLEMENTASI DAN PEMBAHASAN TUGAS

### 3.1 Tugas HTML Dasar: Halaman Profil Prodi Sistem Informasi (`tugas.html`)

#### A. Penjelasan Kode Program:
1. **Layout Utama:** Dibuat menggunakan bingkai tabel induk bergaris 1px (`border: 1px solid black; border-collapse: collapse;`) dengan font serif (`Times New Roman`).
2. **Header Navigasi:** Memuat logo prodi di sebelah kiri, menu navigasi 5 tombol (*Tentang Kami, Akademik, Dosen & Staf, Kerja Sama, Blog*) yang menggunakan *nested table* di bagian tengah, serta tautan *Admisi* di sebelah kanan.
3. **Hero Section:** Slogan *"Excellent in Connecting Systems"* berukuran heading 1 dengan teks penjelas sistem informasi di bawahnya.
4. **3 Kolom Peran Lulusan:** Menggunakan baris tabel bersarang dengan 3 kolom berukuran proporsional (masing-masing 33.33%) untuk mendeskripsikan peran *Project Manager*, *IS Engineer*, dan *Business & System Analyst*.
5. **Footer Informasi:** Terdiri atas 3 kolom informasi:
   - Kolom 1 (50%): Deskripsi sejarah berdirinya Program Studi Sistem Informasi ITTelkom Surabaya.
   - Kolom 2 (25%): Daftar tidak bernomor (`<ul>`) untuk Tautan Penting dan Tautan Bermanfaat.
   - Kolom 3 (25%): Info Kontak lengkap dan media sosial.
6. **Copyright:** Teks hak cipta *"Copyright © 2022 Information Systems - Build with ♥ by CODER Team"*.

#### B. Hasil Tampilan Browser:
![Output Tugas Dasar](assets/screenshots/output_tugas_dasar.png)
*Gambar 3.1: Tampilan Halaman tugas.html pada Browser (Port 5500)*

---

### 3.2 Tugas HTML Semantic: Blog Sistem Informasi (`semantic.html`)

#### A. Penjelasan Kode Program:
1. **`<header>`:** Menampung baris navigasi (logo prodi, menu bar, tautan admisi) serta judul blog *"Blog Sistem Informasi"*.
2. **`<nav>`:** Membungkus tabel menu navigasi internal.
3. **`<main>`:** Menampung isi utama halaman blog yang terbagi ke dalam 2 kolom:
   - **`<article>` (Kolom Kiri 73%):** Berisi judul artikel *"Dua Wisudawan Sistem Informasi Berhasil Meraih Predikat Cumlaude"*, tiga paragraf isi berita, serta sematan pemutar video YouTube melalui tag `<iframe>` dengan URL Dies Natalis ITTelkom Surabaya.
   - **`<aside>` (Kolom Kanan 27%):** Berisi bilah samping untuk artikel terkait, memuat blok *"Artikel Terbaru"* dan *"Artikel Terpopular"* yang dirancang menggunakan tag daftar `<ul>` dan tautan `<a>`.
4. **`<footer>`:** Menampung seluruh blok informasi profil prodi, tautan eksternal, alamat kontak, dan copyright.

#### B. Hasil Tampilan Browser:
![Output Tugas Semantic](assets/screenshots/output_semantic.png)
*Gambar 3.2: Tampilan Halaman semantic.html pada Browser (Port 5500)*

---

### 3.3 Tugas HTML Lanjut: Form Registrasi Mahasiswa (`form.html`)

#### A. Penjelasan Kode Program:
1. **`<form>`:** Menggunakan metode POST untuk pengiriman data formulir registrasi mahasiswa.
2. **`<fieldset>` Biodata:**
   - Nama Mahasiswa: `<input type="text">` dengan placeholder.
   - NIM: `<input type="text">` dengan nilai `123456789` dan atribut `readonly` (tidak dapat disunting).
   - Alamat: Elemen `<textarea>` multi-baris berukuran 6 baris x 45 kolom.
   - Tanggal Lahir: Tiga dropdown bersarang `<select>` untuk tanggal (01–31), bulan (Januari–Desember), dan tahun (1990–2005).
   - Jenis Kelamin: Pilihan eksklusif radio button (`name="jenis_kelamin"` bernilai Pria dan Wanita).
   - Upload Foto: Input berkas dokumen menggunakan `type="file"`.
   - URL Website & Perguruan Tinggi: Input teks URL dan teks nama kampus.
3. **`<fieldset>` Info Akun:** Mengelompokkan input Email (`type="email"`), Username (`type="text"`), Password (`type="password"`), dan Ulangi Password.
4. **`<fieldset>` Kemampuan Dasar:** Memuat pilihan multi-centang berbasis `<input type="checkbox">` untuk opsi bahasa pemrograman dan teknologi: HTML, CSS, Javascript, PHP, MySQL, Laravel, dan React Native.
5. **Tombol Aksi:** Tiga tombol di bagian bawah form:
   - `<input type="reset" value="Reset">`: Mengembalikan nilai form ke semula.
   - `<input type="submit" value="Simpan">`: Mengirim data form.
   - `<input type="button" value="Button">`: Tombol netral.

#### B. Hasil Tampilan Browser:
![Output Tugas Form](assets/screenshots/output_form.png)
*Gambar 3.3: Tampilan Halaman form.html pada Browser (Port 5500)*

---

### 3.4 Publikasi Halaman Web Secara Online
Sesuai ketentuan modul praktikum halaman 17, seluruh berkas HTML dan aset gambar dipublikasikan secara online agar dapat diakses publik oleh asisten lab / dosen:
* **Platform Hosting:** GitHub Pages
* **Domain URL Online:** `https://[username-anda].github.io/praktikum-paw-modul1/`
* **Cara Publikasi Singkat:**
  1. Buat repository publik di GitHub.
  2. Unggah seluruh file praktikum (`index.html`, `tugas.html`, `semantic.html`, `form.html`, dan folder `assets/`).
  3. Aktifkan fitur **Pages** pada menu **Settings** repository (pilih source: `Deploy from a branch` $\rightarrow$ branch `main` $\rightarrow$ folder `/root`).

---

## BAB IV: KESIMPULAN

1. HTML menyediakan struktur fundamental bagi aplikasi web yang mengatur representasi data visual dan interaksi dasar.
2. Penggunaan teknik *nested table* pada `tugas.html` terbukti efektif untuk menjaga proporsi kolom yang tetap konsisten dan seimbang antarbagian halaman.
3. Penerapan tag semantik HTML5 pada `semantic.html` menghasilkan struktur dokumen yang rapi, bermakna, ramah aksesibilitas, serta memudahkan integrasi media interaktif (`<iframe>`).
4. Penggunaan elemen form, `<fieldset>`, dan `<legend>` pada `form.html` memberikan hierarki pengelompokan masukan pengguna yang teratur, bersih, dan mudah digunakan.
