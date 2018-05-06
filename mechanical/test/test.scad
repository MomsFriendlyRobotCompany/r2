module dome(){
    // sort of center mass
    color("Red") scale(1.5264) import("r2-dome.stl");
}

// uneven scaling for displays
//dome();
translate([-310,-80,0]) scale([1.5264,2,1.5264]) import("ld.stl");
cube([60,20,8], center=true);
