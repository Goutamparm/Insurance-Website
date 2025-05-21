from django.db import models

# Insurance Plan (singular)
class Plans(models.Model):  # Changed from Plans to Plan
    heading = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Use DecimalField for price
    plan_type = models.CharField(max_length=100, choices=[
        ('car', 'Car Insurance'),
        ('health', 'Health Insurance'),
        ('house', 'House Insurance'),
        ('life', 'Life Insurance')
    ])
    image = models.ImageField(upload_to='plans/', blank=True, null=True)  # Optional image field

    def __str__(self):
        return self.heading  # Corrected from title to heading


# News/Announcements
class News(models.Model):
    heading = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading  # Corrected from title to heading
# In main/models.py

# main/models.py
class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)  # ✅ Add this
    selected_plan = models.CharField(max_length=100)  # ✅ Add this



