
module dome(){
    sc = 10;
    translate([0,-119,-13])
    union(){
        color("red") translate([-91,6.75,13.2]) scale(sc) import("dome_1.stl");
        color("blue") translate([0.5,0,0.2]) scale(sc) import("dome_2.stl");
        color("green") translate([0.4,0,0.25]) scale(sc) import("dome_3.stl");
        color("yellow") translate([-91,0,0]) scale(sc) import("dome_4.stl");
    }
}

//size = 10;

//color("red") scale(size/10) dome();
//color("lightgray") rotate([0,0,90]) translate([-252,-30,45]) scale(size) import("radar_eye.stl");

//color("lightgray") translate([-123,-113,-17]) {
//    rotate([0,0,0]) translate([0,0,0]) scale(size) import("dome_top.stl");
//    rotate([0,0,0]) translate([0,0,0]) scale(size) import("dome_top_door_holo.stl");
//    rotate([0,0,0]) translate([0,0,0]) scale(size) import("door2.stl");
//    rotate([0,0,0]) translate([0,0,0]) scale(size) import("door3.stl");
//    rotate([0,0,0]) translate([0,0,0]) scale(size) import("door4.stl");
//    rotate([0,0,0]) translate([0,0,0]) scale(size) import("dome_door.stl");
//    rotate([0,0,0]) translate([0,0,0]) scale(size) import("door_dome_1.stl");
//    rotate([0,0,0]) translate([0,0,0]) scale(size) import("dome_door_7.stl");
//    rotate([0,0,0]) translate([0,0,0]) scale(size) import("dome_door_8.stl");
//}

module dome2(){
//    translate([0,-119,-13])
//    union(){
        color("red") translate([0,0,0]) import("dome_1.stl.stl");
        color("blue") translate([0,0,0]) import("dome_2.stl.stl");
//        color("green") translate([0,0,0]) import("dome_3.stl");
//        color("yellow") translate([0,0,0]) import("dome_4.stl");
//    }
}

scale(1.1) dome2();

cube([3,3,3]);
