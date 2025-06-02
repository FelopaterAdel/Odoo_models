from odoo import models, fields

class PatientLog(models.Model):
    _name = 'hms.patient.log'
    _description = 'Patient Log'

    description = fields.Text()
    created_by = fields.Many2one('res.users', string="Created By")
    date = fields.Datetime()
    patient_id = fields.Many2one('hms.patient', string="Patient")
