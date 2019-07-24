def get_filename(filename=str, mode='filename', index=0):
    '''
    filename = (要str，且不能為空)
    mode = 'filename' or 'extension'
    index = (當 mode = 'extension' 才會作用)
    return a str
    ex1 :
    t = get_filename('explosion.hard.txt','extension',-2)
    t = get_filename('explosion.hard.txt',2,-2)
    t -> 'hard'
    ex2 :
    t = get_filename('explosion.hard.txt','extension',-1)
    t = get_filename('explosion.hard.txt',2,-1)
    t -> 'txt'
    '''
    if type(filename) != str:
        raise ValueError('filename is not str')
    if str(filename) == '':
        raise ValueError('filename can not empty')

    if (str(mode) == 'filename' or int(mode) == 1):
        extension = filename.split(".")
        if len(extension) == 1:
            Warning('filename have not extension!')
            return str(extension[0])
        else:
            del extension[-1]
            s = ''
            for i in extension:
                s += (i + '.')
            s = s[0:len(s) - 1]
            return str(s)

    elif (str(mode) == 'extension' or int(mode) == 2):
        if type(index) != int:
            raise ValueError('index is not int')
        extension = filename.split(".")
        if index > 0:
            if len(extension) <= abs(index):
                raise ValueError('index is over')
        else:
            if len(extension) < abs(index):
                raise ValueError('index is over')
        return str(extension[index])
    else:
        raise ValueError('mode is not understand')
