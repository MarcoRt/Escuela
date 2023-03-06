# -*- coding:utf-8 -*-

import logging

from odoo.exceptions import UserError

from odoo import fields, models, api

logger = logging.getLogger(__name__)

class Teacher(models.Model):
    _name = "teacher"
    _description = "Módulo maestro"
    
    name = fields.Char(string="Name")
    teacher_number = fields.Integer(string="ID number")
    subject_id = fields.One2many(comodel_name="subject",
        inverse_name="teacher_id",
        string="Subject",)
    _sql_constraints = [
        ('teacher_number_uniq', 'unique (teacher_number)', 'ID Number must be unique.')
    ]