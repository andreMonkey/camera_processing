PImage img;
String [] imageToPolaroid;
String imgFileName;
String fileType = "png";

PFont font;

String [] pulse;

String imagePath = "C:/Users/Luisa/Desktop/e-camera/adaptation/polaroid/polaroid/transformed_pictures/";
String finalImagePath = "C:/Users/Luisa/Desktop/e-camera/adaptation/polaroid/polaroid/to_be_printed/";


boolean saved = false;
int loops=1;

void setup() {
  

  size(1000,1480);
  background(255);
  

  

  
}

void draw() {
  
  imageToPolaroid =loadStrings("name_of_the_pic");
  imgFileName = imageToPolaroid[0];
  img = loadImage(imagePath + imgFileName+"."+fileType);
  
  int resize= 900;
  img.resize(resize,resize);
  image(img, width/2-resize/2, 200);
  
  //name of the pic
  
  font = loadFont("Monotxt-90.vlw");
  textFont(font,60);
  fill(60);
  textAlign(RIGHT);
  text("n."+ imgFileName, width-(width-resize)/2, 150 );
  //text(imgFileName, 50, 50 );
  
  //pulse
  
  font = loadFont("Monotxt-90.vlw");
  textFont(font,90);
  fill(60);
  textAlign(CENTER);
  pulse =loadStrings("data_for_processing");

  text("PULSE:"+ pulse[0]+"bpm", width/2, resize + 400 );
  //text(imgFileName, 50, 50 );
  
  //luisa-fabrizi.com
    font = loadFont("Dialog.plain-48.vlw");
  textFont(font,20);
  fill(60);
  textAlign(RIGHT);
  text("luisa-fabrizi.com", width-(width-resize)/2, height-30 );
  //text(imgFileName, 50, 50 );

  //luisa-fabrizi.com
  font = loadFont("Dialog.plain-48.vlw");
  textFont(font,20);
  fill(60);
  textAlign(LEFT);
  text("e-camera.tumblr.com", (width-resize)/2, height-30 );
  //text(imgFileName, 50, 50 );
  

 }

    
    
  
  void mouseClicked() {
 
  {
     saveFrame(finalImagePath + imgFileName+"_polaroid.jpg");
     println("saving..");
     delay(2000);
    System.exit(0);
  }
}
    

  