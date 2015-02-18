import urllib.request
import json
import os

input_dir = input('Save directory: ')
print("")
    
def main():
    #obtaining info from user
    board_id = input('Board: ')
    thread_no = input('Thread number: ')
    
    #obtaining json file
    html_response = urllib.request.urlopen( 'http://api.4chan.org/{0}/res/{1}.json'.format(board_id, thread_no) )
    posts = json.loads( html_response.read().decode('utf-8') )['posts']

    #getting a list of image urls
    image_names = []
    total_download_size = 0
    for post in posts:
        if len(post) > 10:
            image_names.append(str(post['tim'])+post['ext'])
            total_download_size += post['fsize']
        
    total_download_size = round(total_download_size/(1024*1024),3)
    
    # directory shit
    try:
        thread_name = posts[0]["sub"].translate(str.maketrans({'\\':'','/':'','*':'','"':'','|':'','<':'','>':'','?':'',':':''}))
    except KeyError:
        thread_name = thread_no
    
    if os.path.exists(input_dir+"\\"+board_id+"\\"+thread_name) == False:
        os.makedirs(input_dir+"\\"+board_id+"\\"+thread_name)
    
    #download shit
    print('Downloading images from /{}/{} - Total: {} ({} MB)'.format(board_id, thread_no, len(image_names), str(total_download_size)))
    i = 0
    for image in image_names:
        i += 1
        j = round(35*(i/len(image_names)))
        image_url = 'http://i.4cdn.org/'+board_id+"/"+image
        image_path = input_dir+"\\"+board_id+"\\"+thread_name+"\\"+image
        if os.path.isfile(image_path) == False:
            with urllib.request.urlopen(image_url) as html_response:
                with open(image_path, 'wb') as image_file:
                    image_file.write(html_response.read())
            print("[" + j*"|" + (35-j)*"-" + "]" + " Done " + str(i) + " out of " + str(len(image_names)) +".", end='\r')
    print("\n")   
    
while 1:
    main()
