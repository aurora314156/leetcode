


all: LSWRC

LSWRC: main.o LSWRC.o
ifeq (${OS}, Windows_NT)
	g++ -o LSWRC main.o LSWRC.o -lgtest
else
	g++ -o LSWRC main.o LSWRC.o -lgtest -lpthread
endif

main.o: main.cpp utLSWRC.h
	g++ -std=gnu++0x -c main.cpp
LSWRC.o: LSWRC.h LSWRC.cpp
	g++ -std=gnu++0x -c LSWRC.cpp

clean:
ifeq (${OS}, Windows_NT)
	del *.o *.exe
else
	rm -f *.o exp
endif
