#/bin/bash

if [ -f "/tmp/problem/test.txt" ]; then
    case $lang in
        python3*) timeout 2 python3 /tmp/code/code.py < /tmp/problem/test.txt > /tmp/code/out.txt 2>> /tmp/code/err.txt; echo $?>tmp/code/res.txt
                ;;
        c++*) g++ /tmp/code/code.cpp -o /tmp/code/a.exe 2> tmp/code/error.txt; timeout 2 /tmp/code/a.exe < /tmp/problem/test.txt > tmp/code/out.txt 2>> tmp/code/err.txt; echo $?>tmp/code/res.txt
                ;;
    esac    
else
    case $lang in
        python3*) timeout 2 python3 /tmp/code/code.py > /tmp/code/out.txt 2>> /tmp/code/err.txt; echo $?>tmp/code/res.txt
                ;;
        c++*) g++ /tmp/code/code.cpp -o /tmp/code/a.exe && timeout 2 /tmp/code/a.exe > tmp/code/out.txt 2>> tmp/code/err.txt; echo $?>tmp/code/res.txt
                ;;
    esac
fi

exit 0