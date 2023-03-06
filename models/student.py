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
     student_number = fields.Integer(string="Numero de estudiante")
     subject_id = fields.Many2one(comodel_name="subject",
        inverse_name="students_ids",
        string="Materia",)