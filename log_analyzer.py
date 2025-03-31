import re, time

Alert={}
time_sleep=0

def main(filename,sleep):
    cont=0
    bf=0
    try:
        with open(filename,'r') as log:
            for line in log:
                cont+=1
                for alert_name, alert_d in Alert.items():
                    if re.search(alert_d,line,re.IGNORECASE):
                        print(f'[+]Alert {alert_name} in line {cont}:\n {line}')
                        bf+=1
                        time.sleep(sleep)
    except FileNotFoundError:
        print(f'[-]No such file: {filename}')
        exit()
    return bf
    
def config():
    config_file={'File':None,'Mode':None,'Alert':Alert}
    try:
        with open('config.ini','r') as file:
            for line_config in file:
                option=line_config.split()
                if option[0]!='Alert' and option[0]!='Sleep':
                    config_file[option[0]]=option[1]
                elif option[0]=='Sleep':
                    time_sleep=int(option[1])
                else:
                    ind=0
                    tmt=len(line_config)
                    s=''
                    for j in range(0,tmt-1):
                        if line_config[j]=='"':
                            if ind==0:
                                ind=1
                                continue
                            else:
                                break
                        if ind==1:
                            s+=line_config[j]
                    config_file[option[0]][option[1]]=s
                            
                        
        if int(config_file['Mode'])==0:
            while True:
                main(config_file['File'],time_sleep)
        else:
            for i in range(1,int(config_file['Mode'])+1):
                print(f"Repetition Number {i}")
                print(f"End - {main(config_file['File'],time_sleep)} Alerts")

    except IndexError:
        print('[-]Error in the config file')
    except FileNotFoundError:
        print('[-]No such file: config.ini')
        

if __name__=="__main__":
    config()
