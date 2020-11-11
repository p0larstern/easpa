import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

"""
range constants TBD for each input
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

