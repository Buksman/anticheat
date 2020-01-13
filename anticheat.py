"""
АНТИЧИТ ХНР (Хреновый Но Рабочий)
=================================
"""

# Настройки
process_name = "game.exe" # название процесса с игрой
signatures = "" # зафиксированные сигнатуры
mode = 1 # режим
v = "1.0.0 BETA" # версия античита
scan_delay = 5 # промежуток сканирования сигнатур

# Функции
def crc (fileName):
	prev = 0
	for eachLine in open(fileName,"rb"):
		prev = zlib.crc32(eachLine, prev)
    return "%X"%(prev & 0xFFFFFFFF)

    # Имплементация
    import os, subprocess, zlib, time
    sigs_path = "./sigs/" + process_name + "sigs.txt"
    sigs_local_path = "./sig.txt"

    if mode:
    	# создание сигнатур процесса 
    	sigs = subprocess.check_output('listdlls  ' + process_name).decode("utf-8")
    	f = open(sigs_path, 'w')
    	f.write( sigs )
    	f.close()

    	print("Сигнатуры процесса " + process_name + " созданы!")

    	# протекции по сигнатурам 
    	f = open(sigs_local_path, 'w')
    	f.write( sigs )
    	f.close

    	while True:
    		print( Сканирую игру ...)

    		sigs = subprocess.check_output('listdlls ' + process_name).decode("utf-8")
    		f = open(sigs_local_path, 'w') 
    	    f.write( sigs )
    	    f.close

    	    check = crc(sigs_path) == crc(sigs_local_path)

    	    if ( check ):
    	    	# Сигнатуры совпали
    	    	print( "Сигнатуры совпали, продолжаю ..." )
    	    	time.sleep(scan_delay);
    	    	continue;
    	    else:
    	        # Сигнатуры не совпали
    	        print( "Сигнатуры НЕ СОВПАЛИ, закрываю игру!")
    	        os.system('taskkill /IM "' + process_name + '" /F')
    	        break;

print("Античит ХНР v "+v+" завершил свою работу.")