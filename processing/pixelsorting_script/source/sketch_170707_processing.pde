/*

 ASDF Pixel Sort
 Kim Asendorf | 2010 | kimasendorf.com
 
 sorting modes
 
 0 = black
 1 = brightness
 2 = white
 
 */

int mode = 2;

// image path is relative to sketch directory
PImage img;
String [] fileToPixelsort;
String imgFileName;

String fileType = "png";

int loops = 1;


// where the pictures are going to be saved
String finalImagePath = "/home/pi/camera_processing/processing/transformed_pictures/";
//String dropboxPath = "C:/Users/Luisa/Desktop/e-camera/adaptation/prova/kim/Dropbox/";


// threshold values to determine sorting start and end pixels
float blackValue = -14000000;
float brightnessValue = 0;
float whiteValue = -6500000;

String [] data;

int row = 0;
int column = 0;

boolean saved = false;

void setup() {
  /*every time we take a picture python writes a textfile called:"name of the pic" with written the name of the new pic. 
  We use this textfile to tell processing which image needs to be sorted */
  fileToPixelsort =loadStrings("name_of_the_pic");
  imgFileName = fileToPixelsort[0];
  img = loadImage("/home/pi/camera_processing/processing/pictures/"+ imgFileName +"."+fileType);
  
  // use only numbers (not variables) for the size() command, Processing 3
  //size(1, 1);
  
  // allow resize and update surface to image dimensions
  surface.setResizable(true);
  surface.setSize(img.width, img.height);
  
  // load image onto surface
  //image(img, 0, 0);
  
 
}


void draw() {
  /*here I am reading the data from the file "data_from_processing". I can only read them as a String Array,
  then I transform it in to float and then assign it to the mode ((mode 1 = brightnessvalue).
  The data are mapped, though with thsi mode is not that necessary.*/
  data =loadStrings("data_for_processing");
  float valueFromSensor = float(data[0]);
  //here I am mapping the sensor to make it work with brightnessvalue
  float newBrightnessValue = map(valueFromSensor, 45, 120, 170, 0);
  brightnessValue =newBrightnessValue ;
  //here I am mapping the sensor to make it work with blackValue
  float newblackValue = map(valueFromSensor, 35, 140,  -5400000, -14000000);
  blackValue =newblackValue ;
  //here I am mapping the sensor to make it work with whiteValue
  float newWhiteValue = map(valueFromSensor, 45, 120, -7400000,  -3500000);
  whiteValue =newWhiteValue ;
  // loop through columns
  while(column < width-1) {
    //println("Sorting Column " + column);
    img.loadPixels(); 
    sortColumn();
    column++;
    img.updatePixels();
  }
  
  // loop through rows
  while(row < height-1) {
    //println("Sorting Row " + column);
    img.loadPixels(); 
    sortRow();
    row++;
    img.updatePixels();
  }
  
  // load updated image onto surface
  //image(img, 0, 0);
  
  if(!saved && frameCount >= loops) {
    
    //saveImage
     
    //img.save(finalImagePath + imgFileName+"_"+mode+"_"+valueFromSensor+".png");
    img.save(finalImagePath + imgFileName+".png");
    
    // save surface
    //saveFrame(imgFileName+"_"+mode+"_"+valueFromSensor+".png");
    saved = true;
    //println("Saved "+frameCount+" Frame(s)");
    
    
    
      if(saved)
  {
    System.exit(0);//closes the file automatically after saving
  }

  }

}



void sortRow() {
  // current row
  int y = row;
  
  // where to start sorting
  //int x = 0;
  int x = 0; ///////////////////this thing already c#=]]anged quite a lot (originally x=0)
  
  // where to stop sorting
  int xend = 0;
  
  while(xend < width-1) {
    switch(mode) {
      case 0:
        x = getFirstNotBlackX(x, y);
        xend = getNextBlackX(x, y);
        break;
      case 1:
        x = getFirstBrightX(x, y);
        xend = getNextDarkX(x, y);
        break;
      case 2:
        x = getFirstNotWhiteX(x, y);
        xend = getNextWhiteX(x, y);
        break;
      default:
        break;
    }
    
    if(x < 0) break;
    
    int sortLength = xend-x;
    
    color[] unsorted = new color[sortLength];
    color[] sorted = new color[sortLength];
    
    for(int i=0; i<sortLength; i++) {
      unsorted[i] = img.pixels[x + i + y * img.width];
    }
    
    sorted = sort(unsorted);
    
    for(int i=0; i<sortLength; i++) {
      img.pixels[x + i + y * img.width] = sorted[i];      
    }
    
    x = xend+1;
  }
}


