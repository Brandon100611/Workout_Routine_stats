import datetime

def run_workout_audit():
    print(f"--- OFFICIAL WORKOUT AUDIT: {datetime.date.today()} ---")
    print("\nCoach: George Benitez | Goal: System Shock / Density")
    
    print("\nLeg day: Exercise | Weight (LBS)/Reps")
    # --- EXERCISE 1: Seated Leg Curls ---
    # George pushed you to 190 lbs here.
    curls_vol = (100 * 8) + (140 * 8) + (180 * 8) + (190 * 7)
    curls_reps = 8 + 8 + 8 + 7
    curls_max = 190
    print(f"\nSeated Leg Curls Max Set: {curls_max} lbs")
    print(f"Seated Leg Curls Total Volume: {curls_vol} lbs")
    print(f"Seated Leg Curls Total Reps: {curls_reps} reps")

    # --- EXERCISE 2: Leg Extensions ---
    # This is where you hit the 215 lb 'Gunslinger' set.
    ext_vol = (170 * 4) + (210 * 8) + (215 * 8)
    ext_reps = 4 + 8 + 8
    ext_max = 215
    print(f"\nLeg Extension Max Set: {ext_max} lbs")
    print(f"Leg Extension Total Volume: {ext_vol} lbs")
    print(f"Leg Extension Total Reps: {ext_reps} reps")

    # --- YOUR TASK: COMPLETE THE REST ---
    # Use the pattern below to add the Leg Press (45lb plates = 45), 
    # RDL Machine, Hip Adduction, and Calves.
    
    # 1. Calculate Leg Press (Hint: 4 plates per side = 8 total plates * 45)
    # leg_press_vol = (400 * 7) + (380 * 7) # Replace with your math

    # --- EXERCISE 3: Leg press ---
    # This is where you hit the 410 lb set.
    leg_press_vol = (180 * 8) + (270 * 8) + (410 * 7) + (390 * 7)
    leg_press_reps = 8 + 8 + 7 + 7
    leg_press_max = 410
    print(f"\nLeg press Max Set: {leg_press_max} lbs")
    print(f"Leg Press Total Volume: {leg_press_vol} lbs")
    print(f"Leg press Total Reps: {leg_press_reps} reps")

    # --- EXERCISE 4: RDL Machine ---
    # This is where you hit the 270 lb set.
    RDL_Machine_vol = (140 * 8) + (180 * 6) + (270 * 4) + (230 * 7)
    RDL_Machine_reps = 8 + 6 + 4 + 7
    RDL_Machine_max = 270
    print(f"\nRDL Machine Max Set: {RDL_Machine_max} lbs")
    print(f"RDL Machine Total Volume: {RDL_Machine_vol} lbs")
    print(f"RDL Machine Total Reps: {RDL_Machine_reps} reps")
    
    # 2. Calculate Hip Adduction (305 lbs is elite volume)
    # adduction_vol = (305 * 8) + (305 * 10)

    # --- EXERCISE 5: Hip Adduction ---
    # This is where you hit the 305 lb set.
    Hip_Adduction_vol = (220 * 8) + (270 * 8) + (305 * 8) + (305 * 10)
    Hip_Adduction_reps = 8 + 8 + 8 + 10
    Hip_Adduction_max = 305
    print(f"\nHip Adduction Max Set: {Hip_Adduction_max} lbs")
    print(f"Hip Adduction Total Volume: {Hip_Adduction_vol} lbs")
    print(f"Hip Adduction Total Reps: {Hip_Adduction_reps} reps")

    # --- EXERCISE 6: Calf Raises Seated Leg Press ---
    # This is where you hit the 230 lb set.
    calf_raises_vol = (170 * 8) + (215 * 10) + (230 * 10)
    calf_raise_reps = 8 + 10 + 10
    calf_raise_max = 230
    print(f"\nCalf Raises Max Set: {calf_raise_max} lbs")
    print(f"Calf Raises Total Volume: {calf_raises_vol} lbs")
    print(f"Calf Raises Total Reps: {calf_raise_reps} reps")

    # --- EXERCISE 7: Calf Raises Seated Leg Press ---
    # This is where you hit the 305 lb set.
    hanging_legraises_reps = (12) + (12) + (12)
    print(f"\nhanging leg raises Total reps: {hanging_legraises_reps} reps")

    # --- FINAL SYSTEM TOTAL ---
    # Once you finish the exercises, add them all here:
    total_session_volume = curls_vol + ext_vol + leg_press_vol + RDL_Machine_vol + Hip_Adduction_vol + calf_raises_vol
    total_session_reps = curls_reps + ext_reps + leg_press_reps + RDL_Machine_reps + Hip_Adduction_reps + calf_raise_reps + hanging_legraises_reps
    print(f"\nTOTAL SESSION Total VOLUME: {total_session_volume} lbs")
    print(f"\nTOTAL SESSION REPS: {total_session_reps} reps")

    # --- GOAL SETTING: SUNDAY SESSION ---
    # We apply a 5% 'Specialist' increase to your peak volume
    overload_factor = 1.05 
    week_goal_volume = total_session_volume * overload_factor
    additional_lbs_needed = week_goal_volume - total_session_volume

    print(f"\n--- Next Week MISSION TARGET ---")
    print(f"Goal Volume: {week_goal_volume:.2f} lbs")
    print(f"Required Increase: +{additional_lbs_needed:.2f} lbs across all sets")

    # --- FINAL SYSTEM TOTAL ---
    total_session_volume = curls_vol + ext_vol + leg_press_vol + RDL_Machine_vol + Hip_Adduction_vol + calf_raises_vol
    
    # 1. CREATE THE DICTIONARY (This defines 'current_stats')
    current_stats = {
        "Seated Leg Curls": curls_vol,
        "Leg Extensions": ext_vol,
        "Leg Press": leg_press_vol,
        "RDL Machine": RDL_Machine_vol,
        "Hip Adduction": Hip_Adduction_vol,
        "Calf Raises": calf_raises_vol
    }

    print(f"\n--- Next Week TARGETS PER EXERCISE (+2.5%) ---")
    
    # 2. THE LOOP (Now it can see 'current_stats')
    for exercise, volume in current_stats.items():
        target = volume * 1.025
        increase = target - volume
        print(f"{exercise}: Aim for {target:.2f} lbs (Increase: +{increase:.2f} lbs)")

    #print(f"\nTOTAL SESSION VOLUME: {total_session_volume} lbs")

if __name__ == "__main__":
    run_workout_audit()