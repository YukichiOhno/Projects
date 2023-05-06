function getDevInfo () {
    let name_stance = document.querySelector("#name");
    let devName = document.querySelector("#developer-name");

    let intro = document.querySelector("#intro");
    let devIntro = document.querySelector("#developer-intro");

    let hobbies = document.querySelector("#hobbies");
    let devHobbies = document.querySelector("#developer-hobbies");

    let socials = document.querySelector("#socials");
    let devSocials = document.querySelector("#developer-socials");

    return { name_stance, devName, intro, devIntro, hobbies, devHobbies, socials, devSocials };
}


const kevin = document.querySelector("#kevin");
const anthony = document.querySelector("#anthony");
const chaker = document.querySelector("#chaker");
const john = document.querySelector("#john");
const thinh = document.querySelector("#thinh");
const vincent = document.querySelector("#vincent");
const kase = document.querySelector("#kase");
const angel = document.querySelector("#angel");
const anh = document.querySelector("#anh");

kevin.addEventListener("click", () => {
    let { name_stance, devName, intro, devIntro, hobbies, devHobbies, socials, devSocials } = getDevInfo();
    name_stance.innerHTML, devName.innerHTML, intro.innerHTML, devIntro.innerHTML, hobbies.innerHTML, devHobbies.innerHTML, socials.innerHTML, devSocials.innerHTML = "";

    name_stance.innerHTML = "Name:";
    intro.innerHTML = "Introduction:";
    hobbies.innerHTML = "Hobbies:";
    socials.innerHTML = "Email:";

    // change only these 4 lines below
    devName.innerHTML = "Kevin Tojin";
    devIntro.innerHTML = "Hello, my name is Kevin and I am a Computer Information Science major. I am just getting older and appreciating more about life";
    devHobbies.innerHTML = "I like building things";
    devSocials.innerHTML = "kdtojin@cougarnet.uh.edu";
});


anthony.addEventListener("click", () => {
    let { name_stance, devName, intro, devIntro, hobbies, devHobbies, socials, devSocials } = getDevInfo();
    name_stance.innerHTML, devName.innerHTML, intro.innerHTML, devIntro.innerHTML, hobbies.innerHTML, devHobbies.innerHTML, socials.innerHTML, devSocials.innerHTML = "";

    name_stance.innerHTML = "Name:";
    intro.innerHTML = "Introduction:";
    hobbies.innerHTML = "Hobbies:";
    socials.innerHTML = "Email:";

    // change only these 4 lines below
    devName.innerHTML = "Anthony Flores";
    devIntro.innerHTML = "Hello my name is Anthony and I am a Computer Information Science Major. I will do whatever it take to make my dreams come true. I am a very dedicated in what I do ";
    devHobbies.innerHTML = " I play video games,  read, watch futbol, and kick it";
    devSocials.innerHTML = "ajflore7@cougarnet.uh.edu";
});

chaker.addEventListener("click", () => {
    let { name_stance, devName, intro, devIntro, hobbies, devHobbies, socials, devSocials } = getDevInfo();
    name_stance.innerHTML, devName.innerHTML, intro.innerHTML, devIntro.innerHTML, hobbies.innerHTML, devHobbies.innerHTML, socials.innerHTML, devSocials.innerHTML = "";

    name_stance.innerHTML = "Name:";
    intro.innerHTML = "Introduction:";
    hobbies.innerHTML = "Hobbies:";
    socials.innerHTML = "Email:";

    // change only these 4 lines below
    devName.innerHTML = "Chaker Hamid";
    devIntro.innerHTML = "My name is Hamid, and my major is Computer Information Sytems. I am a lebanese international student";
    devHobbies.innerHTML = "I like to play soccer and lift";
    devSocials.innerHTML = "achaker@cougarnet.uh.edu";
});

john.addEventListener("click", () => {
    let { name_stance, devName, intro, devIntro, hobbies, devHobbies, socials, devSocials } = getDevInfo();
    name_stance.innerHTML, devName.innerHTML, intro.innerHTML, devIntro.innerHTML, hobbies.innerHTML, devHobbies.innerHTML, socials.innerHTML, devSocials.innerHTML = "";

    name_stance.innerHTML = "Name:";
    intro.innerHTML = "Introduction:";
    hobbies.innerHTML = "Hobbies:";
    socials.innerHTML = "Email:";

    // change only these 4 lines below
    devName.innerHTML = "John Tran";
    devIntro.innerHTML = "My name is John Tran. I go to the University of Houston, majoring in Computer Information Systems. My major has taught me various programming languages like Python and HTML. Learning these new programming languages have been difficult but undoubtedly fun. I previously worked in the human resource field and hope to eventually get into the tech industry.";
    devHobbies.innerHTML = "Some of my hobbies include working out, football, videogames, and binge watching new shows.";
    devSocials.innerHTML = "jptran8@cougarnet.uh.edu";
    
});

thinh.addEventListener("click", () => {
    let { name_stance, devName, intro, devIntro, hobbies, devHobbies, socials, devSocials } = getDevInfo();
    name_stance.innerHTML, devName.innerHTML, intro.innerHTML, devIntro.innerHTML, hobbies.innerHTML, devHobbies.innerHTML, socials.innerHTML, devSocials.innerHTML = "";

    name_stance.innerHTML = "Name:";
    intro.innerHTML = "Introduction:";
    hobbies.innerHTML = "Hobbies:";
    socials.innerHTML = "Email:";

    // change only these 4 lines below
    devName.innerHTML = "Thinh Dang";
    devIntro.innerHTML = "Hello my name is Thinh and I am a Computer Information Science Major.  I'm passionate about servers, VMs, NAS, SAN, & workstations. I want to be a system engineer. ";
    devHobbies.innerHTML = "I like traveling, working-out & cooking ";
    devSocials.innerHTML = "thdang5@cougarnet.uh.edu";
});

