from rest_framework import serializers, viewsets
from .models import Notes

class NoteSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        user = self.context['request'].user
        note = Note.objects.create(user=user, **validated_data)
        return note

    class Meta: 
        model = Notes
        fields = ('title', 'content')

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Notes.objects.all()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return Notes.objects.none()
        else:
            return Notes.objects.filter(user=user)
