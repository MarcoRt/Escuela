# -*- coding:utf-8 -*-

import logging

from odoo.exceptions import UserError

from odoo import fields, models, api

logger = logging.getLogger(__name__)


class StudentLines(models.Model):
    _name = "student_lines"
    _description = "Líneas de estudiantes"

    student = fields.Many2one(comodel_name="student", string="Student")
    student_number = fields.Integer(
        related="student.student_number", string="Student number"
    )
    grade = fields.Selection(
        related="student.grade", string="Grade")
    score = fields.Float(string="Score")
    subject_id = fields.Many2one(
        comodel_name="subject",
        inverse_name="students_ids",
        string="Subject",
    )
