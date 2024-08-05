import { initializeApp } from "https://www.gstatic.com/firebasejs/10.4.0/firebase-app.js";
import { getDatabase, ref, onValue, set} from "https://www.gstatic.com/firebasejs/10.4.0/firebase-database.js";
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
// const dbRef = ref(db);

var fisiologi = document.getElementById("fisiologi");
var psikologi = document.getElementById("psikologi");

let Psikologi;

onValue(ref(db, 'Psikologi/Psikologi_1'), (snapshot) => {
    Psikologi = snapshot.val();
    psikologi.innerHTML = Psikologi;
});

let Fisiologi;

onValue(ref(db, 'Fisiologi/Fisiologi_1'), (snapshot) => {
    Fisiologi = snapshot.val();
    fisiologi.innerHTML = Fisiologi + "%";
});

document.getElementById("Reset").addEventListener("click", function(){
    set(ref(db, 'Psikologi/Psikologi_1'), 0)
    .then(() => {
        console.log('Data Psikologi berhasil diperbarui');
    })
    .catch((error) => {
        console.error('Gagal memperbarui data Psikologi:', error);
    });
    set(ref(db, 'Fisiologi/Fisiologi_1'), 0)
    .then(() => {
        console.log('Data Psikologi berhasil diperbarui');
    })
    .catch((error) => {
        console.error('Gagal memperbarui data Psikologi:', error);
    });
})

