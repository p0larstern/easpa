import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class generator(object):

    def __init__(self, cl, ch, rl, rh, bl, bh, wl, wh):
        self.cfp_lo = cl
        self.cfp_hi = ch
        self.rec_lo = rl
        self.rec_hi = rh
        self.bdg_lo = bl
        self.bdg_hi = bh
        self.wtp_lo = wl
        self.wtp_hi = wh
        self.psi_lo = 0
        self.psi_hi = 100

    def set_variables(self):
        self.cfp = ctrl.Antecedent(np.arange(self.cfp_lo, self.cfp_hi, 1), 'carbon_footprint')
        self.rec = ctrl.Antecedent(np.arange(self.rec_lo, self.rec_hi, 1), 'recyclablilty')
        self.bdg = ctrl.Antecedent(np.arange(self.bdg_lo, self.bdg_hi, 1), 'biodegradability')
        self.wtp = ctrl.Antecedent(np.arange(self.wtp_lo, self.wtp_hi, 1), 'waste_treated_in_prod')

        self.psi = ctrl.Consequent(np.arange(self.psi_lo, self.psi_hi, 1), 'score')

        # L = low, M = medium, H = high
        #cfp[] = fuzz.trimf(cfp.universe, [])
        cm = self.__mp(self.cfp_lo, self.cfp_hi)
        self.cfp['L'] = fuzz.trimf(self.cfp.universe, [self.cfp_lo, self.cfp_lo, cm])
        self.cfp['M'] = fuzz.trimf(self.cfp.universe, [self.cfp_lo, cm, self.cfp_hi])
        self.cfp['H'] = fuzz.trimf(self.cfp.universe, [cm, self.cfp_hi, self.cfp_hi])

        #rec[] = fuzz.trimf(rec.universe, [])
        rm = self.__mp(self.rec_lo, self.rec_hi)
        self.rec['L'] = fuzz.trimf(self.rec.universe, [self.rec_lo, self.rec_lo, rm])
        self.rec['M'] = fuzz.trimf(self.rec.universe, [self.rec_lo, rm, self.rec_hi])
        self.rec['H'] = fuzz.trimf(self.rec.universe, [rm, self.rec_hi, self.rec_hi])

        #bdg[] = fuzz.trimf(bdg.universe, [])
        bm = self.__mp(self.bdg_lo, self.bdg_hi)
        self.bdg['L'] = fuzz.trimf(self.bdg.universe, [self.bdg_lo, self.bdg_lo, bm])
        self.bdg['M'] = fuzz.trimf(self.bdg.universe, [self.bdg_lo, bm, self.bdg_hi])
        self.bdg['H'] = fuzz.trimf(self.bdg.universe, [bm, self.bdg_hi, self.bdg_hi])

        #wtp[] = fuzz.trimf(wtp.universe, [])
        wm = self.__mp(self.wtp_lo, self.wtp_hi)
        self.wtp['L'] = fuzz.trimf(self.wtp.universe, [self.wtp_lo, self.wtp_lo, wm])
        self.wtp['M'] = fuzz.trimf(self.wtp.universe, [self.wtp_lo, wm, self.wtp_hi])
        self.wtp['H'] = fuzz.trimf(self.wtp.universe, [wm, self.wtp_hi, self.wtp_hi])

        # B = bad, P = poor,  A = average, G = good, E = excellent
        #psi[] = fuzz.trapmf(psi.universe, [])
        self.psi['B'] = fuzz.trapmf(self.psi.universe, [0, 0, 20, 30])
        self.psi['P'] = fuzz.trapmf(self.psi.universe, [10, 20, 40, 50])
        self.psi['A'] = fuzz.trapmf(self.psi.universe, [30, 40, 60, 70])
        self.psi['G'] = fuzz.trapmf(self.psi.universe, [50, 60, 80, 90])
        self.psi['E'] = fuzz.trapmf(self.psi.universe, [70, 80, 100, 100])

    def set_rulebase(self):
        #Rule Base
        #ruleX = ctrl.Rule()
        self.rules = [None] * 81
        self.rules[0] = ctrl.Rule(self.rec['H'] & self.bdg['H'] & self.wtp['H'] & self.cfp['H'], self.psi['A'])
        self.rules[1] = ctrl.Rule(self.rec['H'] & self.bdg['H'] & self.wtp['H'] & self.cfp['M'], self.psi['G'])
        self.rules[2] = ctrl.Rule(self.rec['H'] & self.bdg['H'] & self.wtp['H'] & self.cfp['L'], self.psi['E'])
        self.rules[3] = ctrl.Rule(self.rec['H'] & self.bdg['H'] & self.wtp['M'] & self.cfp['H'], self.psi['A'])
        self.rules[4] = ctrl.Rule(self.rec['H'] & self.bdg['H'] & self.wtp['M'] & self.cfp['M'], self.psi['A'])
        self.rules[5] = ctrl.Rule(self.rec['H'] & self.bdg['H'] & self.wtp['M'] & self.cfp['L'], self.psi['G'])
        self.rules[6] = ctrl.Rule(self.rec['H'] & self.bdg['H'] & self.wtp['L'] & self.cfp['H'], self.psi['B'])
        self.rules[7] = ctrl.Rule(self.rec['H'] & self.bdg['H'] & self.wtp['L'] & self.cfp['M'], self.psi['P'])
        self.rules[8] = ctrl.Rule(self.rec['H'] & self.bdg['H'] & self.wtp['L'] & self.cfp['L'], self.psi['A'])
        self.rules[9] = ctrl.Rule(self.rec['H'] & self.bdg['M'] & self.wtp['H'] & self.cfp['H'], self.psi['P'])
        self.rules[10] = ctrl.Rule(self.rec['H'] & self.bdg['M'] & self.wtp['H'] & self.cfp['M'], self.psi['A'])
        self.rules[11] = ctrl.Rule(self.rec['H'] & self.bdg['M'] & self.wtp['H'] & self.cfp['L'], self.psi['G'])
        self.rules[12] = ctrl.Rule(self.rec['H'] & self.bdg['M'] & self.wtp['M'] & self.cfp['H'], self.psi['P'])
        self.rules[13] = ctrl.Rule(self.rec['H'] & self.bdg['M'] & self.wtp['M'] & self.cfp['M'], self.psi['A'])
        self.rules[14] = ctrl.Rule(self.rec['H'] & self.bdg['M'] & self.wtp['M'] & self.cfp['L'], self.psi['A'])
        self.rules[15] = ctrl.Rule(self.rec['H'] & self.bdg['M'] & self.wtp['L'] & self.cfp['H'], self.psi['P'])
        self.rules[16] = ctrl.Rule(self.rec['H'] & self.bdg['M'] & self.wtp['L'] & self.cfp['M'], self.psi['P'])
        self.rules[17] = ctrl.Rule(self.rec['H'] & self.bdg['M'] & self.wtp['L'] & self.cfp['L'], self.psi['A'])
        self.rules[18] = ctrl.Rule(self.rec['H'] & self.bdg['L'] & self.wtp['H'] & self.cfp['H'], self.psi['P'])
        self.rules[19] = ctrl.Rule(self.rec['H'] & self.bdg['L'] & self.wtp['H'] & self.cfp['M'], self.psi['P'])
        self.rules[20] = ctrl.Rule(self.rec['H'] & self.bdg['L'] & self.wtp['H'] & self.cfp['L'], self.psi['A'])
        self.rules[21] = ctrl.Rule(self.rec['H'] & self.bdg['L'] & self.wtp['M'] & self.cfp['H'], self.psi['B'])
        self.rules[22] = ctrl.Rule(self.rec['H'] & self.bdg['L'] & self.wtp['M'] & self.cfp['M'], self.psi['P'])
        self.rules[23] = ctrl.Rule(self.rec['H'] & self.bdg['L'] & self.wtp['M'] & self.cfp['L'], self.psi['A'])
        self.rules[24] = ctrl.Rule(self.rec['H'] & self.bdg['L'] & self.wtp['L'] & self.cfp['H'], self.psi['B'])
        self.rules[25] = ctrl.Rule(self.rec['H'] & self.bdg['L'] & self.wtp['L'] & self.cfp['M'], self.psi['P'])
        self.rules[26] = ctrl.Rule(self.rec['H'] & self.bdg['L'] & self.wtp['L'] & self.cfp['L'], self.psi['P'])
        self.rules[27] = ctrl.Rule(self.rec['M'] & self.bdg['H'] & self.wtp['H'] & self.cfp['H'], self.psi['A'])
        self.rules[28] = ctrl.Rule(self.rec['M'] & self.bdg['H'] & self.wtp['H'] & self.cfp['M'], self.psi['G'])
        self.rules[29] = ctrl.Rule(self.rec['M'] & self.bdg['H'] & self.wtp['H'] & self.cfp['L'], self.psi['G'])
        self.rules[30] = ctrl.Rule(self.rec['M'] & self.bdg['H'] & self.wtp['M'] & self.cfp['H'], self.psi['P'])
        self.rules[31] = ctrl.Rule(self.rec['M'] & self.bdg['H'] & self.wtp['M'] & self.cfp['M'], self.psi['A'])
        self.rules[32] = ctrl.Rule(self.rec['M'] & self.bdg['H'] & self.wtp['M'] & self.cfp['L'], self.psi['G'])
        self.rules[33] = ctrl.Rule(self.rec['M'] & self.bdg['H'] & self.wtp['L'] & self.cfp['H'], self.psi['B'])
        self.rules[34] = ctrl.Rule(self.rec['M'] & self.bdg['H'] & self.wtp['L'] & self.cfp['M'], self.psi['P'])
        self.rules[35] = ctrl.Rule(self.rec['M'] & self.bdg['H'] & self.wtp['L'] & self.cfp['L'], self.psi['A'])
        self.rules[36] = ctrl.Rule(self.rec['M'] & self.bdg['M'] & self.wtp['H'] & self.cfp['H'], self.psi['P'])
        self.rules[37] = ctrl.Rule(self.rec['M'] & self.bdg['M'] & self.wtp['H'] & self.cfp['M'], self.psi['A'])
        self.rules[38] = ctrl.Rule(self.rec['M'] & self.bdg['M'] & self.wtp['H'] & self.cfp['L'], self.psi['G'])
        self.rules[39] = ctrl.Rule(self.rec['M'] & self.bdg['M'] & self.wtp['M'] & self.cfp['H'], self.psi['P'])
        self.rules[40] = ctrl.Rule(self.rec['M'] & self.bdg['M'] & self.wtp['M'] & self.cfp['M'], self.psi['A'])
        self.rules[41] = ctrl.Rule(self.rec['M'] & self.bdg['M'] & self.wtp['M'] & self.cfp['L'], self.psi['G'])
        self.rules[42] = ctrl.Rule(self.rec['M'] & self.bdg['M'] & self.wtp['L'] & self.cfp['H'], self.psi['B'])
        self.rules[43] = ctrl.Rule(self.rec['M'] & self.bdg['M'] & self.wtp['L'] & self.cfp['M'], self.psi['P'])
        self.rules[44] = ctrl.Rule(self.rec['M'] & self.bdg['M'] & self.wtp['L'] & self.cfp['L'], self.psi['P'])
        self.rules[45] = ctrl.Rule(self.rec['M'] & self.bdg['L'] & self.wtp['H'] & self.cfp['H'], self.psi['B'])
        self.rules[46] = ctrl.Rule(self.rec['M'] & self.bdg['L'] & self.wtp['H'] & self.cfp['M'], self.psi['P'])
        self.rules[47] = ctrl.Rule(self.rec['M'] & self.bdg['L'] & self.wtp['H'] & self.cfp['L'], self.psi['A'])
        self.rules[48] = ctrl.Rule(self.rec['M'] & self.bdg['L'] & self.wtp['M'] & self.cfp['H'], self.psi['B'])
        self.rules[49] = ctrl.Rule(self.rec['M'] & self.bdg['L'] & self.wtp['M'] & self.cfp['M'], self.psi['P'])
        self.rules[50] = ctrl.Rule(self.rec['M'] & self.bdg['L'] & self.wtp['M'] & self.cfp['L'], self.psi['A'])
        self.rules[51] = ctrl.Rule(self.rec['M'] & self.bdg['L'] & self.wtp['L'] & self.cfp['H'], self.psi['B'])
        self.rules[52] = ctrl.Rule(self.rec['M'] & self.bdg['L'] & self.wtp['L'] & self.cfp['M'], self.psi['B'])
        self.rules[53] = ctrl.Rule(self.rec['M'] & self.bdg['L'] & self.wtp['L'] & self.cfp['L'], self.psi['P'])
        self.rules[54] = ctrl.Rule(self.rec['L'] & self.bdg['H'] & self.wtp['H'] & self.cfp['H'], self.psi['B'])
        self.rules[55] = ctrl.Rule(self.rec['L'] & self.bdg['H'] & self.wtp['H'] & self.cfp['M'], self.psi['P'])
        self.rules[56] = ctrl.Rule(self.rec['L'] & self.bdg['H'] & self.wtp['H'] & self.cfp['L'], self.psi['A'])
        self.rules[57] = ctrl.Rule(self.rec['L'] & self.bdg['H'] & self.wtp['M'] & self.cfp['H'], self.psi['B'])
        self.rules[58] = ctrl.Rule(self.rec['L'] & self.bdg['H'] & self.wtp['M'] & self.cfp['M'], self.psi['P'])
        self.rules[59] = ctrl.Rule(self.rec['L'] & self.bdg['H'] & self.wtp['M'] & self.cfp['L'], self.psi['P'])
        self.rules[60] = ctrl.Rule(self.rec['L'] & self.bdg['H'] & self.wtp['L'] & self.cfp['H'], self.psi['B'])
        self.rules[61] = ctrl.Rule(self.rec['L'] & self.bdg['H'] & self.wtp['L'] & self.cfp['M'], self.psi['B'])
        self.rules[62] = ctrl.Rule(self.rec['L'] & self.bdg['H'] & self.wtp['L'] & self.cfp['L'], self.psi['P'])
        self.rules[63] = ctrl.Rule(self.rec['L'] & self.bdg['M'] & self.wtp['H'] & self.cfp['H'], self.psi['B'])
        self.rules[64] = ctrl.Rule(self.rec['L'] & self.bdg['M'] & self.wtp['H'] & self.cfp['M'], self.psi['P'])
        self.rules[65] = ctrl.Rule(self.rec['L'] & self.bdg['M'] & self.wtp['H'] & self.cfp['L'], self.psi['A'])
        self.rules[66] = ctrl.Rule(self.rec['L'] & self.bdg['M'] & self.wtp['M'] & self.cfp['H'], self.psi['B'])
        self.rules[67] = ctrl.Rule(self.rec['L'] & self.bdg['M'] & self.wtp['M'] & self.cfp['M'], self.psi['P'])
        self.rules[68] = ctrl.Rule(self.rec['L'] & self.bdg['M'] & self.wtp['M'] & self.cfp['L'], self.psi['P'])
        self.rules[69] = ctrl.Rule(self.rec['L'] & self.bdg['M'] & self.wtp['L'] & self.cfp['H'], self.psi['B'])
        self.rules[70] = ctrl.Rule(self.rec['L'] & self.bdg['M'] & self.wtp['L'] & self.cfp['M'], self.psi['B'])
        self.rules[71] = ctrl.Rule(self.rec['L'] & self.bdg['M'] & self.wtp['L'] & self.cfp['L'], self.psi['P'])
        self.rules[72] = ctrl.Rule(self.rec['L'] & self.bdg['L'] & self.wtp['H'] & self.cfp['H'], self.psi['B'])
        self.rules[73] = ctrl.Rule(self.rec['L'] & self.bdg['L'] & self.wtp['H'] & self.cfp['M'], self.psi['B'])
        self.rules[74] = ctrl.Rule(self.rec['L'] & self.bdg['L'] & self.wtp['H'] & self.cfp['L'], self.psi['P'])
        self.rules[75] = ctrl.Rule(self.rec['L'] & self.bdg['L'] & self.wtp['M'] & self.cfp['H'], self.psi['B'])
        self.rules[76] = ctrl.Rule(self.rec['L'] & self.bdg['L'] & self.wtp['M'] & self.cfp['M'], self.psi['B'])
        self.rules[77] = ctrl.Rule(self.rec['L'] & self.bdg['L'] & self.wtp['M'] & self.cfp['L'], self.psi['B'])
        self.rules[78] = ctrl.Rule(self.rec['L'] & self.bdg['L'] & self.wtp['L'] & self.cfp['H'], self.psi['B'])
        self.rules[79] = ctrl.Rule(self.rec['L'] & self.bdg['L'] & self.wtp['L'] & self.cfp['M'], self.psi['B'])
        self.rules[80] = ctrl.Rule(self.rec['L'] & self.bdg['L'] & self.wtp['L'] & self.cfp['L'], self.psi['B'])

    def start(self):
        print("Starting PSI generator.")
        print("Initialising linguistic variables.", end=" ")
        self.set_variables()
        print("Finished.")
        print("Setting up rulebase.", end=" ")
        self.set_rulebase()
        print("Finished.")

        print("Setting up control system.", end=" ")
        #ControlSystem
        self.control = ctrl.ControlSystem(self.rules)
        self.gen = ctrl.ControlSystemSimulation(self.control)
        print("Finished.")
        print("Generator started.")

    def get_psi(self, c, r, b, w):
        self.gen.input['carbon_footprint'] = c
        self.gen.input['recyclablilty'] = r
        self.gen.input['biodegradability'] = b
        self.gen.input['waste_treated_in_prod'] = w

        self.gen.compute()

        return self.gen.output['score']

    @staticmethod
    def __mp(l, r):
        m = l + (r-l)//2
        return m
