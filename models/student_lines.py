# -*- coding:utf-8 -*-

import logging

from odoo.exceptions import UserError

from odoo import fields, models, api

logger = logging.getLogger(__name__)

class StudentLines(models.Model):
     _name = "student_lines"
     _description = "Líneas de estudiantes"
     
     student = fields.Many2one(comodel_name="student", string="Alumno")
     student_number = fields.Integer(related="student.student_number",string="Número de estudiante")
     score = fields.Float(string="Calificación")
     subject_id = fields.Many2one(comodel_name="subject",
        inverse_name="students_ids",
        string="Materia",)