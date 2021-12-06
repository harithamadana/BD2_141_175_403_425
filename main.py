import socket
import json
import pandas as pd

def prepro(df):
    for i in range(0,len(df['feature1'])):
        clean=list(df["feature1"][i].split(" "))
        print(clean)
        for j in clean:
            if(j.startswith("@")):
                clean.remove(j)
                continue
            if(j.endswith("?")):
                j.replace("?","")
            
            if(j.endswith("!")):
                j.replace("!","")
            
            if(j.endswith(".")):
                j.replace(".","")
            if(j==" "):
                clean.remove(j)
                continue
            
            if(j.startswith("#")):
                clean.remove(j)
            
            if(j.startswith("http://")):
                clean.remove(j)
                continue
        
            if(any(map(str.isdigit, j))):
                clean.remove(j)
                continue
        print(clean)
        
TCP_IP = "localhost"
TCP_PORT = 6100
soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    soc.connect((TCP_IP, TCP_PORT))
    while True:
        json_recv=soc.recv(2048).decode()
        a_json=json.loads(json_recv)
        df=pd.DataFrame.from_dict(a_json,orient="index")
        prepro(df)
        print('.......................................................................................................')
        
except Exception as e:
    print(e)
