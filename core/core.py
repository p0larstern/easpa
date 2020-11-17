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

#psi[] = fuzz.trapmf(psi.universe, [])
psi['B'] = fuzz.trapmf(psi.universe, [])
psi['A'] = fuzz.trapmf(psi.universe, [])
psi['G'] = fuzz.trapmf(psi.universe, [])
psi['E'] = fuzz.trapmf(psi.universe, [])


#Rule Base
#ruleX = ctrl.Rule()


#ControlSystem
controller = ctrl.ControlSystem(rule_list)
generator = ctrl.ControlSystemSimulation(controller)
