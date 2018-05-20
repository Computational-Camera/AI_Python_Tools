#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

//int main(int argc, const char **argv){}
//list entries command: objdump -TC libpyopencv.so
//assume img is a single channel image

extern "C" 
{
    void myprint(void);
    void png2label(unsigned short* p, unsigned char* array,  int nRows, int nCols);
    void png2box  (unsigned short* p, unsigned short* array, unsigned short* label_map, int label_num, unsigned short* label_idx, int nRows, int nCols);

}


