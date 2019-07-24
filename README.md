# get_filename
我絕對不要再為了這個坑花了整整2小時 Orz......


##### get_filename( filename=str, mode='filename', index=0):

    @param  {str} filename (不能為空)
    @param  {str} mode ('filename' or 'extension') or ( 1 or 2)
    @param  {int} index (當 mode = 'extension' 才會作用)
    @return {str}

  ex1 :

    t = get_filename('explosion.hard.txt')
    t -> 'explosion.hard'

  ex2 :

    t = get_filename('explosion.hard.txt','extension',-3)
    t = get_filename('explosion.hard.txt',2,0)
    t -> 'explosion'

  ex3 :

    t = get_filename('explosion.hard.txt','extension',-1)
    t = get_filename('explosion.hard.txt',2,-1)
    t -> 'txt'
