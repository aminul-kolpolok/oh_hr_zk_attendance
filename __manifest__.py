# -*- coding: utf-8 -*-
#############################################################################
#
#    Kolpolok Ltd.
#
#    Copyright (C) 2022-TODAY Kolpolok Technologies
#    Author: Kolpolok Software Solutions
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This mosule is widely served in the hope that it will be useful,
#    but Wit support of your company; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
#    If you face any problem in this module, please contact of our support team:
#	info@kolpolok.com
#    
#
#############################################################################
{
    'name': 'Kolpolok Biometric Device Integration',
    'version': '16.0.1.1.0',
    'summary': """You canIntegrate with your Biometric Device With HR Attendance (Face + Thumb)""",
    'description': 'This module integrates Odoo with the biometric device(Model: ZKteco uFace 202)',
    'category': 'Generic Modules/Human Resources',
 #    'live_test_url': 'https://youtu.be/RHSHHU7nzTo',
    'author': 'Kolpolok Software Limited, HRMS',
 #   'live_test_url': 'https://youtu.be/RHSHHU7nzTo',
    'company': 'Kolpolok Limited',
    'website': "http://www.openhrms.com",
    'depends': ['base_setup', 'hr_attendance'],
    'data': [
        'security/ir.model.access.csv',
        'views/zk_machine_view.xml',
        'views/zk_machine_attendance_view.xml',
        'data/download_data.xml'
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
