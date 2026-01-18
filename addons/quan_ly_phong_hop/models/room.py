from odoo import models, fields, api

class RoomMeeting(models.Model):
    _name = 'room.meeting'
    _description = 'Thông tin phòng họp'

    name = fields.Char(string='Tên phòng', required=True)
    capacity = fields.Integer(string='Sức chứa')
    location = fields.Char(string='Vị trí (Tầng)')

    phong_ban_id = fields.Many2one(
        'phong_ban',
        string='Phòng ban quản lý',
        required=True,
        ondelete='restrict'
    )

    asset_ids = fields.Many2many(
        'tai_san',
        'room_meeting_tai_san_rel',
        'room_id',
        'tai_san_id',
        string='Tài sản trong phòng'
    )
