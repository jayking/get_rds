'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Rds20140815DescribeBackupPolicyRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DBInstanceId = None

	def getapiname(self):
		return 'rds.aliyuncs.com.DescribeBackupPolicy.2014-08-15'