vincent.addEventListener("click", () => {
    let { name_stance, devName, intro, devIntro, hobbies, devHobbies, socials, devSocials } = getDevInfo();
    name_stance.innerHTML, devName.innerHTML, intro.innerHTML, devIntro.innerHTML, hobbies.innerHTML, devHobbies.innerHTML, socials.innerHTML, devSocials.innerHTML = "";

    name_stance.innerHTML = "Name:";
    intro.innerHTML = "Introduction:";
    hobbies.innerHTML = "Hobbies:";
    socials.innerHTML = "Email:";

    // change only these 4 lines below
    devName.innerHTML = "Vincent Tran";
    devIntro.innerHTML = "Hello my name is Vincent and my major is Computer Information Systems. I am 20 years old, and my favorite food is almsot anything with fish.";
    devHobbies.innerHTML = "My current hobbies are bowling, watching anime or movies, and playing video games.";
    devSocials.innerHTML = "vntran22@cougarnet.uh.edu";
});

kase.addEventListener("click", () => {
    let { name_stance, devName, intro, devIntro, hobbies, devHobbies, socials, devSocials } = getDevInfo();
    name_stance.innerHTML, devName.innerHTML, intro.innerHTML, devIntro.innerHTML, hobbies.innerHTML, devHobbies.innerHTML, socials.innerHTML, devSocials.innerHTML = "";

    name_stance.innerHTML = "Name:";
    intro.innerHTML = "Introduction:";
    hobbies.innerHTML = "Hobbies:";
    socials.innerHTML = "Email:";

    // change only these 4 lines below
    devName.innerHTML = "Kase Collins";
    devIntro.innerHTML = "Hello my name is Kase and my major is Computer Information Systems. I currently work in leadership for Amazon, and hope to soon move into their IT department. ";
    devHobbies.innerHTML = "My hobbies include building LEGO, and playing video games such as Hogwarts Legacy and MLB The Show.";
    devSocials.innerHTML = "kkcollin@cougarnet.uh.edu";
});

angel.addEventListener("click", () => {
    let { name_stance, devName, intro, devIntro, hobbies, devHobbies, socials, devSocials } = getDevInfo();
    name_stance.innerHTML, devName.innerHTML, intro.innerHTML, devIntro.innerHTML, hobbies.innerHTML, devHobbies.innerHTML, socials.innerHTML, devSocials.innerHTML = "";

    name_stance.innerHTML = "Name:";
    intro.innerHTML = "Introduction:";
    hobbies.innerHTML = "Hobbies:";
    socials.innerHTML = "Email:";

    // change only these 4 lines below
    devName.innerHTML = "Angelo Angel";
    devIntro.innerHTML = "Not much is going on around my life, but do hmu if you want to turn it around";
    devHobbies.innerHTML = "Play Overwatch 24/7 with Daniel and Phoebe";
    devSocials.innerHTML = "asangel@cougarnet.uh.edu";
});

anh.addEventListener("click", () => {
    let { name_stance, devName, intro, devIntro, hobbies, devHobbies, socials, devSocials } = getDevInfo();
    name_stance.innerHTML, devName.innerHTML, intro.innerHTML, devIntro.innerHTML, hobbies.innerHTML, devHobbies.innerHTML, socials.innerHTML, devSocials.innerHTML = "";

    name_stance.innerHTML = "Name:";
    intro.innerHTML = "Introduction:";
    hobbies.innerHTML = "Hobbies:";
    socials.innerHTML = "Email:";

    // change only these 4 lines below
    devName.innerHTML = "Anh Vo";
    devIntro.innerHTML = "Hello my name is Anh Vo and mu major is Computer Information Systems. I have a passion for all things related to AI, deep learning, and robotics.";
    devHobbies.innerHTML = "Volunteering and community involvement have always been an essential part of my life. I particularly enjoy contributing to the Vietnamese community, as it allows me to give back to the people who have had a significant impact on my life.";
    devSocials.innerHTML = "atvo@cougarnet.uh.edu"; 
});

const submit = document.querySelector("#form-contact");

submit.addEventListener("submit", function(event) {
    let username = document.forms["form-contact"]["username"].value;
    let useremail = document.forms["form-contact"]["useremail"].value;
    let reason = document.forms["form-contact"]["reason"].value;
    let usermessage = document.forms["form-contact"]["usermessage"].value;

    if (username === "" || useremail === "" || reason === "" || usermessage === "") {
        window.alert("Required inputs are empty!");

        if (username === "") {
            window.alert("Please enter your name under the 'Your Name'");
        }

        if (useremail === "") {
            window.alert("Please enter your email under 'Your Email'");
        }

        if (reason === "") {
            window.alert("Please enter your reason for contacting us under 'Reason'");
        }

        if (usermessage === "") {
           window.alert("Please write down a message before submitting");
        }
    } else {
        let formData = new FormData(event.target);
    
            // send the form data using AJAX
            let xhr = new XMLHttpRequest();
            xhr.open("POST", "https://prod-84.westus.logic.azure.com/workflows/cb7cd79f8f01425298782b727e8d462b/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=32hDQGIEvI0XhfJet_E07_aRddsmMLRinTuxVRtI-1U");
            xhr.send(formData);
    }
});
