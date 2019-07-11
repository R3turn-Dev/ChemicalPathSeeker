#
# Chem.atoms
# Author: Eunhak Lee(@return0927)
#
from .prototype import Atom


class Element(Atom):
    atomic_number = 0

    def __repr__(self):
        return self.__class__.__name__

    def __init__(self):
        super().__init__(self.atomic_number)


class H(Element):
    atomic_number = 1
    atomic_name = "Hydrogen"


class He(Element):
    atomic_number = 2
    atomic_name = "Helium"


class Li(Element):
    atomic_number = 3
    atomic_name = "Lithium"


class Be(Element):
    atomic_number = 4
    atomic_name = "Beryllium"


class B(Element):
    atomic_number = 5
    atomic_name = "Boron"


class C(Element):
    atomic_number = 6
    atomic_name = "Carbon"


class N(Element):
    atomic_number = 7
    atomic_name = "Nitrogen"


class O(Element):
    atomic_number = 8
    atomic_name = "Oxygen"


class F(Element):
    atomic_number = 9
    atomic_name = "Fluorine"


class Ne(Element):
    atomic_number = 10
    atomic_name = "Neon"


class Na(Element):
    atomic_number = 11
    atomic_name = "Sodium"


class Mg(Element):
    atomic_number = 12
    atomic_name = "Magnesium"


class Al(Element):
    atomic_number = 13
    atomic_name = "Aluminum"


class Si(Element):
    atomic_number = 14
    atomic_name = "Silicon"


class P(Element):
    atomic_number = 15
    atomic_name = "Phosphorus"


class S(Element):
    atomic_number = 16
    atomic_name = "Sulfur"


class Cl(Element):
    atomic_number = 17
    atomic_name = "Chlorine"


class Ar(Element):
    atomic_number = 18
    atomic_name = "Argon"


class K(Element):
    atomic_number = 19
    atomic_name = "Potassium"


class Ca(Element):
    atomic_number = 20
    atomic_name = "Calcium"


class Sc(Element):
    atomic_number = 21
    atomic_name = "Scandium"


class Ti(Element):
    atomic_number = 22
    atomic_name = "Titanium"


class V(Element):
    atomic_number = 23
    atomic_name = "Vanadium"


class Cr(Element):
    atomic_number = 24
    atomic_name = "Chromium"


class Mn(Element):
    atomic_number = 25
    atomic_name = "Manganese"


class Fe(Element):
    atomic_number = 26
    atomic_name = "Iron"


class Co(Element):
    atomic_number = 27
    atomic_name = "Cobalt"


class Ni(Element):
    atomic_number = 28
    atomic_name = "Nickel"


class Cu(Element):
    atomic_number = 29
    atomic_name = "Copper"


class Zn(Element):
    atomic_number = 30
    atomic_name = "Zinc"


class Ga(Element):
    atomic_number = 31
    atomic_name = "Gallium"


class Ge(Element):
    atomic_number = 32
    atomic_name = "Germanium"


class As(Element):
    atomic_number = 33
    atomic_name = "Arsenic"


class Se(Element):
    atomic_number = 34
    atomic_name = "Selenium"


class Br(Element):
    atomic_number = 35
    atomic_name = "Bromine"


class Kr(Element):
    atomic_number = 36
    atomic_name = "Krypton"


class Rb(Element):
    atomic_number = 37
    atomic_name = "Rubidium"


class Sr(Element):
    atomic_number = 38
    atomic_name = "Strontium"


class Y(Element):
    atomic_number = 39
    atomic_name = "Yttrium"


class Zr(Element):
    atomic_number = 40
    atomic_name = "Zirconium"


class Nb(Element):
    atomic_number = 41
    atomic_name = "Niobium"


class Mo(Element):
    atomic_number = 42
    atomic_name = "Molybdenum"


class Tc(Element):
    atomic_number = 43
    atomic_name = "Technetium"


class Ru(Element):
    atomic_number = 44
    atomic_name = "Ruthenium"


class Rh(Element):
    atomic_number = 45
    atomic_name = "Rhodium"


class Pd(Element):
    atomic_number = 46
    atomic_name = "Palladium"


class Ag(Element):
    atomic_number = 47
    atomic_name = "Silver"


class Cd(Element):
    atomic_number = 48
    atomic_name = "Cadmium"


class In(Element):
    atomic_number = 49
    atomic_name = "Indium"


class Sn(Element):
    atomic_number = 50
    atomic_name = "Tin"


class Sb(Element):
    atomic_number = 51
    atomic_name = "Antimony"


class Te(Element):
    atomic_number = 52
    atomic_name = "Tellurium"


class I(Element):
    atomic_number = 53
    atomic_name = "Iodine"


