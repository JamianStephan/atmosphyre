"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"

def calculate_FWHM(wavelength,airmass,config):
    """Start the Foo.

    :param qux: The first argument to initialize class.
    :type qux: string
    :param spam: Spam me yes or no...
    :type spam: bool

    """
    D = float(config['telescope_diameter'])
    L0 = float(config['wavefront_outer_scale'])
    median_seeing = float(config['median_seeing'])
    median_seeing_wl = float(config['median_seeing_wl'])
       
    r0=0.1*median_seeing**(-1)*(wavelength/median_seeing_wl)**1.2*airmass**(-0.6)  
    F_kolb=1/(1+300*(D/L0))-1
    
    FWHM_atm=median_seeing*airmass**(0.6)*(wavelength/median_seeing_wl)**(-0.2)*np.sqrt(1+F_kolb*2.183*(r0/L0)**0.356)
    FWHM_dl=0.212*wavelength/D
    
    FWHM_total=np.sqrt(FWHM_atm**2+FWHM_dl**2)

    return FWHM_total

