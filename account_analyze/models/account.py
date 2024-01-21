# -*- coding: utf-8 -*-


from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)


class AccountMoveCategory(models.Model):
    """ Account move category """
    _name = "account.move.category"
    _description = "Category of invoice"

    name = fields.Char("name")


class AccountMoveEvent(models.Model):
    """ Account move event """
    _name = "account.move.event"
    _description = "Event of invoice"

    name = fields.Char("name")


class AccountMove(models.Model):
    """ Account move event """
    _inherit = "account.move"

    category_id = fields.Many2one("account.move.category", string="Category")
    event_id = fields.Many2one("account.move.event", string="Event")


class AccountInvoiceReport(models.Model):
    _inherit = 'account.invoice.report'

    category_id = fields.Many2one(comodel_name="account.move.category", string="Category")
    event_id = fields.Many2one(comodel_name="account.move.event", string="Event")

    def _select(self):
        return super()._select() + ", move.category_id as category_id, move.event_id as event_id"
