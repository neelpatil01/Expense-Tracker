import sqlite3
from expense_model import Expense
from budget_model import Budget

FILE_NAME = 'user.db'
    
conn = sqlite3.Connection(FILE_NAME)
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS expenses (
            date text,
            category text,
            subcategory text,
            cost real)""")

c.execute("""CREATE TABLE IF NOT EXISTS budgets (
            cost real, date text)""")

                      #budgets

def get_budgets():
    with conn:
        c.execute("""SELECT rowid, * FROM budgets""")
        return c.fetchall()
    
def get_budget_by_id(rowid):
    with conn:
        c.execute("""SELECT rowid, * FROM budgets WHERE rowid=?""",(rowid,))
        return c.fetchone()

def add_budget(budget):
    with conn:
        c.execute("""INSERT INTO budgets VALUES (?,?)""", (budget.cost,
                                                           budget.date))
        
def delete_budget(id):
    with conn:
        c.execute("""DELETE FROM budgets WHERE rowid=?""", (id,))
        
def find_budget_id(budget):
    with conn:
        return c.execute("""SELECT rowid, * FROM budgets WHERE cost=? AND date=?""",
                  (budget.cost, budget.date)).fetchone()
        return c.fetchone()
    
def find_budget_by_date(budget):
    with conn:
        return c.execute("""SELECT rowid, * FROM budgets WHERE date=?""",
                  (budget.date,)).fetchone()
    
def update_budget(budget, id, tag):
    if tag == "cost":
        with conn:
            c.execute("""UPDATE budgets SET cost=?
                      WHERE rowid=?""", (budget.cost, id))
    if tag == "date":
        with conn:
            c.execute("""UPDATE budgets SET date=?
                      WHERE rowid=?""", (budget.date, id))

                      #expenses
                     
def get_expenses():
    with conn:
        c.execute("""SELECT rowid, * FROM expenses""")
        return c.fetchall()

def add_expense(expense):
    with conn:
        c.execute("""INSERT INTO expenses VALUES (?,?,?,?)""",(expense.date, 
                    expense.category, expense.subcategory, expense.cost))
    
def update_expense(expense, id, tag):
    if tag == "category":
        with conn:
            c.execute("""UPDATE expenses SET category=?
                      WHERE rowid=?""", (expense.category, id))
    if tag == "subcategory":
        with conn:
            c.execute("""UPDATE expenses SET subcategory=?
                      WHERE rowid=?""", (expense.subcategory,id))
    if tag == "cost":
        with conn:
            c.execute("""UPDATE expenses SET cost=?
                      WHERE rowid=?""", (expense.cost, id))
    if tag == "date":
        with conn:
            c.execute("""UPDATE expenses SET date=?
                      WHERE rowid=?""", (expense.date, id))

def delete_expense(id):
    with conn:
        c.execute("""DELETE FROM expenses WHERE rowid=?""", (id,))

def find_id(expense):
    with conn:
        c.execute("""SELECT rowid, * FROM expenses WHERE category=? 
                  AND subcategory=? 
                  AND cost=? AND date=?""", (expense.category, 
                  expense.subcategory, expense.cost, expense.date))
        return c.fetchone()
