# get_filename

我絕對不要再為了這個坑花了整整2小時 Orz......    
如題，只是一個獲取檔案名稱或副檔名的東東。    

From a filename(str) get extension or name.     

----
# 用法 how to use
**get_filename( filename=str, mode='filename', index=0):**

    @param  {str} filename (不能為空)
    @param  {str} mode ('filename' or 'extension') or ( 1 or 2)
    @param  {int} index (當 mode = 'extension' 或 2 才會作用)
    @return {str}

  ex1 :

      t = get_filename('explosion.hard.txt')
      t -> 'explosion.hard'

  ex2 :

    t = get_filename('/path/to/somefile.ext')
    t = 'somefile'

  ex3 :

    t = get_filename('explosion.hard.txt','extension',-3)
    t = get_filename('explosion.hard.txt',2,0)
    t -> 'explosion'

  ex4 :

    t = get_filename('/path/to/somefile.txt','extension',-1)
    t = get_filename('/path/to/somefile.txt',2,-1)
    t -> 'txt'
