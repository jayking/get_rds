'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Rds20140815DescribeRealtimeDiagnosesRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DBInstanceId = None
		self.EndTime = None
		self.Page = None
		self.PageSize = None
		self.StartTime = None
		self.ownerId = None
		self.resourceOwnerAccount = None
		self.resourceOwnerId = None

	def getapiname(self):
		return 'rds.aliyuncs.com.DescribeRealtimeDiagnoses.2014-08-15'
