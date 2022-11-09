from django.contrib import admin

# Register your models here.
from healthcare.models import UserProfile, DoctorProfile, Appointment
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
    readonly_fields = ['id', 'user_id']
    fields = ['id', 'phone', 'gender', 'birth_date', 'user_id']
    autocomplete_fields = ['user_id']
    list_display = ['id', 'user_name', 'phone', 'birth_date', 'user_id']

    def user_name(self, obj):
        return obj.user.username



class DoctorProfileAdmin(admin.ModelAdmin):
    model = DoctorProfile
    list_display = ['id', 'doctor_name', 'specialization', 'county', 'biography']

    def doctor_name(self, obj):
        return obj.user.username
    
    def user_id(self, obj):
        return obj.user.id

class AppointmentAdmin(admin.ModelAdmin):
    model = Appointment
    list_display = ['id', 'created_at', 'status', 'user_id', 'doctor_id']

    def doctor_name(self, obj):
        return obj.user.username
    
    def user_id(self, obj):
        return obj.user.id

admin.site.unregister(User)
admin.site.register(DoctorProfile, DoctorProfileAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(User, AccountsUserAdmin)