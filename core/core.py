import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

"""
DECOMMENT THIS BLOCK WHEN EACH VAR GETS SET
range constants TBD for each variable
cfp_lo =
cfp_hi =
rec_lo =
rec_hi =
bdg_lo =
bdg_hi =
wtp_lo =
wtp_hi =
psi_lo = 0
psi_hi = 100
"""

cfp = ctrl.Antecedent(np.arrange(cfp_lo, cfp_hi, 1), 'carbon_footprint')
rec = ctrl.Antecedent(np.arrange(rec_lo, rec_hi, 1), 'recyclablilty')
bdg = ctrl.Antecedent(np.arrange(bdg_lo, bdg_hi, 1), 'biodegradability')
wtp = ctrl.Antecedent(np.arrange(wtp_lo, wtp_hi, 1), 'waste_treated_in_prod')

psi = ctrl.Consequent(np.arrange(psi_lo, psi_hi, 1), 'score')

# L = low, M = medium, H = high
#cfp[] = fuzz.trimf(cfp.universe, [])
cfp['L'] = fuzz.trimf(cfp.universe, [cfp_lo, cfp_lo, ])
cfp['M'] = fuzz.trimf(cfp.universe, [cfp_lo, , cfp_hi])
cfp['H'] = fuzz.trimf(cfp.universe, [, cfp_hi, cfp_hi])

#rec[] = fuzz.trimf(rec.universe, [])
rec['L'] = fuzz.trimf(rec.universe, [rec_lo, rec_lo, ])
rec['M'] = fuzz.trimf(rec.universe, [rec_lo, , rec_hi])
rec['H'] = fuzz.trimf(rec.universe, [ , rec_hi, rec_hi])

#bdg[] = fuzz.trimf(bdg.universe, [])
bdg['L'] = fuzz.trimf(bdg.universe, [bdg_lo, bdg_lo, ])
bdg['M'] = fuzz.trimf(bdg.universe, [bdg_lo, , bdg_hi])
bdg['H'] = fuzz.trimf(bdg.universe, [ , bdg_hi, bdg_hi])

#wtp[] = fuzz.trimf(wtp.universe, [])
wtp['L'] = fuzz.trimf(wtp.universe, [wtp_lo, wtp_lo, ])
wtp['M'] = fuzz.trimf(wtp.universe, [wtp_lo, , wtp_hi])
wtp['H'] = fuzz.trimf(wtp.universe, [ , wtp_hi, wtp_hi])

# B = bad, A = average, G = good, E = excellent
#psi[] = fuzz.trapmf(psi.universe, [])
psi['B'] = fuzz.trapmf(psi.universe, [])
psi['A'] = fuzz.trapmf(psi.universe, [])
psi['G'] = fuzz.trapmf(psi.universe, [])
psi['E'] = fuzz.trapmf(psi.universe, [])

