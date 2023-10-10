# -*- coding: utf-8 -*-

from odoo import models, fields


class Treatment(models.Model):
    _name = "hospital.treatment"
    _description = "Treatment"
    __rec_name = "name"


    name = fields.Char(string="Name", required=True)
    is_done = fields.Boolean(string="Is Done", default=False)
    appointment = fields.Many2one(comodel_name="dr_patients.appointment", string="Appointment")



