Usage
=====

.. _installation:

Installation
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

.. autofunction:: lumache.calculate_FWHM

.. autofunction:: test.calculate_FWHM

.. autofunction:: test.test.calculate_FWHM

.. automodule:: test.test

.. automodule:: lumache

test22


The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

.. code-block:: console

   (.venv) $ pip install atmosphyre

.. automodule:: atmosphyre.dispersion_functions

.. code-block:: console

   (.venv) $ pip install dipsersion_functions

.. autofunction:: atmosphyre.dispersion_functions.calculate_FWHM

pls

.. autoclass:: atmosphyre.dispersion_analysis.AD_simulation

hmm 

.. automodule:: atmosphyre.dispersion_functions
   :members:
   :private-members:
   :special-members:
test

.. automodule:: atmosphyre.dispersion_analysis
   :members:
   :private-members:
   :special-members: