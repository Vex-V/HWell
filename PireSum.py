from avwx import Pireps
from collections import defaultdict
import requests
from UTC import utc

def Piresum(IDs):
    summary=[]
    for ID in IDs:
        new=Pireps("KLAX")
        time=utc("Metar")
        counters = defaultdict(int)
        x="https://aviationweather.gov/api/data/pirep?id="+ID+"&format=raw&age=1&distance=1000&level=10000&inten=sev&date="+time
        req=requests.get(x)
        pirep_lines = req.text.strip().split('\n')

        for line in pirep_lines:
            
            Pireps.parse(new,line)

            data=new.data
            if data == None:
                pass
            else:
                for pirep in data:
                    if pirep.clouds is not None:
                        counters['clouds'] += 1
                    if pirep.flight_visibility is not None:
                        counters['flight_visibility'] += 1
                    if pirep.icing is not None:
                        counters['icing'] += 1
                    if pirep.turbulence is not None:
                        counters['turbulence'] += 1

            

        counters=dict(counters)
    
        output = f"{ID}: " + ", ".join(f"{k}={v}" for k, v in counters.items())
        summary.append(output)
    return "\n\n".join(summary)


IDs=["KLAX","KJFK","KPHX"]
print(Piresum(IDs))

