{
    'name': 'Hospital Management System',
    'author': 'Felopater',

    'version': '1.0',
    'summary': 'Manage Hospital Patients',
    'depends': ['base','crm'],
    'data': [
        "security/ir.model.access.csv",
        'views/patient_view.xml',
        'views/menu.xml',
        'views/department_view.xml',
        'views/doctors_view.xml',
        "views/patient_log_view.xml",
        'views/res_partner_view.xml',
    ],
    "application": True,
    "installable": True,
}
