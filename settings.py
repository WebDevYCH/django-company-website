# This is a fairly standard Django settings file, with some special additions
# that allow addon applications to auto-configure themselves. If it looks 
# unfamiliar, please see our documentation:
#
#   http://docs.divio.com/en/latest/reference/configuration-settings-file.html
#
# and comments below.


# INSTALLED_ADDONS is a list of self-configuring Divio Cloud addons - see the
# Addons view in your project's dashboard. See also the addons directory in 
# this project, and the INSTALLED_ADDONS section in requirements.in.

INSTALLED_ADDONS = [
    # Important: Items listed inside the next block are auto-generated.
    # Manual changes will be overwritten.

    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    # </INSTALLED_ADDONS>
]

# Now we will load auto-configured settings for addons. See:
#
#   http://docs.divio.com/en/latest/reference/configuration-aldryn-config.html
#
# for information about how this works.
#
# Note that any settings you provide before the next two lines are liable to be
# overwritten, so they should be placed *after* this section.
import os
import sys
import aldryn_addons.settings
aldryn_addons.settings.load(locals())
# Your own Django settings can be applied from here on. Key settings like
# INSTALLED_APPS, MIDDLEWARE and TEMPLATES are provided in the Aldryn Django
# addon. See:
#
#   http://docs.divio.com/en/latest/how-to/configure-settings.html
#
# for guidance on managing these settings.
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..")
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))  # 使apps目录优于其他目录被import语句检索到

# 文章列表分页数量
ARTICLE_PAGINATE_BY = 8
LANGUAGE_CODE = "en-us"
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 书单影单分页数量
BOOK_MOVIE_PAGINATE_BY = 8

# 搜索结果分页
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 7
INSTALLED_APPS.extend([
    # Extend the INSTALLED_APPS setting by listing additional applications here
    'apps.blog',
    'apps.notice',
    'apps.setting',
    'apps.comment',
    'notifications',
    'apps.myzone',
    'apps.mysite',
    
    'xadmin',
    'haystack',
    'mdeditor',
    'ckeditor',
    'crispy_forms',
    'rest_framework',
])

CKEDITOR_CONFIGS = {
    'comment_ckeditor': {
        'toolbar': 'custom',
        'toolbar_custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ["TextColor", "BGColor", 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ["Smiley", "SpecialChar", 'Blockquote','CodeSnippet'],
        ],
        'width': 'auto',
        'height': '180',
        'tabSpaces': 4,
        'removePlugins': 'elementspath',
        'resize_enabled': False,

        'extraPlugins': ','.join(['codesnippet', 'uploadimage', 'widget', 'lineutils', ]),
    },

    'default': {
        'toolbar': 'custom',
        'toolbar_custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ["TextColor", "BGColor", 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ["Smiley", "SpecialChar", 'Blockquote'],
        ],
        'width': 'auto',
        'height': '180',
        'tabSpaces': 4,
        'removePlugins': 'elementspath',
        'resize_enabled': False,
    }
}
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'apps.blog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
DJANGO_NOTIFICATIONS_CONFIG = {
    'USE_JSONFIELD': True
}

# 数据库编码配置
SILENCED_SYSTEM_CHECKS = ['mysql.E001']

# To see the settings that have been applied, use the Django diffsettings 
# management command. 
# See https://docs.divio.com/en/latest/how-to/configure-settings.html#list
