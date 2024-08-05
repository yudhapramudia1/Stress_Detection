let totalScore = 0;
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
    document.getElementById("Submit").addEventListener("click", function(){

    // Mendapatkan nilai jawaban dari setiap soal
    const question1 = parseInt(document.querySelector('input[name="question1"]:checked').value);
    const question2 = parseInt(document.querySelector('input[name="question2"]:checked').value);
    const question3 = parseInt(document.querySelector('input[name="question3"]:checked').value);
    const question4 = parseInt(document.querySelector('input[name="question4"]:checked').value);
    const question5 = parseInt(document.querySelector('input[name="question5"]:checked').value);
    const question6 = parseInt(document.querySelector('input[name="question6"]:checked').value);
    const question7 = parseInt(document.querySelector('input[name="question7"]:checked').value);
    const question8 = parseInt(document.querySelector('input[name="question8"]:checked').value);
    const question9 = parseInt(document.querySelector('input[name="question9"]:checked').value);
    const question10 = parseInt(document.querySelector('input[name="question10"]:checked').value);

    // Menambahkan nilai jawaban dari setiap soal ke totalScore
    totalScore += question1;
    totalScore += question2;
    totalScore += question3;
    totalScore += question4;
    totalScore += question5;
    totalScore += question6;
    totalScore += question7;
    totalScore += question8;
    totalScore += question9;
    totalScore += question10;

    // Tampilkan hasil
    // alert("Total score: " + totalScore);

    // Simpan totalScore ke variabel di JavaScript untuk digunakan di mana pun diperlukan
    // Misalnya, Anda bisa menyimpannya ke database atau melakukan operasi lainnya
    // Di sini saya hanya menampilkan totalScore di console
    console.log(totalScore);
    set(ref(db, 'Psikologi/Psikologi_1'), totalScore)
    .then(() => {
        console.log('Data Psikologi berhasil diperbarui');
    })
    .catch((error) => {
        console.error('Gagal memperbarui data Psikologi:', error);
    });
    })
})