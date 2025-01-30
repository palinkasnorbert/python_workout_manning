def run_timing():
    total_run = 0
    run_count = 0

    while True:
        run_time = input("Enter 10 km run time: ")
        
        if not run_time:
            break
        try:    
            total_run += float(run_time)
            run_count += 1
        except ValueError as e:
            print("Hey! That's not a valid number!")
    
    return f"Average of {total_run/run_count}, over {run_count} runs."

if __name__ == "__main__":
    print(run_timing())