from odoo import models, fields, api
class RoomType(models.Model):
    _name = 'room.type'
    _description = 'Loại phòng họp'
    name = fields.Char('Tên loại phòng', required=True)
    max_capacity = fields.Integer('Sức chứa tối đa')