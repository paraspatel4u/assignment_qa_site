from django.db import models
from django.utils.text import slugify

#Question Model

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_title = models.CharField(max_length=100)
    question_content = models.TextField(max_length=50000)
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.TextField(max_length=20)
    slug = models.SlugField(max_length=40)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question_title)
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.question_title

#Answer Model

class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_content = models.TextField(max_length=50000)
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.TextField(max_length=20)

    def __str__(self):
        return self.answer_content


#comment Model

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    comment_content = models.TextField(max_length=1000)
    commented_by = models.TextField(max_length=20)

    def __str__(self):
        return self.commented_by


#Vote Model

class Vote(models.Model):
    vote_id = models.AutoField(primary_key=True)
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    vote = models.IntegerField()
    increase = models.BooleanField(default=True)