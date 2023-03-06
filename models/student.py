# -*- coding:utf-8 -*-

import logging

from odoo.exceptions import UserError

from odoo import fields, models, api

logger = logging.getLogger(__name__)

class Student(models.Model):
     _name = "student"
     _description = "Módulo estudiante"
     
     name = fields.Char(string="Nombre del alumno")
     grade = fields.Integer(string="Número de grado")
     age = fields.Integer(string="Edad del alumno")
     student_number = fields.Integer(unique=True,string="Numero de estudiante")