from rest_framework import serializers
from rest_app.models import *


#Question Serializer
class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('question_id','question_title','question_content','date_posted','posted_by')

#Answer Serializer
class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('answer_id','question_id','answer_content','date_posted','posted_by')

#Comment Serializer
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('comment_id','question_id','answer_id','comment_content','commented_by')

#Vote Serializer
class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ('answer_id','question_id','increase')

