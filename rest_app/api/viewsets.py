from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response
from rest_app.models import *


#Question Viewset
class QuestionViewSets(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

#Answer Viewset
class AnswerViewSets(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

#Comment Viewset
class CommentViewSets(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

#Vote Viewset
class VoteViewSets(viewsets.ModelViewSet):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()

    def update(self, request, *args, **kwargs):
        try:
            upvote = Vote.objects.filter(answer_id=request.data['answer_id']).values_list('vote', flat=True)
            vote = upvote[-1]
        except Exception as e:
            print(e)

        if request.data['increase'] == "true":
            vote = vote + 1
            data = {"answer_id":request.data['answer_id'],"question_id":request.data['question_id'],"vote":vote}
            serializer = self.get_serializer(data=data)
            serializer.is_valid()
            self.perform_create(serializer)
            return Response(serializer.data)
        else:
            vote = vote - 1
            data = {"answer_id": request.data['answer_id'], "question_id": request.data['question_id'], "vote": vote}
            serializer = self.get_serializer(data=data)
            serializer.is_valid()
            self.perform_create(serializer)
            return Response(serializer.data)


