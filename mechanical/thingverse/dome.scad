//$fn=100;

use <pi.scad>
use <parts/9g_servo.scad>

module dome(r){
    dia = 2*r;
    difference()
    {
        sphere(d=dia);
        sphere(d=dia-8);
        translate([-dia/2,-dia/2,-dia/2]) cube([dia,dia,dia/2]);
    }
}

module door(r,thick){
    dia = 2*r;
    difference()
    {
        sphere(d=dia);
        sphere(d=dia-2*thick);
        cylinder(h=2*dia,d=70, center=true);
        translate([-dia/2,-dia/2,-dia/2]) cube([dia,dia,dia/2]);
        translate([-dia/2,-dia/2,-30]) cube([dia,dia,dia/2]);
        translate([-dia/2,0,0]) cube([dia,dia,dia/2]);
        rotate([0,0,130]) translate([-dia/2,0,0]) cube([dia,dia,dia/2]);
    }
}

module cap(r){
    dia = 2*r;
    difference()
    {
        sphere(d=dia);
        sphere(d=dia-8);
        translate([0,0,-5]) cube([dia,dia,dia], center=true);
    }
}

r = 90;
//for(a=[0:5]) rotate([0,-30,a*50-10]) translate([r-12,0,0]) rotate([0,-90,90]) 9gServo();
//rpi3();
//color("red", 0.5)
difference()
{
    color("red") dome(r);
    cylinder(h=2*r,d=60, center=true);
    translate([0,0,1]) rotate([0,0,0]) door(r,7);
//    translate([0,0,1]) rotate([0,0,1*60]) door(r,7);
//    translate([0,0,1]) rotate([0,0,2*60]) door(r,7);
//    translate([0,0,1]) rotate([0,0,3*60]) door(r,7);
//    translate([0,0,1]) rotate([0,0,4*60]) door(r,7);
//    translate([0,0,1]) rotate([0,0,5*60]) door(r,7);
 //   for (a=[0:0]) translate([0,0,1]) rotate([0,0,a*60]) door(r,7);
}

//for (a=[0:5]) translate([0,0,10]) rotate([0,0,a*60]) color("silver") door(r);

//translate([0,0,10]) color("silver") cap(r);
