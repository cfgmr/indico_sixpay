# -*- coding: utf-8 -*-
##
## This file is part of the SixPay Indico EPayment Plugin.
## Copyright (C) 2017 - 2018 Max Fischer
##
## This is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 3 of the
## License, or (at your option) any later version.
##
## This software is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with SixPay Indico EPayment Plugin;if not, see <http://www.gnu.org/licenses/>.
from __future__ import unicode_literals, division

import iso4217
import uuid
from werkzeug.exceptions import NotImplemented as HTTPNotImplemented

from indico.util.i18n import make_bound_gettext

#: internationalisation/localisation of strings
gettext = make_bound_gettext('payment_sixpay')


NON_DECIMAL_CURRENCY = {'MRU', 'MGA'}


def validate_currency(iso_code):
    """Check whether the currency can be properly handled by this plugin"""
    if iso_code in NON_DECIMAL_CURRENCY:
        raise HTTPNotImplemented(
            gettext("Unsupported currency '{0}' for SixPay. Please contact the organisers").format(iso_code)
        )


def to_small_currency(large_currency_amount, iso_code):
    """
    Convert from an amount from large currency to small currency, e.g. 2.3 Euro to 230 Eurocent

    :param large_currency_amount: the amount in large currency, e.g. ``2.3``
    :param iso_code: the ISO currency code, e.g. ``EUR``
    :return: the amount in small currency, e.g. ``230``
    """
    validate_currency(iso_code)
    exponent = iso4217.Currency(iso_code).exponent
    if exponent == 0:
        return large_currency_amount
    return large_currency_amount * (10 ** exponent)


def to_large_currency(small_currency_amount, iso_code):
    """Reverse of :py:func:`to_small_currency`"""
    validate_currency(iso_code)
    exponent = iso4217.Currency(iso_code).exponent
    if exponent == 0:
        return small_currency_amount
    return small_currency_amount / (10 ** exponent)


def jsonify_payment_form_data(form_data):
    """Compiles map with parameters which can be posted to the saferpay
    json api for payment page initialisation request
        see https://saferpay.github.io/jsonapi/index.html#Payment_v1_PaymentPage_Initialize
    """

    # transaction_parameters = {
    #     'ACCOUNTID': str(plugin_settings.get('account_id')),
    #     # indico handles price as largest currency, but six expects smallest
    #     # e.g. EUR: indico uses 100.2 Euro, but six expects 10020 Cent
    #     'AMOUNT': '{:.0f}'.format(to_small_currency(payment_data['amount'], payment_data['currency'])),
    #     'CURRENCY': payment_data['currency'],
    #     'DESCRIPTION': payment_data['order_description'][:50],
    #     'ORDERID': payment_data['order_identifier'][:80],
    #     'SHOWLANGUAGES': 'yes',
    # }
    # if plugin_settings.get('notification_mail'):
    #     transaction_parameters['NOTIFYADDRESS'] = plugin_settings.get('notification_mail')
    # transaction['SUCCESSLINK'] = url_for_plugin('payment_sixpay.success', registration.locator.uuid, _external=True)
    # transaction['BACKLINK'] = url_for_plugin('payment_sixpay.cancel', registration.locator.uuid, _external=True)
    # transaction['FAILLINK'] = url_for_plugin('payment_sixpay.failure', registration.locator.uuid, _external=True)
    # # where to asynchronously call back from SixPay
    # transaction['NOTIFYURL'] = url_for_plugin('payment_sixpay.notify', registration.locator.uuid, _external=True)

    # JSON API expects customer id and terminal id separately
    C_ID, T_ID = form_data['ACCOUNTID'].split('-')
    # JSON API wants request id, unique for each request and unchanged by resends. Use uuid generated from orderid
    REQUEST_ID = str(uuid.uuid3(uuid.NAMESPACE_OID, form_data['ORDERID'].encode('ascii', 'ignore')))
    json_data =  {
        "RequestHeader": {
            "SpecVersion": "1.8",
            "CustomerId": C_ID,
            "RequestId": REQUEST_ID,
            "RetryIndicator": 0
        },
        "TerminalId": T_ID,
        "Payment": {
            "Amount": {
                "Value": form_data['AMOUNT'],
                "CurrencyCode": form_data['CURRENCY'],
            },
            "OrderId": form_data['ORDERID'],
            "Description": form_data['DESCRIPTION']
        },
        "ReturnUrls": {
            "Success": form_data['SUCCESSLINK'],
            "Fail": form_data['FAILLINK'],
            "Abort": form_data['BACKLINK']
        },
        "Notification": {
            "NotifyUrl": form_data['NOTIFYURL']
        }
    }
    if form_data.get('NOTIFYADDRESS'):
        json_data["Notification"]["MerchantEmail"] = form_data['NOTIFYADDRESS']

    return json_data
