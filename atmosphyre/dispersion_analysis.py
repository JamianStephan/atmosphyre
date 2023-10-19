class AD_simulation:
    """Docstring for class Foo.

    This text tests for the formatting of docstrings generated from output
    ``sphinx.ext.autodoc``. Which contain reST, but sphinx nests it in the
    ``<dl>``, and ``<dt>`` tags. Also, ``<tt>`` is used for class, method names
    and etc, but those will *always* have the ``.descname`` or
    ``.descclassname`` class.

    Term
        It is also possible to include definitions inside docstrings.
        They should be styled as a normal definition list.

    :Field List:
        It is also possible to include definitions inside docstrings.
        They should be styled as a normal definition list.

    .. [1] A footnote contains body elements, consistently indented by at
       least 3 spaces.

    .. [Citation] A citation contains body elements, consistently indented by at
       least 3 spaces.

    Normal ``<tt>`` (like the <tt> I just wrote here) needs to be shown with
    the same style as anything else with ````this type of markup````.

    It's common for programmers to give a code example inside of their
    docstring::

        from test_py_module import Foo

        myclass = Foo()
        myclass.dothismethod('with this argument')
        myclass.flush()

        print(myclass)


    Here is a link to :py:meth:`capitalize`.
    Here is a link to :py:meth:`__init__`.

    """
    def __init__(self,**kwargs):
        """Start the Foo.

        :param qux: The first argument to initialize class.
        :type qux: string
        :param spam: Spam me yes or no...
        :type spam: bool

        """
        self.input={}
        self.output={}
        
        self.config={
        'telescope_diameter':39, #m
        'wavefront_outer_scale':46, #m
        'median_seeing':.68, #arcsec
        'median_seeing_wl':.5, #um
        'simulation_scale':0.01, #arcsec/pixel, default is 0.01
        'HA_intervals':21, #number of intervals in the HA range to simulate
        'relative_plate_PA_angle':0, #deg, relative angle of the plate/apertures and PA=0. For PA=0 along aperture semi major axis, set to 90 deg
        'centring':0.5, #either 0.5 for mid index, or HA index
        'latitude':-24.6272, #deg
        'temperature':10, #deg C
        'humidity':14.5, #%
        'pressure':750.0 #mBa
        }
        
        self.config.update(kwargs)
        
        #note: for a slit spectrograph, this relative_plate_PA_angle becomes vital. will need to implement a slit aperture using "width" and "height",
        #and implement 
        
    def load_wavelengths(self,wavelengths=[]):
        """Start the Foo.

        :param qux: The first argument to initialize class.
        :type qux: string
        :param spam: Spam me yes or no...
        :type spam: bool

        """
        self.output['wavelengths']=np.array(wavelengths)
