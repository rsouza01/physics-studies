import scipy.constants as const

COULOMB_CONSTANT = 9 *10^9

def angstrom_to_m(d):
    return d * 1e-10

def coulomb_force(q1, q2, d):
    return (COULOMB_CONSTANT * q1* q2) / d**2

print(coulomb_force(const.proton_mass, const.electron_mass, angstrom_to_m(0.5)))