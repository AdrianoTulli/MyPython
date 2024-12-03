def main():
    
    file_name = input('File: ').lower().strip()
    dot=file_name.rfind('.')
    filetype = file_name[dot:]
    
    if filetype == '.jpg' or filetype == '.jpeg':
        print('image/jpeg')
    elif filetype == '.png':
        print('image/png')
    elif filetype == '.gif':
        print('image/gif')
    elif filetype == '.pdf':
            print('application/pdf')
    elif filetype == '.txt':
         print('text/plain')
    elif filetype == '.zip':
         print('application/zip')
    else:
         print('application/octet-stream') 

if __name__ == '__main__':
    main()