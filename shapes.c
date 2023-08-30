#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct point {
    int x,y;
};
typedef struct point point;

struct segment{
    point *a;
    point *b;
};
typedef struct segment segment;

struct triangle{
    segment *ab;
    segment *bc;
    segment *ca;
};
typedef struct triangle triangle;

segment *new_segment(int *a);
float segment_lenght(segment *s);
triangle *new_triangle(int *a);
float areatriangle(triangle *abc);
void visualizer(segment *s);

int main(){
    int a[4] = {1,3,2,6};
    segment *s = new_segment(a);
    //visualizer(s);
    int b[6] = {0,0,3,0,1,7};
    triangle *abc = new_triangle(b);
    printf("%f",areatriangle(abc));
}

segment *new_segment(int *a){

    point **lst = malloc(2*sizeof(point*));
    int i = 0;
    int index = 0;
    while (i <= 2){
        point *p = malloc(sizeof(point));
        p->x = a[i];
        p->y = a[i+1];
        lst[index] = p;
        index += 1;
        i+= 2;
    }

    segment *s = malloc(sizeof(segment));
    s->a = lst[0];
    s->b = lst[1];
    return s;
}

void visualizer(segment *s){
    int len = segment_lenght(s);
    int i = 0;
    while (i <= s->b->x){
        if (i <= s->a->x){
            printf("%c",' ');
        }
        else{
            printf("%c",'*');
        }
        i += 1;
    }
}

float segment_lenght(segment *s){
    float lenght = (float)sqrt(pow((s->a->x+s->b->x),2) + pow((s->a->y+s->b->y),2));
    return lenght;
}

triangle *new_triangle(int *b){
    int index = 0;
    point **lst = malloc(3*sizeof(point*));
    segment **seg = malloc(3*sizeof(segment*));
    //creating points
    for (int i = 0; i <= 4; i+=2){
        point *p = malloc(sizeof(point));
        p->x = b[i];
        p->y = b[i+1];
        lst[index] = p;
        index += 1;
    }
    int j = 0;
    triangle *abc = malloc(sizeof(triangle));
    for (int i = 0; i<3; i++){
            segment *s = malloc(sizeof(segment));
            if (i+1 == 3){
                s->a = lst[i];
                s->b = lst[0];
            }
            else{
                s->a = lst[i];
                s->b =lst[i+1];
                seg[i] = s;
            }

        }
    abc->ab =seg[0];
    abc->bc = seg[1];
    abc->ca = seg[2];

    return abc;
}
float areatriangle(triangle *abc){
    segment *base = abc->ab;
    float b = segment_lenght(base);
    
    float m = ((base->b->y) - (base->a->y)) / ((base->b->x) - (base->a->x));
    float c = base->a->y - m*(base->a->x);
   
    float h = fabs(((-m)*(abc->bc->b->x)+(abc->bc->b->y)+c)/sqrt(pow(m,2)+1));
    float area = (b * h)/2;
    return area;
}
