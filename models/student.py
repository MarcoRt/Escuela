# -*- coding:utf-8 -*-

import logging

from odoo.exceptions import UserError

from odoo import fields, models, api

logger = logging.getLogger(__name__)

class Student(models.Model):
     _name = "student"
     _description = "Módulo estudiante"
     
     name = fields.Char(string="Name",required=True)
     grade = fields.Integer(required=True, string="Grade")
     age = fields.Integer(required=True, string="Age")
     student_number = fields.Integer(string="Student number")
     _sql_constraints = [
        ('student_number_uniq', 'unique (student_number)', "Student number must be unique.")
     ]