class Xe(Element):
    atomic_number = 54
    atomic_name = "Xenon"


class Cs(Element):
    atomic_number = 55
    atomic_name = "Cesium"


class Ba(Element):
    atomic_number = 56
    atomic_name = "Barium"


class La(Element):
    atomic_number = 57
    atomic_name = "Lanthanum"


class Ce(Element):
    atomic_number = 58
    atomic_name = "Cerium"


class Pr(Element):
    atomic_number = 59
    atomic_name = "Praseodymium"


class Nd(Element):
    atomic_number = 60
    atomic_name = "Neodymium"


class Pm(Element):
    atomic_number = 61
    atomic_name = "Promethium"


class Sm(Element):
    atomic_number = 62
    atomic_name = "Samarium"


class Eu(Element):
    atomic_number = 63
    atomic_name = "Europium"


class Gd(Element):
    atomic_number = 64
    atomic_name = "Gadolinium"


class Tb(Element):
    atomic_number = 65
    atomic_name = "Terbium"


class Dy(Element):
    atomic_number = 66
    atomic_name = "Dysprosium"


class Ho(Element):
    atomic_number = 67
    atomic_name = "Holmium"


class Er(Element):
    atomic_number = 68
    atomic_name = "Erbium"


class Tm(Element):
    atomic_number = 69
    atomic_name = "Thulium"


class Yb(Element):
    atomic_number = 70
    atomic_name = "Ytterbium"


class Lu(Element):
    atomic_number = 71
    atomic_name = "Lutetium"


class Hf(Element):
    atomic_number = 72
    atomic_name = "Hafnium"


class Ta(Element):
    atomic_number = 73
    atomic_name = "Tantalum"


class W(Element):
    atomic_number = 74
    atomic_name = "Tungsten"


class Re(Element):
    atomic_number = 75
    atomic_name = "Rhenium"


class Os(Element):
    atomic_number = 76
    atomic_name = "Osmium"


class Ir(Element):
    atomic_number = 77
    atomic_name = "Iridium"


class Pt(Element):
    atomic_number = 78
    atomic_name = "Platinum"


class Au(Element):
    atomic_number = 79
    atomic_name = "Gold"


class Hg(Element):
    atomic_number = 80
    atomic_name = "Mercury"


class Tl(Element):
    atomic_number = 81
    atomic_name = "Thallium"


class Pb(Element):
    atomic_number = 82
    atomic_name = "Lead"


class Bi(Element):
    atomic_number = 83
    atomic_name = "Bismuth"


class Po(Element):
    atomic_number = 84
    atomic_name = "Polonium"


class At(Element):
    atomic_number = 85
    atomic_name = "Astatine"


class Rn(Element):
    atomic_number = 86
    atomic_name = "Radon"


class Fr(Element):
    atomic_number = 87
    atomic_name = "Francium"


class Ra(Element):
    atomic_number = 88
    atomic_name = "Radium"


class Ac(Element):
    atomic_number = 89
    atomic_name = "Actinium"


class Th(Element):
    atomic_number = 90
    atomic_name = "Thorium"


class Pa(Element):
    atomic_number = 91
    atomic_name = "Protactinium"


class U(Element):
    atomic_number = 92
    atomic_name = "Uranium"


class Np(Element):
    atomic_number = 93
    atomic_name = "Neptunium"


class Pu(Element):
    atomic_number = 94
    atomic_name = "Plutonium"


class Am(Element):
    atomic_number = 95
    atomic_name = "Americium"


class Cm(Element):
    atomic_number = 96
    atomic_name = "Curium"


class Bk(Element):
    atomic_number = 97
    atomic_name = "Berkelium"


class Cf(Element):
    atomic_number = 98
    atomic_name = "Californium"


class Es(Element):
    atomic_number = 99
    atomic_name = "Einsteinium"


class Fm(Element):
    atomic_number = 100
    atomic_name = "Fermium"


class Md(Element):
    atomic_number = 101
    atomic_name = "Mendelevium"


class No(Element):
    atomic_number = 102
    atomic_name = "Nobelium"


class Lr(Element):
    atomic_number = 103
    atomic_name = "Lawrencium"


class Rf(Element):
    atomic_number = 104
    atomic_name = "Rutherfordium"


class Db(Element):
    atomic_number = 105
    atomic_name = "Dubnium"


class Sg(Element):
    atomic_number = 106
    atomic_name = "Seaborgium"


class Bh(Element):
    atomic_number = 107
    atomic_name = "Bohrium"


class Hs(Element):
    atomic_number = 108
    atomic_name = "Hassium"


class Mt(Element):
    atomic_number = 109
    atomic_name = "Meitnerium"


class Ds(Element):
    atomic_number = 110
    atomic_name = "Darmstadtium"


