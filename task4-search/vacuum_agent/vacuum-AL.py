class VacuumCleanerAgent:
    vacuum_cleaner_number = 1 # Class variable to keep track of the number of vacuum cleaner agents created.

    def __init__(self, environment_data):
        """
        :param environment_data: Dictionary like {'Living Room': 'Dirty', 'Kitchen': 'Clean'} for different types of layouts.
        """
        self.name = "vacuum Cleaner_"+str(VacuumCleanerAgent.vacuum_cleaner_number)
        self.locations = environment_data
        VacuumCleanerAgent.vacuum_cleaner_number += 1

    def sense_and_act(self):
        """
        Iterates through all locations in the layout and cleans them.
        """
        print(f"--- Starting Cleaning Cycle for {self.name} ---")
        
        # Looping through the dictionary, layout, keys and values
        for location, status in self.locations.items():
            print(f"Checking: {location} (Status: {status})")
            
            if status == 'Dirty':
                print(f"[ACTION] Sucking dirt in {location}...")
                self.locations[location] = 'Clean' # Updating the status of the 'room'/environment to clean.
                print(f"[RESULT] {location} is now Clean.")
            else:
                print(f"[INFO] {location} is already clean. Moving on...")
        
        print(f"--- Cleaning Cycle Complete for {self.name} ---")

# This can now be scaled to any number of rooms
house_1 = {
    'Living Room': 'Dirty',
    'Kitchen': 'Clean',
    'Master Bedroom': 'Dirty',
    'Bedroom_1': 'Dirty',
    'Bedroom_2': 'Dirty',
    'Bedroom_3': 'Dirty',
    'Bedroom_4': 'Dirty',
    'Hallway': 'Clean',
    'Porch': 'Dirty',
    'Basement': 'Dirty'
}
house_2 = {
    'Living Room': 'Dirty',
    'Kitchen': 'Clean',
    'Master Bedroom': 'Dirty',
    'Bedroom_1': 'Dirty',
    'Hallway': 'Clean',
}

# Creating the vacuum Object for house1 and house2
agent = VacuumCleanerAgent(house_1)
agent2 = VacuumCleanerAgent(house_2)

# Running the agents
agent.sense_and_act()
agent2.sense_and_act()

# Verifying the final state of the 2 houses.
print(f"\nFinal House Status: {house_1}")
print(f"Final House Status: {house_2}")