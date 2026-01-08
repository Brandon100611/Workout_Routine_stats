import datetime

def run_workout_audit():
    print(f"--- OFFICIAL WORKOUT AUDIT: {datetime.date.today()} ---")
    print("\nCoach: George Benitez | Goal: System Shock / Density")
    
    print("\nUpper Body day: Exercise | Weight (LBS)/Reps")
    # --- EXERCISE 1: lat bar pull down ---
    # George pushed you to 220 lbs for an extra set here.
    LPD_vol = (110 * 6) + (130 * 6) + (200 * 8) + (210 * 8)
    # (one extra set of 220 * 5)
    LPD_reps = 6 + 6 + 8 + 8
    LPD_max = 220
    print(f"\nlat bar pull down Max Set: {LPD_max} lbs")
    print(f"lat bar pull down Total Volume: {LPD_vol} lbs")
    print(f"lat bar pull down Total Reps: {LPD_reps} reps")

    # --- EXERCISE 2: Back Long Fully Rows (overhand grip) ---
    # This is where you hit the 215 lb 'Gunslinger' set.
    BLFR_vol = (135 * 8) + (170 * 7) + (165 * 8)
    BLFR_reps = 8 + 7 + 8
    BLFR_max = 170
    print(f"\nBack Long Fully Rows Max Set: {BLFR_max} lbs")
    print(f"Back Long Fully Rows Total Volume: {BLFR_vol} lbs")
    print(f"Back Long Fully Rows Total Reps: {BLFR_reps} reps")

    # --- YOUR TASK: COMPLETE THE REST ---
    # Use the pattern below to add the Leg Press (45lb plates = 45), 
    # RDL Machine, Hip Adduction, and Calves.
    
    # 1. Calculate Leg Press (Hint: 4 plates per side = 8 total plates * 45)
    # leg_press_vol = (400 * 7) + (380 * 7) # Replace with your math

    # --- EXERCISE 3: Incline Chest Press Machine---
    # This is where you hit the 110 lb set.
    IC_press_vol = (60 * 8) + (90 * 4) + (110 * 7) + (100 * 7)
    IC_press_reps = 8 + 4 + 7 + 7
    IC_press_max = 110
    print(f"\nIncline Chest Press Max Set: {IC_press_max} lbs")
    print(f"Incline Chest Press Total Volume: {IC_press_vol} lbs")
    print(f"Incline Chest Press Total Reps: {IC_press_reps} reps")

    # --- EXERCISE 4: MTS Shoulder Press Machine ---
    # This is where you hit the 140 lb set.
    MTS_Machine_vol = (95 * 8) + (115 * 9) + (140 * 6) + (140 * 6)
    MTS_Machine_reps = 8 + 9 + 6 + 6
    MTS_Machine_max = 140
    print(f"\nMTS Shoulder Press Max Set: {MTS_Machine_max} lbs")
    print(f"MTS Shoulder Press Total Volume: {MTS_Machine_vol} lbs")
    print(f"MTS Shoulder Press Total Reps: {MTS_Machine_reps} reps")

    # --- EXERCISE 5: Bicep Preacher Curl Machine ---
    # This is where you hit the 170 lb set.
    Bicep_curl_vol = (125 * 8) + (145 * 8) + (170 * 6) + (170 * 6)
    Bicep_curl_reps = 8 + 8 + 6 + 6
    Bicep_curl_max = 170
    print(f"\nBicep Preacher Curl Max Set: {Bicep_curl_max} lbs")
    print(f"Bicep Preacher Curl Total Volume: {Bicep_curl_vol} lbs")
    print(f"Bicep Preacher Curl Total Reps: {Bicep_curl_reps} reps")

    # --- EXERCISE 6: Tricep Pull Down ---
    # This is where you hit the 95 lb set.
    Tricep_vol = (65 * 10) + (85 * 10) + (95 * 7) + (95 * 7)
    Tricep_reps = 10 + 10 + 7 + 7
    Tricep_max = 95
    print(f"\nTricep Pull Down Max Set: {Tricep_max} lbs")
    print(f"Tricep Pull Down Total Volume: {Tricep_vol} lbs")
    print(f"Tricep Pull Down Total Reps: {Tricep_reps} reps")

    # --- EXERCISE 7: Ab Crunch Machine ---
    # This is where you hit the 160 lb set.
    Ab_vol = (110 * 10) + (160 * 10) + (160 * 10)
    Ab_reps = 10 + 10 + 10
    Ab_max = 160
    print(f"\nAb Crunch Machine Max Set: {Ab_max} lbs")
    print(f"Ab Crunch Machine Total Volume: {Ab_vol} lbs")
    print(f"Ab Crunch Machine Total Reps: {Ab_reps} reps")

    # --- FINAL SYSTEM TOTAL ---
    # Once you finish the exercises, add them all here:
    total_session_volume = LPD_vol + BLFR_vol + IC_press_vol + MTS_Machine_vol + Bicep_curl_vol + Tricep_vol + Ab_vol
    total_session_reps = LPD_reps + BLFR_reps + IC_press_reps + MTS_Machine_reps + Bicep_curl_reps + Tricep_reps + Ab_reps
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
    total_session_volume = LPD_vol + BLFR_vol + IC_press_vol + MTS_Machine_vol + Bicep_curl_vol + Tricep_vol + Ab_vol
    
    # 1. CREATE THE DICTIONARY (This defines 'current_stats')
    current_stats = {
        "lat bar pull down": LPD_vol,
        "Back Long Fully Rows": BLFR_vol,
        "Incline Chest Press": IC_press_vol,
        "MTS Shoulder Press": MTS_Machine_vol,
        "Bicep Preacher Curl": Bicep_curl_vol,
        "Tricep Pull Down": Tricep_vol,
        "Ab Crunch Machine": Ab_vol
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