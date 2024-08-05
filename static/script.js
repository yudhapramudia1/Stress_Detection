import { initializeApp } from "https://www.gstatic.com/firebasejs/10.4.0/firebase-app.js";
import { getDatabase, ref, set} from "https://www.gstatic.com/firebasejs/10.4.0/firebase-database.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyBOWPF1E9kyoAhKloR2P1zebVI8gSznrVY",
    authDomain: "stres-detection.firebaseapp.com",
    databaseURL: "https://stres-detection-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "stres-detection",
    storageBucket: "stres-detection.appspot.com",
    messagingSenderId: "1056999288449",
    appId: "1:1056999288449:web:6851a290db55a6e7256780"
  };

// Initialize Firebase
// Initialize Firebase
const app = initializeApp(firebaseConfig);

const db = getDatabase();

document.addEventListener("DOMContentLoaded", function() {
    const hitung = document.querySelector(".container");
    const hasil_hitung_tidak_normal = document.querySelector(".container1");
    const hasil_hitung_normal = document.querySelector(".container2");

    
    //tidak dibawah 300
    var input1 = document.getElementById("input1");
    var BPM = document.getElementById("input2");
    var SPO2 = document.getElementById("input3");

    document.getElementById("tombol-home").addEventListener("click", function() {
        hitung.style.display = "grid";
        hasil_hitung_normal.style.display = "none";
        hasil_hitung_tidak_normal.style.display = "none";
    })

    document.getElementById("detect").addEventListener("click", function(){
        // mendefinisikan data dari input
        // BPM
        var nilaiBPM = document.getElementById("input2").value;
        //SPO2
        var nilaiSPO2 = document.getElementById("input3").value;
        //SUHU
        var nilaisuhu = document.getElementById("suhu").innerHTML;
        //Tekanan Darah
        var dataToSend1 = document.getElementById("input1").value;
        // konduktansi kulit
        var nilai_gsr = document.getElementById("gsr").innerHTML;
    
        //Cek apakah semua input telah dimasukkan
        if (input1.value !== "" && BPM.value !== "" && SPO2.value !== "") {
            
            input1.value = "";
            BPM.value = "";
            SPO2.value = "";
    
            var inputInt1 = parseInt(nilaiBPM);
            var inputInt2 = parseInt(nilaiSPO2);
            var inputInt3 = parseInt(nilaisuhu);
            var inputInt4 = parseInt(dataToSend1);
            var inputInt5 = parseInt(nilai_gsr);
            var inputInt6 = 1;
    
            var dataToSend = {
                    data1 : inputInt1,
                    data2: inputInt2,
                    data3: inputInt3,
                    data4: inputInt4,
                    data5: inputInt5,
                    data6: inputInt6
                };
            // memeriksa apakah konversi berhasil    
            if (!isNaN(inputInt1 && inputInt2 && inputInt3 && inputInt4 && inputInt5)){
                fetch('/api/data', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(dataToSend)
                })
                .then(response => response.json())
                .then(data => {
                    setTimeout(function() {
                        console.log(data.hasil1);
                        var hasilElement1 = document.getElementById("hasil1");
                        var hasilElement2 = document.getElementById("hasil2");
                        if (data.hasil2) {
                            hitung.style.display = "none";
                            hasil_hitung_tidak_normal.style.display = "grid";
                            hasil_hitung_normal.style.display = "none";
                            hasilElement1.innerHTML = data.hasil1 + "%";
                            set(ref(db, 'Fisiologi/Fisiologi_1'), data.hasil1)
                            .then(() => {
                              console.log('Data Fisiologi berhasil diperbarui');
                            })
                            .catch((error) => {
                              console.error('Gagal memperbarui data Fisiologi:', error);
                            });
                            
                            
                        } else {
                            hitung.style.display = "none";
                            hasil_hitung_normal.style.display = "grid";
                            hasil_hitung_tidak_normal.style.display = "none";
                            hasilElement2.innerHTML = data.hasil1 + "%";
                            set(ref(db, 'Fisiologi/Fisiologi_1'), data.hasil1)
                            .then(() => {
                              console.log('Data Fisiologi berhasil diperbarui');
                            })
                            .catch((error) => {
                              console.error('Gagal memperbarui data Fisiologi:', error);
                            });
                            
                        }
                    }, ); // Waktu ditulis dalam milidetik (10 detik)
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
            } else {
                alert("masukkan data yang valid (bilangan bulat)");
            }
        } else {
            alert("Silakan isi semua input sebelum menekan tombol.");
        }
    });

    document.getElementById("detect-accurate").addEventListener("click", function(){
        // mendefinisikan data dari input
        // BPM
        var nilaiBPM = document.getElementById("input2").value;
        //SPO2
        var nilaiSPO2 = document.getElementById("input3").value;
        //SUHU
        var nilaisuhu = document.getElementById("suhu").innerHTML;
        //Tekanan Darah
        var dataToSend1 = document.getElementById("input1").value;
        // konduktansi kulit
        var nilai_gsr = document.getElementById("gsr").innerHTML;
    
        //Cek apakah semua input telah dimasukkan
        if (input1.value !== "" && BPM.value !== "" && SPO2.value !== "") {
            
            input1.value = "";
            BPM.value = "";
            SPO2.value = "";
    
            var inputInt1 = parseInt(nilaiBPM);
            var inputInt2 = parseInt(nilaiSPO2);
            var inputInt3 = parseInt(nilaisuhu);
            var inputInt4 = parseInt(dataToSend1);
            var inputInt5 = parseInt(nilai_gsr);
            var inputInt6 = 2;
    
            var dataToSend = {
                    data1 : inputInt1,
                    data2: inputInt2,
                    data3: inputInt3,
                    data4: inputInt4,
                    data5: inputInt5,
                    data6: inputInt6
                };
            // memeriksa apakah konversi berhasil    
            if (!isNaN(inputInt1 && inputInt2 && inputInt3 && inputInt4 && inputInt5)){
                fetch('/api/data', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(dataToSend)
                })
                .then(response => response.json())
                .then(data => {
                    setTimeout(function() {
                        console.log(data.hasil1);
                        var hasilElement1 = document.getElementById("hasil1");
                        var hasilElement2 = document.getElementById("hasil2");
                        if (data.hasil2) {
                            hitung.style.display = "none";
                            hasil_hitung_tidak_normal.style.display = "grid";
                            hasil_hitung_normal.style.display = "none";
                            hasilElement1.innerHTML = data.hasil1 + "%";
                            set(ref(db, 'Fisiologi/Fisiologi_1'), data.hasil1)
                            .then(() => {
                              console.log('Data Fisiologi berhasil diperbarui');
                            })
                            .catch((error) => {
                              console.error('Gagal memperbarui data Fisiologi:', error);
                            });
                            
                            
                        } else {
                            hitung.style.display = "none";
                            hasil_hitung_normal.style.display = "grid";
                            hasil_hitung_tidak_normal.style.display = "none";
                            hasilElement2.innerHTML = data.hasil1 + "%";
                            set(ref(db, 'Fisiologi/Fisiologi_1'), data.hasil1)
                            .then(() => {
                              console.log('Data Fisiologi berhasil diperbarui');
                            })
                            .catch((error) => {
                              console.error('Gagal memperbarui data Fisiologi:', error);
                            });
                            
                        }
                    }, ); // Waktu ditulis dalam milidetik (10 detik)
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
            } else {
                alert("masukkan data yang valid (bilangan bulat)");
            }
        } else {
            alert("Silakan isi semua input sebelum menekan tombol.");
        }
    });

})