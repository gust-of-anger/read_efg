import numpy as np
import argparse

def read_efg(input_efg_file, atom_loc):
    """
    Function to read the electric field gradient from the gipaw output file.
    atom_loc is the atom position in the espresso input file (starting from 1).
    """
    to_va2 = 97.173624
    seq = np.arange(-2, 100)
    set_index = {0, 1, 2}
    pos_efg = atom_loc * 3 + seq[atom_loc - 1]
    efg = {}
    with open(input_efg_file) as fp:
        efgLines = fp.readlines()
        for i, j in enumerate(efgLines):
            if '----- total EFG (symmetrized) -----' in j:
                efg_1 = [efgLines[i + pos_efg].split()[2], efgLines[i + pos_efg].split()[3],
                         efgLines[i + pos_efg].split()[4]]
                efg_2 = [efgLines[i + pos_efg + 1].split()[2], efgLines[i + pos_efg + 1].split()[3],
                         efgLines[i + pos_efg + 1].split()[4]]
                efg_3 = [efgLines[i + pos_efg + 2].split()[2], efgLines[i + pos_efg + 2].split()[3],
                         efgLines[i + pos_efg + 2].split()[4]]
    V = np.array([efg_1, efg_2, efg_3]).astype(float)
    V_principal = np.linalg.eig(V)
    index_z = np.absolute(V_principal[0]).argmax()
    index_x = np.absolute(V_principal[0]).argmin()
    index_y = list(set_index - {index_x, index_z})[0]
    eta = (V_principal[0][index_x] - V_principal[0][index_y]) / V_principal[0][index_z]

    V_zz_ax = V_principal[1].T[index_z]
    V_xx_ax = V_principal[1].T[index_x]
    V_yy_ax = V_principal[1].T[index_y]

    V_ax = np.array([V_xx_ax, V_yy_ax, V_zz_ax])

    efg['Vxx'] = to_va2 * V_principal[0][index_x]
    efg['Vyy'] = to_va2 * V_principal[0][index_y]
    efg['Vzz'] = to_va2 * V_principal[0][index_z]
    efg['eta'] = eta
    efg['axis'] = V_ax
    return efg

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read the electric field gradient of a gipaw output file.')
    parser.add_argument('--inp', type=str, nargs='?', help='Name of the gipaw output file name.', const='efg.out')
    parser.add_argument('--loc', type=int, nargs='?', help='Atom location in the espresso input file')

    args = parser.parse_args()
    efg = read_efg(args.inp, args.loc)

    print('Vzz = %6.3f V\A^2' % (efg['Vzz']))
    print('eta = %7.4f' % (efg['eta']))

