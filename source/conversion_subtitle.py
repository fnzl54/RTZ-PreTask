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

def make_srt(output_file, subtitle_list):

    with open(output_file, 'w', encoding='utf-8') as f:
        subtitle_length = len(subtitle_list) - 1
        
        for i in range( subtitle_length ):
            subtitle = subtitle_list[i].split('/')[0]
            start_time = number_to_time_format(int(subtitle_list[i].split('/')[1]))
            end_time = number_to_time_format(int(subtitle_list[i + 1].split('/')[1]) - 24)
            
            subtitle_line = f"{i+1}\n{start_time} --> {end_time}\n{subtitle}\n\n"
            f.write(subtitle_line)
        
        subtitle = subtitle_list[subtitle_length].split('/')[0]
        start_time = number_to_time_format(int(subtitle_list[subtitle_length].split('/')[1]))
        end_time = number_to_time_format(int(subtitle_list[subtitle_length].split('/')[1]) + 100)
        
        subtitle_line = f"{i+1}\n{start_time} --> {end_time}\n{subtitle}\n\n"
        f.write(subtitle_line)