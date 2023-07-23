def make_subtitle_list (json_data):
    subtitle_list = []
    
    for i in range(len(json_data)):
        for j in range(len(json_data[i]["cues"])):
            temp_str = json_data[i]["cues"][j]['text'] + "/" + str(json_data[i]["cues"][j]['time'])
            subtitle_list.append(temp_str)
             
    return subtitle_list
        
def number_to_time_format(number):
    milliseconds = number % 1000
    seconds = (number // 1000) % 60
    minutes = (number // (1000 * 60)) % 60
    hours = number // (1000 * 60 * 60)
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"