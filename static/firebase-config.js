import { initializeApp } from "https://www.gstatic.com/firebasejs/10.4.0/firebase-app.js";
import { getDatabase, ref, onValue} from "https://www.gstatic.com/firebasejs/10.4.0/firebase-database.js";
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

const db = getDatabase()
// const dbRef = ref(db);

let data_gsr;
//BPM 
onValue(ref(db, 'GSR/GSR_1'), (snapshot) => {
  data_gsr = snapshot.val();
  var tampil_GSR   = document.getElementById('gsr');
  tampil_GSR.innerHTML = data_gsr ;
});

let data_suhu
//Kadar SPO2
onValue(ref(db, 'SUHU/SUHU_1'), (snapshot) => {
  data_suhu = snapshot.val();
  var tampil_suhu   = document.getElementById('suhu');
  tampil_suhu.innerHTML = data_suhu;
});