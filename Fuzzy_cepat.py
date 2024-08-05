import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np

def model_fuzzy(suhu, konduktansi, detak, tekanan, Saturasi_oksigen):
  # Input variables
  suhu_tubuh = ctrl.Antecedent(np.arange(0, 60, 1), 'Suhu_Tubuh')
  konduktansi_kulit = ctrl.Antecedent(np.arange(0, 10, 1), 'Konduktansi_Kulit')
  detak_jantung = ctrl.Antecedent(np.arange(60, 200, 1), 'Detak_Jantung')
  tekanan_darah = ctrl.Antecedent(np.arange(100, 200, 1), 'Tekanan_Darah')
  spo2 = ctrl.Antecedent(np.arange(0, 100, 0.5), 'SpO2')

  # Output variable
  output1 = ctrl.Consequent(np.arange(0, 100, 1), 'output1')

  # Membership functions for input variables
  suhu_tubuh['SuhuTidakNormal'] = fuzz.trapmf(suhu_tubuh.universe, [0, 30, 30, 33])
  suhu_tubuh['SuhuNormal'] = fuzz.trapmf(suhu_tubuh.universe, [30, 34, 56, 60])

  konduktansi_kulit['KonduktansiNormal'] = fuzz.trapmf(konduktansi_kulit.universe, [0, 2, 5, 7])
  konduktansi_kulit['KonduktansiTidakNormal'] = fuzz.trapmf(konduktansi_kulit.universe, [6, 8, 9, 10])

  detak_jantung['DetakNormal'] = fuzz.trapmf(detak_jantung.universe, [60, 70, 80, 90])
  detak_jantung['DetakTidakNormal'] = fuzz.trapmf(detak_jantung.universe, [85, 100, 185, 200])

  tekanan_darah['TekananNormal'] = fuzz.trapmf(tekanan_darah.universe, [100, 105, 105, 130])
  tekanan_darah['TekananTidakNormal'] = fuzz.trapmf(tekanan_darah.universe, [125, 140, 150, 200])

  spo2['Spo2TidakNormal'] = fuzz.trapmf(spo2.universe, [0, 25, 70, 95])
  spo2['Spo2Normal'] = fuzz.trapmf(spo2.universe, [93, 97.5, 98, 100])

  # Membership functions for output variable
  output1['Normal'] = fuzz.trapmf(output1.universe, [0, 25, 25, 50])
  output1['TidakNormal'] = fuzz.trapmf(output1.universe, [48, 75, 75, 100])

  # Rule definition
  rule1 = ctrl.Rule(suhu_tubuh['SuhuTidakNormal'] & konduktansi_kulit['KonduktansiTidakNormal'] & detak_jantung['DetakTidakNormal'] & tekanan_darah['TekananTidakNormal'] & spo2['Spo2TidakNormal'], output1['TidakNormal'])
  rule2 = ctrl.Rule(suhu_tubuh['SuhuTidakNormal'] & konduktansi_kulit['KonduktansiTidakNormal'] & detak_jantung['DetakTidakNormal'] & tekanan_darah['TekananTidakNormal'] & spo2['Spo2Normal'], output1['TidakNormal'])
  rule3 = ctrl.Rule(suhu_tubuh['SuhuTidakNormal'] & konduktansi_kulit['KonduktansiTidakNormal'] & detak_jantung['DetakTidakNormal'] & tekanan_darah['TekananNormal'] & spo2['Spo2TidakNormal'], output1['TidakNormal'])
  rule4 = ctrl.Rule(suhu_tubuh['SuhuTidakNormal'] & konduktansi_kulit['KonduktansiTidakNormal'] & detak_jantung['DetakTidakNormal'] & tekanan_darah['TekananNormal'] & spo2['Spo2Normal'], output1['TidakNormal'])
  rule5 = ctrl.Rule(suhu_tubuh['SuhuTidakNormal'] & konduktansi_kulit['KonduktansiTidakNormal'] & detak_jantung['DetakNormal'] & tekanan_darah['TekananTidakNormal'] & spo2['Spo2TidakNormal'], output1['TidakNormal'])
  rule6 = ctrl.Rule(suhu_tubuh['SuhuTidakNormal'] & konduktansi_kulit['KonduktansiTidakNormal'] & detak_jantung['DetakNormal'] & tekanan_darah['TekananTidakNormal'] & spo2['Spo2Normal'], output1['TidakNormal'])
  rule7 = ctrl.Rule(suhu_tubuh['SuhuTidakNormal'] & konduktansi_kulit['KonduktansiTidakNormal'] & detak_jantung['DetakNormal'] & tekanan_darah['TekananNormal'] & spo2['Spo2TidakNormal'], output1['Normal'])
  rule8 = ctrl.Rule(suhu_tubuh['SuhuTidakNormal'] & konduktansi_kulit['KonduktansiTidakNormal'] & detak_jantung['DetakNormal'] & tekanan_darah['TekananNormal'] & spo2['Spo2Normal'], output1['Normal'])
  rule9 = ctrl.Rule(suhu_tubuh['SuhuTidakNormal'] & konduktansi_kulit['KonduktansiNormal'] & detak_jantung['DetakTidakNormal'] & tekanan_darah['TekananTidakNormal'] & spo2['Spo2TidakNormal'], output1['TidakNormal'])
  rule10 = ctrl.Rule(suhu_tubuh['SuhuTidakNormal'] & konduktansi_kulit['KonduktansiNormal'] & detak_jantung['DetakTidakNormal'] & tekanan_darah['TekananTidakNormal'] & spo2['Spo2Normal'], output1['TidakNormal'])
  rule11 = ctrl.Rule(suhu_tubuh['SuhuTidakNormal'] & konduktansi_kulit['KonduktansiNormal'] & detak_jantung['DetakTidakNormal'] & tekanan_darah['TekananNormal'] & spo2['Spo2TidakNormal'], output1['TidakNormal'])
  rule12 = ctrl.Rule(suhu_tubuh['SuhuTidakNormal'] & konduktansi_kulit['KonduktansiNormal'] & detak_jantung['DetakTidakNormal'] & tekanan_darah['TekananNormal'] & spo2['Spo2Normal'], output1['Normal'])
  rule13 = ctrl.Rule(suhu_tubuh['SuhuTidakNormal'] & konduktansi_kulit['KonduktansiNormal'] & detak_jantung['DetakNormal'] & tekanan_darah['TekananTidakNormal'] & spo2['Spo2TidakNormal'], output1['TidakNormal'])
  rule14 = ctrl.Rule(suhu_tubuh['SuhuTidakNormal'] & konduktansi_kulit['KonduktansiNormal'] & detak_jantung['DetakNormal'] & tekanan_darah['TekananTidakNormal'] & spo2['Spo2Normal'], output1['Normal'])
  rule15 = ctrl.Rule(suhu_tubuh['SuhuTidakNormal'] & konduktansi_kulit['KonduktansiNormal'] & detak_jantung['DetakNormal'] & tekanan_darah['TekananNormal'] & spo2['Spo2TidakNormal'], output1['Normal'])
  rule16 = ctrl.Rule(suhu_tubuh['SuhuTidakNormal'] & konduktansi_kulit['KonduktansiNormal'] & detak_jantung['DetakNormal'] & tekanan_darah['TekananNormal'] & spo2['Spo2Normal'], output1['Normal'])
  rule17 = ctrl.Rule(suhu_tubuh['SuhuNormal'] & konduktansi_kulit['KonduktansiTidakNormal'] & detak_jantung['DetakTidakNormal'] & tekanan_darah['TekananTidakNormal'] & spo2['Spo2TidakNormal'], output1['TidakNormal'])
  rule18 = ctrl.Rule(suhu_tubuh['SuhuNormal'] & konduktansi_kulit['KonduktansiTidakNormal'] & detak_jantung['DetakTidakNormal'] & tekanan_darah['TekananTidakNormal'] & spo2['Spo2Normal'], output1['TidakNormal'])
  rule19 = ctrl.Rule(suhu_tubuh['SuhuNormal'] & konduktansi_kulit['KonduktansiTidakNormal'] & detak_jantung['DetakTidakNormal'] & tekanan_darah['TekananNormal'] & spo2['Spo2TidakNormal'], output1['TidakNormal'])
  rule20 = ctrl.Rule(suhu_tubuh['SuhuNormal'] & konduktansi_kulit['KonduktansiTidakNormal'] & detak_jantung['DetakTidakNormal'] & tekanan_darah['TekananNormal'] & spo2['Spo2Normal'], output1['Normal'])
  rule21 = ctrl.Rule(suhu_tubuh['SuhuNormal'] & konduktansi_kulit['KonduktansiTidakNormal'] & detak_jantung['DetakNormal'] & tekanan_darah['TekananTidakNormal'] & spo2['Spo2TidakNormal'], output1['TidakNormal'])
  rule22 = ctrl.Rule(suhu_tubuh['SuhuNormal'] & konduktansi_kulit['KonduktansiTidakNormal'] & detak_jantung['DetakNormal'] & tekanan_darah['TekananTidakNormal'] & spo2['Spo2Normal'], output1['Normal'])
  rule23 = ctrl.Rule(suhu_tubuh['SuhuNormal'] & konduktansi_kulit['KonduktansiTidakNormal'] & detak_jantung['DetakNormal'] & tekanan_darah['TekananNormal'] & spo2['Spo2TidakNormal'], output1['Normal'])
  rule24 = ctrl.Rule(suhu_tubuh['SuhuNormal'] & konduktansi_kulit['KonduktansiTidakNormal'] & detak_jantung['DetakNormal'] & tekanan_darah['TekananNormal'] & spo2['Spo2Normal'], output1['Normal'])
  rule25 = ctrl.Rule(suhu_tubuh['SuhuNormal'] & konduktansi_kulit['KonduktansiNormal'] & detak_jantung['DetakTidakNormal'] & tekanan_darah['TekananTidakNormal'] & spo2['Spo2TidakNormal'], output1['TidakNormal'])
  rule26 = ctrl.Rule(suhu_tubuh['SuhuNormal'] & konduktansi_kulit['KonduktansiNormal'] & detak_jantung['DetakTidakNormal'] & tekanan_darah['TekananTidakNormal'] & spo2['Spo2Normal'], output1['Normal'])
  rule27 = ctrl.Rule(suhu_tubuh['SuhuNormal'] & konduktansi_kulit['KonduktansiNormal'] & detak_jantung['DetakTidakNormal'] & tekanan_darah['TekananNormal'] & spo2['Spo2TidakNormal'], output1['Normal'])
  rule28 = ctrl.Rule(suhu_tubuh['SuhuNormal'] & konduktansi_kulit['KonduktansiNormal'] & detak_jantung['DetakTidakNormal'] & tekanan_darah['TekananNormal'] & spo2['Spo2Normal'], output1['Normal'])
  rule29 = ctrl.Rule(suhu_tubuh['SuhuNormal'] & konduktansi_kulit['KonduktansiNormal'] & detak_jantung['DetakNormal'] & tekanan_darah['TekananTidakNormal'] & spo2['Spo2TidakNormal'], output1['Normal'])
  rule30 = ctrl.Rule(suhu_tubuh['SuhuNormal'] & konduktansi_kulit['KonduktansiNormal'] & detak_jantung['DetakNormal'] & tekanan_darah['TekananTidakNormal'] & spo2['Spo2Normal'], output1['Normal'])
  rule31 = ctrl.Rule(suhu_tubuh['SuhuNormal'] & konduktansi_kulit['KonduktansiNormal'] & detak_jantung['DetakNormal'] & tekanan_darah['TekananNormal'] & spo2['Spo2TidakNormal'], output1['Normal'])
  rule32 = ctrl.Rule(suhu_tubuh['SuhuNormal'] & konduktansi_kulit['KonduktansiNormal'] & detak_jantung['DetakNormal'] & tekanan_darah['TekananNormal'] & spo2['Spo2Normal'], output1['Normal'])


  
  # Control System
  stres_detection_ctrl = ctrl.ControlSystem([
      rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32])
  stres_detection_sim = ctrl.ControlSystemSimulation(stres_detection_ctrl)

  # Example Input Values
  stres_detection_sim.input['Suhu_Tubuh'] = suhu
  stres_detection_sim.input['Konduktansi_Kulit'] = konduktansi
  stres_detection_sim.input['Detak_Jantung'] = detak
  stres_detection_sim.input['Tekanan_Darah'] = tekanan
  stres_detection_sim.input['SpO2'] = Saturasi_oksigen

  # Compute
  stres_detection_sim.compute()

  # # Output
  # print(stres_detection_sim.output['output1'])

  result = stres_detection_sim.output['output1']
  return result
  

