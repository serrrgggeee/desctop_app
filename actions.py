from objectpack import observer
from objectpack.ui import ModelEditWindow
from functools import partial
from objectpack.filters import ColumnFilterEngine, FilterByField


from objectpack.actions import ObjectPack
from m3 import actions

from m3.actions.results import OperationResult
from m3.actions.context import ActionContextDeclaration
from .ui import ContentTypeAddWindow, UserAddWindow, GroupAddWindow, PermissionAddWindow
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group, Permission
from django.db import transaction


class ContentTypePack(ObjectPack):
	model = ContentType
	#edit_window = add_window = ContentTypeAddWindow
	edit_window = add_window = ModelEditWindow.fabricate(
			ContentType
		)
	add_to_menu = True
	filter_engine_clz = ColumnFilterEngine

	f = partial(FilterByField, model)

	columns = [
        {
            'data_index': 'name',
            'header': u'Название',
            'width': 2,
        }
	]


class UserPack(ObjectPack):
	model = User
	edit_window = add_window = UserAddWindow
	add_to_menu = True

	filter_engine_clz = ColumnFilterEngine
	f = partial(FilterByField, model)
	columns = [
        {
            'data_index': 'first_name',
            'header': u'Имя',
            'width': 2,
        },
        {
            'data_index': 'username',
            'header': u'Логин',
            'width': 2,
        },
	]


class GroupPack(ObjectPack):
	model = Group
	edit_window = add_window = GroupAddWindow
	add_to_menu = True
	filter_engine_clz = ColumnFilterEngine

	f = partial(FilterByField, model)

	columns = [
        {
            'data_index': 'name',
            'header': u'Название',
            'width': 2,
        }
	]


class PermissionPack(ObjectPack):
	model = Permission
	#edit_window = add_window = PermissionAddWindow
	edit_window = add_window = ModelEditWindow.fabricate(
			Permission
		)
	add_to_menu = True
	filter_engine_clz = ColumnFilterEngine

	f = partial(FilterByField, model)

	columns = [
        {
            'data_index': 'name',
            'header': u'Название',
            'width': 2,
        }
	]

