/**
 * @summary Script handles logic used in help center component.
 * @author Kevin Tojin <kevintojin19@gmail.com>
 * @version 1.0.0
 * @created 2023-08-03
 * @modified 2023-08-03
 */
/*
=======================================
SETUP INSTRUCTIONS
=======================================
1. ADD THIS EXTERNAL SCRIPT TO DESIRED PAGE USING THE FOLLOWING IN HEAD "<script src="../javascript/helpcenter.js" defer></script>"
 */


// When the user clicks on the button, scroll to the top of the document
function qaBackToTop() {
    window.scrollTo({top: 0, behavior: 'smooth'});
}

function qaHelpCenter(paramFunction){
    let helpCenterContextMenuOverlay = document.getElementById("QA-help-center-context-menu-container");
    switch (paramFunction){
        case 'show-container':
            helpCenterContextMenuOverlay.style.display="flex";
            break;
        case 'hide-container':
            helpCenterContextMenuOverlay.style.display="none";
            break;
        case 'run-contactus':
            window.open("/html/about-us.html","_self");
            break;
        case 'run-emailus':
            window.open("mailto:support@easybites.com");
            break;
    }
}