#Rule Base
#ruleX = ctrl.Rule()
rules = [None] * 81
rules[0] = ctrl.Rule(rec['H'] & bdg['H'] & wtp['H'] & cfp['H'], psi[])
rules[1] = ctrl.Rule(rec['H'] & bdg['H'] & wtp['H'] & cfp['M'], psi[])
rules[2] = ctrl.Rule(rec['H'] & bdg['H'] & wtp['H'] & cfp['L'], psi[])
rules[3] = ctrl.Rule(rec['H'] & bdg['H'] & wtp['M'] & cfp['H'], psi[])
rules[4] = ctrl.Rule(rec['H'] & bdg['H'] & wtp['M'] & cfp['M'], psi[])
rules[5] = ctrl.Rule(rec['H'] & bdg['H'] & wtp['M'] & cfp['L'], psi[])
rules[6] = ctrl.Rule(rec['H'] & bdg['H'] & wtp['L'] & cfp['H'], psi[])
rules[7] = ctrl.Rule(rec['H'] & bdg['H'] & wtp['L'] & cfp['M'], psi[])
rules[8] = ctrl.Rule(rec['H'] & bdg['H'] & wtp['L'] & cfp['L'], psi[])
rules[9] = ctrl.Rule(rec['H'] & bdg['M'] & wtp['H'] & cfp['H'], psi[])
rules[10] = ctrl.Rule(rec['H'] & bdg['M'] & wtp['H'] & cfp['M'], psi[])
rules[11] = ctrl.Rule(rec['H'] & bdg['M'] & wtp['H'] & cfp['L'], psi[])
rules[12] = ctrl.Rule(rec['H'] & bdg['M'] & wtp['M'] & cfp['H'], psi[])
rules[13] = ctrl.Rule(rec['H'] & bdg['M'] & wtp['M'] & cfp['M'], psi[])
rules[14] = ctrl.Rule(rec['H'] & bdg['M'] & wtp['M'] & cfp['L'], psi[])
rules[15] = ctrl.Rule(rec['H'] & bdg['M'] & wtp['L'] & cfp['H'], psi[])
rules[16] = ctrl.Rule(rec['H'] & bdg['M'] & wtp['L'] & cfp['M'], psi[])
rules[17] = ctrl.Rule(rec['H'] & bdg['M'] & wtp['L'] & cfp['L'], psi[])
rules[18] = ctrl.Rule(rec['H'] & bdg['L'] & wtp['H'] & cfp['H'], psi[])
rules[19] = ctrl.Rule(rec['H'] & bdg['L'] & wtp['H'] & cfp['M'], psi[])
rules[20] = ctrl.Rule(rec['H'] & bdg['L'] & wtp['H'] & cfp['L'], psi[])
rules[21] = ctrl.Rule(rec['H'] & bdg['L'] & wtp['M'] & cfp['H'], psi[])
rules[22] = ctrl.Rule(rec['H'] & bdg['L'] & wtp['M'] & cfp['M'], psi[])
rules[23] = ctrl.Rule(rec['H'] & bdg['L'] & wtp['M'] & cfp['L'], psi[])
rules[24] = ctrl.Rule(rec['H'] & bdg['L'] & wtp['L'] & cfp['H'], psi[])
rules[25] = ctrl.Rule(rec['H'] & bdg['L'] & wtp['L'] & cfp['M'], psi[])
rules[26] = ctrl.Rule(rec['H'] & bdg['L'] & wtp['L'] & cfp['L'], psi[])
rules[27] = ctrl.Rule(rec['M'] & bdg['H'] & wtp['H'] & cfp['H'], psi[])
rules[28] = ctrl.Rule(rec['M'] & bdg['H'] & wtp['H'] & cfp['M'], psi[])
rules[29] = ctrl.Rule(rec['M'] & bdg['H'] & wtp['H'] & cfp['L'], psi[])
rules[30] = ctrl.Rule(rec['M'] & bdg['H'] & wtp['M'] & cfp['H'], psi[])
rules[31] = ctrl.Rule(rec['M'] & bdg['H'] & wtp['M'] & cfp['M'], psi[])
rules[32] = ctrl.Rule(rec['M'] & bdg['H'] & wtp['M'] & cfp['L'], psi[])
rules[33] = ctrl.Rule(rec['M'] & bdg['H'] & wtp['L'] & cfp['H'], psi[])
rules[34] = ctrl.Rule(rec['M'] & bdg['H'] & wtp['L'] & cfp['M'], psi[])
rules[35] = ctrl.Rule(rec['M'] & bdg['H'] & wtp['L'] & cfp['L'], psi[])
rules[36] = ctrl.Rule(rec['M'] & bdg['M'] & wtp['H'] & cfp['H'], psi[])
rules[37] = ctrl.Rule(rec['M'] & bdg['M'] & wtp['H'] & cfp['M'], psi[])
rules[38] = ctrl.Rule(rec['M'] & bdg['M'] & wtp['H'] & cfp['L'], psi[])
rules[39] = ctrl.Rule(rec['M'] & bdg['M'] & wtp['M'] & cfp['H'], psi[])
rules[40] = ctrl.Rule(rec['M'] & bdg['M'] & wtp['M'] & cfp['M'], psi[])
rules[41] = ctrl.Rule(rec['M'] & bdg['M'] & wtp['M'] & cfp['L'], psi[])
rules[42] = ctrl.Rule(rec['M'] & bdg['M'] & wtp['L'] & cfp['H'], psi[])
rules[43] = ctrl.Rule(rec['M'] & bdg['M'] & wtp['L'] & cfp['M'], psi[])
rules[44] = ctrl.Rule(rec['M'] & bdg['M'] & wtp['L'] & cfp['L'], psi[])
rules[45] = ctrl.Rule(rec['M'] & bdg['L'] & wtp['H'] & cfp['H'], psi[])
rules[46] = ctrl.Rule(rec['M'] & bdg['L'] & wtp['H'] & cfp['M'], psi[])
rules[47] = ctrl.Rule(rec['M'] & bdg['L'] & wtp['H'] & cfp['L'], psi[])
rules[48] = ctrl.Rule(rec['M'] & bdg['L'] & wtp['M'] & cfp['H'], psi[])
rules[49] = ctrl.Rule(rec['M'] & bdg['L'] & wtp['M'] & cfp['M'], psi[])
rules[50] = ctrl.Rule(rec['M'] & bdg['L'] & wtp['M'] & cfp['L'], psi[])
rules[51] = ctrl.Rule(rec['M'] & bdg['L'] & wtp['L'] & cfp['H'], psi[])
rules[52] = ctrl.Rule(rec['M'] & bdg['L'] & wtp['L'] & cfp['M'], psi[])
rules[53] = ctrl.Rule(rec['M'] & bdg['L'] & wtp['L'] & cfp['L'], psi[])
rules[54] = ctrl.Rule(rec['L'] & bdg['H'] & wtp['H'] & cfp['H'], psi[])
rules[55] = ctrl.Rule(rec['L'] & bdg['H'] & wtp['H'] & cfp['M'], psi[])
rules[56] = ctrl.Rule(rec['L'] & bdg['H'] & wtp['H'] & cfp['L'], psi[])
rules[57] = ctrl.Rule(rec['L'] & bdg['H'] & wtp['M'] & cfp['H'], psi[])
rules[58] = ctrl.Rule(rec['L'] & bdg['H'] & wtp['M'] & cfp['M'], psi[])
rules[59] = ctrl.Rule(rec['L'] & bdg['H'] & wtp['M'] & cfp['L'], psi[])
rules[60] = ctrl.Rule(rec['L'] & bdg['H'] & wtp['L'] & cfp['H'], psi[])
rules[61] = ctrl.Rule(rec['L'] & bdg['H'] & wtp['L'] & cfp['M'], psi[])
rules[62] = ctrl.Rule(rec['L'] & bdg['H'] & wtp['L'] & cfp['L'], psi[])
rules[63] = ctrl.Rule(rec['L'] & bdg['M'] & wtp['H'] & cfp['H'], psi[])
rules[64] = ctrl.Rule(rec['L'] & bdg['M'] & wtp['H'] & cfp['M'], psi[])
rules[65] = ctrl.Rule(rec['L'] & bdg['M'] & wtp['H'] & cfp['L'], psi[])
rules[66] = ctrl.Rule(rec['L'] & bdg['M'] & wtp['M'] & cfp['H'], psi[])
rules[67] = ctrl.Rule(rec['L'] & bdg['M'] & wtp['M'] & cfp['M'], psi[])
rules[68] = ctrl.Rule(rec['L'] & bdg['M'] & wtp['M'] & cfp['L'], psi[])
rules[69] = ctrl.Rule(rec['L'] & bdg['M'] & wtp['L'] & cfp['H'], psi[])
rules[70] = ctrl.Rule(rec['L'] & bdg['M'] & wtp['L'] & cfp['M'], psi[])
rules[71] = ctrl.Rule(rec['L'] & bdg['M'] & wtp['L'] & cfp['L'], psi[])
rules[72] = ctrl.Rule(rec['L'] & bdg['L'] & wtp['H'] & cfp['H'], psi[])
rules[73] = ctrl.Rule(rec['L'] & bdg['L'] & wtp['H'] & cfp['M'], psi[])
rules[74] = ctrl.Rule(rec['L'] & bdg['L'] & wtp['H'] & cfp['L'], psi[])
rules[75] = ctrl.Rule(rec['L'] & bdg['L'] & wtp['M'] & cfp['H'], psi[])
rules[76] = ctrl.Rule(rec['L'] & bdg['L'] & wtp['M'] & cfp['M'], psi[])
rules[77] = ctrl.Rule(rec['L'] & bdg['L'] & wtp['M'] & cfp['L'], psi[])
rules[78] = ctrl.Rule(rec['L'] & bdg['L'] & wtp['L'] & cfp['H'], psi[])
rules[79] = ctrl.Rule(rec['L'] & bdg['L'] & wtp['L'] & cfp['M'], psi[])
rules[80] = ctrl.Rule(rec['L'] & bdg['L'] & wtp['L'] & cfp['L'], psi[])

#ControlSystem
controller = ctrl.ControlSystem(rules)
generator = ctrl.ControlSystemSimulation(controller)
