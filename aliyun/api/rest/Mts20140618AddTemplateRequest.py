'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Mts20140618AddTemplateRequest(RestApi):
	def __init__(self,domain='mts.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.Audio = None
		self.Container = None
		self.MuxConfig = None
		self.Name = None
		self.TransConfig = None
		self.Video = None

	def getapiname(self):
		return 'mts.aliyuncs.com.AddTemplate.2014-06-18'
