from django.db import models

# TransactionQuerySet: Custom QuerySet class for Transaction model
class TransactionQuerySet(models.QuerySet):
    
    # get_expenses method: Sirf expense type ke transactions return karta hai
    def get_expenses(self):
        return self.filter(type='expense')
    
    # get_income method: Sirf income type ke transactions return karta hai
    def get_income(self):
        return self.filter(type='income')
    
    # get_total_expenses method: Sab expenses ka total return karta hai
    def get_total_expenses(self):
        return self.get_expenses().aggregate(
            total=models.Sum('amount')  # Amount ka sum karta hai
        )['total'] or 0  # Agar total None ho toh 0 return karta hai

    # get_total_income method: Sab income ka total return karta hai
    def get_total_income(self):
        return self.get_income().aggregate(
            total=models.Sum('amount')  # Amount ka sum karta hai
        )['total'] or 0  # Agar total None ho toh 0 return karta hai
