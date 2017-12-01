``indico_sixpay`` - SIX EPayment Plugin for Indico
==================================================

.. image:: https://readthedocs.org/projects/indico_sixpay/badge/?version=latest
    :target: http://indico_sixpay.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. toctree::
    :maxdepth: 1
    :caption: Subtopics Overview:

    source/configuration
    source/design
    Changelog <source/changelog>
    Module Index <source/api/modules>

The :py:mod:`indico_sixpay` adds an EPayment option for
the *SIX Payment Services* provider
to the *Indico* event management system.

Overview
--------

If the plugin is enabled, event participants can select the ``SixPay`` payment method during the EPayment checkout.
Payment is performed via the **Saferpay Payment Page**, an external service provided by SIX Payment Services.
The plugin handles the user interaction inside Indico, and the secure, asynchronous transaction with SIX Payment Services.

The plugin must be installed for an entire Indico instance.
It can be enabled and configured for the entire instance and per individual event.
Note that a valid account with *SIX Payment Services* is required to receive payments.

The plugin follows the **Saferpay Payment Page** specification version ``5.1``.

*This is a prerelease for Indico 2.0.*
*The legacy plugin for Indico 1.2 is `hosted on github <https://github.com/maxfischer2781/indico_sixpay/tree/indico-1.2>`_.*

Usage Overview
--------------

To enable the plugin, it must be installed for the python version running ``indico``.

.. code:: bash

    python -m pip install indico_sixpay

Once installed, it can be enabled in the administrator and event settings.
Configuration uses the same options for global defaults and event specific overrides.

Contributing and Feedback
-------------------------

The project is hosted on `github <https://github.com/maxfischer2781/indico_sixpay>`_.
Feedback, pull requests and other contributions are always welcome.
If you have issues or suggestions, check the issue tracker: |issues|

Disclaimer
----------

This plugin is in no way endorsed, supported or provided by SIX, Indico or any other service, provider or entity.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

----------

.. |issues| image:: https://img.shields.io/github/issues-raw/maxfischer2781/indico_sixpay.svg
   :target: https://github.com/maxfischer2781/indico_sixpay/issues
   :alt: Open Issues

Documentation built from ``indico_sixpay`` |version| at |today|.