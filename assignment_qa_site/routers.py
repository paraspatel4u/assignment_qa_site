from rest_app.api.viewsets import *
from rest_framework import routers


#routes to all apis
routers = routers.DefaultRouter()
routers.register('questions',QuestionViewSets,base_name='Question')
routers.register('answers',AnswerViewSets,base_name='Answer')
routers.register('comments',CommentViewSets,base_name='Comment')
routers.register('votes',VoteViewSets,base_name='Vote')