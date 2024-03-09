from .extension import masrhmallow

class BookSchema(masrhmallow.Schema):
	class Meta:
		fields = ('id', 'title', 'author', 'year', 'created_at', 'updated_at')