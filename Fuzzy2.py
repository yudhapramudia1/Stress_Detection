import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definisi variabel input
detak_jantung = ctrl.Antecedent(np.arange(50, 151, 1), 'detak_jantung')
tekanan_darah = ctrl.Antecedent(np.arange(80, 181, 1), 'tekanan_darah')
suhu_tubuh = ctrl.Antecedent(np.arange(30, 41, 1), 'suhu_tubuh')
konduktivitas_kulit = ctrl.Antecedent(np.arange(0, 11, 1), 'konduktivitas_kulit')
oksigen_darah = ctrl.Antecedent(np.arange(70, 101, 1), 'oksigen_darah')

# Definisi variabel output
stres = ctrl.Consequent(np.arange(0, 101, 1), 'stres')

# Menentukan fungsi keanggotaan untuk masing-masing variabel
detak_jantung['normal'] = fuzz.trimf(detak_jantung.universe, [60, 90, 100])
detak_jantung['tidak_normal'] = fuzz.trapmf(detak_jantung.universe, [100, 100, 150, 150])

tekanan_darah['normal'] = fuzz.trimf(tekanan_darah.universe, [100, 130, 150])
tekanan_darah['tidak_normal'] = fuzz.trapmf(tekanan_darah.universe, [130, 130, 180, 180])

suhu_tubuh['normal'] = fuzz.trimf(suhu_tubuh.universe, [33, 37, 40])
suhu_tubuh['tidak_normal'] = fuzz.trapmf(suhu_tubuh.universe, [30, 30, 33, 33])

konduktivitas_kulit['normal'] = fuzz.trimf(konduktivitas_kulit.universe, [2, 6, 10])
konduktivitas_kulit['tidak_normal'] = fuzz.trapmf(konduktivitas_kulit.universe, [6, 6, 10, 10])

oksigen_darah['normal'] = fuzz.trimf(oksigen_darah.universe, [95, 100, 100])
oksigen_darah['tidak_normal'] = fuzz.trimf(oksigen_darah.universe, [70, 95, 95])

stres['rendah'] = fuzz.trimf(stres.universe, [0, 30, 50])
stres['sedang'] = fuzz.trimf(stres.universe, [30, 50, 70])
stres['tinggi'] = fuzz.trimf(stres.universe, [50, 70, 100])

# Rule base
rule1 = ctrl.Rule(detak_jantung['normal'] & tekanan_darah['normal'] & suhu_tubuh['normal'] & konduktivitas_kulit['normal'] & oksigen_darah['normal'], stres['rendah'])
rule2 = ctrl.Rule(detak_jantung['tidak_normal'] | tekanan_darah['tidak_normal'] | suhu_tubuh['tidak_normal'] | konduktivitas_kulit['tidak_normal'] | oksigen_darah['tidak_normal'], stres['tinggi'])

# Mengatur rule base
stres_ctrl = ctrl.ControlSystem([rule1, rule2])
stres_detection_sim = ctrl.ControlSystemSimulation(stres_ctrl)

# Fungsi untuk mendeteksi stres
def model_fuzzy(detak_jantung_val, tekanan_darah_val, suhu_tubuh_val, konduktivitas_kulit_val, oksigen_darah_val):
    stres_detection_sim.input['detak_jantung'] = detak_jantung_val
    stres_detection_sim.input['tekanan_darah'] = tekanan_darah_val
    stres_detection_sim.input['suhu_tubuh'] = suhu_tubuh_val
    stres_detection_sim.input['konduktivitas_kulit'] = konduktivitas_kulit_val
    stres_detection_sim.input['oksigen_darah'] = oksigen_darah_val

    stres_detection_sim.compute()
    return stres_detection_sim.output['stres']

# # Contoh penggunaan
# hasil = round(model_fuzzy(40, 100, 21, 9, 90), 2)
# print("Tingkat stres:", hasil)
