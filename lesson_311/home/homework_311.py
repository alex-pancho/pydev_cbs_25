
from pathlib import Path
from datetime import datetime, timedelta

     
def analyze_heartbeats(events):
    key_dict = {}
    for event in events:
        if "Key" in event and "Timestamp" in event:
            key = event["Key"] 
            time = event["Timestamp"]
            
            if key in key_dict:
                heartbeat = key_dict[key] - datetime.strptime(time, "%H:%M:%S")
                if heartbeat > timedelta(seconds=31):
                    if heartbeat <= timedelta(seconds=33):#  WARNING
                        yield f"WARNING {key} delta={heartbeat.total_seconds():.1f}s at {time}"
                    else:
                        yield f"ERROR {key} delta={heartbeat.total_seconds():.1f}s at {time}"
                        
            key_dict[key] = datetime.strptime(time, "%H:%M:%S")

       
def parse_line(line: str) -> dict:
    line = line.strip().lstrip("{").rstrip("}")
    tokens = line.split()

    result = {}
    n = len(tokens)
    value = ""
    key = ""
    
    for token in tokens:
        if token == "Trade" or token == "Queue" or token == "PriceClass" or token == "Timestamp" or token == "Key" or token == "TradePrice" or token == "TradeSize":
            if len(value):
                try:
                    value = int(value)
                except ValueError:
                    pass
                result[key] = value
                value = ""
            
            key = token
        else:
            if(len(value)):
                value += " "
            
            value += token
    
    if(len(value)):
       result[key] = value         
    return result        

def process_file(input_path: str, output_path: str):
    input_path = Path(input_path)
    output_path = Path(output_path)

    with input_path.open("r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    event_list =[]
    for line in lines:
        event_list.append(parse_line(line))
        
    results = list(analyze_heartbeats(event_list))

    with output_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(results))

    

my_dir = Path(__file__).parent

if __name__ == "__main__":
    process_file(my_dir/"hblog", my_dir/"hb_test.log")