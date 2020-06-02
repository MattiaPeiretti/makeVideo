//Browser library to browse the different pages of the whole app

const { remote } = nodeRequire('electron')

//Pages
const pages = ['loadFile.html', 'page1.html', 'page2.html']; 
const pagesPath = "/pages/";


eel.expose(loadCustomUrl);
function loadCustomUrl(url) { 
    remote.getCurrentWindow().loadURL(url);
}

eel.expose(loadPage);
function loadPage(page) { 
    if (pages.includes(page)) {
        window.location.href = pagesPath + page;
    } else {
        throw404();
    }
}

eel.expose(load404Page);
function load404Page(page) { 
    page404 = page;
}

function throw404() {
    alert('ERROR: Pages does not exist!')
}