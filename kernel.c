void kernel_main();
int xxx=0;
int yyy=0;
int zzz=0;
int video;
 char *keymap="==1234567890-===qwertyuiop====asdfghjkl====\\zxcvbnm,.;/==== ";
 volatile unsigned int *timerss;
static double PI = 3.141592653589793;
static unsigned char *memoryStart=(char *)0x200000;
typedef int size_t;

int NULL;
// Estrutura para representar um bitmap com cabeçalho
typedef struct Bitmap {
    int x;          // Comprimento em X
    int y;          // Comprimento em Y
    unsigned char* data; // Ponteiro para os dados do bitmap
} Bitmap;
char *scr2=(char *)0x000b8000L;//[80*26*2];

void clear(){
	int n=0;
	char *src = scr2;//(char *)0x000b8000L;
	for(n=0;n<80*24*2;n=n+2){
		src[n]=32;
		src[n+1]=0xe7;
	}
}
void scrollb8000()
{
	int n=0;
	int nn=0;
	
	char *src = scr2;//(char *)0x000b8000L;
	 
	for(n=0;n<80*24*2;n++)src[n]=src[n+160];
}
void copyb8000(int address,char *s)
{
	int n=0;
	int nn=0;
	
	char *src = scr2;//(char *)0x000b8000L;
	 
	while(s[n]!=0){
		src[address+nn]=s[n];
		nn++;
		nn++;
		n++;
	}
}
void locate(int x,int y){

	xxx=x;
	yyy=y;
	if(x>79)x=79;
	if(y>24)y=24;
	zzz=y*80*2+x*2;
}
void putss(char* s){
	copyb8000(zzz,s);
	xxx=0;
	yyy++;
	if (yyy>24){
		yyy=24;
		scrollb8000();
	}
	locate(xxx,yyy);
}

void kernel_main(){
    clear();
    putss("hello world\n\n");
    for(;;);
}