# -*- coding:utf-8 -*-

import logging

from odoo.exceptions import UserError

from odoo import fields, models, api

logger = logging.getLogger(__name__)

class Student(models.Model):
     _name = "student"
     _description = "Módulo estudiante"
     
     name = fields.Char(string="Nombre del alumno",required=True)
     grade = fields.Integer(required=True, string="Grado")
     age = fields.Integer(required=True, string="Edad del alumno")
     student_number = fields.Integer(string="Número de estudiante")
     _sql_constraints = [
        ('student_number_uniq', 'unique (student_number)', 'El número de alumno debe de ser único')
     ]
