from django.db import models
from account.models import User
from common.models import Media
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    clicked_count = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class SubjectTitle(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Subject Title"
        verbose_name_plural = "Subject Titles"




class Subject(models.Model):
    SUBJECT_TYPE_CHOICES = [
        ('local', 'LOCAL'),
        ('global', 'GLOBAL'),
    ]
    name = models.CharField(max_length=255)
    subject_type = models.CharField(max_length=255, choices=SUBJECT_TYPE_CHOICES)
    subject_title = models.ForeignKey(SubjectTitle, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"


class UserSubject(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total_test_ball = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.subject}"
    
    class Meta:
        verbose_name = "User Subject"
        verbose_name_plural = "User Subjects"


class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"



class Step(models.Model):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Step"
        verbose_name_plural = "Steps"
        ordering = ['order']


class Club(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Club"
        verbose_name_plural = "Clubs"


class UserClub(models.Model):
    user = models.ManyToManyField(User, related_name="users")
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.club}"
    
    class Meta:
        verbose_name = "User Club"
        verbose_name_plural = "User Clubs"


class ClubMeetings(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Club Meeting"
        verbose_name_plural = "Club Meetings"


class StepLesson(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.ForeignKey(Media, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Step Lesson"
        verbose_name_plural = "Step Lessons"


class StepTest(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('multiple', 'MULTIPLE'),
        ('single', 'SINGLE'),
    ]
    STEP_TEST_TYPE_CHOICES = [
        ('midterm', 'MIDTERM'),
        ('final', 'FINAL'),
    ]
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    ball_for_each_test = models.FloatField(null=True)
    question_count = models.PositiveIntegerField(default=0)
    question_type = models.CharField(max_length=255, choices=QUESTION_TYPE_CHOICES)
    step_test_type = models.CharField(max_length=255, choices=STEP_TEST_TYPE_CHOICES)
    time_for_question = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.step} - {self.step_test_type}"
    
    class Meta:
        verbose_name = "Step Test"
        verbose_name_plural = "Step Tests"
        ordering = ['step_test_type']


class TestQuestion(models.Model):
    steptest = models.ForeignKey(StepTest, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.steptest} - {self.id}"
    
    class Meta:
        verbose_name = "Test Question"
        verbose_name_plural = "Test Questions"
        ordering = ['id']



class TestAnswer(models.Model):
    test_question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    answer_text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.test_question} - {self.answer_text}"
    
    class Meta:
        verbose_name = "Test Answer"
        verbose_name_plural = "Test Answers"



class UserTestResult(models.Model):
    test_question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_answer = models.ForeignKey(TestAnswer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.test_question}"
    
    class Meta:
        verbose_name = "User Test Result"
        verbose_name_plural = "User Test Results"



class UserTotalResult(models.Model):
    step_test = models.ForeignKey(StepTest,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ball = models.FloatField()
    correct_ans = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.user} - {self.step_test}"
    
    class Meta:
        verbose_name = "User Total Result"
        verbose_name_plural = "User Total Results"
