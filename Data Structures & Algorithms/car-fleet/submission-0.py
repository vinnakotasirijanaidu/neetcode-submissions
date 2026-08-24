class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair each position with its corresponding speed
        cars = zip(position, speed)
        
        # Sort cars by position in descending order (closest to destination first)
        sorted_cars = sorted(cars, reverse=True)
        
        fleets = 0
        current_fleet_time = 0.0
        
        for pos, spd in sorted_cars:
            # Calculate time needed to reach the target
            time_to_target = (target - pos) / spd
            
            # If this car takes more time than the leading fleet ahead of it,
            # it cannot catch up. It becomes the leader of a new fleet.
            if time_to_target > current_fleet_time:
                fleets += 1
                current_fleet_time = time_to_target
                
        return fleets
