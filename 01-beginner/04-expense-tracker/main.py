import pandas as pd

FILE_NAME = 'expenses.csv'

try:
    df = pd.read_csv('expenses.csv')
except FileNotFoundError:
    print("There is no file with such file.")

class Expense:
    def __init__(self, dataframe):
        self.df = dataframe        
    
    def category_summary(self):
      total_category = df.groupby('category')['amount'].sum()
      print(total_category)
    
    def monthly_summary(self):

      df['date'] = pd.to_datetime(df['date'])
      monthly_totals = df.groupby(df['date'].dt.to_period('M'))['amount'].sum()
      print(monthly_totals)

    def add_expense(self):
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        date = input("Enter date (YYYY-MM-DD) [Leave blank for today]: ")
        description = input("Enter the description: ")
        if not date:
           date = pd.Timestamp.now().strftime('%Y-%m-%d')

        if self.df.empty:
            next_id = 1.0
        else:
            next_id = int(self.df['id'].max()) + 1.0

        new_expense = {
           'id' : next_id,
           'category': category,
           'amount': amount,
           'date': date,
           'description' : description
         }
    
        self.df = pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)
        self.df.to_csv(FILE_NAME, index=False)

        print(f"\n Success: Added {category} expense of ${amount:.2f} for {date}! With its description {description}.")
    
    def view_expenses(self):
       print(df)
       


tracker = Expense(df)

track_add_view = int(input("Do you want to track your expenses, Add a new one , or to view the expenses?, To track (type 1), To add (type 2), To view (type 3): "))

if track_add_view == 1:
   tracker.category_summary()
   tracker.monthly_summary()
if track_add_view == 2:
   tracker.add_expense()
if track_add_view == 3:
   tracker.view_expenses()
