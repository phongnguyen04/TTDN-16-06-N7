# -*- coding: utf-8 -*-
from odoo import models, fields, api

class RoomBooking(models.Model):
    _name = 'room.booking'
    _description = 'Lịch đặt phòng họp'

    name = fields.Char(string='Mục đích họp', required=True)
    
    # KẾT NỐI VỚI modun nhan su
    employee_id = fields.Many2one('nhan_vien', string='Nhân viên đặt phòng', required=True)
    
    room_id = fields.Many2one('room.meeting', string='Phòng họp', required=True)
    start_time = fields.Datetime(string='Bắt đầu', required=True)
    end_time = fields.Datetime(string='Kết thúc', required=True)
    state = fields.Selection([
        ('draft', 'Nháp'),
        ('confirm', 'Đã xác nhận'),
        ('cancel', 'Đã hủy')
    ], string='Trạng thái', default='draft')
    participant_ids = fields.One2many('room.booking.participant', 'booking_id', string='Người tham gia')
    service_ids = fields.One2many('room.booking.service', 'booking_id', string='Dịch vụ đi kèm')
    approval_ids = fields.One2many('room.booking.approval', 'booking_id', string='Lịch sử phê duyệt')
    def action_confirm(self):
        """Hàm xử lý khi bấm nút Xác nhận"""
        for record in self:
            if record.state == 'draft':
                record.state = 'confirm'
        return True

    def action_cancel(self):
        """Hàm xử lý khi bấm nút Hủy (nên thêm để đầy đủ logic)"""
        for record in self:
            record.state = 'cancel'
        return True