def make_subtitle_list (json_data):
    subtitle_list = []
    
    for i in range(len(json_data)):
        for j in range(len(json_data[i]["cues"])):
            temp_str = json_data[i]["cues"][j]['text'] + "/" + str(json_data[i]["cues"][j]['time'])
            subtitle_list.append(temp_str)
             
    return subtitle_list