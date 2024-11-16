from django.db import models





class Actor(models.Model):
    fullname=models.CharField(max_length=50)
    
    def __str__(self):
        return self.fullname








class Movie(models.Model):
    title=models.CharField( max_length=50)
    year=models.DateField(auto_now=True)
    time=models.DateTimeField( auto_now=True)
    lang=models.CharField(max_length=50)
    dt_rl=models.DateField(auto_now=True)
    rel_country=models.CharField(max_length=50)

    def __str__(self):
        return self.title




class MovieCast(models.Model):
    act_id=models.ForeignKey(Actor, on_delete=models.CASCADE)
    role=models.CharField(max_length=50)
    move_id=models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.role





class Director(models.Model):
    fullname=models.CharField(max_length=60)

    def __str__(self):
        return self.fullname



class MovieDirection(models.Model):
    dir_id=models.ForeignKey(Director, on_delete=models.CASCADE)
    mov_id=models.ForeignKey(Movie, on_delete=models.CASCADE)










class Genres(models.Model):
    gen_title=models.CharField( max_length=50)

    def __str__(self):
        return self.gen_title



class MovieGenres(models.Model):
    mov_id=models.ForeignKey(Movie, on_delete=models.CASCADE)
    gen_id=models.ForeignKey(Genres, on_delete=models.CASCADE)




class Reviewer(models.Model):
    name=models.CharField( max_length=50)


    def __str__(self):
        return self.name


class Rating(models.Model):
    mov_id=models.ForeignKey(Movie, on_delete=models.CASCADE)
    rev_id=models.ForeignKey(Reviewer,on_delete=models.CASCADE)

    def __str__(self):
        return self.rev_id
