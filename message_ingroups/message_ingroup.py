def messages_ingroup(groupid, older_than,file_cnt):
    file_path = '/opt/app/group_name/'
    if older_than == '':
        url = "https://www.yammer.com/api/v1/messages/in_group/"+groupid+".json?"
        request = Request(url, headers=headers)
        response = urlopen(request)
        elevations = response.read()
        file_nm = file_path+str(file_cnt)+'.json'
        file = open(file_nm,'w') 
        file.write(elevations)
        file.close()
        file = open(file_nm, 'r') 
        data = file.read() 
        data = json.loads(data)
        dt_normalise = json_normalize(data)
        import pandas as pd
        df = pd.DataFrame(dt_normalise)
        for id in data['messages']:
            older_than = id['id']
        messages_ingroup(groupid,str(older_than),file_cnt)
    else:
        file_cnt = file_cnt+1
        file_nm = file_path+str(file_cnt)+'.json'
        url = "https://www.yammer.com/api/v1/messages/in_group/"+groupid+".json?"+"older_than="+older_than
        request = Request(url, headers=headers)
        response = urlopen(request)
        elevations = response.read()
        file = open(file_nm,'w') 
        file.write(elevations)
        file.close()
        file = open(file_nm, 'r') 
        data = file.read() 
        data = json.loads(data)
        dt_normalise = json_normalize(data)
        import pandas as pd
        df = pd.DataFrame(dt_normalise)
        for id in data['messages']:
            older_than = id['id']
    
        if df['meta.older_available'].bool()==0:
            return
        elif older_than <> '':
            messages_ingroup(groupid,str(older_than),file_cnt)