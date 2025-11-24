import pandas as pd

def total_time(employees):
    employees["session_time"] = employees["out_time"] - employees["in_time"]

    result = (
        employees
        .groupby(["event_day", "emp_id"], as_index=False)["session_time"]
        .sum()
        .rename(columns={
            "event_day": "day",
            "session_time": "total_time"
        })
    )
    
    return result

