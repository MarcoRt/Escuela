# -*- coding:utf-8 -*-

import logging

from odoo.exceptions import UserError

from odoo import fields, models, api

logger = logging.getLogger(__name__)

class Teacher(models.Model):
    _name = "teacher"
    _description = "Módulo maestro"
    
    name = fields.Char(string="Nombre del maestro")
    teacher_number = fields.Integer(unique=True, string="Cédula del maestro")