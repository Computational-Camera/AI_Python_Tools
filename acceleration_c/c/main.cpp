#include "main.h"

//int main(int argc, const char **argv){}
//list entries command: objdump -TC libpyopencv.so
//assume img is a single channel image

void myprint(){
    printf("hello world\n");
}

void png2label(unsigned short* p, unsigned char* array, int nRows, int nCols){

    int label, id;   
    int label_num[256] = {0};

    for(int y = 0; y < nRows; ++y){
        for (int x = 0; x < nCols; ++x){
        
            int value = *p;
            
            if ((value>255)&&(value<65535)){
                label = int((float)value/1000.0f);
                id    = (value - 1000*label) +1;
                //if (label==0) {cout<<id<<" "<<i<<" "<<j<<endl;while(1);}
                if (label_num[label]<id){
                    label_num[label] = id;
                    array[label] = id;
                }            
            }
            
            p++;
        }
    }    
    
    //for (int j=30; j<42; j++)
        //cout<<j<<" "<<int(array[j])<<endl;
}


void png2box  (unsigned short* p, unsigned short* array, unsigned short* label_map, int label_num, unsigned short* label_idx, int nRows, int nCols){
    
    int label, id;   
    for(int y = 0; y < nRows; ++y){
        for (int x = 0; x < nCols; ++x){
        
            int value = *p;          
            if ((value>255)&&(value<65535)){
                        
                label = int((float)value/1000.0f);
                
                int label_idx1;
                for (int k=0; k<label_num; k++)
                    if (label_map[k]== label)
                        label_idx1 = k-1;
                
                id    = value - 1000*label;

                int   idx = 4*label_idx[label_idx1] + 4*id;
                //cout<<id<<" "<<label_idx1<<" "<<idx<<endl;
                unsigned short* box_coordinate = &array[idx];
                
                if (x<box_coordinate[0])
                    box_coordinate[0] = x;
                else if (x>box_coordinate[1])
                    box_coordinate[1] = x;
                if (y<box_coordinate[2])
                    box_coordinate[2] = y;
                else if (y>box_coordinate[3])
                    box_coordinate[3] = y;                         
            }         
            p++;
        }
    }    
    //for (int j=0; j<12; j++)
    //    cout<<j<<" "<<array[j]<<endl;
}
