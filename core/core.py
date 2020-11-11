import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

"""
range constants TBD for each variable
cfp_lo =
cfp_hi =
rec_lo =
rec_hi =
bdg_lo =
bdg_hi =
wtp_lo =
wtp_hi =
psi_lo =
psi_hi =
"""

cfp = ctrl.Antecedent(np.arrange(cfp_lo, cfp_hi, 1), 'carbon_footprint')
rec = ctrl.Antecedent(np.arrange(rec_lo, rec_hi, 1), 'recyclablilty')
bdg = ctrl.Antecedent(np.arrange(bdg_lo, bdg_hi, 1), 'biodegradability')
wtp = ctrl.Antecedent(np.arrange(wtp_lo, wtp_hi, 1), 'waste_treated_in_prod')

psi = ctrl.Consequent(np.arrange(psi_lo, psi_hi, 1), 'score')


#cfp[] = fuzz.trimf(cfp.universe, [])
cfp['low'] = fuzz.trimf(cfp.universe, [])
cfp['mdm'] = fuzz.trimf(cfp.universe, [])
cfp['high'] = fuzz.trimf(cfp.universe, [])

#rec[] = fuzz.trimf(rec.universe, [])
rec['low'] = fuzz.trimf(rec.universe, [])
rec['mdm'] = fuzz.trimf(rec.universe, [])
rec['high'] = fuzz.trimf(rec.universe, [])

#bdg[] = fuzz.trimf(bdg.universe, [])
bdg['low'] = fuzz.trimf(bdg.universe, [])
bdg['mdm'] = fuzz.trimf(bdg.universe, [])
bdg['high'] = fuzz.trimf(bdg.universe, [])

#wtp[] = fuzz.trimf(wtp.universe, [])
wtp['low'] = fuzz.trimf(wtp.universe, [])
wtp['mdm'] = fuzz.trimf(wtp.universe, [])
wtp['high'] = fuzz.trimf(wtp.universe, [])
