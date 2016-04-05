# -*- coding: utf-8 -*-
######################################################################################################
#
# Copyright (C) B.H.C. sprl - All Rights Reserved, http://www.bhc.be
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied,
# including but not limited to the implied warranties
# of merchantability and/or fitness for a particular purpose
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
######################################################################################################

{
    "name": "Ingram Test 4",
    "version": "3.0.0",
    "depends": [
                "base",
                "sale",
                "product",
                "stock",
                "purchase",
                "procurement"],
    "author": "BHC",
    "category": "Hidden",
    "description": """
    This module provides an XML integration between Odoo and Ingram Micro Servers. 
    It allows to maintain the Ingram product catalog and price list up to date automatically. 
    It also provides a real-time integration for quotation, sales, purchases and deliveries. 
    Actions in Odoo generate requests toward Ingram to get informations, or to place an order directly, 
    without using any external tool or website. 
    
    2.0: Add the name of file to import for products categories and products in the configuration. Supplier informations are now synchronized in the o2m fields to add other supplier on a product. 
    2.1 : Improve products categories synchronization
    """,
    'images': ['images/main_screenshot.png','images/Sale_Order.png','images/Ingram_Category.png','images/Purchase_Order.png','images/Delivery.png',],
    'website': 'http://www.bhc.be/en/application/ingram-micro',
    "data": [
             "product_view.xml",
    "purchase_view.xml",
    "sale_view.xml",
    "stock_picking_view.xml",
    "ingram_config_view.xml",
    "procurement.xml",
    "security/ir.model.access.csv",
    'scheduler.xml'],
    'demo_xml': [],
    'installable': True,
    'active': False,
}