#
# Chem.atoms
# Author: Eunhak Lee(@return0927)
#


class Element:
    def __init__(self, num=0):
        self.atomic_number = num

    def __repr__(self):
        return self.__class__.__name__


class H(Element):
    atomic_name = "Hydrogen"

    def __init__(self):
        super().__init__(1)


class He(Element):
    atomic_name = "Helium"

    def __init__(self):
        super().__init__(2)


class Li(Element):
    atomic_name = "Lithium"

    def __init__(self):
        super().__init__(3)


class Be(Element):
    atomic_name = "Beryllium"

    def __init__(self):
        super().__init__(4)


class B(Element):
    atomic_name = "Boron"

    def __init__(self):
        super().__init__(5)


class C(Element):
    atomic_name = "Carbon"

    def __init__(self):
        super().__init__(6)


class N(Element):
    atomic_name = "Nitrogen"

    def __init__(self):
        super().__init__(7)


class O(Element):
    atomic_name = "Oxygen"

    def __init__(self):
        super().__init__(8)


class F(Element):
    atomic_name = "Fluorine"

    def __init__(self):
        super().__init__(9)


class Ne(Element):
    atomic_name = "Neon"

    def __init__(self):
        super().__init__(10)


class Na(Element):
    atomic_name = "Sodium"

    def __init__(self):
        super().__init__(11)


class Mg(Element):
    atomic_name = "Magnesium"

    def __init__(self):
        super().__init__(12)


class Al(Element):
    atomic_name = "Aluminum"

    def __init__(self):
        super().__init__(13)


class Si(Element):
    atomic_name = "Silicon"

    def __init__(self):
        super().__init__(14)


class P(Element):
    atomic_name = "Phosphorus"

    def __init__(self):
        super().__init__(15)


class S(Element):
    atomic_name = "Sulfur"

    def __init__(self):
        super().__init__(16)


class Cl(Element):
    atomic_name = "Chlorine"

    def __init__(self):
        super().__init__(17)


class Ar(Element):
    atomic_name = "Argon"

    def __init__(self):
        super().__init__(18)


class K(Element):
    atomic_name = "Potassium"

    def __init__(self):
        super().__init__(19)


class Ca(Element):
    atomic_name = "Calcium"

    def __init__(self):
        super().__init__(20)


class Sc(Element):
    atomic_name = "Scandium"

    def __init__(self):
        super().__init__(21)


class Ti(Element):
    atomic_name = "Titanium"

    def __init__(self):
        super().__init__(22)


class V(Element):
    atomic_name = "Vanadium"

    def __init__(self):
        super().__init__(23)


class Cr(Element):
    atomic_name = "Chromium"

    def __init__(self):
        super().__init__(24)


class Mn(Element):
    atomic_name = "Manganese"

    def __init__(self):
        super().__init__(25)


class Fe(Element):
    atomic_name = "Iron"

    def __init__(self):
        super().__init__(26)


class Co(Element):
    atomic_name = "Cobalt"

    def __init__(self):
        super().__init__(27)


class Ni(Element):
    atomic_name = "Nickel"

    def __init__(self):
        super().__init__(28)


class Cu(Element):
    atomic_name = "Copper"

    def __init__(self):
        super().__init__(29)


class Zn(Element):
    atomic_name = "Zinc"

    def __init__(self):
        super().__init__(30)


class Ga(Element):
    atomic_name = "Gallium"

    def __init__(self):
        super().__init__(31)


class Ge(Element):
    atomic_name = "Germanium"

    def __init__(self):
        super().__init__(32)


class As(Element):
    atomic_name = "Arsenic"

    def __init__(self):
        super().__init__(33)


class Se(Element):
    atomic_name = "Selenium"

    def __init__(self):
        super().__init__(34)


class Br(Element):
    atomic_name = "Bromine"

    def __init__(self):
        super().__init__(35)


class Kr(Element):
    atomic_name = "Krypton"

    def __init__(self):
        super().__init__(36)


class Rb(Element):
    atomic_name = "Rubidium"

    def __init__(self):
        super().__init__(37)


class Sr(Element):
    atomic_name = "Strontium"

    def __init__(self):
        super().__init__(38)


class Y(Element):
    atomic_name = "Yttrium"

    def __init__(self):
        super().__init__(39)


class Zr(Element):
    atomic_name = "Zirconium"

    def __init__(self):
        super().__init__(40)


class Nb(Element):
    atomic_name = "Niobium"

    def __init__(self):
        super().__init__(41)


class Mo(Element):
    atomic_name = "Molybdenum"

    def __init__(self):
        super().__init__(42)


class Tc(Element):
    atomic_name = "Technetium"

    def __init__(self):
        super().__init__(43)


class Ru(Element):
    atomic_name = "Ruthenium"

    def __init__(self):
        super().__init__(44)


class Rh(Element):
    atomic_name = "Rhodium"

    def __init__(self):
        super().__init__(45)


class Pd(Element):
    atomic_name = "Palladium"

    def __init__(self):
        super().__init__(46)


class Ag(Element):
    atomic_name = "Silver"

    def __init__(self):
        super().__init__(47)


class Cd(Element):
    atomic_name = "Cadmium"

    def __init__(self):
        super().__init__(48)


class In(Element):
    atomic_name = "Indium"

    def __init__(self):
        super().__init__(49)


class Sn(Element):
    atomic_name = "Tin"

    def __init__(self):
        super().__init__(50)


class Sb(Element):
    atomic_name = "Antimony"

    def __init__(self):
        super().__init__(51)


class Te(Element):
    atomic_name = "Tellurium"

    def __init__(self):
        super().__init__(52)


class I(Element):
    atomic_name = "Iodine"

    def __init__(self):
        super().__init__(53)


class Xe(Element):
    atomic_name = "Xenon"

    def __init__(self):
        super().__init__(54)


class Cs(Element):
    atomic_name = "Cesium"

    def __init__(self):
        super().__init__(55)


class Ba(Element):
    atomic_name = "Barium"

    def __init__(self):
        super().__init__(56)


class La(Element):
    atomic_name = "Lanthanum"

    def __init__(self):
        super().__init__(57)


class Ce(Element):
    atomic_name = "Cerium"

    def __init__(self):
        super().__init__(58)


class Pr(Element):
    atomic_name = "Praseodymium"

    def __init__(self):
        super().__init__(59)


class Nd(Element):
    atomic_name = "Neodymium"

    def __init__(self):
        super().__init__(60)


class Pm(Element):
    atomic_name = "Promethium"

    def __init__(self):
        super().__init__(61)


class Sm(Element):
    atomic_name = "Samarium"

    def __init__(self):
        super().__init__(62)


class Eu(Element):
    atomic_name = "Europium"

    def __init__(self):
        super().__init__(63)


class Gd(Element):
    atomic_name = "Gadolinium"

    def __init__(self):
        super().__init__(64)


class Tb(Element):
    atomic_name = "Terbium"

    def __init__(self):
        super().__init__(65)


class Dy(Element):
    atomic_name = "Dysprosium"

    def __init__(self):
        super().__init__(66)


class Ho(Element):
    atomic_name = "Holmium"

    def __init__(self):
        super().__init__(67)


class Er(Element):
    atomic_name = "Erbium"

    def __init__(self):
        super().__init__(68)


class Tm(Element):
    atomic_name = "Thulium"

    def __init__(self):
        super().__init__(69)


class Yb(Element):
    atomic_name = "Ytterbium"

    def __init__(self):
        super().__init__(70)


class Lu(Element):
    atomic_name = "Lutetium"

    def __init__(self):
        super().__init__(71)


class Hf(Element):
    atomic_name = "Hafnium"

    def __init__(self):
        super().__init__(72)


class Ta(Element):
    atomic_name = "Tantalum"

    def __init__(self):
        super().__init__(73)


