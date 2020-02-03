# -*- coding:utf-8 -*-
import xadmin
from .models import *
from xadmin import views


# 此类可以定义admin后台显示的字段，比如文章列表显示标题，创建时间，
class JobAdmin(object):

    list_display = ['id', 'user', 'title','slug','last_date','location']
    search_fields = ['name','role','title','location']
    list_filter = ['id', 'title', 'created_at', 'status','last_date',]
    
    model_icon = 'fa fa-user'
    # 修改默认排序
    ordering = ['-id']

    readonly_field = ['views','created_at']

    exclude = ['views','created_at']

    list_display_link = ['name','created_at']

    # style_fields = {'body':'ueditor'}
class JobCategoryAdmin(object):
    list_display = ['id','name']
    search_fields = ['name']
    model_icon = 'fa fa-file-text'

class ApplicantAdmin(object):
    list_display = ['id','user','job']
    search_fields = ['job']
    model_icon = 'fa fa-file-text'
    
xadmin.site.register(Applicant,ApplicantAdmin)
xadmin.site.register(JobCategory,JobCategoryAdmin)
xadmin.site.register(Job,JobAdmin)
class TeamExpertAdmin(object):

    list_display = ['id', 'name', 'role', 'about', 'facebook','twitter','instagram','linkedin','github']
    search_fields = ['name','role']
    list_filter = ['id', 'name', 'created_time', 'status']
    
    model_icon = 'fa fa-user'
    # 修改默认排序
    ordering = ['-id']

    # 设置只读字段
    readonly_field = ['views','created_time']

    # 不显示某一字段
    exclude = ['views','created_time']

    list_display_link = ['name','created_time']

    # style_fields = {'body':'ueditor'}

xadmin.site.register(TeamExpert,TeamExpertAdmin)
class PortfolioAdmin(object):
    # 展示的字段
    list_display = ['id', 'title','slug' ,'status']
    # 按文章名进行搜索
    search_fields = ['title']
    # 筛选
    list_filter = ['id', 'title', 'created_time', 'status']
    # 修改图标
    model_icon = 'fa fa-briefcase'
    # 修改默认排序
    ordering = ['-id']

    # 设置只读字段
    readonly_field = ['']

    # 不显示某一字段
    exclude = ['views','created_time']

    list_display_link = ['title']
xadmin.site.register(Portfolio,PortfolioAdmin)
class PostAdmin(object):
    # 展示的字段
    list_display = ['id', 'title', 'created_time', 'category', 'status']
    # 按文章名进行搜索
    search_fields = ['title']
    # 筛选
    list_filter = ['id', 'title', 'created_time', 'category', 'status']
    # 修改图标
    model_icon = 'fa fa-file-text'
    # 修改默认排序
    ordering = ['-id']

    # 设置只读字段
    readonly_field = ['']

    # 不显示某一字段
    exclude = ['views','created_time']

    list_display_link = ['title']

    # style_fields = {'body':'ueditor'}


class CategoryAdmin(object):
    list_display = ['id','name']
    search_fields = ['name']
    model_icon = 'fa fa-file-text'


class TagAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-file-text'


# 图书分类
class BookCategoryAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-book'


# 图书
class BookAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-book'


# 图书标签
class BookTagAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-book'


# 电影分类
class MovieCategoryAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-film'


# 电影
class MovieAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-film'


# 电影标签
class MovieTagAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-film'


class MeanListAdmin(object):
    list_display = ['id', 'title', 'link', 'icon', 'status']
    search_field = ['title']
    model_icon = 'fa fa-list'


class CoursesAdmin(object):
    list_display = ['id','title','views','category','created_time','comments','numbers']
    model_icon = 'fa fa-gift'


class MessagesAdmin(object):
    list_display = ['id', 'name']
    model_icon = 'fa fa-commenting'


xadmin.site.register(Post,PostAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Tag,TagAdmin)

xadmin.site.register(BookCategory,BookCategoryAdmin)
xadmin.site.register(Book,BookAdmin)
xadmin.site.register(BookTag,BookTagAdmin)

xadmin.site.register(MovieCategory,MovieCategoryAdmin)
xadmin.site.register(Movie,MovieAdmin)
xadmin.site.register(MovieTag,MovieTagAdmin)

xadmin.site.register(MeanList,MeanListAdmin)

xadmin.site.register(Courses,CoursesAdmin)
xadmin.site.register(Messages,MessagesAdmin)


# 修改xadmin的基础配置
class BaseSetting(object):
    # 允许使用主题
    enable_themes = True
    use_bootswatch = True


# 修改xadmin的全局配置
class GlobalSetting(object):
    site_title = 'Eastward notebook'
    site_footer = '2019'

    # Models收起功能
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView,BaseSetting )