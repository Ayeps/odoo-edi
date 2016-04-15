# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2016 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'EDI GS1',
    'version': '0.1',
    'category': 'edi',
    'summary': 'GS1 – the global language of business',
    'licence': 'AGPL-3',
    'description': """
Global Trade Item Number (GTIN)
http://www.gs1.se/en/Standards/Identify/gtin/

Serial Shipping Container Code (SSCC)
http://www.gs1.se/en/Standards/Identify/sscc/

Global Location number (GLN)
http://www.gs1.se/en/Standards/Identify/gln/

GS1 Company prefix

Consignor - the party sending the goods.
Consignee - the party receiving the goods.
Forwarder - the party planning the transport on behalf of the consignor or consignee.
Carrier - the party transporting the goods between two points.

GS1 standards in use in Sweden 2016 to be used in 
for example ESAP20 edi-flow.

 +-----------------+-------------+---------------+
 | EDI standard    | Implemented |  in / out     |
 +-----------------+-------------+---------------+
 | PARTIN          |      N      |               |
 +-----------------+-------------+---------------+
 | PRICAT          |      N      |               |
 +-----------------+-------------+---------------+ 
 | ORDERS          |      Y      |   in          |
 +-----------------+-------------+---------------+ 
 | REPORD          |      Y      |   out         |
 +-----------------+-------------+---------------+            
 | CONTRL          |      Y      |   in/out      |
 +-----------------+-------------+---------------+                
 | ORDRSP          |      Y      |   in/out      |
 +-----------------+-------------+---------------+    
 | IFTMIN          |      N      |               |
 +-----------------+-------------+---------------+ 
 | IFTSTA          |      N      |               |
 +-----------------+-------------+---------------+ 
 | DESADV          |      Y      |   out         |
 +-----------------+-------------+---------------+    
 | RECADV          |      N      |               |
 +-----------------+-------------+---------------+ 
 | INVOIC          |      Y      |   out         |
 +-----------------+-------------+---------------+
 | FINSTA          |      N      |               |
 +-----------------+-------------+---------------+

http://www.gs1.org/sites/default/files/docs/EDI/edi_implementation_2015_-_detailed_report.pdf
page 9

Order
Order Response
Invoice
Despatch_advice
http://ocp.gs1.org/sites/faq/Pages/if-i-want-to-use-the-gs1-xml-standards-what-documents-should-i-download.aspx
http://www.gs1.se/EANCOM%202000/Index.htm


Res.partner has a GLN and product.product GTIN-numbers. SSCC can be
generated for stock.picking / stock.pack.


""",
    'author': 'Vertel AB',
    'website': 'http://www.vertel.se',
    'depends': ['edi_route','sale','product','stock','account'],
    'data': [
        'res_partner_view.xml',
        'product_view.xml',
        'res_company_view.xml',
        'ica_data.xml',
        #'security/ir.model.access.csv',
    ],
    'application': False,
    'installable': True,
 #   'demo': ['calendar_ics_demo.xml',],
}
# vim:expandtab:smartindent:tabstop=4s:softtabstop=4:shiftwidth=4:
