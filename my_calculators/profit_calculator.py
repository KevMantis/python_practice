# ----------------------------------------------------------------------
# Simple Profit Calculator
# version 0.1
# 
# Copyright (C) 2020 Kevin Green, San Antonio, TX
# email: kevgreen7@gmail.com
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------

def profit_calculator(sales, cost):
  profit_dollars = sales - cost
  profit_margin = (profit_dollars / sales)
  if profit_dollars <= 0:
    return profit_dollars, 100
  else:
    return profit_dollars, profit_margin

choice = 'Y'

while choice == 'Y':
  total_sales = float(input('''
Profit Calculator

Please enter the total sales dollars: '''))
  total_cost = float(input('Please enter the total cost: '))
  print('''
Profit dollars = ${:,.2f}
Profit margin = {:.2%}
'''.format(*profit_calculator(total_sales, total_cost)))
  choice_response = input('Would you like to calculate another? (Y/N): ')
  choice = choice_response.upper()