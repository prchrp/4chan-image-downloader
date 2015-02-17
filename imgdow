import urllib.request
import json
import os

board_id = input('GIB BOARD PLOX: ')
thread_no = input('GIB THREAD NUMBER PLOX: ')
directory = input('Choose save directory: ')

def main():
    json_url = 'http://api.4chan.org/{0}/res/{1}.json'.format(board_id,thread_no)

    with urllib.request.urlopen(json_url) as html_response:
        json_file = html_response.read().decode('utf-8')

    print('Downloading all images from /{0}/{1}'.format(board_id,thread_no))
    number_of_posts = len(json.loads(json_file)['posts'])
    file_dir = '{2}\\{0}\\{1}\\'.format(board_id,thread_no,directory)
   
    if os.path.exists('{1}\\{0}\\'.format(board_id,directory)) == False:
        os.mkdir('{1}\\{0}\\'.format(board_id,directory))
    elif os.path.exists('{2}\\{0}\\{1}\\'.format(board_id,thread_no,directory)) == False:
        os.mkdir('{2}\\{0}\\{1}\\'.format(board_id,thread_no,directory))
    
    i = 1

    for post in json.loads(json_file)['posts']:
        i += 1
        print('Post ({0}/{1}):'.format(i, number_of_posts+1))
        try:
            file_size = '{0} MB'.format(round(post['fsize']/(1024*1024),2))
            print('Downloading image ({0}) ...'.format(file_size))
            img_url = 'http://i.4cdn.org/{0}/{1}{2}'.format(board_id, post['tim'], post['ext'])
            img_path = '{0}{1}{2}'.format(file_dir, post['tim'], post['ext'])
            if os.path.isfile(img_path) == True:
                print("    ... Image already downloaded.")
            else:
                with urllib.request.urlopen(img_url) as html_response:
                    with open(img_path, 'wb') as img_file:
                        img_file.write(html_response.read())
                print('    ... Done.')
        except KeyError:
            print('    ... Encountered post with no image.')

if __name__ == '__main__':
    main()
