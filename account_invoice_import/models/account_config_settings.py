# -*- coding: utf-8 -*-
# © 2017 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class AccountConfigSettings(models.TransientModel):
    _inherit = 'account.config.settings'

    adjustment_credit_account_id = fields.Many2one(
        related='company_id.adjustment_credit_account_id')
    adjustment_debit_account_id = fields.Many2one(
        related='company_id.adjustment_debit_account_id')
    invoice_import_email = fields.Char(
        related='company_id.invoice_import_email')
    invoice_import_create_bank_account = fields.Boolean(
        related='company_id.invoice_import_create_bank_account')
