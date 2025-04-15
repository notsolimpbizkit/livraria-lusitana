from django.contrib import admin

class LivrariaAdminSite(admin.AdminSite):
    site_header = 'Livraria Lusitana Administration'
    site_title = 'Livraria Lusitana Admin Portal'
    index_title = 'Bem-vindo ao Portal Administrativo'
    
admin_site = LivrariaAdminSite(name='livraria_admin')