/**
 * @summary Script inserts "componentes" into a page. Useful for implementing headers, footers, and other page sections that will be used in multiple pages.
 * @author Kevin Tojin <kevintojin19@gmail.com>
 * @version 1.0.0
 * @created 2023-26-02
 * @modified 2023-26-02
 */
/*
=======================================
SETUP INSTRUCTIONS
=======================================
1. ADD ENTREE OF COMPONENT TO THE "componentLists" ARRAY. "id" IS THE ID OF HTML ELEMENT WHERE COMPONENT IS TO BE INSTERTED. "fileNname" IS HTML FILE THAT WILL BE USED AS THE COMPONENT.
2. ADD THIS EXTERNAL SCRIPT TO DESIRED PAGE USING THE FOLLOWING IN HEAD "<script src="../javascript/components.js" defer></script>"
 */

//CREATES COMPONENT LIST METADATA
const componentLists = 
[
    {
            "id":"page-header",
            "fileName":"header.html"
        },
        {
            "id":"page-footer",
            "fileName":"footer.html"
        },
        {
            "id":"helpcenter-component",
            "fileName":"helpcenter.html"
        }
];
//CREATES HEADER STRUCTURE TO BE SENT AS PART OF REQUEST
const requestHeader = {
    "Cache-Control": "max-age=0",
    "Connection": "close",
    "Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*; q=0.8,application/signed-exchange; v=b3; q=0.7",
    "Accept-Encoding": "br,gzip,deflate",
    "Accept-Language": "en-US,en; q=0.9"
    }
//FOR EACH COMPONENT, GETS HTML CODE FROM FILE AND INSERTS IT INTO DESIGNATED HTML TAG USING THE ID
componentLists.forEach(
    componentItem => {

        fetch("../components/"+componentItem.fileName, {requestHeader})
            .then((response) => {
                    response.text()
                        .then(html => {
                            document.getElementById(componentItem.id).innerHTML = html;
                        }
                        )
                }
            ) 
    });
