


all: LSWRC

LSWRC: main.cpp utLSWRC.h LSWRC.o
ifeq (${OS}, Windows_NT)
	g++ main.cpp -o LSWRC LSWRC.o -lgtest
else
	g++ main.cpp -o LSWRC LSWRC.o -lgtest -lpthread
endif

LSWRC.o: LSWRC.h LSWRC.cpp
	g++ -std=gnu++0x -c LSWRC.cpp

clean:
ifeq (${OS}, Windows_NT)
	del *.o *.exe
else
	rm -f *.o exp
endif