class W(Element):
    atomic_name = "Tungsten"

    def __init__(self):
        super().__init__(74)


class Re(Element):
    atomic_name = "Rhenium"

    def __init__(self):
        super().__init__(75)


class Os(Element):
    atomic_name = "Osmium"

    def __init__(self):
        super().__init__(76)


class Ir(Element):
    atomic_name = "Iridium"

    def __init__(self):
        super().__init__(77)


class Pt(Element):
    atomic_name = "Platinum"

    def __init__(self):
        super().__init__(78)


class Au(Element):
    atomic_name = "Gold"

    def __init__(self):
        super().__init__(79)


class Hg(Element):
    atomic_name = "Mercury"

    def __init__(self):
        super().__init__(80)


class Tl(Element):
    atomic_name = "Thallium"

    def __init__(self):
        super().__init__(81)


class Pb(Element):
    atomic_name = "Lead"

    def __init__(self):
        super().__init__(82)


class Bi(Element):
    atomic_name = "Bismuth"

    def __init__(self):
        super().__init__(83)


class Po(Element):
    atomic_name = "Polonium"

    def __init__(self):
        super().__init__(84)


class At(Element):
    atomic_name = "Astatine"

    def __init__(self):
        super().__init__(85)


class Rn(Element):
    atomic_name = "Radon"

    def __init__(self):
        super().__init__(86)


class Fr(Element):
    atomic_name = "Francium"

    def __init__(self):
        super().__init__(87)


class Ra(Element):
    atomic_name = "Radium"

    def __init__(self):
        super().__init__(88)


class Ac(Element):
    atomic_name = "Actinium"

    def __init__(self):
        super().__init__(89)


class Th(Element):
    atomic_name = "Thorium"

    def __init__(self):
        super().__init__(90)


class Pa(Element):
    atomic_name = "Protactinium"

    def __init__(self):
        super().__init__(91)


class U(Element):
    atomic_name = "Uranium"

    def __init__(self):
        super().__init__(92)


class Np(Element):
    atomic_name = "Neptunium"

    def __init__(self):
        super().__init__(93)


class Pu(Element):
    atomic_name = "Plutonium"

    def __init__(self):
        super().__init__(94)


class Am(Element):
    atomic_name = "Americium"

    def __init__(self):
        super().__init__(95)


class Cm(Element):
    atomic_name = "Curium"

    def __init__(self):
        super().__init__(96)


class Bk(Element):
    atomic_name = "Berkelium"

    def __init__(self):
        super().__init__(97)


class Cf(Element):
    atomic_name = "Californium"

    def __init__(self):
        super().__init__(98)


class Es(Element):
    atomic_name = "Einsteinium"

    def __init__(self):
        super().__init__(99)


class Fm(Element):
    atomic_name = "Fermium"

    def __init__(self):
        super().__init__(100)


class Md(Element):
    atomic_name = "Mendelevium"

    def __init__(self):
        super().__init__(101)


class No(Element):
    atomic_name = "Nobelium"

    def __init__(self):
        super().__init__(102)


class Lr(Element):
    atomic_name = "Lawrencium"

    def __init__(self):
        super().__init__(103)


class Rf(Element):
    atomic_name = "Rutherfordium"

    def __init__(self):
        super().__init__(104)


class Db(Element):
    atomic_name = "Dubnium"

    def __init__(self):
        super().__init__(105)


class Sg(Element):
    atomic_name = "Seaborgium"

    def __init__(self):
        super().__init__(106)


class Bh(Element):
    atomic_name = "Bohrium"

    def __init__(self):
        super().__init__(107)


class Hs(Element):
    atomic_name = "Hassium"

    def __init__(self):
        super().__init__(108)


class Mt(Element):
    atomic_name = "Meitnerium"

    def __init__(self):
        super().__init__(109)


class Ds(Element):
    atomic_name = "Darmstadtium"

    def __init__(self):
        super().__init__(110)


