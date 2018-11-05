from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext
from django.contrib.contenttypes.models import ContentType


class ContentTypeAddWindow(BaseEditWindow):

	def _init_components(self):

		"""
		Здесь следует инициализировать компоненты окна и складывать их в
		:attr:`self`.
		"""
		super(ContentTypeAddWindow, self)._init_components()

		self.field__name = ext.ExtStringField(
			label=u'Название',
			name='name',
			allow_blank=False,
			anchor='100%')

	def _do_layout(self):
		"""
		Здесь размещаем компоненты в окне
		"""
		super(ContentTypeAddWindow, self)._do_layout()
		self.form.items.extend((
			self.field__name,
		))

	def set_params(self, params):
		"""
		Установка параметров окна

		:params: Словарь с параметрами, передается из пака
		"""
		super(ContentTypeAddWindow, self).set_params(params)
		self.height = 'auto'


class UserAddWindow(BaseEditWindow):

	def _init_components(self):

		"""
		Здесь следует инициализировать компоненты окна и складывать их в
		:attr:`self`.
		"""
		super(UserAddWindow, self)._init_components()

		self.field__first_name = ext.ExtStringField(
			label=u'Имя',
			name='first_name',
			allow_blank=True,
			anchor='100%')

		self.field__username = ext.ExtStringField(
			label=u'Логин',
			name='username',
			allow_blank=False,
			anchor='100%')

	def _do_layout(self):
		"""
		Здесь размещаем компоненты в окне
		"""
		super(UserAddWindow, self)._do_layout()
		self.form.items.extend((
			self.field__first_name,
			self.field__username,
		))

	def set_params(self, params):
		"""
		Установка параметров окна

		:params: Словарь с параметрами, передается из пака
		"""
		super(UserAddWindow, self).set_params(params)
		self.height = 'auto'


class GroupAddWindow(BaseEditWindow):

	def _init_components(self):

		"""
		Здесь следует инициализировать компоненты окна и складывать их в
		:attr:`self`.
		"""
		super(GroupAddWindow, self)._init_components()

		self.field__name = ext.ExtStringField(
			label=u'Название',
			name='name',
			allow_blank=False,
			anchor='100%')

	def _do_layout(self):
		"""
		Здесь размещаем компоненты в окне
		"""
		super(GroupAddWindow, self)._do_layout()
		self.form.items.extend((
			self.field__name,
		))

	def set_params(self, params):
		"""
		Установка параметров окна

		:params: Словарь с параметрами, передается из пака
		"""
		super(GroupAddWindow, self).set_params(params)
		self.height = 'auto'


class PermissionAddWindow(BaseEditWindow):

	def _init_components(self):

		"""
		Здесь следует инициализировать компоненты окна и складывать их в
		:attr:`self`.
		"""
		super(PermissionAddWindow, self)._init_components()
		self.field__name = ext.ExtStringField(
			label=u'Название',
			name='name',
			allow_blank=False,
			anchor='100%')
		print(ContentType.objects.all().values())
		self.field__content_type = make_combo_box(
			label=u'content type',
			name='content_type',
			allow_blank=False,
			anchor='100%',
			data=ContentType.objects.all())

		self.field__codename = ext.ExtStringField(
			label=u'codename',
			name='codename',
			allow_blank=False,
			anchor='100%')

	def _do_layout(self):
		"""
		Здесь размещаем компоненты в окне
		"""
		super(PermissionAddWindow, self)._do_layout()
		self.form.items.extend((
			self.field__name,
			self.field__content_type,
			self.field__codename,
		))


	def set_params(self, params):
		print(params)
		#obj.content_type = ContentType.objects.get(app_label=obj.content_type)
		"""
		Установка параметров окна

		:params: Словарь с параметрами, передается из пака
		"""
		super(PermissionAddWindow, self).set_params(params)
		self.height = 'auto'

