'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Ecs20130110DeleteSnapshotRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DiskId = None
		self.InstanceId = None
		self.SnapshotId = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.DeleteSnapshot.2013-01-10'
