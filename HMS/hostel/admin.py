from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class UserModel(UserAdmin):pass

admin.site.register(CustomUser, UserModel)

admin.site.register(AdminDean)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaff)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaff)