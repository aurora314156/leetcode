

int hammingDistance(int x, int y) {
    int result = x ^ y;
        int mask = 1;
        int counter = 0;
        while (result != 0)
        {
            if ((mask & result) == 1)
            {
                counter++;
            }
            result = result >> 1;
        }
        return counter;
}