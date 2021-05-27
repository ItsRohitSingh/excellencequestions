from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
  cname = serializers.CharField(max_length=50, required=True)
  EmailID = serializers.EmailField(max_length=100, required=False)

  def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
    return Todo.objects.create(
      cname=validated_data.get('cname'),
      EmailID=validated_data.get('EmailID'),
    )

  def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the todo item instance in the database
    instance.text = validated_data.get('cname', instance.text)
    instance.save()
    return instance

  class Meta:
    model = Todo
    fields = (
      'id',
      'cname',
      'EmailID'
    )