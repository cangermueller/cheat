reStructuredText
################

References
==========

http://docutils.sourceforge.net/docs/user/rst/quickref.html

Commands
========

- ``rst2html``
- ``rst2latex``
- ``rst2odt``


Headings
========

Heading1
########

Heading2
========

Heading 3
---------

Heading 4
~~~~~~~~~

Formats
=======

*italic - emphasis*

**bold - strong emphasis**

`interpretet`

``code - inline literal``

Links
=====

Publication [1]_, [2]_

.. [1] Ghahramani, Zoubin, Matthew J Beal, Gatsby Computational, and Neuroscience Unit. “Variational Inference for Bayesian Mixtures of Factor Analysers.” NIPS, 1999. `Link <http://www.gatsby.ucl.ac.uk/publications/papers/06-2000.pdf>`_
.. [2] Publication 2


External link to Google_

.. _Google: http://www.google.com

External link to `Google <http://www.google.com>`_

Internal link like here_

.. _here: 

Here is the internally referenced text

Heading1_ is an implicit reference

Downloadable file :download:`here <rst.rst>`

Lists
=====
- Enum1
- Enum2
  Description Enum2

* Enum1
* Enum2

+ Enum1
+ Enum2

1. Item1
2. Item2
   Description Item2

Tables
======

==  ====  =====
Id  Name  Value
==  ====  =====
1   n1    1.0
2   n2    2.0
3   n3    3.0
==  ====  =====


Source code
===========

Simple code example in Python::

  print('Hello world')

Inline :code:`a = 10`

.. code:: python

  def sum_values(a, b):
    a = np.random.rand(3, 4)
    return a + b

Doctest blocks
==============
>>> a = 1
>>> b = 2
>>> c = a + b
>>> c
3

Math
====
Inline :math:`a=\frac{b}{c}`

.. math::

  \alpha = e^{\frac{\beta}{\gamma}}

Comments
========
.. This line
  and the following lines 
  will not be shown
