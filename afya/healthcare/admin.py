from django.contrib import admin

# Register your models here.
from healthcare.models import UserProfile, DoctorProfile, Appointment, Region, Schedule, DoctorApplication
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

class UserProfileInLine(admin.StackedInline):
    model = UserProfile
    can_delete = False

class AccountsUserAdmin(AuthUserAdmin):
    list_display = ('id', 'username', 'email')
    search_fields = ('id', 'username', 'email')
    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(AccountsUserAdmin, self).add_view(*args, **kwargs)
    
    def change_view(self, *args, **kwargs):
        self.inlines = [UserProfileInLine]
        return super(AccountsUserAdmin, self).change_view(*args, **kwargs)

class UserProfileAdmin(admin.ModelAdmin):
    # readonly_fields = ['id', 'user_id']
    # fields = ['id', 'phone', 'gender', 'birth_date', 'user_id']
    autocomplete_fields = ['user_id']
    list_display = ['id', 'user_name', 'phone', 'birth_date', 'user_id']

    def user_name(self, obj):
        return obj.user.username



class DoctorProfileAdmin(admin.ModelAdmin):
    model = DoctorProfile
    # fields = ['id', ]
    list_display = ['id', 'doctor_name', 'specialization', 'region_name', 'biography', 'has_schedule']

    def doctor_name(self, obj):
        return obj.user.username
    
    def user_id(self, obj):
        return obj.user.id

    def region_name(self, obj):
        return obj.county.county

class AppointmentAdmin(admin.ModelAdmin):
    model = Appointment
    list_display = ['id', 'created_at', 'status', 'user_id', 'patient_name','doctor_id', 'doctor_name']

    def doctor_name(self, obj):
        return obj.doctor.user.first_name

    def patient_name(self, obj):
        return obj.user.user.first_name
    
    def user_id(self, obj):
        return obj.user.id

class RegionAdmin(admin.ModelAdmin):
    model = Region
    list_display = ['id', 'county']

class ScheduleAdmin(admin.ModelAdmin):
    model = Region
    list_display = ['id', 'doctor']

class ApplicationAdmin(admin.ModelAdmin):
    model = DoctorApplication
    list_display = ['id', 'status']

admin.site.unregister(User)
admin.site.register(DoctorProfile, DoctorProfileAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(DoctorApplication, ApplicationAdmin)
admin.site.register(User, AccountsUserAdmin)