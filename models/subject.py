# -*- coding:utf-8 -*-

import logging

from odoo.exceptions import UserError

from odoo import fields, models, api

logger = logging.getLogger(__name__)


class Subject(models.Model):
    _name = "subject"
    _description = "Módulo materias"
    
    @api.onchange("students_ids")
    def _onchange_students_ids(self):
        for line in self.students_ids:
            print("line.score ",line.score) 
            if line.score > 10:
                raise UserError("La calificación no puede ser mayor a 10")
            if line.score < 0:
                raise UserError("La calificación no puede ser menor a 0")
            
    name = fields.Char(string="Name")
    teacher_id = fields.Many2one(
        comodel_name="teacher",
        inverse_name="subject_id",
        string="Teacher",
    )
    teacher_number = fields.Integer(
        related="teacher_id.teacher_number", string="ID number"
    )
    grade = fields.Selection(
        selection=[
            ("one", "1"),
            ("two", "2"),
            ("three", "3"),
            ("four", "4"),
            ("five", "5"),
            ("six", "6"),
            ("seven", "7"),
            ("eight", "8"),
            ("nine", "9"),
            ("ten", "10"),
        ],
        default="one",
        string="Grade",
        copy=False,
    )
    classroom_number = fields.Selection(
        selection=[
            ("one", "1"),
            ("two", "2"),
            ("three", "3"),
            ("four", "4"),
            ("five", "5"),
            ("six", "6"),
            ("seven", "7"),
            ("eight", "8"),
            ("nine", "9"),
            ("ten", "10"),
        ],
        default="one",
        string="Classroom",
        copy=False,
    )
    state = fields.Selection(
        selection=[
            ("active", "Active"),
            ("inactive", "Inactive"),
        ],
        default="active",
        string="State",
        copy=False,
    )
    students_ids = fields.One2many(
        comodel_name="student_lines",
        inverse_name="subject_id",
        string="Students",
    )
    start_date = fields.Datetime(string="Start date", copy=False)
    end_date = fields.Datetime(string="End date", copy=False)
    schedule = fields.Selection(
        selection=[
            ("7_8", "De 7 a 8"),
            ("8_9", "De 8 a 9"),
            ("9_10", "De 9 a 10"),
            ("10_11", "De 10 a 11"),
            ("11_12", "De 11 a 12"),
            ("12_13", "De 12 a 13"),
            ("13_14", "De 13 a 14"),
            ("14_15", "De 14 a 15"),
            ("15_16", "De 15 a 16"),
            ("16_17", "De 16 a 17"),
            ("17_18", "De 17 a 18"),
            ("18_19", "De 18 a 19"),
            ("19_20", "De 19 a 20"),
        ],
        default="7_8",
        string="Schedule",
        copy=False,
    )

    def activate_student(self):
        self.state = "active"

    def inactive_student(self):
        self.state = "inactive"
