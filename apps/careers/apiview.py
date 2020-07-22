from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import JobSerializers
from .models import Job, JobCategory, JobLocation
from rest_framework import pagination

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 7 # change the records per page from here

    page_size_query_param = 'page_size'

class JobsListing(ListAPIView):
    # set the pagination and serializer class

	pagination_class = StandardResultsSetPagination
	serializer_class = JobSerializers

	def get_queryset(self):
        # filter the queryset based on the filters applied

		queryList = Job.objects.all()
		location = self.request.query_params.get('location', None)
		category = self.request.query_params.get('category', None)
		jobtype1 = self.request.query_params.get('jobtype1', None)
		jobtype2 = self.request.query_params.get('jobtype2', None)
		jobtype3 = self.request.query_params.get('jobtype3', None)
		jobtype4 = self.request.query_params.get('jobtype4', None)
		jobtype5 = self.request.query_params.get('jobtype5', None)

		if location:
		    queryList = queryList.filter(location = location)
		if category:
		    queryList = queryList.filter(jobcategory = category)
		if jobtype1:
		    queryList = queryList.filter(jobtype = jobtype1)
		if jobtype2:
		    queryList = queryList.filter(jobtype = jobtype2)
		if jobtype3:
		    queryList = queryList.filter(jobtype = jobtype3)
		if jobtype4:
		    queryList = queryList.filter(jobtype = jobtype4)
		if jobtype5:
		    queryList = queryList.filter(jobtype = jobtype5)

        # sort it if applied on based on price/points

		# if sort_by == "price":
		#     queryList = queryList.order_by("price")
		# elif sort_by == "points":
		#     queryList = queryList.order_by("points")
		return queryList



