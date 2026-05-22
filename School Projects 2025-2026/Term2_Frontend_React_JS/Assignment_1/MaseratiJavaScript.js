// Desc: JavaScript for QAP 1
// Author: Stephen Fennelly
// Dates: May 26 - June 2

// function for greeting based on time of day
    function showGreeting() {

        let currDate = new Date()
        let currHour = currDate.getHours()
        let greeting = ""

        if (currHour >= 6 && currHour <= 12) {
            greeting = "Good Morning";
        } else if (currHour >= 12 && currHour <= 18) {
            greeting = "Good Afternoon";
        } else if (currHour >= 18 && currHour <= 24) {
            greeting = "Good Evening";
        } else {
            greeting = "Good Night";
        }

        greeting += " - " + currDate.toDateString();
        document.writeln(greeting);
    }

// Slide show function
    let step = 0
    let Images = new Array()

    Images[0] = "Images/Gallery Page/Slideshow/GT Engine.jpg";
    Images[1] = "Images/Gallery Page/Slideshow/GT Interior 1.jpg";
    Images[2] = "Images/Gallery Page/Slideshow/GT Interior 2.jpg";
    Images[3] = "Images/Gallery Page/Slideshow/GT Yellow.jpg";
    Images[4] = "Images/Gallery Page/Slideshow/GT Red.jpg";

    window.onload = setInterval(gallery, 6000);

    function gallery() {
        const imgSlideElement = document.getElementById("ImgSlide");
        if (imgSlideElement) {
            imgSlideElement.src = Images[step];
        }

        if (step < Images.length - 1) {
            step++;
        } else {
            step = 0;
        }
    }
