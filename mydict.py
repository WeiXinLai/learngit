#!/usr/bin/env python3
class Dict(dict):
	def __init__(self,**kw):
		super().__init__(**kw)
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has not attribut '%s'" % key)
	def _setattr__(self,key,value):
		self[key]=value


