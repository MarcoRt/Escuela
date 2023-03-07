# -*- coding:utf-8 -*-

import logging

from odoo.exceptions import UserError

from odoo import fields, models, api

logger = logging.getLogger(__name__)


class Student(models.Model):
    _name = "student"
    _description = "Módulo estudiante"

    name = fields.Char(string="Name", required=True)
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
    age = fields.Integer(required=True, string="Age")
    student_number = fields.Integer(string="Student number")
    student_lines_ids = fields.One2many(comodel_name="student_lines",
        inverse_name="student",
        string="Student lines",)
    _sql_constraints = [
        (
            "student_number_uniq",
            "unique (student_number)",
            "Student number must be unique.",
        )
    ]
