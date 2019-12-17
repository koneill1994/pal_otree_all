from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1.00, participation_fee=0.00, doc="")

SESSION_CONFIGS = [
    # dict(
       # name='pal',
       # display_name="pal",
       # num_demo_participants=4,
       # app_sequence=['pal']
    # ),
    # dict(
       # name='pal_hometime',
       # display_name="pal_hometime",
       # num_demo_participants=1,
       # app_sequence=['pal_hometime']
    # ),
    dict(
       name='pal_exam',
       display_name="pal_exam",
       num_demo_participants=1,
       app_sequence=['pal_exam']
    ),
    # must not contain duplicate elements
    # need to combine hometime and schooltime into a single app
    dict(
       name='ratpal_full',
       display_name="ratpal_full",
       num_demo_participants=4,
       app_sequence=['ratpal_full','pal_exam']
    ),
    # dict(
       # name='cr_survey',
       # display_name="cr_survey",
       # num_demo_participants=1,
       # app_sequence=['cr_survey']
    # ),
    # {
    # 'name': 'minimum_effort_game',
    # 'display_name': "Minimum Effort Game",
    # 'num_demo_participants': 4,
    # 'app_sequence': ['minimum_effort_game'],    
    # },

]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'truststudy'   #environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '^p9cj=3dv%(_5pbva%=$k*u@2$@$614p#3r1(px(o2nzb9&mo7'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