void sortColumn() {
  // current column
  int x = column;
  
  // where to start sorting
  int y = 0;
  
  // where to stop sorting
  int yend = 0;
  
  while(yend < height-1) {
    switch(mode) {
      case 0:
        y = getFirstNotBlackY(x, y);
        yend = getNextBlackY(x, y);
        break;
      case 1:
        y = getFirstBrightY(x, y);
        yend = getNextDarkY(x, y);
        break;
      case 2:
        y = getFirstNotWhiteY(x, y);
        yend = getNextWhiteY(x, y);
        break;
      default:
        break;
      }
    
    if(y < 0) break;
    
    int sortLength = yend-y;
    
    color[] unsorted = new color[sortLength];
    color[] sorted = new color[sortLength];
    
    for(int i=0; i<sortLength; i++) {
      unsorted[i] = img.pixels[x + (y+i) * img.width];
    }
    
    sorted = sort(unsorted);
    
    for(int i=0; i<sortLength; i++) {
      img.pixels[x + (y+i) * img.width] = sorted[i];
    }
    
    y = yend+1;
  }
}


// black x
int getFirstNotBlackX(int x, int y) {
  
  while(img.pixels[x + y * img.width] < blackValue) {
    x++;
    if(x >= width) 
      return -1;
  }
  
  return x;
}

int getNextBlackX(int x, int y) {
  x++;
  
  while(img.pixels[x + y * img.width] > blackValue) {
    x++;
    if(x >= width) 
      return width-1;
  }
  
  return x-1;
}

// brightness x
int getFirstBrightX(int x, int y) {
  
  while(brightness(img.pixels[x + y * img.width]) < brightnessValue) {
    x++;
    if(x >= width)
      return -1;
  }
  
  return x;
}

int getNextDarkX(int _x, int _y) {
  int x = _x+1;
  int y = _y;
  
  while(brightness(img.pixels[x + y * img.width]) > brightnessValue) {
    x++;
    if(x >= width) return width-1;
  }
  return x-1;
}

// white x
int getFirstNotWhiteX(int x, int y) {

  while(img.pixels[x + y * img.width] > whiteValue) {
    x++;
    if(x >= width) 
      return -1;
  }
  return x;
}

int getNextWhiteX(int x, int y) {
  x++;

  while(img.pixels[x + y * img.width] < whiteValue) {
    x++;
    if(x >= width) 
      return width-1;
  }
  return x-1;
}


// black y
int getFirstNotBlackY(int x, int y) {

  if(y < height) {
    while(img.pixels[x + y * img.width] < blackValue) {
      y++;
      if(y >= height)
        return -1;
    }
  }
  
  return y;
}

int getNextBlackY(int x, int y) {
  y++;

  if(y < height) {
    while(img.pixels[ img.width] > blackValue) {
      y++;
      if(y >= height)
        return height-1;
    }
  }
  
  return y-1;
}

// brightness y
int getFirstBrightY(int x, int y) {

  if(y < height) {
    while(brightness(img.pixels[x + y * img.width]) < brightnessValue) {
      y++;
      if(y >= height)
        return -1;
    }
  }
  
  return y;
}

int getNextDarkY(int x, int y) {
  y++;

  if(y < height) {
    while(brightness(img.pixels[x + y * img.width]) > brightnessValue) {
      y++;
      if(y >= height)
        return height-1;
    }
  }
  return y-1;
}

// white y
int getFirstNotWhiteY(int x, int y) {

  if(y < height) {
    while(img.pixels[x + y * img.width] > whiteValue) {
      y++;
      if(y >= height)
        return -1;
    }
  }
  
  return y;
}

int getNextWhiteY(int x, int y) {
  y++;
  
  if(y < height) {
    while(img.pixels[x + y * img.width] < whiteValue) {
      y++;
      if(y >= height) 
        return height-1;
    }
  }
  
  return y-1;
  

}