from rest_framework import serializers
from .models import Job, JobCategory,JobLocation

class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ['name', 'created_at']

class JobLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLocation
        fields = ['location', 'created_at']

class JobSerializers(serializers.ModelSerializer):
	jobcategory = JobCategorySerializer(read_only=True)
	location = JobLocationSerializer(read_only=True)
	class Meta:
	    model = Job
	    fields = "__all__"