from art import logo
import os


print(logo)
print("Welcome to the secret auction program.")
participants = []


def add_new_participants(participant_name, participant_bid):
    my_dict = {
        "name": participant_name,
        "bid" : participant_bid
    }
    return participants.append(my_dict)

def run():
  access = True
  
  while access:
    mayor = 0
    name = input("What is your name ?: ")
    bid = int(input("What's your bid?: $"))
    add_new_participants(name,bid)
    level2 = True
    
    while level2:
      should_continue  = input("Are there any other bidders? Type 'yes' or 'no'.\n")
      if (should_continue  == "no"):
        for participant in range(len(participants)):      
          if(participants[participant]["bid"] > mayor):
            mayor = participants[participant]["bid"]
            winner = participants[participant]["name"]
        print(f"the winner is {winner} with a bid of ${mayor}")
        
        access = False
        level2 = False

      elif(should_continue  == "yes"):
        os.system ("clear") 
        level2 = False
      
      else:
        print("invalid option.")    


if __name__== "__main__":
  run()

