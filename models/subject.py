# -*- coding:utf-8 -*-

import logging

from odoo.exceptions import UserError

from odoo import fields, models, api

logger = logging.getLogger(__name__)

class Subject(models.Model):
    _name = "subject"
    _description = "Módulo materias"
    
    name = fields.Char(string="Nombre de la materia")
    #teacher_number = fields.Integer(unique=True,string="Numero de estudiante")
    grade = fields.Integer(string="Número de grado")
    classroom_number = fields.Integer(string="Número de aula")
    state = fields.Selection(selection=[
        ('active','Activo'),
        ('inactive','Inactivo'),
    ],default='active', string='Estados', copy=False)
    students_ids = fields.One2many(comodel_name="student_lines",
        inverse_name="subject_id",
        string="Alumnos",)
    start_date = fields.Datetime(string='Fecha de inicio de la materia', copy=False)
    end_date = fields.Datetime(string='Fecha fin de la materia', copy=False)
    schedule = fields.Selection(selection=[
        ('7_8','De 7 a 8'),
        ('8_9','De 8 a 9'),
        ('9_10','De 9 a 10'),
        ('10_11','De 10 a 11'),
        ('11_12','De 11 a 12'),
        ('12_13','De 12 a 13'),
        ('13_14','De 13 a 14'),
        ('14_15','De 14 a 15'),
        ('15_16','De 15 a 16'),
        ('16_17','De 16 a 17'),
        ('17_18','De 17 a 18'),
        ('18_19','De 18 a 19'),
        ('19_20','De 19 a 20'),
    ],default='7_8', string='Horario', copy=False)
    
    def activate_student(self):
        self.state = 'active'
     
    def inactivate_student(self):
        self.state = 'inactive'