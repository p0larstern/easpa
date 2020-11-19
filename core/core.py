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

# B = bad, P = poor,  A = average, G = good, E = excellent
#psi[] = fuzz.trapmf(psi.universe, [])
psi['B'] = fuzz.trapmf(psi.universe, [])
psi['P'] = fuzz.trapmf(psi.universe, [])
psi['A'] = fuzz.trapmf(psi.universe, [])
psi['G'] = fuzz.trapmf(psi.universe, [])
psi['E'] = fuzz.trapmf(psi.universe, [])

#Rule Base
#ruleX = ctrl.Rule()
rules = [None] * 81
rules[0] = ctrl.Rule(rec['H'] & bdg['H'] & wtp['H'] & cfp['H'], psi['A'])
rules[1] = ctrl.Rule(rec['H'] & bdg['H'] & wtp['H'] & cfp['M'], psi['G'])
rules[2] = ctrl.Rule(rec['H'] & bdg['H'] & wtp['H'] & cfp['L'], psi['E'])
rules[3] = ctrl.Rule(rec['H'] & bdg['H'] & wtp['M'] & cfp['H'], psi['A'])
rules[4] = ctrl.Rule(rec['H'] & bdg['H'] & wtp['M'] & cfp['M'], psi['A'])
rules[5] = ctrl.Rule(rec['H'] & bdg['H'] & wtp['M'] & cfp['L'], psi['G'])
rules[6] = ctrl.Rule(rec['H'] & bdg['H'] & wtp['L'] & cfp['H'], psi['B'])
rules[7] = ctrl.Rule(rec['H'] & bdg['H'] & wtp['L'] & cfp['M'], psi['P'])
rules[8] = ctrl.Rule(rec['H'] & bdg['H'] & wtp['L'] & cfp['L'], psi['A'])
rules[9] = ctrl.Rule(rec['H'] & bdg['M'] & wtp['H'] & cfp['H'], psi['P'])
rules[10] = ctrl.Rule(rec['H'] & bdg['M'] & wtp['H'] & cfp['M'], psi['A'])
rules[11] = ctrl.Rule(rec['H'] & bdg['M'] & wtp['H'] & cfp['L'], psi['G'])
rules[12] = ctrl.Rule(rec['H'] & bdg['M'] & wtp['M'] & cfp['H'], psi['P'])
rules[13] = ctrl.Rule(rec['H'] & bdg['M'] & wtp['M'] & cfp['M'], psi['A'])
rules[14] = ctrl.Rule(rec['H'] & bdg['M'] & wtp['M'] & cfp['L'], psi['A'])
rules[15] = ctrl.Rule(rec['H'] & bdg['M'] & wtp['L'] & cfp['H'], psi['P'])
rules[16] = ctrl.Rule(rec['H'] & bdg['M'] & wtp['L'] & cfp['M'], psi['P'])
rules[17] = ctrl.Rule(rec['H'] & bdg['M'] & wtp['L'] & cfp['L'], psi['A'])
rules[18] = ctrl.Rule(rec['H'] & bdg['L'] & wtp['H'] & cfp['H'], psi['P'])
rules[19] = ctrl.Rule(rec['H'] & bdg['L'] & wtp['H'] & cfp['M'], psi['P'])
rules[20] = ctrl.Rule(rec['H'] & bdg['L'] & wtp['H'] & cfp['L'], psi['A'])
rules[21] = ctrl.Rule(rec['H'] & bdg['L'] & wtp['M'] & cfp['H'], psi['B'])
rules[22] = ctrl.Rule(rec['H'] & bdg['L'] & wtp['M'] & cfp['M'], psi['P'])
rules[23] = ctrl.Rule(rec['H'] & bdg['L'] & wtp['M'] & cfp['L'], psi['A'])
rules[24] = ctrl.Rule(rec['H'] & bdg['L'] & wtp['L'] & cfp['H'], psi['B'])
rules[25] = ctrl.Rule(rec['H'] & bdg['L'] & wtp['L'] & cfp['M'], psi['P'])
rules[26] = ctrl.Rule(rec['H'] & bdg['L'] & wtp['L'] & cfp['L'], psi['P'])
rules[27] = ctrl.Rule(rec['M'] & bdg['H'] & wtp['H'] & cfp['H'], psi['A'])
rules[28] = ctrl.Rule(rec['M'] & bdg['H'] & wtp['H'] & cfp['M'], psi['G'])
rules[29] = ctrl.Rule(rec['M'] & bdg['H'] & wtp['H'] & cfp['L'], psi['G'])
rules[30] = ctrl.Rule(rec['M'] & bdg['H'] & wtp['M'] & cfp['H'], psi['P'])
rules[31] = ctrl.Rule(rec['M'] & bdg['H'] & wtp['M'] & cfp['M'], psi['A'])
rules[32] = ctrl.Rule(rec['M'] & bdg['H'] & wtp['M'] & cfp['L'], psi['G'])
rules[33] = ctrl.Rule(rec['M'] & bdg['H'] & wtp['L'] & cfp['H'], psi['B'])
rules[34] = ctrl.Rule(rec['M'] & bdg['H'] & wtp['L'] & cfp['M'], psi['P'])
rules[35] = ctrl.Rule(rec['M'] & bdg['H'] & wtp['L'] & cfp['L'], psi['A'])
rules[36] = ctrl.Rule(rec['M'] & bdg['M'] & wtp['H'] & cfp['H'], psi['P'])
rules[37] = ctrl.Rule(rec['M'] & bdg['M'] & wtp['H'] & cfp['M'], psi['A'])
rules[38] = ctrl.Rule(rec['M'] & bdg['M'] & wtp['H'] & cfp['L'], psi['G'])
rules[39] = ctrl.Rule(rec['M'] & bdg['M'] & wtp['M'] & cfp['H'], psi['P'])
rules[40] = ctrl.Rule(rec['M'] & bdg['M'] & wtp['M'] & cfp['M'], psi['A'])
rules[41] = ctrl.Rule(rec['M'] & bdg['M'] & wtp['M'] & cfp['L'], psi['G'])
rules[42] = ctrl.Rule(rec['M'] & bdg['M'] & wtp['L'] & cfp['H'], psi['B'])
rules[43] = ctrl.Rule(rec['M'] & bdg['M'] & wtp['L'] & cfp['M'], psi['P'])
rules[44] = ctrl.Rule(rec['M'] & bdg['M'] & wtp['L'] & cfp['L'], psi['P'])
rules[45] = ctrl.Rule(rec['M'] & bdg['L'] & wtp['H'] & cfp['H'], psi['B'])
rules[46] = ctrl.Rule(rec['M'] & bdg['L'] & wtp['H'] & cfp['M'], psi['P'])
rules[47] = ctrl.Rule(rec['M'] & bdg['L'] & wtp['H'] & cfp['L'], psi['A'])
rules[48] = ctrl.Rule(rec['M'] & bdg['L'] & wtp['M'] & cfp['H'], psi['B'])
rules[49] = ctrl.Rule(rec['M'] & bdg['L'] & wtp['M'] & cfp['M'], psi['P'])
rules[50] = ctrl.Rule(rec['M'] & bdg['L'] & wtp['M'] & cfp['L'], psi['A'])
rules[51] = ctrl.Rule(rec['M'] & bdg['L'] & wtp['L'] & cfp['H'], psi['B'])
rules[52] = ctrl.Rule(rec['M'] & bdg['L'] & wtp['L'] & cfp['M'], psi['B'])
rules[53] = ctrl.Rule(rec['M'] & bdg['L'] & wtp['L'] & cfp['L'], psi['P'])
rules[54] = ctrl.Rule(rec['L'] & bdg['H'] & wtp['H'] & cfp['H'], psi['B'])
rules[55] = ctrl.Rule(rec['L'] & bdg['H'] & wtp['H'] & cfp['M'], psi['P'])
rules[56] = ctrl.Rule(rec['L'] & bdg['H'] & wtp['H'] & cfp['L'], psi['A'])
rules[57] = ctrl.Rule(rec['L'] & bdg['H'] & wtp['M'] & cfp['H'], psi['B'])
rules[58] = ctrl.Rule(rec['L'] & bdg['H'] & wtp['M'] & cfp['M'], psi['P'])
rules[59] = ctrl.Rule(rec['L'] & bdg['H'] & wtp['M'] & cfp['L'], psi['P'])
rules[60] = ctrl.Rule(rec['L'] & bdg['H'] & wtp['L'] & cfp['H'], psi['B'])
rules[61] = ctrl.Rule(rec['L'] & bdg['H'] & wtp['L'] & cfp['M'], psi['B'])
rules[62] = ctrl.Rule(rec['L'] & bdg['H'] & wtp['L'] & cfp['L'], psi['P'])
rules[63] = ctrl.Rule(rec['L'] & bdg['M'] & wtp['H'] & cfp['H'], psi['B'])
rules[64] = ctrl.Rule(rec['L'] & bdg['M'] & wtp['H'] & cfp['M'], psi['P'])
rules[65] = ctrl.Rule(rec['L'] & bdg['M'] & wtp['H'] & cfp['L'], psi['A'])
rules[66] = ctrl.Rule(rec['L'] & bdg['M'] & wtp['M'] & cfp['H'], psi['B'])
rules[67] = ctrl.Rule(rec['L'] & bdg['M'] & wtp['M'] & cfp['M'], psi['P'])
rules[68] = ctrl.Rule(rec['L'] & bdg['M'] & wtp['M'] & cfp['L'], psi['P'])
rules[69] = ctrl.Rule(rec['L'] & bdg['M'] & wtp['L'] & cfp['H'], psi['B'])
rules[70] = ctrl.Rule(rec['L'] & bdg['M'] & wtp['L'] & cfp['M'], psi['B'])
rules[71] = ctrl.Rule(rec['L'] & bdg['M'] & wtp['L'] & cfp['L'], psi['P'])
rules[72] = ctrl.Rule(rec['L'] & bdg['L'] & wtp['H'] & cfp['H'], psi['B'])
rules[73] = ctrl.Rule(rec['L'] & bdg['L'] & wtp['H'] & cfp['M'], psi['B'])
rules[74] = ctrl.Rule(rec['L'] & bdg['L'] & wtp['H'] & cfp['L'], psi['P'])
rules[75] = ctrl.Rule(rec['L'] & bdg['L'] & wtp['M'] & cfp['H'], psi['B'])
rules[76] = ctrl.Rule(rec['L'] & bdg['L'] & wtp['M'] & cfp['M'], psi['B'])
rules[77] = ctrl.Rule(rec['L'] & bdg['L'] & wtp['M'] & cfp['L'], psi['B'])
rules[78] = ctrl.Rule(rec['L'] & bdg['L'] & wtp['L'] & cfp['H'], psi['B'])
rules[79] = ctrl.Rule(rec['L'] & bdg['L'] & wtp['L'] & cfp['M'], psi['B'])
rules[80] = ctrl.Rule(rec['L'] & bdg['L'] & wtp['L'] & cfp['L'], psi['B'])

#ControlSystem
controller = ctrl.ControlSystem(rules)
generator = ctrl.ControlSystemSimulation(controller)
