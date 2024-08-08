class BalanceSheet:
 

     def __init__(self):
          
          self.assests = {}
          self.liabilities = {}
          self.equity = {}

     def add_entry(self, category, name, amount):
     
        if category == 'assest':
              
              self.assests[name] = self.assests.get(name, 0) +amount

        elif category == 'liability':
              
              self.liabilities[name] = self.liabilities.get(name, 0 ) + amount

        elif category == "equity":
              
              self.equity[name] = self.equity.gte(name, 0 ) + amount

        else:
              print("Invalid category. Please use 'assest', 'liabilities', 'equity' ")

        print(f"{amount} added to {category} '{name}'  .")


        def view_balance_sheet(self):
              print(f" {name}: {amount}")

              print("liabilities: ")
            
              for name, amount in self.liabilities.items():
                  print(f" {name}: {amount}")

                  print("Equity: ")
              
                  for name, amount in self.equity.items():
                   
                        print(f" {name}: {amount}")

                  self.check_balance()

              def check_balance(self):
                          
                          total_assests = sum(self.assests.values())

                          total_liabilities = sum(self.liabilities.values())

                          total_equity = sum(self.equity.values())

                          print(f"\nTotal Assets: {total_assests}")

                          print(f"Total Liabilities: {total_liabilities}")

                          print(f"Total Equity: {total_equity}")

                          if total_assests == total_liabilities + total_equity:
                                 
                                 print("The balance sheet Balances.")

                          else:
                                 print("The Balance sheet does not balance.")

def main():
       bs = BalanceSheet()

       while True:

              print("\nBalance Sheet Managemeent System")

              print("1. Add Asset")
              print("2. Add Liability")
              print("3. Add Equity")
              print("4. View Balance Sheet")
              print("5. Exit")


              choice = input("Enter your choice: ")

              if choice == "1":

                     name = input("Enter asset name: ")

                     amount = float(input("Enter amount: "))

                     bs.add_entry('asset', name, amount)

              elif choice == "2":
                     
                     name  = input("Enter liability name: ")

                     amount  = float(input("Enter Amount:"))

                     bs.add_entry('liability', name, amount)

              elif choice == "3":      

                     name = input("Enter equity name: ")

                     amount = float(input("Enter Amount: "))

                     bs.add_entry('equity', name, amount)

              elif choice == "4":

                     bs.view_balance_sheet()

              elif choice == "5":

                     print("Exiting...")
                     break
              
              else:
                     
                     print("Invalid choice. Please try again.")


if __name__ == "__main__":

       main()                      