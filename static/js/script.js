
// ==========================================================
// DAWOOD ANALYTICS WEBSITE SCRIPT
// Phase 12.1.3 Navigation Upgrade
// ==========================================================


// Confirm website loaded

console.log("Website Loaded Successfully");



// ==========================================================
// MOBILE MENU TOGGLE
// ==========================================================

const menuToggle = document.querySelector(".menu-toggle");

const navLinks = document.querySelector(".nav-links");


if(menuToggle){

    menuToggle.addEventListener(
        "click",
        () => {

            navLinks.classList.toggle("active");

        }
    );

}



// ==========================================================
// CLOSE MOBILE MENU AFTER CLICK
// ==========================================================

const links = document.querySelectorAll(".nav-link");


links.forEach(
    link => {

        link.addEventListener(
            "click",
            () => {

                navLinks.classList.remove("active");

            }
        );

    }
);



// ==========================================================
// SMOOTH SCROLLING
// ==========================================================

document.querySelectorAll('a[href^="#"]').forEach(
    anchor => {

        anchor.addEventListener(
            "click",
            function(e){

                const target =
                document.querySelector(
                    this.getAttribute("href")
                );


                if(target){

                    e.preventDefault();


                    target.scrollIntoView(
                        {
                            behavior:"smooth"
                        }
                    );

                }

            }
        );

    }
);



// ==========================================================
// ACTIVE NAVIGATION ON SCROLL
// ==========================================================

const sections =
document.querySelectorAll("section");


window.addEventListener(
    "scroll",
    () => {


        let current = "";


        sections.forEach(
            section => {


                const sectionTop =
                section.offsetTop - 150;


                if(
                    pageYOffset >= sectionTop
                ){

                    current =
                    section.getAttribute("id");

                }

            }
        );


        links.forEach(
            link => {


                link.classList.remove(
                    "active"
                );


                if(
                    link.getAttribute("href")
                    ==
                    "#" + current
                ){

                    link.classList.add(
                        "active"
                    );

                }

            }
        );


    }
);
