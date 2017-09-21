from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    num_tokens = models.IntegerField()
    num_flags = models.IntegerField()

    def as_json(self):
        return dict(
            user_id = self.id,
            first_name = self.first_name,
            last_name = self.last_name,
            username = self.username,
            num_tokens = self.num_tokens,
            num_flags = self.num_flags
        )

class Bet(models.Model):
    privacy = models.BooleanField()
    response_limit = models.IntegerField()
    question = models.CharField(max_length=200)
    description = models.TextField()
    outcome = models.BooleanField()
    min_buyin = models.IntegerField()
    per_person_cap = models.IntegerField()
    initiation = models.DateTimeField()
    expiration = models.DateTimeField()

    def as_json(self):
        return dict(
            bet_id = self.id,
            privacy = self.privacy,
            response_limit = self.response_limit,
            question = self.question,
            description = self.description,
            outcome = self.outcome,
            min_buyin = self.min_buyin,
            per_person_cap = self.per_person_cap,
            initiation = self.initiation,
            expiration = self.expiration
        )

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bet = models.ForeignKey(Bet, on_delete=models.CASCADE)
    answer = models.BooleanField()
    amount = models.IntegerField()
    resp_timestamp = models.DateTimeField()
    
    def as_json(self):
        return dict(
            response_id = self.id,
            user_id = self.user,
            bet = self.bet,
            answer = self.answer,
            amount = self.amount,
            resp_timestamp = self.resp_timestamp
        )
